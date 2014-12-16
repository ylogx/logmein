#!/usr/bin/env python3
#
#   logmein.py - Automatically log into Panjab University Wifi Network
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


import atexit
import os
import platform
import random
import re
import sys

from argparse import ArgumentParser

if sys.version_info >= (3,):
    import urllib.request as urllib2
    import urllib.parse as urlparse
    import urllib.error as urlerror
else:
    import urllib2
    import urlparse

class StatusCode:
    UNKNOWN_ERROR       = -3
    INPUT_ERROR         = -2
    CONNECTION_ERROR    = -1
    SUCCESS             = 0
    LOGGED_IN           = 0
    AUTH_ERROR          = 1
    MULTIPLE_LOGIN      = 2

def login_pucampus(username, password):
    ''' Perform login '''
    url = 'https://securelogin.arubanetworks.com/cgi-bin/login?cmd=login'
    values = {'user' : username,
              'password' : password}
    # Create request
    data = urlparse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib2.Request(url, data)
    # Send request
    try:
        response = urllib2.urlopen(req)         #res.geturl(), .url=str, .status=200, .info=200, .msg=OK,
    except urlerror.HTTPError as exep:
        print('The server couldn\'t fulfill the request.',
              'Error code: ', exep.code)
        print('You\'re probably logged in!')
        return StatusCode.LOGGED_IN
    except urlerror.URLError as exep:
        print('We failed to reach a server.')
        print('Reason: ', exep.reason)
        return StatusCode.CONNECTION_ERROR
    else:
        # everything is fine
        the_page = str(response.read()) # More pythonic than .decode('utf-8')
        # Parse for success or failure
        match = re.search('Authentication failed', the_page)
        if match:
            print('Authentication failed.')
            print('Maybe your username or password is wrong.')
            return StatusCode.AUTH_ERROR
        success = re.search('External Welcome Page', the_page)
        if success:
            print('Authentication Success. You\'re logged in')
            return StatusCode.SUCCESS
        if re.search('Only one user login session is allowed', the_page):
            print('Only one user login session is allowed')
            return StatusCode.MULTIPLE_LOGIN

def logout_pucampus():
    ''' Perform logout '''
    print('Sending logout request')
#     url = 'http://172.16.4.204/cgi-bin/login'
#     data = urlparse.urlencode({'cmd' : 'logout' })
#     full_url = url + '?' + data
#     req = urllib2.Request(full_url)         #req.full_url,
    # Send request
    try:
        #response = urllib2.urlopen(full_url)
        #res.geturl(), .url=str, .status=200, .info=200, .msg=OK,
        response = urllib2.urlopen(
                'https://securelogin.arubanetworks.com/cgi-bin/login?cmd=logout'
                )
    except urlerror.HTTPError as exep:
        print('The server couldn\'t fulfill the request.',
              'Error code: ', exep.code)
    except urlerror.URLError as exep:
        print('We failed to reach a server.')
        print('Reason: ', exep.reason)
    else:
        # everything is fine
        the_page = str(response.read()) # More pythonic than .decode('utf-8')
        # Parse for success or failure
        if re.search('Logout', the_page):
            print('Logout successful')
            return StatusCode.SUCCESS
        elif re.search('User not logged in', the_page):
            print('You\'re not logged in')
            return StatusCode.SUCCESS
        else:
            print(the_page)
            return StatusCode.UNKNOWN_ERROR

def parse_file_for_credential(filename):
    ''' Parses the input file for login credentials
    '''
    try:
        fhan = open(filename, 'rU')
    except FileNotFoundError:
        print('Create a file named login.txt or .login.txt in home folder')
        print('type your username and password in seperate lines.')
        print('e.g. for user 11uit424 with password blaboo,',
              'file will be like this')
        print('\n11uit424')
        print('The_Password123')
        raise
    except KeyboardInterrupt:
        fhan.close()
        raise
    username = fhan.readline().strip()
    password = fhan.readline().strip()
    fhan.close()
    return (username, password)

def print_usage():
    ''' Simpler usage message '''
    print('Usage: ', sys.argv[0], ' [filename <Default: .login.txt>] || [password] || [username password]')

