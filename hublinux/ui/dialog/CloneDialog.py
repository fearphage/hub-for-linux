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

import os
import logging
from threading import Thread

from gettext import gettext as _

from gi.repository import Gtk, GLib

from hublinux.Config import HubLinuxConfig

LOG = logging.getLogger(__name__)

class CloneDialog(Gtk.Dialog):

    def __init__(self, repo):
        super(CloneDialog, self).__init__()
        self.repository = repo
        self.__directory = None

        self.__initUI()

    def __initUI(self):
        box = self.get_content_area()

        self._infoLabel = Gtk.Label()
        box.add(self._infoLabel)

        layout = Gtk.Box()

        layout.add(Gtk.Label(_('Change base directory: ')))
        self._dirButton = Gtk.FileChooserButton()
        self._dirButton.set_title(_('Change the base directory'))
        self._dirButton.set_action(Gtk.FileChooserAction.SELECT_FOLDER)
        self._dirButton.set_current_folder(os.path.split(self.directory)[0])
        self._dirButton.connect('current-folder-changed', self.__onSelectFile)
        layout.pack_start(self._dirButton, True, True, 0)

        box.add(layout)

        self.add_button(Gtk.STOCK_OK, Gtk.ResponseType.OK)
        self.add_button(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL)
        self.__loadUI()

    def __loadUI(self):
        isOK = self.validatDirectory()

        if not isOK:
            text = _("Clone directory already exist and is not empty.")
        else:
            text = _("Clone to %s?") % self.directory

        self._infoLabel.set_text(text)

        self.get_widget_for_response(Gtk.ResponseType.OK).set_sensitive(isOK)

        self.show_all()

    def __onSelectFile(self, btn, *args):
        self.directory = btn.get_current_folder()
        self.__loadUI()

    def run(self):
        response = super(CloneDialog, self).run()

        #clone
        def asyncClone(self):
            #TODO: need better UI indicator
            LOG.info('Clone to %s' % self.directory)
            self.repository.doClone(self.directory)
            LOG.info('Cloning done!')

            def showDlg():
                messageDlg = Gtk.MessageDialog(
                    self,
                    Gtk.DialogFlags.MODAL,
                    Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK,
                    _('Cloning repository %s to %s finished.') % (self.repository.name, self.directory))
                messageDlg.run()
                messageDlg.destroy()

            GLib.idle_add(showDlg)

        if response == Gtk.ResponseType.OK:
            Thread(target=asyncClone, args=(self,)).start()

        return response

    def validatDirectory(self):
        return (not os.path.exists(self.directory)) or (os.path.isdir(self.directory) and len(os.listdir(self.directory)) == 0)

    @property
    def directory(self):
        if self.__directory is None:
            basePath =  HubLinuxConfig().gitPath
        else:
            basePath = self.__directory

        return os.path.join(basePath, self.repository.cloneName)

    @directory.setter
    def directory(self, dir):
        self.__directory = dir