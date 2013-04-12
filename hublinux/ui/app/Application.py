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
import logging
from gettext import gettext as _

from gi.repository import GLib, Gtk, Gio, Notify

from hublinux.Constant import APP_ID, APP_NAME, ROOT_DIR

from hublinux.ui.menu.AppMenu import AppMenu
from hublinux.ui.app.Window import Window

from hublinux.ui.assistant import InitialSetupAssistant

from hublinux.Config import HubLinuxConfig

LOG = logging.getLogger(__name__)

class Application(Gtk.Application):
    def __init__(self):
        super(Application, self).__init__()

        self.appMenu = AppMenu(self)
        self.set_application_id(APP_ID)
        self.set_flags(Gio.ApplicationFlags.HANDLES_COMMAND_LINE)

        # BUG: signal 'open' can't handle well
        # Workaround: parse cli's self
        self.connect('command-line', self.__onCommands)

    @property
    def window(self):
        return self.appWindow

    def __onCommands(self, app, args):
        # try to start gui
        self.do_activate()

        #parse args
        argv = args.get_arguments()
        if(len(argv) > 1):
            self.window.openRepository(argv[1])

        return False
        
    def do_activate(self):
        # only one instance
        if len(self.get_windows()) > 0:
            self.window.present(); # main window to foreground
            return

        # start setup if no login
        if not HubLinuxConfig().hasLogin:
            loop = GLib.MainLoop(GLib.main_context_default())
            assistance = InitialSetupAssistant(loop)
            assistance.show()
            loop.run()

        # setup canceled?
        if HubLinuxConfig().hasLogin:
            self.set_app_menu(self.appMenu)
            self.appWindow = Window(self)

            self.provider = Gtk.CssProvider()
            self.provider.load_from_path(ROOT_DIR + "/data/style.css")
            screen = self.appWindow.get_screen()

            self.appWindow.get_style_context().add_provider_for_screen(screen, self.provider, 1000)

            self.appWindow.show_all()
        else:
            LOG.warning("No login credentials -> Exit")

    def do_startup(self):
        Gtk.Application.do_startup(self)