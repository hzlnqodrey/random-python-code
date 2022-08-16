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
