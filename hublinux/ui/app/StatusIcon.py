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

from gettext import gettext as _

from gi.repository import Gtk

from hublinux.Constant import ROOT_DIR

class StatusIcon(Gtk.StatusIcon):
    def __init__(self, app):
        super(Gtk.StatusIcon, self).__init__()
        self.application = app
        self.menu = Gtk.Menu()

        self.set_from_file(ROOT_DIR + "/data/images/icon.png")
        self.__initMenu()
        self.connect("popup-menu", self.__onMenuShow)

    def __initMenu(self):
        # show/hide
        showHide = Gtk.MenuItem(_("Show/Hide"))
        showHide.connect("activate", self.__onShowHide)
        self.menu.append(showHide)
        self.menu.append(Gtk.SeparatorMenuItem())

        # quit
        quit = Gtk.MenuItem(_("Quit"))
        quit.connect("activate", self.__onQuit)
        self.menu.append(quit)

    def __onMenuShow(self, icon, button, time):
        self.menu.show_all()

        def pos(menu, icon):
            return Gtk.StatusIcon.position_menu(menu, icon)
        self.menu.popup(None, None, pos, self, button, time)

    def __onShowHide(self, *args):
        """
        toggle the app-window between show/hide
        """
        if self.application.window.get_visible():
            self.application.window.hide()
        else:
            self.application.window.show()

    def __onQuit(self, *args):
        """
        quit the application
        """
        self.application.quit()
