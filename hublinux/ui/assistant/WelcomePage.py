# -*- coding: utf-8 -*-
# Copyright (C) 2013 Peter Golm
#
# Authors:
#  Peter Golm <golm.peter@gmail.com>
#
# This file is part of hub:linux.
#
# hub:linux is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; version 3.
#
# hub:linux is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

from gettext import gettext as _

from gi.repository import Gtk

class WelcomePage(Gtk.Grid):
    def __init__(self):
        super(WelcomePage, self).__init__()

        self.set_row_spacing(25)

        self.__initUi()

    def __initUi(self):
        self.logoImage = Gtk.Image()
        self.logoImage.set_from_file("./data/images/logo.png")
        self.attach(self.logoImage, 0, 0, 1, 1)

        self.welcomeText = Gtk.Label(_('Welcome to hub:linux! You need to setup your github account first.'))
        self.attach(self.welcomeText, 0, 1, 1, 1)