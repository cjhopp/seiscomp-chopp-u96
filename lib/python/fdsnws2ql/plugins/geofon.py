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
# Author: Stephan Herrnkind, Erik Miers                                       #
# Email: herrnkind@gempa.de, miers@gempa.de                                   #
###############################################################################

# pylint: disable=consider-using-f-string
# remove once Python2 support can be dropped
from __future__ import absolute_import, division, print_function

from seiscomp import core

from fdsnws2ql.event import Event
from .fdsnws import FDSNWS


class Geofon(FDSNWS):
    # --------------------------------------------------------------------------
    def eventSelectURL(self, startTime):
        return (
            "{}?fmt=txt&nmax=200&datemin={}&latmax={}&lonmin={}&lonmax={}"
            "&latmin={}&magmin={}".format(
                self.host.url,
                startTime.toString("%F"),
                self.host.filter.boundingBox.latitude.max,
                self.host.filter.boundingBox.latitude.min,
                self.host.filter.boundingBox.longitude.max,
                self.host.filter.boundingBox.longitude.min,
                self.host.filter.magnitude.value.min,
            )
        )

    # -------------------------------------------------------------------------
    def eventFromLine(self, line):
        if line.startswith("#"):
            return None

        # example line:
        # gfz2019pmcm all 5.2 C 2019-08-09 01:55:56 -4.50 -106.07  10 0
        toks = line.strip().split()
        nToks = len(toks)
        if nToks != 10:
            raise ValueError(
                "invalid number of tokens, got {}, expected {}".format(nToks, 10)
            )

        otime = core.Time.FromString(" ".join(toks[4:6]), "%F %T")
        lat = float(toks[6])
        lon = float(toks[7])
        ep = Event(toks[0], otime, lat, lon)
        ep.magnitude = float(toks[2]) if toks[2] else None
        ep.depth = float(toks[8]) if toks[8] else None

        return ep
