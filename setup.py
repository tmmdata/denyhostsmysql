#!/usr/bin/env python
# Copyright 2005-2006 (C) Phil Schwartz <phil_schwartz@users.sourceforge.net>
# Copyright 2014 (C) Jesse Smith <jessefrgsmith@yahoo.ca>
# Copyright 2017 (C) Jose' Vargas <jose.vargas@tmmdata.com>

from glob import glob
from os.path import join as ospj

from distutils.core import setup

from DenyHostsMySQL.util import normalize_whitespace
from DenyHostsMySQL.version import VERSION

etcpath = "/etc"
manpath = "/usr/share/man/man8"
libpath = "/usr/share/denyhostsmysql"
scriptspath = ospj("scripts", libpath)
pluginspath = ospj("plugins", libpath)

setup(
    name="DenyHostsMySQL",
    version=VERSION,
    description="DenyHostMySQL is a utility to help sys admins thwart mysql hackers.  This was forked from Denyhosts made by Jessie Smith",
    author="Jose' Vargas",
    author_email="jose.vargas@tmmdata.com",
    url="http://github.com/tmmdata/denyhostsmysql",
    scripts=['denyhostsmysql.py', 'daemon-control-dist'],
    package_dir={'DenyHostsMySQL': 'DenyHostsMySQL'},
    packages=["DenyHostsMySQL"],
    requires=["ipaddr"],
    data_files=[
        (etcpath, glob("denyhostsmysql.conf")),
        (manpath, glob("denyhostsmysql.8")),
    ],
    license="GPL v2",
    long_description=normalize_whitespace(
        """
        DenyHostsMySQL is a python program that automatically blocks MySQL attacks
        by adding entries to /etc/hosts.deny. DenyHostsMySQL will also inform
        administrators about offending hosts, attacked users and suspicious
        logins. Originally written by Phil Schwartz. Expanded by Jessie Smith
        """
    ),
)
