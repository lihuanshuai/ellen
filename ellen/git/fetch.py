#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ellen.utils.process import git_with_repo


def fetch_repository(repository, **kw):
    git = git_with_repo(repository)
    git.fetch(**kw)

