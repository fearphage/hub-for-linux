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

import logging
from gettext import gettext as _

from gi.repository import Gtk

from hublinux.Constant import APP_NAME, ROOT_DIR, WINDOW_SIZE
from hublinux.ui.app.StatusIcon import StatusIcon
from hublinux.ui.widgets.toolbar import Toolbar
from hublinux.ui.panel.MainPanel import MainPanel
from hublinux.ui.dialog.CloneDialog import CloneDialog

from hublinux.backend.Github import Github
from hublinux.backend.ProviderImpl.GithubProvider import GithubRepositoryProvider


LOG = logging.getLogger(__name__)

class Window(Gtk.ApplicationWindow):

    def __init__(self, app):
        super(Window, self).__init__(application=app)
        self.application = app
        self.statusIcon = StatusIcon(self.application)
        self.layout = Gtk.Box()
        self.toolBar = Toolbar(self.application)

        self.mainPanel = MainPanel()

        self.set_default_size(WINDOW_SIZE[0], WINDOW_SIZE[1])
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_icon_from_file(ROOT_DIR + "/data/images/icon.png")
        self.set_title(APP_NAME)

        self.__initUI()
        self.__initSignals()

    def __initUI(self):
        """
        initialize the UI
        """
        self.layout.set_orientation(Gtk.Orientation.VERTICAL)
        self.layout.pack_start(self.toolBar, False, True, 0)
        self.layout.pack_start(self.mainPanel, True, True, 0)
        self.add(self.layout)

    def __initSignals(self):
        self.connect('delete-event', self.__onHide)# hide on close button

    def __onHide(self, *args):
        self.hide()
        return args

    def openRepository(self, name):
        LOG.info("Open Repository:" + name)

        #FIXME: first QUICK&DIRTY implementation
        #need better url parsing
        startPos = name.find("github.com/")
        if startPos > -1:
            parts = name[startPos:].split('/')

            userName = parts[1]
            repoName = parts[2]

            try:
                rawRepo = Github().getGithub().get_user(userName).get_repo(repoName)
                repo = GithubRepositoryProvider(rawRepo)
                dlg = CloneDialog(repo)
                dlg.run()
                dlg.destroy()

            except Exception:
                messageDlg = Gtk.MessageDialog(
                    self,
                    Gtk.DialogFlags.MODAL,
                    Gtk.MessageType.ERROR,
                    Gtk.ButtonsType.OK,
                    _('Something went wrong with %s.') % name)
                messageDlg.run()
                messageDlg.destroy()
        else:
            messageDlg = Gtk.MessageDialog(
                self,
                Gtk.DialogFlags.MODAL,
                Gtk.MessageType.ERROR,
                Gtk.ButtonsType.OK,
                _('Wrong URL: %s.') % name)
            messageDlg.run()
            messageDlg.destroy()