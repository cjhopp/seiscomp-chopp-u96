###############################################################################
# Copyright (C) 2014 by gempa GmbH                                            #
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
# Python 2/3 compatibility layer                                              #
#                                                                             #
###############################################################################

from __future__ import absolute_import, division, print_function

import sys


# -----------------------------------------------------------------------------
# Converts a unicode string to a byte string
b_str = lambda s: s.encode("utf-8", "replace")


# -----------------------------------------------------------------------------
# Converts a byte string to a unicode string
u_str = lambda s: s.decode("utf-8", "replace")


# -----------------------------------------------------------------------------
# Python 2/3 compatibility
if sys.version_info[0] < 3:
    isPy3 = False
    text_str_type = unicode  # pylint: disable=E0602
    byte_str_type = str
    byte_stdin = sys.stdin
    byte_stdout = sys.stdout
    byte_stderr = sys.stderr
    py2bstr = b_str
    py2ustr = u_str
    py3bstr = str
    py3ustr = str
    py3ustrlist = lambda l: l
else:
    isPy3 = True
    text_str_type = str
    byte_str_type = bytes
    byte_stdin = sys.stdin.buffer
    byte_stdout = sys.stdout.buffer
    byte_stderr = sys.stderr.buffer
    py2bstr = str
    py2ustr = str
    py3bstr = b_str
    py3ustr = u_str
    py3ustrlist = lambda l: [u_str(x) for x in l]


# -----------------------------------------------------------------------------
def to_text_string(data):
    if isinstance(data, text_str_type):
        return data
    if isinstance(data, byte_str_type):
        return u_str(data)
    try:
        return py2ustr(str(data))
    except BaseException:
        raise TypeError(
            "object of type '{}' does not support text string "
            "conversion".format(type(data))
        )


# -----------------------------------------------------------------------------
def to_byte_string(data):
    if isinstance(data, byte_str_type):
        return data
    if isinstance(data, text_str_type):
        return b_str(data)

    if isPy3:
        try:
            return bytes(data)
        except BaseException:
            pass

    try:
        return py3bstr(str(data))
    except BaseException:
        raise TypeError(
            "object of type '{}' does not support byte string "
            "conversion".format(type(data))
        )


# -----------------------------------------------------------------------------
def to_native_string(data):
    return to_text_string(data) if isPy3 else to_byte_string(data)


# vim: ts=4 et tw=79
