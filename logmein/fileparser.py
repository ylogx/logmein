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

