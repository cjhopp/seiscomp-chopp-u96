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

import requests

from seiscomp import logging

from fdsnws2ql.event import Event
from fdsnws2ql.compat import isPy3
from fdsnws2ql.plugin import RequestHandler


class FDSNWS(RequestHandler):
    # --------------------------------------------------------------------------
    def fetchEvents(self, startTime):
        url = self.eventSelectURL(startTime)
        logging.debug("[{}] fetching events from {}".format(self.host.name, url))

        resp = requests.get(
            url, timeout=self.host.app.config.requestTimeout, stream=True
        )
        resp.raise_for_status()
        if resp.status_code != 200:
            logging.debug(
                "[{}] no events returned, HTTP status: {}".format(
                    self.host.name, resp.status_code
                )
            )
            return []

        events = []
        i = 0

        if self.host.app.isExitRequested():
            return events

        if resp.encoding is None:
            resp.encoding = "utf-8"

        for line in resp.iter_lines(decode_unicode=isPy3):
            i += 1
            try:
                ep = self.eventFromLine(line)
                if ep is None:
                    continue

                if ep.time < startTime:
                    logging.warning(
                        "[{}] ignoring event {} with origin "
                        "time before requested startTime".format(
                            self.host.name, ep.eventID
                        )
                    )
                else:
                    events.append(ep)
            except ValueError as e:
                raise ValueError("could not parse line #{}: {}\n{}".format(i, line, e))

        return events

    # --------------------------------------------------------------------------
    def eventSelectURL(self, startTime):
        url = "{}?format=text&starttime={}{}".format(
            self.host.url, startTime.toString("%FT%T"), self.host.filter.formatURL()
        )
        if self.host.updatedAfter and self.host.lastUpdate.valid():
            url += "&updatedafter={}".format(self.host.lastUpdate.toString("%FT%T.%f"))
        return url

    # -------------------------------------------------------------------------
    def eventFromLine(self, line):
        if line.startswith("#"):
            return None

        return Event.fromLine(line)
