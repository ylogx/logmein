#!/usr/bin/env python3
#
#   update.py - Update logmein from web
#   Copyright (c) 2014 Shubham Chaudhary <me@shubhamchaudhary.in>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import sys, urllib
import os, platform, os.path
import urllib.error

if sys.version_info >= (3, ):
    import urllib.request as urllib2
    import urllib.parse as urlparse
else:
    import urllib2
    import urlparse


def main(argv):
    default_credential_files = [
        os.path.join(os.path.expanduser('~'), '.login.txt'),
        os.path.join(os.path.expanduser('~'), 'login.txt'),
        os.path.join(os.path.expanduser('.'), '.login.txt'),
        os.path.join(os.path.expanduser('.'), 'login.txt')
    ]

    # Parse command line arguments
    from optparse import OptionParser
    usage = "%prog [-f credential_file]"
    parser = OptionParser(usage=usage, version="%prog 1.0")
    parser.add_option("-f", "--file",
                      type='str',
                      dest="file",
                      help="Use the specified file")
    parser.add_option(
        "-i", "--login",
        action='store_true',
        dest="login",
        help=
        "Login <Default behaviour except that it randomizes crypt password, better if you want to hide password>")
    parser.add_option("-o", "--logout",
                      action='store_true',
                      dest="logout",
                      help="Logout")
    (options, args) = parser.parse_args()
    argc = len(args)

    try:
        update_logme()
    except:
        raise
    return 0


if __name__ == '__main__':
    try:
        main(sys.argv)
        if os.name == 'nt' or platform.system() == 'Windows':
            input('Press Enter or Close the window to exit !')
    except KeyboardInterrupt:
        print('\nClosing garacefully :)', sys.exc_info()[1])
    except urllib.error.HTTPError:
        print('HTTP Error:', sys.exc_info()[1])
    ### TODO: Handle other errors
    except SystemExit:
        pass
    except:
        print('Unexpected Error:', sys.exc_info()[0], '\nDetails:',
              sys.exc_info()[1])
#         raise;
