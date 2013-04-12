# -*- coding: utf-8 -*-
# Copyright (C) 2013 Peter Golm
#
# Authors:
#  Peter Golm <golm.peter@gmail.com>
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; version 3.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

import os
import sys

ROOT_DIR = os.path.abspath(os.path.dirname(__file__) + '/../' )

APP_ID = "app.hub4linux"
APP_NAME = "hub:linux"

APP_DIR = os.path.expanduser("~/.hub4linux")
DATABASE_FILE = APP_DIR + "data.db"
CACHE_DIR = APP_DIR + "/cache"

WINDOW_SIZE = (800,600)

ASSISTANCE_SIZE = (600,300)