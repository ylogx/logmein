logmein
=======

This software will help you automatically login to PU@CAMPUS wifi ![logo unavailable](http://physics.puchd.ac.in/events/exfor2011/includes/webimages/logo1-tr.png "PU @ Campus")  

Installation
------------

#### **Linux** user: 
* Download this folder using the [Download as zip][zip] link on right side.
* Unzip the folder by double clicking (or command `unzip logmein-master.zip`).
* Run the install file by typing `./install` in the command line
* Enter your system sudo password when prompted
* Next you'll be asked to setup a credential file, press y
* Enter your username and password. These will be stored in a hidden file `~/.login.txt`.

#### **Windows** user:
* Install python3 if you don't have one from this [official python website][python3] or click here for [32 bit version][32python34] or [64 bit version][64python34]
* Download this folder using the [Download as zip][zip] link on right side.
* Copy and paste the file *logmein.py* to your Desktop or some other suitable place.
* Create a file named **login.txt** or **.login.txt** (preferably in *C:\Users\yourHomeFolder* or in the same folder where you copied *logmein.py*)
* Open this credential file (login.txt) in any text editor and enter two lines: first your *username* and then your *password* in the next line. 
* It is recommended that you hide this credential file.

Usage
-----

#### Windows user
Once you've carefully installed it as instructed above you may simply **double click** the *logmein.py* file to login.  

#### Linux user
All you need to do is type in `logmein` or `logmein -i` in your command line to login PUCampus.  
Plus you also get some more additional functionality through command accessible via command line options listed below:  

#### Command line options
**Usage:** ```logmein [-i || -o || -f credential_file || username password] ```  

| **Help option** | **Alternative** | **Usage**                                 |
| -------------   |:-------------:  | -----:                                    |
| -h              | --help          | Show this help message and exit           |
| -i              | --login         | Login                                     |
| -o              | --logout        | Logout                                    |
| -f FILE         | --file=FILE     | Use the specified file as credential file |

You may also use `logmein USERNAME PASSWORD` to login as some other user.  


[zip]: https://github.com/shubhamchaudhary/logmein/archive/master.zip
[python3]: https://www.python.org/download/
[32python34]: https://www.python.org/ftp/python/3.4.1/python-3.4.1.msi
[64python34]: https://www.python.org/ftp/python/3.4.1/python-3.4.1.amd64.msi
