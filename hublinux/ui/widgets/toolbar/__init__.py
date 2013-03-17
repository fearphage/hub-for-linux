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

from gi.repository import Gtk

from MenuButtonItem import MenuButtonItem

class Toolbar(Gtk.Toolbar):

    def __init__(self):
        super(Gtk.Toolbar, self).__init__()
        self.__initUI()

    def __initUI(self):
        separator = Gtk.SeparatorToolItem()
        separator.set_expand(True)
        self.insert(separator, -1)

        self.menuItem = MenuButtonItem()
        self.insert(self.menuItem, -1)