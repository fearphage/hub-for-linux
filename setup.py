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

import glob
import setuptools

VERSION = "0.0.1"

setuptools.setup(
    name="hub:linux",
    version=VERSION,
    description="Github for Linux",
    author="Peter Golm",
    author_email="golm.peter@gmail.com",
    url="https://github.com/pgolm/hub-for-linux",
    packages=[
        "assets",
        "data",
        "data.schema",
        "hublinux",
        "hublinux.backend",
        "hublinux.backend.ProviderImpl",
        "hublinux.ui",
        "hublinux.ui.app",
        "hublinux.ui.assistant",
        "hublinux.ui.menu",
        "hublinux.ui.panel",
        "hublinux.ui.widgets",
        "hublinux.ui.widgets.repositorylist",
        "hublinux.ui.widgets.sourcelist",
        "hublinux.ui.widgets.toolbar",
    ],
    package_data={
        'assets': ['*'],
        'data': ['schema/*']},
    py_modules=["hublinux"],
    scripts=["hublinux.py"],
)