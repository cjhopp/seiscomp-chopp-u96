#!/usr/bin/env seiscomp-python

###############################################################################
# Copyright (C) 2020 by gempa GmbH                                            #
#                                                                             #
# All Rights Reserved.                                                        #
#                                                                             #
# NOTICE: All information contained herein is, and remains                    #
# the property of gempa GmbH and its suppliers, if any. The intellectual      #
# and technical concepts contained herein are proprietary to gempa GmbH       #
# and its suppliers.                                                          #
# Dissemination of this information or reproduction of this material          #
# is strictly forbidden unless prior written permission is obtained           #
# from gempa GmbH.                                                            #
#                                                                             #
# Author: Stephan Herrnkind                                                   #
# Email: herrnkind@gempa.de                                                   #
###############################################################################

# pylint: disable=consider-using-f-string,raise-missing-from
# remove once Python2 support can be dropped
from __future__ import absolute_import, division, print_function

import importlib
import os
import socket
import ssl
import time
import traceback

from tempfile import NamedTemporaryFile
from threading import Thread

import requests

from seiscomp import core, datamodel, logging
from seiscomp import io as scio

from .compat import isPy3, py3bstr, py3ustr
from .event import Event
from .plugins.fdsnws import FDSNWS
from .plugin import RequestHandler
from .sink import StringBuffer

# -----------------------------------------------------------------------------
# Python 2/3 compatibility
if isPy3:
    from urllib.parse import urlparse
else:
    from urlparse import urlparse  # pylint: disable=E0401


