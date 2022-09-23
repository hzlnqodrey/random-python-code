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

### Time Conversion User Input

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September$ nano seconds.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September$ sudo chmod 777 seconds.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September$ nano seconds.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September$ ./seconds.py
Welcome to this thime converter program
Enter the number of hours: 2
Enter the number of minutes: 30
Enter the number of seconds: 45
That's 9045 seconds

Do you want to do another conversion? [y to continue] Y
Enter the number of hours: 100
Enter the number of minutes: 60
Enter the number of seconds: 60
That's 363660 seconds

Do you want to do another conversion? [y to continue] n
Good bye!
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September$

#!/usr/bin/env python3

def to_seconds(hours, minutes, seconds):
        return hours*3600+minutes*60+seconds

print("Welcome to this thime converter program")

cont = "y"
while(cont.lower() == 'y'):
        hours = int(input("Enter the number of hours: ")) # data type casting
        minutes = int(input("Enter the number of minutes: ")) # data type casting
        seconds = int(input("Enter the number of seconds: ")) # data type casting

        print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
        print()
        cont = input("Do you want to do another conversion? [y to continue] ")

print("Good bye!")


## STDIN | STDOUT | STDERR [Input | Output | Error]

#!/usr/bin/env.python3

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
print("Now we generate an error to STDERR" + data + 1) # output is might be error, because if data is string, u can't added up directly with one

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively$ ./streams.py
This will come from STDIN: Saya
Now we write it to STDOUT: Saya
Traceback (most recent call last):
  File "./streams.py", line 5, in <module>
    print("Now we generate an error to STDERR" + data + 1)
TypeError: can only concatenate str (not "int") to str

####### ENV [environment variable in Shell/CLI]
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively$ env
SHELL=/bin/bash
WSL_DISTRO_NAME=Ubuntu
NAME=DESKTOP-V1LR167
PWD=/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively
LOGNAME=qodri123
MOTD_SHOWN=update-motd
HOME=/home/qodri123
LANG=C.UTF-8
WSL_INTEROP=/run/WSL/11_interop
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
LESSCLOSE=/usr/bin/lesspipe %s %s
TERM=xterm-256color
LESSOPEN=| /usr/bin/lesspipe %s
USER=qodri123
SHLVL=1
WSLENV=
XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/lib/wsl/lib:/mnt/c/Python310/Scripts/:/mnt/c/Python310/:/mnt/c/Program Files (x86)/Common Files/Intel/Shared Libraries/redist/intel64/compiler:/mnt/c/Windows/system32:/mnt/c/Windows:/mnt/c/Windows/System32/Wbem:/mnt/c/Windows/System32/WindowsPowerShell/v1.0/:/mnt/c/Windows/System32/OpenSSH/:/mnt/c/Program Files (x86)/NVIDIA Corporation/PhysX/Common:/mnt/c/Program Files/NVIDIA Corporation/NVIDIA NvDLISR:/mnt/c/Program Files/Microsoft SQL Server/130/Tools/Binn/:/mnt/c/Program Files/Microsoft SQL Server/Client SDK/ODBC/170/Tools/Binn/:/mnt/c/Program Files/dotnet/:/mnt/c/Program Files/mingw-w64/x86_64-8.1.0-posix-seh-rt_v6-rev0/mingw64/bin:/mnt/c/Users/HAZLAN M QODRI/AppData/Roaming/Python/Python37/Scripts:/mnt/c/Program Files/Git/cmd:/mnt/c/WINDOWS/system32:/mnt/c/WINDOWS:/mnt/c/WINDOWS/System32/Wbem:/mnt/c/WINDOWS/System32/WindowsPowerShell/v1.0/:/mnt/c/WINDOWS/System32/OpenSSH/:/mnt/c/ProgramData/chocolatey/bin:/mnt/c/Program Files/nodejs/:/mnt/c/Program Files/MongoDB/Server/4.4/bin:/mnt/c/Users/HAZLAN M QODRI/AppData/Local/Programs/Python/Python39-32/Scripts:/mnt/c/Users/HAZLAN M QODRI/AppData/Local/Programs/Python/Python39-32:/mnt/c/Users/HAZLAN M QODRI/AppData/Local/Programs/Python/Python38/:/mnt/c/Users/HAZLAN M QODRI/AppData/Local/Programs/Python/Python38/Scripts/:/mnt/c/Program Files/Cloudflare/Cloudflare WARP/:/mnt/c/Program Files/Go/bin:/mnt/c/Program Files/Docker/Docker/resources/bin:/mnt/c/ProgramData/DockerDesktop/version-bin:/mnt/c/Users/HAZLAN M QODRI/AppData/Local/Programs/Python/Python39/Scripts/:/mnt/c/Users/HAZLAN M QODRI/AppData/Local/Programs/Python/Python39/:/mnt/c/Users/HAZLAN M QODRI/AppData/Local/Microsoft/WindowsApps:/mnt/c/Users/HAZLAN M QODRI/AppData/Local/Programs/Microsoft VS Code/bin:/mnt/c/Users/HAZLAN M QODRI/.dotnet/tools:/mnt/c/Users/HAZLAN M QODRI/AppData/Local/GitHubDesktop/bin:/mnt/c/Users/HAZLAN M QODRI/AppData/Roaming/npm:/mnt/c/Users/HAZLAN M QODRI/AppData/Local/Google/Cloud SDK/google-cloud-sdk/bin:/mnt/c/Users/HAZLAN M QODRI/AppData/Local/atom/bin:/mnt/c/Program Files/JetBrains/PyCharm Community Edition 2022.2/bin:/mnt/c/Users/HAZLAN M QODRI/go/bin:/mnt/c/Program Files/heroku/bin:/snap/bin
HOSTTYPE=x86_64
OLDPWD=/mnt/c/WINDOWS/system32/programming_exercise/September
_=/usr/bin/env

