import requests as req
import pandas as pd

response = req.get("http://instagram.com")

print(response)

visitors = [1234, 5232, 9223, 8856, 7752]
errors = [23, 52, 62, 89, 12]

df = pd.DataFrame( {"visitors": visitors, "errors": errors}, index=["Mon", "Tue", "Wed", "Thu", "Fri"] )

print(df)

# DataFrame operator method [Mean, Average, Sum, etc]
errors_mean = df["errors"].mean()
print(errors_mean)


"hello " * 10 # print on interactive interpreter CLI

import shutil
du = shutil.disk_usage("/")
print(du)
# -> usage(total=269490393088, used=1470783488, free=254258937856)

du.free/du.total*100
# -> 94.34805261238893

import psutil
psutil.cpu_percent(.1)
psutil.cpu_percent(.1)
0.0
psutil.cpu_percent(.1)
0.0

########## Health Check (of a PC) Script's

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

# putty vm


############################ Reading Files

file = open("spider.txt")
# print(file.readline()) # read the first line
# print(file.readline()) # read the second line
# print(file.readlines()) # read the second line
print(file.read()) # read the second line

file.close() # open-use-close: is a typical way of working with files in most prog lang

# with 'with block' Python will automatically close the file 
with open("spider.txt") as file1:
    print(file1.read())

# Both methods read from the current position. The readline() method reads one line, while read() reads until the end of the file.

# file object can be iterated the same way as other Python sequences (string, list, dict, set)

# you can do this to uppercase ur text lines:

with open("spider.txt") as file:
    for line in file:
        print(line.upper()) # this will create a weird a empty line before read the next line

# how to avoid a empty new line?
# we can use string method: strip() to remove  all surrounding white spaces [including: tabs and new lines]

with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())

# Good work! Here, we are iterating line by line, and the strip() command is used to remove extra whitespace.

# store file line to list (the element is line by line (each line))

file = open("spider.txt")
lines = file.readlines() # list
file.close() # eventhough we close it, the lines has the all the infos from file
print(lines)

### Write content to file
# by default the 'open()' use "r" mode to read-only the file
# the "w" argument is to write-only mode, if the file doesn't exist then Python will create it
# then if the file does exist, the current content will be overwritten by whatever we decide to write using our script
# remember you can't read if the argument is write-only mode, u need to "r+" [read-write] mode
# if you want to add content at the end of an existing content in file, use "a" (to append) 
with open("novel.txt", "w") as file:
    file.write("It was a dark and stormy night")

# You nailed it! When using write mode, the old contents get deleted as soon as the file is opened.


############### OS MODULE
# Delete, Rename, or modified time or else, use os module

# Remove File
import os

os.remove("novel.txt")

# If you try to remove file that you already remove or file that's not even created in the first hand, it will raise an Error
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# FileNotFoundError: [Errno 2] No such file or directory: 'novel.txt'

# os.rename(arg1, arg2)
# arg1 -> the old name
# arg2 -> the new name

# os.rename("spider.txt", "tarantula.txt") # it changed!

## how do we check if the file is exist or not?
# submodule of OS [os.path sub-module]
os.path.exists("tarantula.txt")
os.path.exists("spider.txt")

# >>> with open("sayagila.txt", "w") as newFile:
# ...   newFile.write("sayaaaaaaaaaaa")
# ...
# 14
# >>> os.path.exists("sayagila.txt")
# True


### os.path.[module]

# [1] getsize -> to check how big the size of the file in bytes
os.path.getsize("sayagila.txt")
# >>> os.path.getsize("sayagila.txt")
# 14

# [2] gettime -> to check when the file was last modified
os.path.getmtime("sayagila.txt")
# >>> os.path.getmtime("sayagila.txt")
# 1661339935.40045 -> # Issa UNIX TIMESTAMP and hard to read, convert it to datestamp module

import datetime
time_stamp = os.path.getmtime("sayagila.txt")
datetime.datetime.fromtimestamp(time_stamp)
# datetime.datetime(2022, 8, 24, 18, 18, 55, 400450) -> output

# in os.path we can work with absolute and relative paths
# .abspath() -> to locate where exactly located on dir
os.path.abspath("sayagila.txt")
# 'C:\\Users\\<user>\\AppData\\Local\\Programs\\Python\\Python38\\sayagila.txt'

######## How to work with | DIRECTORIES | or folders(?)

# [1] getcwd -> To check which current directory my python program is executing in
print(os.getcwd())
# C:\Users\<user>\AppData\Local\Programs\Python\Python38

# [2] mkdir -> to create directory
os.mkdir("new_dir")

# [3] chdir -> change directories
os.chdir("new_dir")

# [4] rmdir -> remove directory (if empty)
os.rmdir("new_dir")

# [5] listdir -> return a list of all the files and sub-directories in given directory
os.listdir("new_dir")


## Practice Quiz

# Q1: Question 1
# The create_python_script function creates a new python script in the current working directory, adds the line of comments to it declared  by the 'comments' variable, and returns the size of the new file. Fill in the gaps to create a script called "program.py".

def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, "w") as file:
    filesize = file.write(comments)
  return(filesize)

print(create_python_script("program.py"))



























































































