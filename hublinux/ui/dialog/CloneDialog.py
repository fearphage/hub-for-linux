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

from gettext import gettext as _

from gi.repository import Gtk

from hublinux.Config import HubLinuxConfig
class CloneDialog(Gtk.Dialog):

    def __init__(self, repo):
        super(CloneDialog, self).__init__()
        self.repository = repo

        self.__initUI()

    def __initUI(self):
        exists = os.path.exists(self.directory)

        if exists:
            text = _("%s already exist, please remove/rename the directory.") % self.directory
        else:
            text = _("Clone to %s?") % self.directory

        label = Gtk.Label(text)

        box = self.get_content_area()
        box.add(label)

        if not exists:
            self.add_button(Gtk.STOCK_OK, Gtk.ResponseType.OK)

        self.add_button(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL)
        self.show_all()

    def run(self):
        response = super(CloneDialog, self).run()

        #clone
        if response == Gtk.ResponseType.OK:
            self.repository.doClone(self.directory)

        return response

    @property
    def directory(self):
        return os.path.join(HubLinuxConfig().gitPath, self.repository.cloneName)