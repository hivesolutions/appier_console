#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Appier Framework
# Copyright (c) 2008-2018 Hive Solutions Lda.
#
# This file is part of Hive Appier Framework.
#
# Hive Appier Framework is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Appier Framework is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Appier Framework. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2018 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import os
import sys

def is_tty(stream = sys.stdout):
    """
    Verifies if the provided stream is capable of a TTY like
    interaction (input and output).

    Otherwise its considered to be an output only stream.

    :type stream: Stream
    :param stream: The stream to be tested for TTY like capabilities.
    :rtype: bool
    :return: If the provided stream is TTY capable.
    :see: https://en.wikipedia.org/wiki/Teleprinter
    """

    return hasattr(stream, "isatty") and stream.isatty()

def is_color():
    plat = sys.platform
    supported_platform = not plat == "Pocket PC" and\
        (not plat == "win32" or "ANSICON" in os.environ)
    if not supported_platform or not is_tty(): return False
    return True
