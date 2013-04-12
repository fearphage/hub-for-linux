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

from gi.repository import Gio

import os
import keyring # use gtk 2.0 api -> bad!

from hublinux.Constant import APP_ID, ROOT_DIR

class HubLinuxConfig(object):
    def __new__(type, *args):
        if not '_the_instance' in type.__dict__:
            type._the_instance = object.__new__(type)
        return type._the_instance

    def __init__(self):
        if not '_ready' in dir(self):
            schema_source = Gio.SettingsSchemaSource.new_from_directory(
                os.path.expanduser(ROOT_DIR + "/data/schema"),
                Gio.SettingsSchemaSource.get_default(),
                False,
            )
            schema = schema_source.lookup('hublinux.config', False)
            self.settings = Gio.Settings.new_full(schema, None, None)
            self._ready = True

    def sync(self):
        """
        write all changed settings
        """
        self.settings.sync()

    @property
    def hasLogin(self):
        return self.login != ""

    login = property(
        lambda self: self.settings.get_string('github-login'),
        lambda self, value: self.settings.set_string('github-login', value),
        None,
        "Define the login (username/email) for github."
    )

    password = property(
        lambda self: keyring.get_password(APP_ID, self.login),
        lambda self, value: keyring.set_password(APP_ID, self.login, value),
        None,
        "Password for github."
    )

    def clearCredentials(self):
        """
        delete login and password
        """
        self.login = ""
        self.password = ""
        self.sync()

    gitPath = property(
        lambda self: self.settings.get_string('git-path'),
        lambda self, value: self.settings.set_string('git-path', value),
        None,
        "Path to local git directories."
    )
