# -*- coding: utf-8 -*-
#
# mididings
#
# Copyright (C) 2008-2009  Dominic Sacré  <dominic.sacre@gmx.de>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#

from mididings import *


_BLACK = [1, 3, 6, 8, 10]
_BLACK_KEYS = [_n for _n in range(128) if _n%12 in _BLACK]
_WHITE_KEYS = [_n for _n in range(128) if _n%12 not in _BLACK]


def BlackKeys():
    return Fork([
            KeyFilter(n) for n in _BLACK_KEYS
        ], NOTE)


def WhiteKeys():
    return Fork([
            KeyFilter(n) for n in _WHITE_KEYS
        ], NOTE)