###############################################################################
class Host(Thread):
    # -------------------------------------------------------------------------
    class Range(object):
        def __init__(self):
            self.min = None
            self.max = None

        def isEmpty(self):
            return self.min is None and self.max is None

        def format(self, ts=4, indent=0):
            if self.isEmpty():
                return "None"
            prefix = " " * ts * indent
            return "\n{0}min: {1}" "\n{0}max: {2}".format(prefix, self.min, self.max)

        def formatURL(self, suffix=""):
            retn = ""
            if self.min is not None:
                retn += "&min{}={}".format(suffix, self.min)
            if self.max is not None:
                retn += "&max{}={}".format(suffix, self.max)
            return retn

    # -------------------------------------------------------------------------
    class BoundingBox(object):
        def __init__(self):
            self.latitude = Host.Range()
            self.longitude = Host.Range()

        def isEmpty(self):
            return self.latitude.isEmpty() and self.longitude.isEmpty()

        def format(self, ts=4, indent=0):
            if self.isEmpty():
                return "None"
            prefix = " " * ts * indent
            indent1 = indent + 1
            return "\n{0}latitude : {1}" "\n{0}longitude: {2}".format(
                prefix,
                self.latitude.format(ts, indent1),
                self.longitude.format(ts, indent1),
            )

        def formatURL(self):
            return "{}{}".format(
                self.latitude.formatURL("latitude"),
                self.longitude.formatURL("longitude"),
            )

    # -------------------------------------------------------------------------
    class BoundingCircle(object):
        def __init__(self):
            self.latitude = None
            self.longitude = None
            self.radius = Host.Range()

        def isEmpty(self):
            return (
                self.latitude is None
                and self.longitude is None
                and self.radius.isEmpty()
            )

        def format(self, ts=4, indent=0):
            if self.isEmpty():
                return "None"
            prefix = " " * ts * indent
            return (
                "\n{0}latitude : {1}"
                "\n{0}longitude: {2}"
                "\n{0}radius   : {3}".format(
                    prefix,
                    self.latitude,
                    self.longitude,
                    self.radius.format(ts, indent + 1),
                )
            )

        def formatURL(self):
            if self.isEmpty():
                return ""
            return "&latitude={}&longitude={}{}".format(
                self.latitude, self.longitude, self.radius.formatURL("radius")
            )

    # -------------------------------------------------------------------------
    class Magnitude(object):
        def __init__(self):
            self.value = Host.Range()
            self.type = None

        def isEmpty(self):
            return self.value.isEmpty() and self.type is None

        def format(self, ts=4, indent=0):
            if self.isEmpty():
                return "None"
            prefix = " " * ts * indent
            return "\n{0}value : {1}" "\n{0}type  : {2}".format(
                prefix, self.value.format(ts, indent + 1), str(self.type)
            )

        def formatURL(self):
            retn = self.value.formatURL("magnitude")
            if self.type:
                retn += "&magnitudetype={}".format(self.type)
            return retn

    # -------------------------------------------------------------------------
    class EventFilter(object):
        def __init__(self):
            self.boundingBox = Host.BoundingBox()
            self.boundingCircle = Host.BoundingCircle()
            self.depth = Host.Range()
            self.magnitude = Host.Magnitude()
            self.eventTypes = []
            self.catalog = None
            self.contributor = None

        def isEmpty(self):
            return (
                self.boundingBox.isEmpty()
                and self.boundingCircle.isEmpty()
                and self.depth.isEmpty()
                and not self.eventTypes
                and self.catalog is None
                and self.contributor is None
            )

        def format(self, ts=4, indent=0):
            if self.isEmpty():
                return "None"
            prefix = " " * ts * indent
            indent1 = indent + 1
            return (
                "\n{0}boundingBox   : {1}"
                "\n{0}boundingCircle: {2}"
                "\n{0}depth         : {3}"
                "\n{0}magnitude     : {4}"
                "\n{0}eventTypes    : {5}"
                "\n{0}catalog       : {6}"
                "\n{0}contributor   : {7}".format(
                    prefix,
                    self.boundingBox.format(ts, indent1),
                    self.boundingCircle.format(ts, indent1),
                    self.depth.format(ts, indent1),
                    self.magnitude.format(ts, indent1),
                    ", ".join(
                        [
                            "unknown" if i < 0 else datamodel.EEventTypeNames.name(i)
                            for i in sorted(self.eventTypes)
                        ]
                    ),
                    self.catalog,
                    self.contributor,
                )
            )

        def formatURL(self):
            retn = "{}{}{}{}".format(
                self.boundingBox.formatURL(),
                self.boundingCircle.formatURL(),
                self.depth.formatURL("depth"),
                self.magnitude.formatURL(),
            )

            if self.eventTypes:
                retn += "&eventtype={}".format(
                    ",".join(
                        [
                            "unknown"
                            if i < 0
                            else datamodel.QMLTypeMapper.EventTypeToString(i)
                            for i in sorted(self.eventTypes)
                        ]
                    )
                )
            if self.catalog:
                retn += "&catalog={}".format(self.catalog)
            if self.contributor:
                retn += "&contributor={}".format(self.contributor)

            return retn

    # -------------------------------------------------------------------------
    class Content(object):
        def __init__(self):
            self.text = None
            self.xml = None

        def isEmpty(self):
            return self.text is None and self.xml is None

        def format(self, ts=4, indent=0):
            if self.isEmpty():
                return "None"

            if self.text:
                return "text" + self.text.format(ts, indent)
            return "XML" + self.xml.format(ts, indent)

    # -------------------------------------------------------------------------
    class XSLT(object):
        def __init__(self):
            self.version = None
            self.idPrefix = None
            self.custom = None

        def format(self, ts=4, indent=0):
            prefix = " " * ts * indent
            return (
                "\n{0}version      : {1}"
                "\n{0}idPrefix     : {2}"
                "\n{0}custom       : {3}".format(
                    prefix, self.version, self.idPrefix, self.custom
                )
            )

    # -------------------------------------------------------------------------
    class XMLContent(object):
        def __init__(self):
            self.enabled = False
            self.sc3ml = False
            self.allOrigins = False
            self.allMagnitudes = False
            self.arrivals = False
            self.xslt = None

        def format(self, ts=4, indent=0):
            prefix = " " * ts * indent
            retn = (
                "\n{0}sc3ml        : {1}"
                "\n{0}allOrigins   : {2}"
                "\n{0}allMagnitudes: {3}"
                "\n{0}arrivals     : {4}".format(
                    prefix,
                    self.sc3ml,
                    self.allOrigins,
                    self.allMagnitudes,
                    self.arrivals,
                )
            )
            if self.xslt:
                retn += "\n{}XSLT:{}".format(prefix, self.xslt.format(ts, indent + 1))

            return retn

        def formatURL(self):
            retn = "&format={}".format("sc3ml" if self.sc3ml else "xml")
            if self.allOrigins:
                retn += "&includeallorigins=true"
            if self.allMagnitudes:
                retn += "&includeallmagnitudes=true"
            if self.arrivals:
                retn += "&includearrivals=true"

            return retn

    # -------------------------------------------------------------------------
    class TextContent(object):
        def __init__(self):
            self.agencyID = None
            self.evaluationMode = datamodel.MANUAL
            self.evaluationStatus = datamodel.CONFIRMED

        def format(self, ts=4, indent=0):
            prefix = " " * ts * indent
            return (
                "\n{0}agencyID        : {1}"
                "\n{0}evaluationMode  : {2}"
                "\n{0}evaluationStatus: {3}".format(
                    prefix,
                    self.agencyID,
                    datamodel.EEvaluationModeNames_name(self.evaluationMode),
                    datamodel.EEvaluationStatusNames_name(self.evaluationStatus),
                )
            )

    # -------------------------------------------------------------------------
    def __init__(self, app, name):
        Thread.__init__(self)

        self.app = app
        self.name = name

        self.journalFile = os.path.join(
            app.config.journalDir, "{}.journal".format(name)
        )

        # request URL
        self.url = None

        # if updatedafter request parameter is supported by service the last
        # update time will be used instead of a fixed time window
        self.updatedAfter = False

        # event filter parameter
        self.filter = Host.EventFilter()

        # request handler
        self.requestHandler = None

        # content settings
        self.content = Host.Content()

        # time the last successful update was performed
        self.lastUpdate = core.Time()

        # event journal mapping event id to Event object
        self.journal = {}

        # converts SeisComP objects to text
        self.exporter = None

        # XML parser and XSLT required for QuakeML to SeisComPML conversion
        self.xmlParser = None
        self.qml2SCML = None
        self.idPrefix = None

        self.readConfig()

    # -------------------------------------------------------------------------
    def run(self):
        while not self.app.isExitRequested():
            start = core.Time.GMT()
            try:
                self.process()
            except Exception as e:
                logging.error("[{}] processing error: {}".format(self.name, e))
                logging.debug(traceback.format_exc())
            while (
                not self.app.isExitRequested()
                and (core.Time.GMT() - start).seconds() < self.app.config.interval
            ):
                time.sleep(1)

        logging.info("[{}] terminated".format(self.name))

    # -------------------------------------------------------------------------
    def setParser(self, xmlParser, qml2SCML, idPrefix=None):
        self.xmlParser = xmlParser
        self.qml2SCML = qml2SCML
        self.idPrefix = idPrefix

    # -------------------------------------------------------------------------
    def fetchEvents(self, now):
        startTime = now - core.TimeSpan(int(self.app.config.backlog * 86400.0), 0)

        return self.requestHandler.fetchEvents(startTime)

    # -------------------------------------------------------------------------
    def fetchXML(self, eventID):
        url = self.eventXMLURL(eventID)
        logging.debug(
            "[{}] fetching XML of event {} from {}".format(self.name, eventID, url)
        )

        # fetch xml from FDSNWS server
        resp = requests.get(url, timeout=self.app.config.requestTimeout)
        resp.raise_for_status()
        if resp.status_code != 200:
            raise ValueError(
                "no events returned, HTTP status: {}".format(resp.status_code)
            )

        xml = None
        if self.app.isExitRequested():
            return xml

        if self.content.xml.sc3ml:
            # the server retured SeisComPML which may be returned directly
            xml = resp.content
        elif not self.xmlParser:
            raise ValueError("no parser for QuakeML conversion set")
        else:
            logging.debug(
                "[{}] converting QuakeML of event {} to SeisComPML".format(
                    self.name, eventID
                )
            )
            # the server returned QuakeML which needs to be transformed to
            # SeisComPML first
            from lxml import etree  # pylint: disable=C0415

            try:
                # with open('/tmp/test/{}-qml.xml'.format(eventID), 'wb') as f:
                #    f.write(resp.content)
                qml = etree.fromstring(resp.content, parser=self.xmlParser)
                if self.idPrefix:
                    scML = self.qml2SCML(qml, ID_PREFIX=self.idPrefix)
                else:
                    scML = self.qml2SCML(qml)

                # override QuakeML event ID as it contains slashes which
                # can't be processed by QuakeLink
                ns = {
                    "s": "http://geofon.gfz-potsdam.de/ns/seiscomp3-schema/{}".format(
                        self.content.xml.xslt.version
                    )
                }
                nodes = scML.xpath(
                    "/s:seiscomp/s:EventParameters/s:event", namespaces=ns
                )
                for eventNode in nodes:
                    eventNode.attrib["publicID"] = eventID

                xml = etree.tostring(scML)
                # with open('/tmp/test/{}-scml.xml'.format(eventID), 'wb') as f:
                #    f.write(xml)
            except etree.XMLSyntaxError as e:
                raise ValueError("could not parse QuakeML: {}".format(e))
            except etree.XSLTError as e:
                raise ValueError(
                    "could not transform QuakeML to SeisComPML: " "{}".format(e)
                )

        return xml

    # -------------------------------------------------------------------------
    def createXML(self, event):
        # EventParameters holding origin and event object
        ep = datamodel.EventParameters()

        # Event
        eID = (
            event.eventID.replace("/", "_")
            .replace("\\", "_")
            .replace(":", "_")
            .replace(".", "_")
        )

        logging.debug(
            "[{}] creating XML of event {} from text parameters".format(self.name, eID)
        )

        e = datamodel.Event.Create(eID)
        ep.add(e)

        if event.locationName:
            e.add(datamodel.EventDescription(event.locationName, datamodel.REGION_NAME))

        if event.eventType is not None:
            e.setType(event.eventType)

        if event.catalog:
            c = datamodel.Comment()
            c.setId("catalog")
            c.setText(event.catalog)
            e.add(c)

        if event.contributorID:
            c = datamodel.Comment()
            c.setId("contributorID")
            c.setText(event.contributorID)
            e.add(c)

        ci = None
        if self.content.text.agencyID or event.author or event.contributor:
            ci = datamodel.CreationInfo()
            if event.author:
                ci.setAuthor(event.author)
            if self.content.text.agencyID:
                ci.setAgencyID(self.content.text.agencyID)
            elif event.contributor:
                ci.setAgencyID(event.contributor)
            e.setCreationInfo(ci)

        # Origin
        o = datamodel.Origin.Create()
        ep.add(o)
        e.setPreferredOriginID(o.publicID())

        if ci is not None:
            o.setCreationInfo(ci)

        o.setEvaluationMode(self.content.text.evaluationMode)
        o.setEvaluationStatus(self.content.text.evaluationStatus)

        o.setLatitude(datamodel.RealQuantity(event.latitude))
        o.setLongitude(datamodel.RealQuantity(event.longitude))
        if event.depth is not None:
            o.setDepth(datamodel.RealQuantity(event.depth))

        #        quality = datamodel.OriginQuality()
        #        quality.setUsedStationCount(o.phaseCount)
        #        quality.setUsedPhaseCount(o.phaseCount)
        #        origin.setQuality(quality)

        o.setTime(datamodel.TimeQuantity(core.Time(event.time)))

        # Magnitude
        if event.magnitude is not None:
            mag = datamodel.Magnitude.Create()
            o.add(mag)
            e.setPreferredMagnitudeID(mag.publicID())
            mag.setMagnitude(datamodel.RealQuantity(event.magnitude))
            mag.setType(event.magType)
            mag.setStationCount(1)
            if event.magAuthor:
                ci = datamodel.CreationInfo()
                ci.setAuthor(event.magAuthor)
                mag.setCreationInfo(ci)

        if self.app.isExitRequested():
            return None

        if not self.exporter:
            self.exporter = scio.Exporter.Create("trunk")
            if not self.exporter:
                raise RuntimeError("could not create 'trunk' exporter")

        buf = StringBuffer()
        self.exporter.write(buf.sink, ep)
        return bytes(buf)

    # -------------------------------------------------------------------------
    def sendData(self, now, sock, data, eID):
        header = (
            "Content-Type: text/xml\r\n"
            "Content-Timestamp: {}\r\n"
            "Content-Length: {}\r\n"
            "\r\n".format(now.toString("%FT%T.%f"), len(data))
        )
        sock.sendall(py3bstr(header))
        sock.sendall(data)
        sock.sendall(py3bstr("\r\n"))

        resp = py3ustr(sock.recv(1024))
        if resp.strip()[:3] == "200":
            eid = None
            rev = None
            for line in resp.splitlines():
                lineUpper = line.upper()
                if lineUpper[:9] == "EVENT-ID:":
                    eid = line[9:].strip()
                if lineUpper[:15] == "EVENT-REVISION:":
                    try:
                        rev = int(line[15:])
                    except ValueError:
                        logging.warning(
                            "[{}] could not parse QuakeLink "
                            "event revision : {}".format(self.name, line[15:])
                        )
            logging.debug(
                "[{}] event received by QuakeLink sever: {}/{}".format(
                    self.name, eid, rev
                )
            )
            return True

        logging.warning(
            "[{}] event {} not accepted by QuakeLink server ".format(self.name, eID)
        )
        resp = resp.replace("\r", "").replace("\n", ", ")
        logging.debug("[{}] server response: {}".format(self.name, resp))
        return False

    # -------------------------------------------------------------------------
    def process(self):
        logging.debug("[{}] start processing".format(self.name))

        now = core.Time().GMT()

        # fetch events in text format
        events = self.fetchEvents(now)

        # connect to QuakeLink server
        sock = None
        if events:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if self.app.config.ssl:
                    sock = ssl.wrap_socket(sock)
                logging.debug(
                    "[{}] connecting to QuakeLink server {}:{} "
                    "(SSL: {})".format(
                        self.name,
                        self.app.config.host,
                        self.app.config.port,
                        self.app.config.ssl,
                    )
                )
                sock.connect((self.app.config.host, self.app.config.port))
            except socket.error as e:
                logging.error(
                    "[{}] could not connect to QuakeLink server: "
                    "{}".format(self.name, e)
                )
                sock.close()
                return

        # process events
        newCnt = 0
        updCnt = 0
        processed = []
        for event in events:
            eID = event.eventID

            # compare events with journal, search for new and changed
            if eID in self.journal:
                journalEvent = self.journal[eID]
                if event == journalEvent:
                    continue
                updCnt += 1
                logging.debug(
                    "[{}] event {} was changed: {}".format(
                        self.name, eID, event.diff(journalEvent)
                    )
                )
            else:
                logging.debug("[{}] found new event {}".format(self.name, eID))
                newCnt += 1

            # generate or fetch XML
            xml = None
            try:
                if self.content.text:
                    xml = self.createXML(event)
                else:
                    xml = self.fetchXML(eID)
            except Exception as e:
                logging.error(
                    "[{}] could not {} XML for event {}: {}".format(
                        self.name, "fetch" if self.content.xml else "create", eID, e
                    )
                )
                continue

            if self.app.isExitRequested():
                break
            if xml is None:
                continue

            # send XML to QuakeLink server
            try:
                # with open("/tmp/test.xml", "wb") as f:
                #    f.write(xml)
                if self.sendData(now, sock, xml, eID):
                    # mark event as processed
                    processed.append(event)
            except OSError as e:
                logging.error(
                    "[{}] QuakeLink communication error while "
                    "sending event {}: {}".format(self.name, eID, e)
                )
                # Communication errors are catched at this stage because
                # some events might have been successfully send to the
                # QuakeLink server and need to be updated in the journal
                break

        # close QuakeLink connection
        if sock:
            sock.close()

        errorCnt = newCnt + updCnt - len(processed)
        logging.info(
            "[{}] processed events (fetched/new/updated/errors): "
            "{}/{}/{}/{}".format(self.name, len(events), newCnt, updCnt, errorCnt)
        )

        # update journal
        if len(processed) == len(events):
            self.lastUpdate = now
        for event in processed:
            self.journal[event.eventID] = event
        if processed:
            self.writeJournal()

    # -------------------------------------------------------------------------
    def format(self, ts=4, indent=0):
        prefix = " " * ts * indent
        prefix2 = " " * ts * (indent + 1)
        handler = type(self.requestHandler)
        return (
            "{0}{2}:"
            "\n{1}url           : {3}"
            "\n{1}updatedAfter  : {4}"
            "\n{1}requestHandler: {5}.{6}"
            "\n{1}filter        : {7}"
            "\n{1}content       : {8}".format(
                prefix,
                prefix2,
                self.name,
                self.url,
                self.updatedAfter,
                handler.__module__,
                handler.__name__,
                self.filter.format(ts, indent + 2),
                self.content.format(ts, indent + 2),
            )
        )

    # -------------------------------------------------------------------------
    def eventXMLURL(self, eventID):
        return "{}?eventid={}{}".format(self.url, eventID, self.content.xml.formatURL())

    # -------------------------------------------------------------------------
    def readConfig(self):
        prefix = "host.{}.".format(self.name)
        param = ""

        try:
            # URL
            param = prefix + "url"
            self.url = self.app.configGetString(param)
            parsedURL = urlparse(self.url)
            if not parsedURL.path:
                self.url += "/fdsnws/event/1/query"

            # updateAfter support
            param = prefix + "updatedAfter"
            try:
                self.updatedAfter = self.app.configGetBool(param)
            except RuntimeError:
                pass

            # request handler
            param = prefix + "requestHandler"
            try:
                handlerName = self.app.configGetString(param)
            except RuntimeError:
                handlerName = None

            if handlerName:
                toks = handlerName.split(".")
                packageName = ".".join(toks[0:-1])
                className = toks[-1]
                try:
                    klass = getattr(importlib.import_module(packageName), className)
                except:
                    raise RuntimeError("Could not load class: {}".format(handlerName))

                if not issubclass(klass, RequestHandler):
                    raise RuntimeError(
                        "{} not a subclass of {}.{}".format(
                            handlerName,
                            RequestHandler.__module__,
                            RequestHandler.__name__,
                        )
                    )

                self.requestHandler = klass(self)
            else:
                self.requestHandler = FDSNWS(self)

            # event filter, general prefix
            filterPrefix = prefix + "filter."

            # event filter types
            param = filterPrefix + "eventTypes"
            try:
                self.filter.eventTypes = self.parseEventTypes(
                    self.app.configGetStrings(param)
                )
            except RuntimeError:
                pass

            # event filter catalog and contributor
            param = filterPrefix + "catalog"
            try:
                self.filter.catalog = self.app.configGetString(param)
            except RuntimeError:
                pass

            param = filterPrefix + "contributor"
            try:
                self.filter.contributor = self.app.configGetString(param)
            except RuntimeError:
                pass

            # event filter bounding box
            bbPrefix = filterPrefix + "boundingBox."
            bb = self.filter.boundingBox

            param = bbPrefix + "minLatitude"
            try:
                bb.latitude.min = self.app.configGetDouble(param)
            except RuntimeError:
                pass

            param = bbPrefix + "maxLatitude"
            try:
                bb.latitude.max = self.app.configGetDouble(param)
            except RuntimeError:
                pass

            param = bbPrefix + "minLongitude"
            try:
                bb.longitude.min = self.app.configGetDouble(param)
            except RuntimeError:
                pass

            param = bbPrefix + "maxLongitude"
            try:
                bb.longitude.max = self.app.configGetDouble(param)
            except RuntimeError:
                pass

            # event filter bounding circle
            bcPrefix = filterPrefix + "boundingCircle."
            bc = self.filter.boundingCircle

            param = bcPrefix + "latitude"
            try:
                bc.latitude = self.app.configGetDouble(param)
            except RuntimeError:
                pass

            param = bcPrefix + "longitude"
            try:
                bc.longitude = self.app.configGetDouble(param)
            except RuntimeError:
                pass
            param = bcPrefix + "minRadius"
            try:
                bc.radius.min = self.app.configGetDouble(param)
            except RuntimeError:
                pass

            param = bcPrefix + "maxRadius"
            try:
                bc.radius.max = self.app.configGetDouble(param)
            except RuntimeError:
                pass

            if not bc.radius.isEmpty():
                if bc.latitude is None or bc.longitude is None:
                    raise ValueError(
                        "latitude and longitude must be set in " + bcPrefix
                    )

            # event filter depth
            depthPrefix = filterPrefix + "depth."

            param = depthPrefix + "min"
            try:
                self.filter.depth.min = self.app.configGetDouble(param)
            except RuntimeError:
                pass

            param = depthPrefix + "max"
            try:
                self.filter.depth.max = self.app.configGetDouble(param)
            except RuntimeError:
                pass

            # event filter magnitude
            magPrefix = filterPrefix + "magnitude."

            param = magPrefix + "min"
            try:
                self.filter.magnitude.value.min = self.app.configGetDouble(param)
            except RuntimeError:
                pass

            param = magPrefix + "max"
            try:
                self.filter.magnitude.value.max = self.app.configGetDouble(param)
            except RuntimeError:
                pass

            param = magPrefix + "type"
            try:
                self.filter.magnitude.type = self.app.configGetString(param)
            except RuntimeError:
                pass

            contentPrefix = prefix + "content."
            param = contentPrefix + "fetchXML"

            try:
                fetchXML = self.app.configGetBool(param)
            except RuntimeError:
                fetchXML = False

            # fetch XML
            if fetchXML:
                self.content.xml = Host.XMLContent()
                contentXMLPrefix = contentPrefix + "xml."

                param = contentXMLPrefix + "sc3ml"
                try:
                    self.content.xml.sc3ml = self.app.configGetBool(param)
                except RuntimeError:
                    pass

                contentXMLIncludePrefix = contentXMLPrefix + "include."

                param = contentXMLIncludePrefix + "allOrigins"
                try:
                    self.content.xml.allOrigins = self.app.configGetBool(param)
                except RuntimeError:
                    pass

                param = contentXMLIncludePrefix + "allMagnitudes"
                try:
                    self.content.xml.allMagnitudes = self.app.configGetBool(param)
                except RuntimeError:
                    pass

                param = contentXMLIncludePrefix + "arrivals"
                try:
                    self.content.xml.arrivals = self.app.configGetBool(param)
                except RuntimeError:
                    pass

                # with sc3ml set to false a XSLT script is used to convert
                # QuakeML to SC3ML
                if not self.content.xml.sc3ml:
                    self.content.xml.xslt = Host.XSLT()
                    xslt = self.content.xml.xslt
                    contentXSLTPrefix = contentXMLPrefix + "xslt."

                    param = contentXSLTPrefix + "custom"
                    try:
                        xslt.custom = self.app.configGetString(param)
                    except RuntimeError:
                        pass

                    if not xslt.custom:
                        param = contentXSLTPrefix + "version"
                        try:
                            xslt.version = self.app.configGetString(param)
                        except RuntimeError:
                            pass

                    param = contentXSLTPrefix + "idPrefix"
                    try:
                        xslt.idPrefix = self.app.configGetString(param)
                    except RuntimeError:
                        pass

            # generate content from text parameters
            else:
                self.content.text = Host.TextContent()
                contentTextPrefix = contentPrefix + "text."

                param = contentTextPrefix + "agencyID"
                try:
                    self.content.text.agencyID = self.app.configGetString(param)
                except RuntimeError:
                    pass

                param = contentTextPrefix + "evaluationMode"
                try:
                    modeStr = self.app.configGetString(param)
                    mode = None
                    for i in range(datamodel.EEvaluationModeQuantity):
                        if datamodel.EEvaluationModeNames.name(i) == modeStr:
                            mode = i
                            break
                    if mode is None:
                        raise ValueError("No such evaluation mode: {}".format(modeStr))
                    self.content.text.evaluationMode = mode
                except RuntimeError:
                    pass

                param = contentTextPrefix + "evaluationStatus"
                try:
                    statusStr = self.app.configGetString(param)
                    status = None
                    for i in range(datamodel.EEvaluationStatusQuantity):
                        if datamodel.EEvaluationStatusNames.name(i) == statusStr:
                            status = i
                            break
                    if status is None:
                        raise ValueError(
                            "No such evaluation status: {}".format(statusStr)
                        )
                    self.content.text.evaluationStatus = status
                except RuntimeError:
                    pass

        except Exception as e:
            raise ValueError("Invalid parameter {}: {}".format(param, e))

    # -------------------------------------------------------------------------
    @staticmethod
    def parseEventTypes(names):
        types = set()
        typeMap = {
            datamodel.EEventTypeNames.name(i): i
            for i in range(datamodel.EEventTypeQuantity)
        }
        for n in names:
            name = n.lower().strip()
            if name == "unknown":
                types.add(-1)
            else:
                if name in typeMap:
                    types.add(typeMap[name])
                else:
                    raise ValueError("event type name '{}' not supported".format(name))

        return types

    # -------------------------------------------------------------------------
    def readJournal(self):
        self.journal = {}
        self.lastUpdate = core.Time()

        if not os.path.exists(self.journalFile):
            return True

        logging.debug(
            "[{}] reading journal from {}".format(self.name, self.journalFile)
        )

        # minimum origin time used to purge old events from journal,
        # we add one additional minute to the backlog value in case the origin
        # time was changed in between
        startTime = core.Time.GMT() - core.TimeSpan(
            int(self.app.config.backlog * 86400.0 + 60.0), 0
        )
        outdated = 0

        i = 0
        try:
            with open(self.journalFile, "rb") as f:
                while True:
                    line = py3ustr(f.readline())
                    if not line:
                        break
                    i += 1

                    # first line holds last update time
                    if i == 1:
                        if not self.lastUpdate.fromString(
                            line, "%FT%T.%f"
                        ) and not self.lastUpdate.fromString(line, "%FT%T"):
                            logging.error(
                                "[{}] could not read last update time from "
                                "first line of file {}".format(
                                    self.name, self.journalFile
                                )
                            )
                            return False
                        continue

                    # ignore comments
                    if line.startswith("#"):
                        continue

                    ep = Event.fromLine(line)
                    if ep.time < startTime:
                        outdated += 1
                    else:
                        self.journal[ep.eventID] = ep

        except Exception as e:
            logging.error(
                "[{}] error reading journal {} (#{}): {}".format(
                    self.name, self.journalFile, i, e
                )
            )
            logging.debug(traceback.format_exc())
            return False

        if outdated > 0:
            logging.debug("[{}] ignored {} outdated events".format(self.name, outdated))
        logging.info(
            "[{}] read {} events from file {}".format(
                self.name, len(self.journal), self.journalFile
            )
        )
        return True

    # -------------------------------------------------------------------------
    def writeJournal(self):
        logging.debug("[{}] writing journal to {}".format(self.name, self.journalFile))

        # extract directory name and create directory if it does not exist yet
        fileDir = os.path.dirname(self.journalFile)

        # write to a temparary file
        # encoding parameter not supported by Python2 version
        with NamedTemporaryFile(mode="wb", dir=fileDir, delete=False) as f:
            # first line holds last update time
            f.write(py3bstr("{}\n".format(self.lastUpdate.toString("%FT%T.%f"))))

            # write events in order of eventID
            for event in self.journal.values():
                f.write(py3bstr("{}\n".format(event)))

        # NamedTemporaryFile ignores the umask for security reasons.
        # To obtain the currect umask we need to set it and subsequently
        # restore the old version.
        umask = os.umask(0o666)
        os.umask(umask)
        os.chmod(f.name, 0o666 & ~umask)

        # move temporary file to final name
        os.rename(f.name, self.journalFile)
