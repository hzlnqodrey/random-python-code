############# USING PYTHON TO INTERACT WITH THE OPERATING SYSTEM ##############

# Check Whether python installed on our OS
python --version
# Python 3.8.0

# External modules: pypi.org
# External modules are generally managed with a command line tool called 'pip'
# pip is cross-platform tool to install, update, and remove external modules

# to install web browser request external module, we need to type
pip install requests

# Downgrade PIP Version
# Downgrading may be necessary if a new version of PIP starts performing undesirably. To downgrade PIP to a prior version, specifying the version you want.

# To downgrade PIP, use the syntax:

python -m pip install pip==version_number

# For example, to downgrade to version 18.1, you would run:

python -m pip install pip==18.1

# You should now see the version of PIP that you specified.


########### to run command on linux

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32$ mkdir programming_exercise
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32$ cd programming_exercise
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ ls
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ touch hello_world.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ ls
hello_world.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ cat hello_world.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ vi hello_world.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ cat hello_world.py
print("Hello World")
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ hello_world.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ run hello_world.py

############ to run python file on CLI

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ python3 hello_world.py


########## CLI CODE EDITOR on LINUX

# 1. VI (VIM)
# 2. NANO

# This line below tell OS that we want to run script using Python 3
#!/usr/bin/env python3 -> called shebang

print('Hello, World!')

# chmod - Linux Command
# this command let us change the file permissions (r,w,x [Read, Write, Execute])
# marking +r/+w/+x to the hello_world.py
chmod +x hello_world.py

# now the hello_world.py can run with the prefix './'
# the dot '.' in the prefix means represent the current directory, so we're basically telling the OS to find script in the current directory and then execute it.
# be sure is "#!/usr/bin/env python3" always on the top of the file

########## exercise - areas.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ touch areas.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ nano areas.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ cat areas.py
#!/usr/bin/env python3
import math

def triangle(base, height):
  return base * height/2

def rectangle(base, height):
  return base * height

def circle(radius):
  return math.pi * (radius**2)


qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ ./areas.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ ./areas.py print(circle(2))
# -bash: syntax error near unexpected token `('
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ python3 areas.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ python3 areas.py circle(2)
# -bash: syntax error near unexpected token `(' 
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$  nano areas.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ ./areas.py
50.26548245743669
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$

