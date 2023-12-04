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

from __future__ import absolute_import, division, print_function


class RequestHandler(object):
    """
    Base class for all fdsnws2ql plugins which must be derived.
    """

    def __init__(self, host):
        """
        Constructor
        @param host: fdsnws2ql.host.Host object
        """
        self.host = host

    def fetchEvents(self, startTime):
        """
        Fetches events for a datasource starting at startTime.
        @param startTime: seiscomp.Core.Time object.
        @return List of fdsnws2ql.event.Event objects
        """
        raise NotImplementedError
