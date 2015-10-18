LogMeIn [![Stories in Ready](https://badge.waffle.io/shubhamchaudhary/logmein.png?label=ready&title=Ready)](https://waffle.io/shubhamchaudhary/logmein) [![Circle CI](https://circleci.com/gh/shubhamchaudhary/logmein.svg?style=svg)](https://circleci.com/gh/shubhamchaudhary/logmein) 
=======

This software will help you automatically login to PU@CAMPUS wifi ![logo unavailable](http://upload.wikimedia.org/wikipedia/en/6/6f/Seal_Panjab_University.jpg "PU @ Campus")  

Installation
------------

#### **Linux** user: 
1. `pip install logmein` or `easy_install logmein`: Install logmein from pip using 

1. `xdg-open ~/.login.txt`: Next you need to create a credential file `~/.login.txt` if you don't want to enter username/password everytime.
1. Enter your username and password in two separate lines e.g:

```
11uit424
password
```

#### **Windows** user:
* Install python3 if you don't have one from this [official python website][python3] or click here for [32 bit version][32python34] or [64 bit version][64python34]
* Please select all components during installation of python.
* Installing by downloading the zip:
    * Download this folder using the [Download as zip][zip] link on right side.
    * Copy and paste the file *run.py* and the folder *logmein* to your Desktop or some other suitable place.
* Installing using pip or easy_install:
    * If you can run python in command line, you should be able to install logmein by `pip install logmein` or `easy_install logmein`
    * Copy and paster the file *run.py* to your Desktop or some other suitable place.
* Create a file named **login.txt** or **.login.txt** (preferably in *C:\\Users\\yourHomeFolder* or in the same folder where you copied *run.py*). Desktop is also a good alternative.
* Open this credential file (login.txt) in any text editor and enter two lines: first your *username* and then your *password* in the next line. 
* It is recommended that you hide this credential file.

Usage
-----

#### Windows user
Once you've carefully installed it as instructed above you may simply **double click** the *run.py* file to login.  

#### Linux user
All you need to do is type in `logmein` or `logmein -i` in your command line to login PUCampus.  

Plus you also get some more additional functionality through command accessible via command line options listed below:  

###### FAQ
Q: I'm on windows and when I double click, it asks me to select an application to open this file.  

A: You haven't enabled python setup to connect with .py filetype. Run the Python setup again and select all the option for installation  


#### Command line options
**Usage:** ```logmein [-i | -o] [-f credential_file | username password] [-t TIMEOUT]```  

| **Help option** | **Alternative**  | **Usage**                                 |
| -------------   |:-------------:   | -----:                                    |
| -h              | --help           | Show this help message and exit           |
| -i              | --login          | Login                                     |
| -o              | --logout         | Logout                                    |
| -f FILE         | --file=FILE      | Use the specified file as credential file |
| -t TIMEOUT      | --timeout TIMEOUT| Loop and keep on sending requests at specified time interval (in seconds) |

You may also use `logmein USERNAME PASSWORD` to login as some other user.  


[zip]: https://github.com/shubhamchaudhary/logmein/archive/master.zip
[python3]: https://www.python.org/download/
[32python34]: https://www.python.org/ftp/python/3.4.2/python-3.4.2.msi
[64python34]: https://www.python.org/ftp/python/3.4.2/python-3.4.2.amd64.msi


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/shubhamchaudhary/logmein/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

