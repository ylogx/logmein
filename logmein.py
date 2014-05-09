#!/usr/bin/python3
#  auto_login_wifi.py
#
#  Copyright 2014 Shubham Chaudhary <shubham.chaudhary@kdemail.net>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

import sys,re,urllib
import os.path

if sys.version_info >= (3,):
    import urllib.request as urllib2
    import urllib.parse as urlparse
else:
    import urllib2
    import urlparse


def login_pucampus(username,password):
    url = 'http://172.16.4.204/cgi-bin/login'
    values = {'user' : username,
              'password' : password }

    data = urlparse.urlencode(values)
    data = data.encode('utf-8');
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read().decode('utf-8');


    #Parse for success or failure
    match = re.search('Authentication failed',the_page);
    if match:
        print('Authentication failed. Maybe your username or password is wrong.');
    success = re.search('External Welcome Page',the_page);
    if success:
       print('Authentication Success. You\'re logged in');
    if re.search('Only one user login session is allowed',the_page):
        print('Only one user login session is allowed');

def logout_pucampus():
    url = 'http://172.16.4.204/cgi-bin/login?cmd=logout'
    print('Sending logout request');
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read().decode('utf-8');

    if re.search('Logout',the_page):
        print ('Logout successful');
    elif re.search('User not logged in',the_page):
        print('You\'re not logged in');


def parse_file_for_credential(filename):
    try:
        f = open(filename,'rU');
    except FileNotFoundError:
        print('Create a file named login.txt or .login.txt in home folder and type your username and password in seperate lines.');
        print('e.g. for user 11uit424 with password blaboo, file will be like this');
        print('\n11uit424');
        print('The_Password123');
        raise
        return
    except KeyboardInterrupt:
        f.close();
        raise;
    username = f.readline().strip();
    password = f.readline().strip();
    f.close();
    return (username, password);

def print_usage():
    print('Usage: ',sys.argv[0],' [filename <Default: .login.txt>] || [password] || [username password]');

def print_help():
    print('--------- PU@CAMPUS Auto Login Help ---------');
    print_usage();
    text = ['There are several ways to use this software.',
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
        print(line);

def main(argv):
    default_credential_files = [ os.path.join(os.path.expanduser('~'),'.login.txt'),
                                os.path.join(os.path.expanduser('~'),'login.txt') ]

    # Parse command line arguments
    from optparse import OptionParser
    usage = "%prog [-f credential_file]";
    parser = OptionParser(usage=usage, version="%prog 1.0")
    parser.add_option("-f", "--file", type='str', dest="file", help="Use the specified file")
    parser.add_option("-o", "--logout", action='store_true', dest="logout", help="LogOut")
    (options, args) = parser.parse_args()
    argc = len(args);

    username = ''; password = '';
    if options.file != None:
        username, password = parse_file_for_credential(options.file);
    elif options.logout:
        try:
            logout_pucampus();
        except:
            raise;
        return;
    else:   #Only file option used in shopt right now, so 'else'
        if not args:
            for default_file in default_credential_files:
                if os.path.isfile(default_file):
                    username, password = parse_file_for_credential(default_file);
                    break;
        elif argc == 1:
            if os.path.isfile(args[0]):
                username, password = parse_file_for_credential(args[0]);
            else:
                print_usage();
                return;
        elif argc == 2:
            username = args[0];
            password = args[1];
        else:
            print_usage();
            return;

    # Check input
    if not username:
        print('FATAL ERROR: No username specified');
        print('Check your login file or command syntax');
        return;
    if not password:
        print('FATAL ERROR: No password specified');
        print('Check your login file or command syntax');
        return;
    elif (password[0] == "'" and password[-1] == "'") or (password[0] == '"' and password[-1] == '"'):
        print('Note: You don\'t need to put quotes in the credential text file');
        password = password[1:-1];

    # Show some details to user
    crypt_password = password[0];
    for i in range(1,len(password)-1):
        crypt_password += '*';
    crypt_password += password[-1];
    print('Sending request to login with',username,'&',crypt_password);

    try:
        login_pucampus(username,password);
    except:
        raise;
    return 0

if __name__ == '__main__':
    try:
        main(sys.argv);
    except KeyboardInterrupt:
        print('\nClosing garacefully :)',sys.exc_info()[1]);
    except urllib.error.HTTPError:
        print('HTTP Error:',sys.exc_info()[1]);
        print('Usually means you\'re already logged in.');
    ### TODO: Handle other errors
    except SystemExit:
        pass;
#     except:
#         print('Unexpected Error:',sys.exc_info()[0],'\nDetails:',sys.exc_info()[1]);
#         raise;
