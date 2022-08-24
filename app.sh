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
-bash: syntax error near unexpected token `('
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ python3 areas.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ python3 areas.py circle(2)
-bash: syntax error near unexpected token `('
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