# Import areas.py to reduce code reuse

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ python3
Python 3.8.10 (default, Jun  2 2021, 10:49:15)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import areas
50.26548245743669
>>> import areas
>>> areas.triangle(5, 4)
10.0
>>> areas.rectangle(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: rectangle() missing 1 required positional argument: 'height'
>>> areas.rectangle(5, 10)
50
>>> areas.circle(10)
314.1592653589793
>>>


##### 

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ ls -l /usr/lib/python3/dist-packages/requests
total 216
-rw-r--r-- 1 root root  3921 May 16  2019 __init__.py # every module has this because interpreter will read it first
drwxr-xr-x 2 root root  4096 Aug 20  2021 __pycache__
-rw-r--r-- 1 root root   436 May 16  2019 __version__.py
-rw-r--r-- 1 root root  1096 May 16  2019 _internal_utils.py
-rw-r--r-- 1 root root 21344 May 16  2019 adapters.py
-rw-r--r-- 1 root root  6271 May 16  2019 api.py
-rw-r--r-- 1 root root 10206 May 16  2019 auth.py
-rw-r--r-- 1 root root   453 May 16  2019 certs.py
-rw-r--r-- 1 root root  1678 May 16  2019 compat.py
-rw-r--r-- 1 root root 18430 May 16  2019 cookies.py
-rw-r--r-- 1 root root  3185 May 16  2019 exceptions.py
-rw-r--r-- 1 root root  3515 May 16  2019 help.py
-rw-r--r-- 1 root root   757 May 16  2019 hooks.py
-rw-r--r-- 1 root root 34210 May 16  2019 models.py
-rw-r--r-- 1 root root   542 May 16  2019 packages.py
-rw-r--r-- 1 root root 29332 May 16  2019 sessions.py
-rw-r--r-- 1 root root  4129 May 16  2019 status_codes.py
-rw-r--r-- 1 root root  2981 May 16  2019 structures.py
-rw-r--r-- 1 root root 30049 May 16  2019 utils.py


# sooo, if you have a module split into separate files, and you want the interpreter to recognize the directory has a module
# we need to create the __init__.py file

qodri123@DESKTOP-V1LR167:/mnt/c/Windows/system32/programming_exercise$ touch health_check.py
qodri123@DESKTOP-V1LR167:/mnt/c/Windows/system32/programming_exercise$ vi health_check.py
qodri123@DESKTOP-V1LR167:/mnt/c/Windows/system32/programming_exercise$ cat health_check.py
#!/usr/bin/env python3
import shutil
import psutil

# to check disk usage, return true if there's more than 20 percent free or false if it's less
def check_disk_usage(disk):
    disk_usage = shutil.disk_usage(disk)
    free = disk_usage.free / disk_usage.total * 100
    return free > 20

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(1)
    return cpu_usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything is OK!")
qodri123@DESKTOP-V1LR167:/mnt/c/Windows/system32/programming_exercise$ ./health_check.py
Everything is OK!
qodri123@DESKTOP-V1LR167:/mnt/c/Windows/system32/programming_exercise$

# mkdir
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ mkdir folder1
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ ls
__pycache__  areas.py  folder1  health_check.py  hello_world.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$

# mkdir in python (using os.mkdir)
>>> import os
>>> os.mkdir("new_dir")
>>>
[1]+  Stopped                 python3
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ ls
__pycache__  areas.py  folder1  health_check.py  hello_world.py  new_dir

# chdir
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ python3
Python 3.8.10 (default, Jun 22 2022, 20:18:18)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.chdir("new_dir")
>>> os.getcwd()
'/mnt/c/WINDOWS/system32/programming_exercise/new_dir'
>>>
[3]+  Stopped                 python3
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ python3
Python 3.8.10 (default, Jun 22 2022, 20:18:18)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.getcwd()
'/mnt/c/WINDOWS/system32/programming_exercise'
>>> os.chdir("new_dir")
>>> os.getcwd()
'/mnt/c/WINDOWS/system32/programming_exercise/new_dir'
>>>

# remove dir
# if directory empty just use:
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ rm -r 'directory'

# force delete
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ rm -rf 'directory'

# list dir
>>> os.getcwd()
'/mnt/c/WINDOWS/system32/programming_exercise/new_dir'
>>> os.mkdir("newer_dir")
>>> os.listdir("newer_dir")
[]
>>> os.listdir(os.getcwd())
['newer_dir']
>>>

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ ls
__pycache__  areas.py  folder1  health_check.py  hello_world.py  website
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ python3
Python 3.8.10 (default, Jun 22 2022, 20:18:18)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.listdir("website")
['favicon.ico', 'images', 'index.html']
>>> dir = "website"
>>> for name in os.listdir(dir):
...   fullname = os.path.join(dir, name)
...   if os.path.isdir(fullname):
...     print("{} is a directory".format(fullname))
...   else:
...     print("{} is a file".format(fullname))
...
website/favicon.ico is a file
website/images is a directory
website/index.html is a file
>>>

in linux and MacOS, the portions of a file are split using a forward slash (/)
on Windows, theyre split using a backslash (\)
with using os.path.join work with all operating systems

>>> import csv
>>> f = open("employees.txt")
>>> csv_read = csv.reader(f)
>>> print(csv_read)
<_csv.reader object at 0x7f574ff2fcf0>
>>> print(csv_read.name)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: '_csv.reader' object has no attribute 'name'
>>> print(csv_read.[0])
  File "<stdin>", line 1
    print(csv_read.[0])
                   ^
SyntaxError: invalid syntax
>>> for row in csv_read:
...   print(row)
...
['Hazlan', '0815', 'Backend Engineer']
['Rivano', '9823', 'Android Developer']
['Riko', '4823', 'Frontend Engineer']
>>>

>>> file = open("employees.txt")
.reader(file)
for row in file_csv:
    name, phone, role = row
    p>>> file_csv = csv.reader(file)
print(>>> for row in file_csv:
Name: ...     name, phone, role = row
...     print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
...
Name: Hazlan, Phone: 0815, Role: Backend Engineer
Name: Rivano, Phone: 9823, Role: Android Developer
Name: Riko, Phone: 4823, Role: Frontend Engineer

# generate csv files
...
>>> file = open("hosts.csv")
>>> print(csv.reader(file))
<_csv.reader object at 0x7f2fd4675580>
>>> file_csv = csv.reader(file)
>>> for row in file_csv:
...   print(row)
...
['workstation.local', '192.168.25.46']
['webserver.cloud', '10.2.5.6']
>>>
[3]+  Stopped                 python3
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/August$ ls
employees.txt  hosts.csv
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/August$ cat hosts.csv
workstation.local,192.168.25.46
webserver.cloud,10.2.5.6
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/August$

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
student-04-2675d58b4395@linux-instance:~$ ls
data  scripts
student-04-2675d58b4395@linux-instance:~$ cd data
student-04-2675d58b4395@linux-instance:~/data$ ls
employees.csv
student-04-2675d58b4395@linux-instance:~/data$ cat employees.csv
Full Name, Username, Department
Audrey Miller, audrey, Development
Arden Garcia, ardeng, Sales
Bailey Thomas, baileyt, Human Resources
Blake Sousa, sousa, IT infrastructure
Cameron Nguyen, nguyen, Marketing
Charlie Grey, greyc, Development
Chris Black, chrisb, User Experience Research
Courtney Silva, silva, IT infrastructure
Darcy Johnsonn, darcy, IT infrastructure
Elliot Lamb, elliotl, Development
Emery Halls, halls, Sales
Flynn McMillan, flynn, Marketing
Harley Klose, harley, Human Resources
Jean May Coy, jeanm, Vendor operations
Kay Stevens, kstev, Sales
Lio Nelson, lion, User Experience Research
Logan Tillas, tillas, Vendor operations
Micah Lopes, micah, Development
Sol Mansi, solm, IT infrastructure
student-04-2675d58b4395@linux-instance:~/data$

# You will write your python script in this generate_report.py file. 
# This script begins with a line containing 
#  the '#!' character combination, which is commonly called hash bang or shebang, 
# and continues with the path to the interpreter. 
# If the kernel finds that the first two bytes are '#!' 
# then it uses the rest of the line as an interpreter and passes the file as an argument. 
# We will use the following shebang in this script:

#!/usr/bin/env python3

# We also need to pass a dialect as a parameter to this function. There isn't a well-defined standard for comma-separated value files, so the parser needs to be flexible. Flexibility here means that there are many parameters to control how csv parses or writes data. Rather than passing each of these parameters to the reader and writer separately, we group them together conveniently into a dialect object.

# Dialect classes can be registered by name so that callers of the CSV module don't need to know the parameter settings in advance. We will now register a dialect empDialect.

  csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
# Copied!
# The main purpose of this dialect is to remove any leading spaces while parsing the CSV file.

## Basic Matching with grep
# CLI: grep [word] /usr/share/dict/words

# GREP is case sensitive

# use '-i' to match a string regardless of case,

# RESERVED CHARACTERS [., +, *, ?, ^, $, (, ), [, ], {, }, |, \. etc]

CLI: grep l.rts /usr/share/dict/words
output:
alerts
blurts
flirts

# Using the terminal, which of the following commands will correctly use grep to find the words “sling” and “sting” (assuming they are in our file, file.txt)?
# Correct Answer: user@ubuntu:~$ grep s.ing /usr/file.txt
# Nice work! In regex, a dot is a wildcard, so it can represent any character. This command will print both “sting” and “sling”, if they are in the file.

# Circumflex (^) is the beginning and dollar sign ($) is the end
# Circumflex (^) will return the matches pattern with sub-word in the beginning of the line
# example: ^fruit
grep ^fruit /usr/share/dict/words
output:
fruit, fruits, fruitless, fruitier, etc

# dollar sign ($) will return the matches pattern with sub-word in the end of the line
# example: cat$
grep cat$ /usr/share/dict/words
output:
muscat, cat, tomcat, copycat, ducat, lolcat, pussycat, etc

student-04-97715962a5ea@linux-instance:~$ cd data
student-04-97715962a5ea@linux-instance:~/data$ ls
user_emails.csv
student-04-97715962a5ea@linux-instance:~/data$ cat user_emails.csv
Full Name, Email Address
Blossom Gill, blossom@abc.edu
Hayes Delgado, nonummy@utnisia.com
Petra Jones, ac@abc.edu
Oleg Noel, noel@liberomauris.ca
Ahmed Miller, ahmed.miller@nequenonquam.co.uk
Macaulay Douglas, mdouglas@abc.edu
Aurora Grant, enim.non@abc.edu
Madison Mcintosh, mcintosh@nisiaenean.net
Montana Powell, montanap@semmagna.org
Rogan Robinson, rr.robinson@abc.edu
Simon Rivera, sri@abc.edu
Benedict Pacheco, bpacheco@abc.edu
Maisie Hendrix, mai.hendrix@abc.edu
Xaviera Gould, xlg@utnisia.net
Oren Rollins, oren@semmagna.com
Flavia Santiago, flavia@utnisia.net
Jackson Owens, jackowens@abc.edu
Britanni Humphrey, britanni@ut.net
Kirk Nixon, kirknixon@abc.edu
Bree Campbell, breee@utnisia.net

## After Replacing 'abc.edu' to 'xyz.edu'

student-04-97715962a5ea@linux-instance:~/data$ cat updated_user_emails.csv
Full Name, Email Address
Blossom Gill, blossom@xyz.edu
Hayes Delgado, nonummy@utnisia.com
Petra Jones, ac@xyz.edu
Oleg Noel, noel@liberomauris.ca
Ahmed Miller, ahmed.miller@nequenonquam.co.uk
Macaulay Douglas, mdouglas@xyz.edu
Aurora Grant, enim.non@xyz.edu
Madison Mcintosh, mcintosh@nisiaenean.net
Montana Powell, montanap@semmagna.org
Rogan Robinson, rr.robinson@xyz.edu
Simon Rivera, sri@xyz.edu
Benedict Pacheco, bpacheco@xyz.edu
Maisie Hendrix, mai.hendrix@xyz.edu
Xaviera Gould, xlg@utnisia.net
Oren Rollins, oren@semmagna.com
Flavia Santiago, flavia@utnisia.net
Jackson Owens, jackowens@xyz.edu
Britanni Humphrey, britanni@ut.net
Kirk Nixon, kirknixon@xyz.edu
Bree Campbell, breee@utnisia.net

############################################################# Reading Data Interactively

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September$ sudo chmod 777 hello.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September$ nano hello.py


Use "fg" to return to nano.

[1]+  Stopped                 nano hello.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September$ fg
nano hello.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September$ ./hello.py
Please enter your name: Qodrey
Hello, Qodrey
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September$ cat hello.py
#!/usr/bin/env python3

name = input("Please enter your name: ")
print("Hello, " + name)

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September$