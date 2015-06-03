from __future__ import print_function
import re
import sys

from logmein.statuscode import StatusCode

if sys.version_info >= (3, ):
    import urllib.request as urllib2
    import urllib.error as urlerror
    from urllib.error import HTTPError, URLError
    from urllib.parse import urlencode
else:
    import urllib2
    import urlparse
    from urllib2 import HTTPError, URLError
    from urllib import urlencode


def login_pucampus(username, password):
    ''' Perform login '''
    url = 'https://securelogin.arubanetworks.com/cgi-bin/login?cmd=login'
    values = {'user': username, 'password': password}
    # Create request
    data = urlencode(values)
    data = data.encode('utf-8')
    req = urllib2.Request(url, data)
    # Send request
    try:
        response = urllib2.urlopen(
            req)  #res.geturl(), .url=str, .status=200, .info=200, .msg=OK,
    except HTTPError as exep:
        print('The server couldn\'t fulfill the request.', 'Error code: ',
              exep.code)
        print('You\'re probably logged in!')
        return StatusCode.LOGGED_IN
    except URLError as exep:
        print('We failed to reach a server.')
        print('Reason: ', exep.reason)
        return StatusCode.CONNECTION_ERROR
    else:
        # everything is fine
        the_page = str(response.read())  # More pythonic than .decode('utf-8')
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
            'https://securelogin.arubanetworks.com/cgi-bin/login?cmd=logout')
    except HTTPError as exep:
        print('The server couldn\'t fulfill the request.', 'Error code: ',
              exep.code)
    except URLError as exep:
        print('We failed to reach a server.')
        print('Reason: ', exep.reason)
    else:
        # everything is fine
        the_page = str(response.read())  # More pythonic than .decode('utf-8')
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