def print_help():
    ''' Print a better help message '''
    print('--------- PU@CAMPUS Auto Login Help ---------')
    print_usage()
    text = [
        'There are several ways to use this software.',
        ' * Create a file named .login.txt in your home directory and save your credentials in that.',
        '   Using . in front of filename will make it hidden file. If you want to use some other name/folder and specify it as a command line argument.',
        ' * Simply type your username and password in the command line. If you\'ve special character in password (e.g bl@b00$), type it in quotes(\'bl@boo$\'or "bl@boo$" when using command line arguments',
        ' * You may also automate it to run with your browser, so that everytime you open the browser it logs you in.',
        '       1. Create a batch file (e.g \'magic.bat\') and type:',
        '           start "C:/Python3/python.exe D:/Path/To/your/script"',
        '           start /d "C:/Program Files (x86)/Mozilla Firefox" firefox.exe',
        '       2. Save this and note down the proper path to this file (e.g D://Study/hidden/mystuff/magic.bat)',
        '       3. Click on properties in mozilla shortcut',
        '       4. Change the path from C://Program Files/Mozilla/firefox.exe to your batch file location',
        ]
    for line in text:
        print(line)

def main():
    ''' Main function '''
    default_credential_files = [
        os.path.join(os.path.expanduser('~'), '.login.txt'),
        os.path.join(os.path.expanduser('~'), 'login.txt'),
        os.path.join(os.path.expanduser('.'), '.login.txt'),
        os.path.join(os.path.expanduser('.'), 'login.txt'),
        ]

    # Parse command line arguments
    #usage = "%prog [-f credential_file]"
    #parser = ArgumentParser(usage=usage)
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", type=str, dest="file",
                        help="Use the specified file")
    parser.add_argument("-i", "--login", action='store_true', dest="login",
                        help='Login <Default behaviour except that it '
                            'randomizes crypt password, better if you want to '
                            'hide password>')
    parser.add_argument("-o", "--logout", action='store_true', dest="logout",
                        help="Logout")
    #parser.add_argument('otherthings', nargs='*')
    #args = parser.parse_args()
    args, otherthings = parser.parse_known_args()
    argc = len(otherthings)

    username = ''
    password = ''
    if args.file != None:
        username, password = parse_file_for_credential(args.file)
    elif args.logout:
        try:
            logout_pucampus()
        except:
            raise
        return
    else:   #Only file option used in shopt right now, so 'else'
        if not otherthings:
            for default_file in default_credential_files:
                if os.path.isfile(default_file):
                    username, password = parse_file_for_credential(default_file)
                    break
        elif argc == 1:
            if os.path.isfile(otherthings[0]):
                username, password = parse_file_for_credential(otherthings[0])
            else:
                print_usage()
                return
        elif argc == 2:
            username = otherthings[0]
            password = otherthings[1]
        else:
            print_usage()
            return

    # Check input
    if not username:
        print('FATAL ERROR: No username specified')
        print('Check your login file or command syntax')
        return StatusCode.INPUT_ERROR
    if not password:
        print('FATAL ERROR: No password specified')
        print('Check your login file or command syntax')
        return StatusCode.INPUT_ERROR
    elif ((password[0] == "'" and password[-1] == "'")
          or (password[0] == '"' and password[-1] == '"')):
        print('Note: You don\'t need to put quotes in the credential text file')
        password = password[1:-1]

    # Show some details to user
    if args.login:
        crypt_password = '*' * random.randint(len(password), 3*len(password))
    else:
        crypt_password = password[0]
        for _ in range(1, len(password)-1):
            crypt_password += '*'
        crypt_password += password[-1]
    print('Sending request to login with', username, '&', crypt_password)

    try:
        return login_pucampus(username, password)
    except:
        raise
    return 0

def stop_for_windows():
    ''' If on windows platform, stop and wait for input
    '''
    if os.name == 'nt' or platform.system() == 'Windows':
        input('Press Enter or Close the window to exit !')

if __name__ == '__main__':
    # Run this function everytime on exit
    atexit.register(stop_for_windows)
    try:
        return_code = main()
        sys.exit(return_code)
    except KeyboardInterrupt:
        print('\nClosing garacefully :)', sys.exc_info()[1])
    except urlerror.HTTPError:
        print('HTTP Error:', sys.exc_info()[1])
    #TODO: Handle other errors
    except SystemExit:
        pass
    except:
        print('Unexpected Error:', sys.exc_info()[0])
        print('Details:', sys.exc_info()[1])
        #raise
