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

# pylint: disable=consider-using-f-string
# remove once Python2 support can be dropped
from __future__ import absolute_import, division, print_function

from seiscomp import core, datamodel

from .compat import b_str, isPy3, py2ustr


###############################################################################
class Event(object):
    # -------------------------------------------------------------------------
    class SignificantChange:
        class Precision(object):
            def __init__(self):
                self.time = 1e-02
                self.coordinates = 1e-06
                self.depth = 1e-03
                self.magnitude = 1e-02

        # singleton instance
        __instance = None

        @staticmethod
        def getInstance():
            # pylint: disable=W0212
            if Event.SignificantChange.__instance is None:
                Event.SignificantChange()

            return Event.SignificantChange.__instance

        def __init__(self):
            # pylint: disable=W0212
            if Event.SignificantChange.__instance is not None:
                raise RuntimeError(
                    "Singleton class! Use getInstance to retrieve "
                    "one and only instance."
                )

            self.time = True
            self.coordinates = True
            self.depth = True
            self.author = True
            self.catalog = True
            self.contributor = True
            self.contributorID = True
            self.magType = True
            self.magnitude = True
            self.magAuthor = True
            self.locationName = True
            self.eventType = True

            self.precision = self.Precision()

            Event.SignificantChange.__instance = self

    # -------------------------------------------------------------------------
    def __init__(self, eventID, otime, latitude, longitude):
        self.eventID = eventID
        self.time = otime
        self.latitude = latitude
        self.longitude = longitude
        self.depth = None
        self.author = ""
        self.catalog = ""
        self.contributor = ""
        self.contributorID = ""
        self.magType = ""
        self.magnitude = None
        self.magAuthor = ""
        self.locationName = ""
        self.eventType = None

    # -------------------------------------------------------------------------
    @staticmethod
    def hasValue(value):
        if not value:
            return False
        return value.lower() not in ("-", "none", "null", "nil")

    # -------------------------------------------------------------------------
    @classmethod
    def fromLine(cls, line):
        toks = [x.strip() for x in line.strip().split("|")]
        nToks = len(toks)
        if nToks > 14:
            raise ValueError("to many tokens, got {}, maximum 14".format(nToks))
        if nToks < 13:
            raise ValueError("to few tokens, got {}, minimum 13".format(nToks))
        toks = [x.strip() for x in toks]

        eventID = toks[0]
        if not eventID:
            raise ValueError("eventID must not be empty")
        otime = core.Time()
        if not otime.fromString(toks[1], "%FT%T.%f") and not otime.fromString(
            toks[1], "%FT%T"
        ):
            raise ValueError("invalid origin time")
        latitude = float(toks[2])
        longitude = float(toks[3])

        ep = cls(eventID, otime, latitude, longitude)

        ep.depth = float(toks[4]) if toks[4] else None
        ep.author = toks[5]
        ep.catalog = toks[6]
        ep.contributor = toks[7]
        ep.contributorID = toks[8]
        ep.magType = toks[9]
        ep.magnitude = float(toks[10]) if toks[10] else None
        ep.magAuthor = toks[11]
        ep.locationName = toks[12]
        if len(toks) > 13 and cls.hasValue(toks[13]):
            # map QuakeML event type to SeisComP, raises ValueError if type
            # can't be mapped
            ep.eventType = datamodel.QMLTypeMapper.EventTypeFromString(toks[13])

        return ep

    # -------------------------------------------------------------------------
    @staticmethod
    def _sigChange(o1, o2, compare, precision):
        if not compare:
            return False
        if o1 is None and o2 is None:
            return False
        if o1 is None and o2 is not None or o1 is not None and o2 is None:
            return True
        return abs(float(o1 - o2)) > precision

    # -------------------------------------------------------------------------
    def __eq__(self, other):
        sig = self.SignificantChange.getInstance()
        pre = sig.precision

        return (
            self.eventID == other.eventID
            and not self._sigChange(self.time, other.time, sig.time, pre.time)
            and not self._sigChange(
                self.latitude, other.latitude, sig.coordinates, pre.coordinates
            )
            and not self._sigChange(
                self.longitude, other.longitude, sig.coordinates, pre.coordinates
            )
            and not self._sigChange(self.depth, other.depth, sig.depth, pre.depth)
            and (not sig.author or self.author == other.author)
            and (not sig.catalog or self.catalog == other.catalog)
            and (not sig.contributor or self.contributor == other.contributor)
            and (not sig.contributorID or self.contributorID == other.contributorID)
            and (not sig.magType or self.magType == other.magType)
            and not self._sigChange(
                self.magnitude, other.magnitude, sig.magnitude, pre.magnitude
            )
            and (not sig.magAuthor or self.magAuthor == other.magAuthor)
            and (not sig.locationName or self.locationName == other.locationName)
            and (not sig.eventType or self.eventType == other.eventType)
        )

    # -------------------------------------------------------------------------
    def __ne__(self, other):
        return not self == other

    # -------------------------------------------------------------------------
    def __unicode__(self):
        return "{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}".format(
            py2ustr(self.eventID),
            self.time.toString("%FT%T.%f"),
            self.latitude,
            self.longitude,
            "" if self.depth is None else self.depth,
            py2ustr(self.author),
            py2ustr(self.catalog),
            py2ustr(self.contributor),
            py2ustr(self.contributorID),
            py2ustr(self.magType),
            "" if self.magnitude is None else self.magnitude,
            py2ustr(self.magAuthor),
            py2ustr(self.locationName),
            ""
            if self.eventType is None
            else datamodel.QMLTypeMapper.EventTypeToString(self.eventType),
        )

    # -------------------------------------------------------------------------
    def __bytes__(self):
        return b_str(self.__unicode__())

    # -------------------------------------------------------------------------
    def __repr__(self):
        return self.__unicode__() if isPy3 else self.__bytes__()

    # -------------------------------------------------------------------------
    def diff(self, other):
        sig = self.SignificantChange.getInstance()
        pre = sig.precision
        res = ""
        if self.eventID != other.eventID:
            res = "eventID: {} != {}".format(self.eventID, other.eventID)
        elif self._sigChange(self.time, other.time, sig.time, pre.time):
            res = "time: {} != {}".format(self.time.iso(), other.time.iso())
        elif self._sigChange(
            self.latitude, other.latitude, sig.coordinates, pre.coordinates
        ):
            res = "latitude: {} != {}".format(self.latitude, other.latitude)
        elif self._sigChange(
            self.longitude, other.longitude, sig.coordinates, pre.coordinates
        ):
            res = "longitude: {} != {}".format(self.longitude, other.longitude)
        elif self._sigChange(self.depth, other.depth, sig.depth, pre.depth):
            res = "depth: {} != {}".format(self.depth, other.depth)
        elif sig.author and self.author != other.author:
            res = "author: {} != {}".format(self.author, other.author)
        elif sig.catalog and self.catalog != other.catalog:
            res = "catalog: {} != {}".format(self.catalog, other.catalog)
        elif sig.contributor and self.contributor != other.contributor:
            res = "contributor: {} != {}".format(self.contributor, other.contributor)
        elif sig.contributorID and self.contributorID != other.contributorID:
            res = "contributorID: {} != {}".format(
                self.contributorID, other.contributorID
            )
        elif sig.magType and self.magType != other.magType:
            res = "magType: {} != {}".format(self.magType, other.magType)
        elif self._sigChange(
            self.magnitude, other.magnitude, sig.magnitude, pre.magnitude
        ):
            res = "magnitude: {} != {}".format(self.magnitude, other.magnitude)
        elif sig.magAuthor and self.magAuthor != other.magAuthor:
            res = "magAuthor: {} != {}".format(self.magAuthor, other.magAuthor)
        elif sig.locationName and self.locationName != other.locationName:
            res = "locationName: {} != {}".format(self.locationName, other.locationName)
        elif sig.eventType and self.eventType != other.eventType:
            res = "eventType: {} != {}".format(self.eventType, other.eventType)

        return res
