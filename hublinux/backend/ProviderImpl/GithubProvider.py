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

import git

from gi.repository import GLib

from hublinux.backend.ProviderImpl import Provider, SourceProvider, RepositoryProvider
from hublinux.backend.Github import Github

from hublinux.EventBus import LoadingEventBus

class GithubProvider(Provider):
    @property
    def sources(self):
        user = Github.getGithub().get_user()
        result = [GithubSourceProvider(user)]
        for org in user.get_orgs():
            result.append(GithubSourceProvider(org))

        return result

class GithubSourceProvider(SourceProvider):

    def __init__(self, source):
        self.source = source
        super(GithubSourceProvider, self).__init__()

    @property
    def name(self):
        return self.source.login

    @property
    def image(self):
        return Github.getAvatarPixbuf(self.source, (24, 24))

    def _doScanRepositories(self):
        LoadingEventBus().start()
        for repo in self.source.get_repos():
            self._findRepository(repo)
        LoadingEventBus().stop()

    def _getRepositoryProvider(self, repo):
        return GithubRepositoryProvider(repo)

class GithubRepositoryProvider(RepositoryProvider):
    def __init__(self, repository):
        self.repository = repository

    @property
    def id(self):
        return self.repository.id

    @property
    def name(self):
        return self.repository.full_name

    @property
    def description(self):
        return self.repository.description

    def doClone(self, dir):
        return git.Repo.clone_from(self.repository.git_url, dir)
