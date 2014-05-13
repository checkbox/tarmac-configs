#!/usr/bin/python
# Copyright 2014 Canonical Ltd.
# Written by:
#   James Westby <james.westby@canonical.com>
#
# Originally part of the tarmac charm at
# http://launchpad.net/~james-w/charms/precise/tarmac/trunk/
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License version 3, as published by the
# Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.



import subprocess
import sys

from launchpadlib.credentials import Credentials

web_root="https://launchpad.net/"

creds = Credentials("tarmac")
url = creds.get_request_token(web_root=web_root)

subprocess.call(['xdg-open', url])
print("Once you have authenticated then press enter")
sys.stdin.readline()
creds.exchange_request_token_for_access_token(web_root=web_root)

f = open("credentials", "wb")
try:
    creds.save(f)
finally:
    f.close()