######## ENV PATH VARIALBE
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/lib/wsl/lib:/mnt/c/Python310/Scripts/:/mnt/c/Python310/:/mnt/c/Program Files (x86)/Common Files/Intel/Shared Libraries/redist/intel64/compiler:/mnt/c/Windows/system32:/mnt/c/Windows:/mnt/c/Windows/System32/Wbem:/mnt/c/Windows/System32/WindowsPowerShell/v1.0/:/mnt/c/Windows/System32/OpenSSH/:/mnt/c/Program Files (x86)/NVIDIA Corporation/PhysX/Common:/mnt/c/Program Files/NVIDIA Corporation/NVIDIA NvDLISR:/mnt/c/Program Files/Microsoft SQL Server/130/Tools/Binn/:/mnt/c/Program Files/Microsoft SQL Server/Client SDK/ODBC/170/Tools/Binn/:/mnt/c/Program Files/dotnet/:/mnt/c/Program Files/mingw-w64/x86_64-8.1.0-posix-seh-rt_v6-rev0/mingw64/bin:/mnt/c/Users/HAZLAN M QODRI/AppData/Roaming/Python/Python37/Scripts:/mnt/c/Program Files/Git/cmd:/mnt/c/WINDOWS/system32:/mnt/c/WINDOWS:/mnt/c/WINDOWS/System32/Wbem:/mnt/c/WINDOWS/System32/WindowsPowerShell/v1.0/:/mnt/c/WINDOWS/System32/OpenSSH/:/mnt/c/ProgramData/chocolatey/bin:/mnt/c/Program Files/nodejs/:/mnt/c/Program Files/MongoDB/Server/4.4/bin:/mnt/c/Users/HAZLAN M QODRI/AppData/Local/Programs/Python/Python39-32/Scripts:/mnt/c/Users/HAZLAN M QODRI/AppData/Local/Programs/Python/Python39-32:/mnt/c/Users/HAZLAN M QODRI/AppData/Local/Programs/Python/Python38/:/mnt/c/Users/HAZLAN M QODRI/AppData/Local/Programs/Python/Python38/Scripts/:/mnt/c/Program Files/Cloudflare/Cloudflare WARP/:/mnt/c/Program Files/Go/bin:/mnt/c/Program Files/Docker/Docker/resources/bin:/mnt/c/ProgramData/DockerDesktop/version-bin:/mnt/c/Users/HAZLAN M QODRI/AppData/Local/Programs/Python/Python39/Scripts/:/mnt/c/Users/HAZLAN M QODRI/AppData/Local/Programs/Python/Python39/:/mnt/c/Users/HAZLAN M QODRI/AppData/Local/Microsoft/WindowsApps:/mnt/c/Users/HAZLAN M QODRI/AppData/Local/Programs/Microsoft VS Code/bin:/mnt/c/Users/HAZLAN M QODRI/.dotnet/tools:/mnt/c/Users/HAZLAN M QODRI/AppData/Local/GitHubDesktop/bin:/mnt/c/Users/HAZLAN M QODRI/AppData/Roaming/npm:/mnt/c/Users/HAZLAN M QODRI/AppData/Local/Google/Cloud SDK/google-cloud-sdk/bin:/mnt/c/Users/HAZLAN M QODRI/AppData/Local/atom/bin:/mnt/c/Program Files/JetBrains/PyCharm Community Edition 2022.2/bin:/mnt/c/Users/HAZLAN M QODRI/go/bin:/mnt/c/Program Files/heroku/bin:/snap/bin

