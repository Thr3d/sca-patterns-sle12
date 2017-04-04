#!/usr/bin/python
#
# Title:       Important Security Announcement for util-linux SUSE-SU-2017:0555-1
# Description: Security fixes for SUSE Linux Enterprise 12 SP1
# Source:      Security Announcement Parser v1.3.6
# Modified:    2017 Apr 04
#
##############################################################################
# Copyright (C) 2017 SUSE LLC
##############################################################################
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
#  Authors/Contributors:
#   Jason Record (jason.record@suse.com)
#
##############################################################################

import os
import Core
import SUSE

META_CLASS = "Security"
META_CATEGORY = "SLE"
META_COMPONENT = "util-linux"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2017-02/msg00040.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'util-linux'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2017:0555-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 12):
	if ( SERVER['DistroPatchLevel'] == 1 ):
		PACKAGES = {
			'libblkid-devel': '2.25-40.1',
			'libblkid1': '2.25-40.1',
			'libblkid1-32bit': '2.25-40.1',
			'libblkid1-debuginfo': '2.25-40.1',
			'libblkid1-debuginfo-32bit': '2.25-40.1',
			'libmount-devel': '2.25-40.1',
			'libmount1': '2.25-40.1',
			'libmount1-32bit': '2.25-40.1',
			'libmount1-debuginfo': '2.25-40.1',
			'libmount1-debuginfo-32bit': '2.25-40.1',
			'libsmartcols-devel': '2.25-40.1',
			'libsmartcols1': '2.25-40.1',
			'libsmartcols1-debuginfo': '2.25-40.1',
			'libuuid-devel': '2.25-40.1',
			'libuuid1': '2.25-40.1',
			'libuuid1-32bit': '2.25-40.1',
			'libuuid1-debuginfo': '2.25-40.1',
			'libuuid1-debuginfo-32bit': '2.25-40.1',
			'python-libmount': '2.25-40.2',
			'python-libmount-debuginfo': '2.25-40.2',
			'python-libmount-debugsource': '2.25-40.2',
			'util-linux': '2.25-40.1',
			'util-linux-debuginfo': '2.25-40.1',
			'util-linux-debugsource': '2.25-40.1',
			'util-linux-lang': '2.25-40.1',
			'util-linux-systemd': '2.25-40.1',
			'util-linux-systemd-debuginfo': '2.25-40.1',
			'util-linux-systemd-debugsource': '2.25-40.1',
			'uuidd': '2.25-40.1',
			'uuidd-debuginfo': '2.25-40.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

