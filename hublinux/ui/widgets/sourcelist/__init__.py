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

import threading
from gettext import gettext as _

from gi.repository import Gtk, GLib

from hublinux.backend.Provider import GithubProvider

class SourceList(Gtk.Box):
    def __init__(self):
        super(SourceList, self).__init__()
        self.set_orientation(Gtk.Orientation.VERTICAL)
        self.sourceSelectListeners = []

        # dummy button to group all buttons
        self.groupBtn = Gtk.RadioButton()

        self.localSourceBox = Gtk.Box()
        self.githubSourceBox = Gtk.Box()

        self.githubProvider = GithubProvider()

        self.__initUI()

    def __initUI(self):
        # init local
#        title = Gtk.Label()
#        text = "<span size=\"larger\">%s</span>" % _('local')
#        title.set_markup(text)
#
#        box = Gtk.Box()
#        box.pack_start(title, False, True, 0)
#        box.pack_start(Gtk.Label(), True, True, 0)
#        self.pack_start(box, False, True, 0)
#
#        self.pack_start(self.localSourceBox, False, True, 0)

        # init github
        title = Gtk.Label()
        text = "<span size=\"larger\">%s</span>" % _('github')
        title.set_markup(text)

        box = Gtk.Box()
        box.pack_start(title, False, True, 0)
        box.pack_start(Gtk.Label(), True, True, 0)
        self.pack_start(box, False, True, 0)

        self.githubSourceBox.set_orientation(Gtk.Orientation.VERTICAL)
        self.pack_start(self.githubSourceBox, False, True, 0)

    def addSourceSelectListener(self, listener):
        """
        the listener is registered after call loadSources
        """
        assert callable(listener)
        if listener not in self.sourceSelectListeners:
            self.sourceSelectListeners.append(listener)


    def loadSources(self):
        #clean buttons
        for widget in self.githubSourceBox.get_children():
            widget.remove()

        def asyncGithub(self):
            for source in self.githubProvider.sources:
                image = Gtk.Image()
                image.set_from_pixbuf(source.image)

                btn = self.__createSourceButton(source.name, image)

                for listener in self.sourceSelectListeners:
                    btn.connect('toggled', listener, source)

                GLib.idle_add(self.githubSourceBox.pack_start, btn, True, True, 0)
            GLib.idle_add(self.githubSourceBox.show_all)

        threading.Thread(target=asyncGithub, args=(self, )).start()

    def __createSourceButton(self, label, image):
        sourceBtn = Gtk.RadioButton()
        sourceBtn.join_group(self.groupBtn)
        sourceBtn.set_label(" " + label + " ")
        sourceBtn.set_mode(False) # disable draw-indicator
        sourceBtn.set_relief(Gtk.ReliefStyle.NONE)

        sourceBtn.set_image(image)
        sourceBtn.set_always_show_image(True)
        return sourceBtn