######## ENVIRON DICTIONARY OF OS MODULE
#!/usr/bin/env python3

import os

print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively$ ./variables.py
HOME: /home/qodri123
SHELL: /bin/bash
FRUIT:

# Why value of fruit is missing?
# because the value of the key "FRUIT" is not present in ENVIRONMENT variables in Shell
# we need to do this to set the key and value into shell (check below)

# Export command
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively$ export FRUIT=Pineapple
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively$ ./variables.py
HOME: /home/qodri123
SHELL: /bin/bash
FRUIT: Pineapple


## Command-Line Arguments and Exit Status
# -> Parameters that are passed to a program when it's started
# really useful for system administator tasks
# That's because we can specify the information that we want our program to use before it even starts

## argv | sys

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively$ cat parameters.py
#!/usr/bin/env python3
import sys
print(sys.argv)

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively$ ./parameters.py
['./parameters.py'] # The name of the program/command that we just executed 

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively$ ./parameters.py one two three
['./parameters.py', 'one', 'two', 'three']

Where are the command line arguments stored?

>sys

Correct
Nice job! The list of arguments are stored in the sys module.

### Exit status/Return Code
# -> a bridge between a shell and program that gets executed inside of it
# -> the value returned by a program to the shell

# exit status 0 is succeded program, other than 0 is error | each number specify what its error

# to check Exit status, use Question Mark variabel (?), 
# and to see the contents use dolar sign, we use $?

# wc (word counts)
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively$ wc variables.py
  8  19 175 variables.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively$ $?
0: command not found # run zero because wc run successfully
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively$ $?
127: command not found # Exit code 127 means job's command can not be found or executed.

### create_file.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively$ cat create_file.py
#!/usr/bin/env python3

import os
import sys

filename=sys.argv[1]

if not os.path.exists(filename):
        with open(filename, "w") as f:
                f.write("New file created\n")
else:
        print("Error, the file {} already exists!".format(filename))
        sys.exit(1) # generate exit code 1
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively$ ./create_file.py test-1.txt
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively$ ls
create_file.py  parameters.py  streams.py  test-1.txt  variables.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively$

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively$ ./create_file.py test-1.txt
Error, the file test-1.txt already exists!
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively$ $?
1: command not found

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively$ mkdir Subprocess
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively$ ls
Subprocess  create_file.py  parameters.py  streams.py  test-1.txt  variables.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively$ cd Subprocess/
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively/Subprocess$ touch main.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively/Subprocess$ nano main.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively/Subprocess$ sudo chmod 777 main.py
[sudo] password for qodri123:
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively/Subprocess$ ./main.py
Mon Sep 12 16:09:24 WIB 2022

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively/Subprocess$ ./main.py
Mon Sep 12 16:19:23 WIB 2022
ls: cannot access 'this_file_does_not_exist': No such file or directory
2 # Return Code of failed LS fetch file


qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively/Subprocess$ nano host.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively/Subprocess$ ./host.py
0
b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively/Subprocess$ ./host.py
0
8.8.8.8.in-addr.arpa domain name pointer dns.google. # String output, good

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively/Subprocess$ ./host.py
0
['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively/Subprocess$ ./host.py
0
['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']
1 # RM command is failed, because saya_gila.txt is nowhere to be found

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively/Subprocess$ ./host.py
0
['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']
1
b''
b"rm: cannot remove 'saya_gila.txt': No such file or directory\n"
rm: cannot remove 'saya_gila.txt': No such file or directory

## IF rm command was succesfully

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively/Subprocess$ nano will_delete.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively/Subprocess$ ls
host.py  main.py  will_delete.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively/Subprocess$ ./host.py
0
['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']
0
b''
b''

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively/Subprocess$ ls
host.py  main.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Reading-Data-interactively/Subprocess$

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Python-Test$ nano rearrange.py
  GNU nano 4.8                                                                             rearrange.py                                                                                       
#!/usr/bin/env python3

import re

def rearrange_name(name):
        result = re.search(r"^([\w .]*), ([\w .]*)$", name)
        return "{} {}".format(result[2], result[1])

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Python-Test$ python3
Python 3.8.10 (default, Jun 22 2022, 20:18:18)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from rearrange import rearrange_name
>>> rearrange_name("Qodrey, Hazlan")
'Hazlan Qodrey'
>>>


qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Python-Test$ nano rearrange_test.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Python-Test$ chmod +x rearrange_test.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Python-Test$ ./rearrange_test.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Python-Test$

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Python-Test$ nano rearrange_test.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Python-Test$ ./rearrange_test.py
.E
======================================================================
ERROR: test_empty (__main__.TestRearrange)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./rearrange_test.py", line 18, in test_empty
    self.assertEqual(rearrange_name(testcase), expected)
  File "/mnt/c/WINDOWS/system32/programming_exercise/September/Python-Test/rearrange.py", line 7, in rearrange_name
    return "{} {}".format(result[2], result[1])
TypeError: 'NoneType' object is not subscriptable

----------------------------------------------------------------------
Ran 2 tests in 0.016s

FAILED (errors=1)

## after we manually error handling in rearrange.py

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Python-Test$ ./rearrange_test.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK

## additional test cases - 3rd Cases

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Python-Test$ ./rearrange_test.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK

## 4th Cases

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Python-Test$ ./rearrange_test.py
...F
======================================================================
FAIL: test_one_name (__main__.TestRearrange)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./rearrange_test.py", line 29, in test_one_name
    self.assertEqual(rearrange_name(testcase), expected)
AssertionError: '' != 'Voltaire' # Assertion Error -> Which means the original unexpected values don't match
+ Voltaire

----------------------------------------------------------------------
Ran 4 tests in 0.002s

FAILED (failures=1)

# Yay!

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Python-Test$ ./rearrange_test.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK

## Validate User

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Python-Test/ErrorHandling$ python3
Python 3.8.10 (default, Jun 22 2022, 20:18:18)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from validations import validate_user
>>> validate_user("", -1)
False
>>>

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Python-Test/ErrorHandling$ python3
Python 3.8.10 (default, Jun 22 2022, 20:18:18)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from validations import validate_user
>>> validate_user("", -1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/mnt/c/WINDOWS/system32/programming_exercise/September/Python-Test/ErrorHandling/validations.py", line 5, in validate_user
    raise ValueError("minlen must be at least one")
ValueError: minlen must be at least one
>>>

>>> validate_user("", 1)
False
>>> validate_user("hzlnqodrey", 1)
True
>>>

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Python-Test/ErrorHandling$ python3
Python 3.8.10 (default, Jun 22 2022, 20:18:18)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from validations import validate_user
>>> validate_user([3], 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/mnt/c/WINDOWS/system32/programming_exercise/September/Python-Test/ErrorHandling/validations.py", line 4, in validate_user
    assert type(username) == str, "username must be a string"
AssertionError: username must be a string
>>>

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/Python-Test/ErrorHandling$ ./validations_test.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ mkdir mynewdir
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ cd mynewdir/
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/mynewdir$

## they dont print anything if succeed, they will only print when there is an error

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/mynewdir$ pwd
/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/mynewdir
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/mynewdir$

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/mynewdir$ cp ../../seconds.py .
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/mynewdir$ ls
seconds.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/mynewdir$

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/mynewdir$ touch myfile.txt
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/mynewdir$ ls
myfile.txt  seconds.py

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/mynewdir$ ls -l
total 0
-rwxrwxrwx 1 qodri123 qodri123   0 Sep 22 12:27 myfile.txt
-rwxrwxrwx 1 qodri123 qodri123 528 Sep 22 11:21 seconds.py

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/mynewdir$ ls -la
total 0
drwxrwxrwx 1 qodri123 qodri123 4096 Sep 22 12:27 .
drwxrwxrwx 1 qodri123 qodri123 4096 Sep 22 11:18 ..
-rwxrwxrwx 1 qodri123 qodri123    0 Sep 22 12:27 myfile.txt
-rwxrwxrwx 1 qodri123 qodri123  528 Sep 22 11:21 seconds.py

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/mynewdir$ mv myfile.txt emptyfile.txt
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/mynewdir$ ls
emptyfile.txt  seconds.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/mynewdir$ cp seconds.py yetanotherfile.txt
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/mynewdir$ ls
emptyfile.txt  seconds.py  yetanotherfile.txt
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/mynewdir$ cat yetanotherfile.txt
#!/usr/bin/env python3

def to_seconds(hours, minutes, seconds):
        return hours*3600+minutes*60+seconds

print("Welcome to this thime converter program")

cont = "y"
while(cont.lower() == 'y'):
        hours = int(input("Enter the number of hours: "))
        minutes = int(input("Enter the number of minutes: "))
        seconds = int(input("Enter the number of seconds: "))

        print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
        print()
        cont = input("Do you want to do another conversion? [y to continue] ")

print("Good bye!")
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/mynewdir$

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/mynewdir$ ls -l
total 0
-rwxrwxrwx 1 qodri123 qodri123   0 Sep 22 12:27 emptyfile.txt
-rwxrwxrwx 1 qodri123 qodri123 528 Sep 22 11:21 seconds.py
-rwxrwxrwx 1 qodri123 qodri123 528 Sep 22 12:38 yetanotherfile.txt
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/mynewdir$

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/mynewdir$ rm *
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/mynewdir$ ls
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/mynewdir$ ls -l
total 0
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/mynewdir$

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ rmdir mynewdir
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ ls
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ ls mynewdir
ls: cannot access 'mynewdir': No such file or directory
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ ls September
BashScripting  Dicoding  Python-Test  Reading-Data-interactively  hello.py  seconds.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$ ls September -la
total 0
drwxrwxrwx 1 qodri123 qodri123 4096 Sep 22 11:13 .
drwxrwxrwx 1 qodri123 qodri123 4096 Sep 13 10:23 ..
drwxrwxrwx 1 qodri123 qodri123 4096 Sep 22 12:42 BashScripting
drwxrwxrwx 1 qodri123 qodri123 4096 Sep 20 15:54 Dicoding
drwxrwxrwx 1 qodri123 qodri123 4096 Sep 22 09:57 Python-Test
drwxrwxrwx 1 qodri123 qodri123 4096 Sep 12 16:08 Reading-Data-interactively
-rwxrwxrwx 1 qodri123 qodri123   90 Sep  6 00:19 hello.py
-rwxrwxrwx 1 qodri123 qodri123  528 Sep  6 00:26 seconds.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise$

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ cat stdout_example.py
#!/usr/bin/env python3

print("jsut a bit of text here...")
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ ls
stdout_example.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ ./stdout_example.py
jsut a bit of text here...
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ ./stdout_example.py > newfile.txt
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ ls
newfile.txt  stdout_example.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ cat newfile.txt
jsut a bit of text here...
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ ./stdout_example.py >> newfile.txt
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ cat newfile.txt
jsut a bit of text here...
jsut a bit of text here...
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ ls ../Reading-Data-interactively/
Subprocess  create_file.py  parameters.py  streams.py  test-1.txt  variables.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ cp ../Reading-Data-interactively/streams.py .
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ ls
newfile.txt  stdout_example.py  streams.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ cat streams.py
#!/usr/bin/env python3

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
print("Now we generate an error to STDERR" + data + 1)
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ ./streams.py < newfile.txt
This will come from STDIN: Now we write it to STDOUT: jsut a bit of text here...
Traceback (most recent call last):
  File "./streams.py", line 5, in <module>
    print("Now we generate an error to STDERR" + data + 1)
TypeError: can only concatenate str (not "int") to str
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$


qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ ./streams.py < newfile.txt 2> error_file.txt
This will come from STDIN: Now we write it to STDOUT: jsut a bit of text here...
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ cat error_file.txt
Traceback (most recent call last):
  File "./streams.py", line 5, in <module>
    print("Now we generate an error to STDERR" + data + 1)
TypeError: can only concatenate str (not "int") to str
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ echo "Just a single line here" > my_amazing_file.txt
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ cat my_amazing_file.txt
Just a single line here
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$

## IDK WHAT IS THIS LMAO

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ cat newfile.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head
      2 text
      2 of
      2 jsut
      2 here...
      2 bit
      2 a
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ cat haiku.txt
advance your career,
automating with Python,
its so fun to learn.
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ cat haiku.txt | ./capitalize.py
Advance your career,
Automating with python,
Its so fun to learn.
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$

# or you can just do by this

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ ./capitalize.py < haiku.txt
Advance your career,
Automating with python,
Its so fun to learn.


###### SIGNALLING

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ ping www.google.com
PING forcesafesearch.google.com (216.239.38.120) 56(84) bytes of data.
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=1 ttl=57 time=63.7 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=2 ttl=57 time=26.3 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=3 ttl=57 time=29.1 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=4 ttl=57 time=30.6 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=5 ttl=57 time=39.1 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=6 ttl=57 time=30.1 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=7 ttl=57 time=32.5 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=8 ttl=57 time=26.2 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=9 ttl=57 time=26.4 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=10 ttl=57 time=26.9 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=11 ttl=57 time=27.2 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=12 ttl=57 time=52.2 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=13 ttl=57 time=27.0 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=14 ttl=57 time=28.0 ms

^C
--- forcesafesearch.google.com ping statistics ---
89 packets transmitted, 89 received, 0% packet loss, time 88101ms
rtt min/avg/max/mdev = 25.563/29.647/126.124/13.243 ms

64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=37 ttl=57 time=26.1 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=38 ttl=57 time=26.3 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=39 ttl=57 time=26.1 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=40 ttl=57 time=28.3 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=41 ttl=57 time=26.5 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=42 ttl=57 time=26.1 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=43 ttl=57 time=26.3 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=44 ttl=57 time=32.3 ms
^Z
[2]+  Stopped                 ping www.google.com
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ fg
ping www.google.com
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=45 ttl=57 time=26.2 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=46 ttl=57 time=28.3 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=47 ttl=57 time=26.2 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=48 ttl=57 time=27.6 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=49 ttl=57 time=28.9 ms

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ ps
  PID TTY          TIME CMD
   12 pts/0    00:00:00 bash
  136 pts/0    00:00:00 less
  206 pts/0    00:00:00 ps

  qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ ps ax
  PID TTY      STAT   TIME COMMAND
    1 ?        Sl     0:00 /init
   10 ?        Ss     0:00 /init
   11 ?        R      0:00 /init
   12 pts/0    Ss     0:00 -bash
  136 pts/0    T      0:00 less
  224 pts/0    R+     0:00 ps ax

  qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32$ ps ax
  PID TTY      STAT   TIME COMMAND
    1 ?        Sl     0:00 /init
   10 ?        Ss     0:00 /init
   11 ?        S      0:00 /init
   12 pts/0    Ss     0:00 -bash
  136 pts/0    T      0:00 less
  225 pts/0    S+     0:00 ping www.google.com  ## WE NEED TO KILL THIS IN OTHER TERMINAL YES YES YES
  226 ?        Ss     0:00 /init
  227 ?        S      0:00 /init
  228 pts/1    Ss     0:00 -bash
  241 pts/1    R+     0:00 ps ax

# use GREP to match our search word
  qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32$ ps ax | grep ping
  225 pts/0    S+     0:00 ping www.google.com
  246 pts/1    S+     0:00 grep --color=auto ping
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32$

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32$ kill 225
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32$

....
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=137 ttl=57 time=26.9 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=138 ttl=57 time=28.0 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=139 ttl=57 time=34.3 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=140 ttl=57 time=27.1 ms
64 bytes from any-in-2678.1e100.net (216.239.38.120): icmp_seq=141 ttl=57 time=25.9 ms
Terminated
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ cat gather-information.sh
#!/bin/bash

echo "Starting at: $(date)"
echo

echo "UPTIME"
uptime # cmd
echo # empty lines

echo "FREE"
free # cmd
echo # empty lines

echo "WHO"
who  # cmd
echo # empty lines

echo "Finishing at $(date)"
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ ./gather-information.sh
Starting at: Thu Sep 22 16:18:52 WIB 2022

UPTIME
 16:18:52 up 3 min,  0 users,  load average: 0.00, 0.00, 0.00

FREE
              total        used        free      shared  buff/cache   available
Mem:       13029044       93216    12900712          68       35116    12766668
Swap:       4194304           0     4194304

WHO

Finishing at Thu Sep 22 16:18:52 WIB 2022

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ example=hello
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ echo $example
hello

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ ./gather-information.sh
Starting at: Thu Sep 22 16:30:55 WIB 2022

./gather-information.sh: line 7: ---------------------------------------------: command not found
UPTIME
 16:30:55 up 15 min,  0 users,  load average: 0.00, 0.00, 0.00
---------------------------------------------
FREE
              total        used        free      shared  buff/cache   available
Mem:       13029044       99204    12858768          68       71072    12742748
Swap:       4194304           0     4194304
---------------------------------------------
WHO
---------------------------------------------
Finishing at Thu Sep 22 16:30:55 WIB 2022

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ echo *.py
capitalize.py stdout_example.py streams.py
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ echo *.txt
error_file.txt haiku.txt my_amazing_file.txt newfile.txt
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ if test -n "$PATH"; then echo "Your path is not empty"; fi
Your path is not empty

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ if [ -n "$PATH" ]; then echo "Your path is not empty"; fi
Your path is not empty

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ cat while.sh
#!/bin/bash

n=1

while [ $n -le 5 ]; do
        echo "Iteration number - $n"
        ((n+=1))
done
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ ./while.sh
Iteration number - 1
Iteration number - 2
Iteration number - 3
Iteration number - 4
Iteration number - 5

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ ./retry.sh ./random-exit.py
Returning: 0
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ ./retry.sh ./random-exit.py
Returning: 1
Retry #1
Returning: 1
Retry #2
Returning: 2
Retry #3
Returning: 1
Retry #4
Returning: 0

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ ./fruits.sh
I love apple
I love orange
I love peach

################ RENAMING FILE WITH FOR LOOP IN BASH

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/old_websites$ ls -l
total 0
-rwxrwxrwx 1 qodri123 qodri123  0 Sep 22 19:46 about.HTM
-rwxrwxrwx 1 qodri123 qodri123  0 Sep 22 19:46 footer.HTM
-rwxrwxrwx 1 qodri123 qodri123  0 Sep 22 19:46 index.HTM
-rwxrwxrwx 1 qodri123 qodri123 12 Sep 22 19:49 rename.sh

-rwxrwxrwx 1 qodri123 qodri123 12 Sep 22 19:49 rename.sh
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/old_websites$ nano rename.sh
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/old_websites$ chmod +x rename.sh
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/old_websites$ ./rename.sh
mv about.HTM file
mv footer.HTM file
mv index.HTM file
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/old_websites$ nano rename.sh
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/old_websites$ ./rename.sh
mv about.HTM about
mv footer.HTM footer
mv index.HTM index
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/old_websites$ nano rename.sh
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/old_websites$ ./rename.sh
mv about.HTM about.html
mv footer.HTM footer.html
mv index.HTM index.html
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/old_websites$ nano rename.sh
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/old_websites$ ./rename.sh
about.HTM about.html
footer.HTM footer.html
index.HTM index.html
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/old_websites$ nano rename.sh
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/old_websites$ ./rename.sh
qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/old_websites$ ls -la
total 0
drwxrwxrwx 1 qodri123 qodri123 4096 Sep 23 13:50 .
drwxrwxrwx 1 qodri123 qodri123 4096 Sep 22 19:46 ..
-rwxrwxrwx 1 qodri123 qodri123    0 Sep 22 19:46 about.html
-rwxrwxrwx 1 qodri123 qodri123    0 Sep 22 19:46 footer.html
-rwxrwxrwx 1 qodri123 qodri123    0 Sep 22 19:46 index.html
-rwxrwxrwx 1 qodri123 qodri123   94 Sep 23 13:50 rename.sh


### Advanced Command Interaction

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/old_websites$ tail /var/log/syslog | cut -d' ' -f5-

# -d' ' : is space as a delimiter
# -f5-  : we want to extract the fifth field

qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting/old_websites$ cut -d' ' -f5- /var/log/syslog | sort | uniq -c | sort -nr | head