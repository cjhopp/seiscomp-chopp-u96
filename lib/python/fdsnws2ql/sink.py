###############################################################################
# Copyright (C) 2022 by gempa GmbH                                            #
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
#                                                                             #
#                                                                             #
# SeisComP ExportSink compatibility layer                                     #
#                                                                             #
###############################################################################

from seiscomp import core
from seiscomp import io as scio

from .compat import isPy3, py3ustr, py3bstr

# with API 15.0.0 the write() method of IO.Export Sink changed from characters
# to bytes
BYTE_SINK = core.SC_API_VERSION >= 0x0F0000  # 15.0.0

# SC_API and Python version dependent imports
if BYTE_SINK:
    from io import BytesIO as Buffer
else:
    if isPy3:
        from io import StringIO as Buffer
    else:
        from StringIO import StringIO as Buffer  # pylint: disable=E0401


###############################################################################
class Sink(scio.ExportSink):
    # -------------------------------------------------------------------------
    def __init__(self, buf):
        scio.ExportSink.__init__(self)
        self.buf = buf


###############################################################################
# Since SeisComP API 15.0.0 write is called with bytes and without size
class ByteSink(Sink):
    # -------------------------------------------------------------------------
    def write(self, data):
        self.buf.write(data)
        return len(data)


###############################################################################
# Prior to SeisComP API 15.0.0 write was invoked with chars and size
class StringSink(Sink):
    # -------------------------------------------------------------------------
    def write(self, data, size):  # pylint: disable=W0221
        self.buf.write(data[:size])
        return size


###############################################################################
class StringBuffer(Buffer):
    # -------------------------------------------------------------------------
    def __init__(self):
        Buffer.__init__(self)
        self.sink = ByteSink(self) if BYTE_SINK else StringSink(self)

    # -------------------------------------------------------------------------
    def __str__(self):
        return py3ustr(self.getvalue()) if BYTE_SINK else self.getvalue()

    # -------------------------------------------------------------------------
    def __bytes__(self):
        return self.getvalue() if BYTE_SINK else py3bstr(self.getvalue())

    # -------------------------------------------------------------------------
    def tobytes(self):
        return self.bytes()
