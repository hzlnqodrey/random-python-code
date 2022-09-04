from dataclasses import field
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

os.rename("spider.txt", "tarantula.txt") # it changed!

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

# Q2: Question 2
# The new_directory function creates a new directory inside the current working directory, then creates a new empty file inside the new directory, and returns the list of files in that directory. Fill in the gaps to create a file "script.py" in the directory "PythonPrograms". 

import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename, "w") as file:
    pass

  # Return the list of files in the new directory
  return os.listdir(os.getcwd())

print(new_directory("PythonPrograms", "script.py"))


# Q4: Question 4
# The file_date function creates a new file in the current working directory, checks the date that the file was modified, and returns just the date portion of the timestamp in the format of yyyy-mm-dd. Fill in the gaps to create a file called "newfile.txt" and check the date that it was modified.

import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  file = open(filename, "w")
  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  t = datetime.datetime.fromtimestamp(timestamp)
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{t}".format(t=t.strftime("%Y-%m-%d")))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd


# Q5: Question 5
# The parent_directory function returns the name of the directory that's located just above the current working directory. Remember that '..' is a relative path alias that means "go up to the parent directory". Fill in the gaps to complete this function.



import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  relative_parent = os.path.join(os.getcwd(), os.pardir)

  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)

print(parent_directory())


#### CSV Files

# Parsing
# -> Analyzing a file's content to correctly structure the data

# CSV module

import csv
# open a file first
f = open("employees.txt")
# parsing txt to csv format
f_csv = csv.reader(f)
for row in f_csv:
    print(row)

# the reader() function of the CSV module will interpret the file as a CSV.

file = open("employees.txt")
file_csv = csv.reader(file)
for row in file_csv:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))

# Generating a CSV file 
hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]

with open("hosts.csv", "w") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)


# Dict Reader
# -> This reader turn each row of the data in CSV file into a dictionary

import csv
with open("software.csv") as software:
  reader = csv.DictReader(software)
  for row in reader:
    print(("{} has {} users").format(row["name"], row["users"]))

# Facebook has 28892392992 users
# MailTree has 23 users
# SkullHorn has 8 users

# Dict Writer

# so we have list of dictionaries
users = [
    {"name": "Sol Mansi", "username": "solm", "departement": "IT Infrastructure"},
    {"name": "Lio Nelson", "username": "lion", "departement": "User Experience Research"},
    {"name": "Charlie Grey", "username": "greyc", "departement": "Development"}
]

# define keys/column
keys = ["name", "username", "departement"]

# writing them to csv file
with open("by_departement.csv", "w") as by_departement:
    writer = csv.DictWriter(by_departement, fieldnames=keys)
    writer.writeheader() # will create the first line on csv based on keys we passed in fieldnames
    writer.writerows(users)

##########################################################################################

# Regular Expression [REGEX  or REGEXP]
## so what are these expression and why are they regular? (lol)

# -> is essentially a search query for text that's expressed by STRING PATTERN

import re 

log = "July 31 mycomputer bad_processes[12345]: ERROR Performing package upgrade"

regex = r"\[(\d+)\]" # this means: d means integer - "\[...\]" means marked by square brackets
# full meaning of the regex symbol: As long as there's a single sequence of number in the string marked by square brackets
# the regex will extract those numbers for us

result = re.search(regex, log)

print(result[0])

## Basic Matching with grep
# CLI: grep [word] /usr/share/dict/words

# GREP is case sensitive

# use '-i' to match a string regardless of case,

# RESERVED CHARACTERS [., +, *, ?, ^, $, (, ), [, ], {, }, |, \. etc]

# CLI: grep l.rts /usr/share/dict/words
# output:
# alerts
# blurts
# flirts

# Using the terminal, which of the following commands will correctly use grep to find the words “sling” and “sting” (assuming they are in our file, file.txt)?
# Correct Answer: user@ubuntu:~$ grep s.ing /usr/file.txt
# Nice work! In regex, a dot is a wildcard, so it can represent any character. This command will print both “sting” and “sling”, if they are in the file.

# Circumflex (^) is the beginning and dollar sign ($) is the end
# Circumflex (^) will return the matches pattern with sub-word in the beginning of the line
# example: ^fruit
# grep ^fruit /usr/share/dict/words
# output:
# fruit, fruit's, fruitless, fruitier, etc

# dollar sign ($) will return the matches pattern with sub-word in the end of the line
# example: cat$
# grep cat$ /usr/share/dict/words
# output:
# muscat, cat, tomcat, copycat, ducat, lolcat, pussycat, etc

#####################################################################

## Basic Regular Expression

# Simple Mathing

import re
result = re.search(r"aza", "plaza") # 'r' indicates RAWSTRING [No Special Characters (!*&@%$!^*@#*!@#^)]
print(result)

# substring in different location
result = re.search(r"aza", "bazaar") # 'r' indicates RAWSTRING [No Special Characters (!*&@%$!^*@#*!@#^)]
print(result)

# no matching
result = re.search(r"aza", "Turmoil") # 'r' indicates RAWSTRING [No Special Characters (!*&@%$!^*@#*!@#^)]
print(result) # None

## Simple Matching with Special Character

# Circumflex (^)

print(re.search(r"^x", "xenon"))
# <re.Match object; span=(0, 1), match='x'>

# Dot (.)
word = ["penguin", "ping", "Absolutely", "Holy ping", "Clapping", "Sponge", "Rapping"]
print(re.search(r"p.ng", word[1]))

for w in word:
  comp = re.search(r"p.ng", w)
  if comp:
    print(comp)

# Short Quiz: Simple Matching in Python
# Fill in the code to check if the text passed contains the vowels a, e and i, with exactly one occurrence of any other character in between.
import re
def check_aei(text):
  result = re.search(r"a.e.i.", text) # another solution: r"([aei]).\1"
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

# Here is your output:
# True
# False
# True

# Great work! You've written your first regular expression!

# to Ignore the case use -> re.IGNORECASE
word = ["Pangaea", "penguin", "ping", "Absolutely", "Holy ping", "Clapping", "Sponge", "Rapping"]
print(re.search(r"p.ng", word[1]))

for w in word:
  comp = re.search(r"p.ng", w, re.IGNORECASE)
  if comp:
    print(comp)



## Wildcards and Character Classes

# Wildcards like dot syntax is WILD, if you want more stricter matches use: CHARACTER CLASSES
# Characters Classes: Written in Square Brackets [], and let us list the character we want to match inside of those brackets.
# example:
print(re.search(r"[Pp]ython", "Python"))

# to range a character alphabetically use dash (-) -> REGEX TOKEN: [a-z]
print(re.search(r"[a-z]way", "What a way to go")) # hway

# combine a lower/upper case alpha and numeric
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))

# Short Quiz: Wildcards and Character Classes
# Fill in the code to check if the text passed contains punctuation symbols: commas, periods, colons, semicolons, question marks, and exclamation points.

import re
def check_punctuation (text):
  result = re.search(r"[^a-zA-Z0-9\s]+", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

# Here is your output:
# True
# False
# True
# True
# False

# Right on! You're seeing the flexibility of character classes in regular expressions!

## [^a-zA-Z0-9\s]+ Explanation (from regex101.com):
# [^a-zA-Z0-9\s]+/g
# Match a single character not present in the list below [^a-zA-Z0-9\s]
# + matches the previous token between one and unlimited times, as many times as possible, giving back as needed (greedy)
# a-z matches a single character in the range between a (index 97) and z (index 122) (case sensitive)
# A-Z matches a single character in the range between A (index 65) and Z (index 90) (case sensitive)
# 0-9 matches a single character in the range between 0 (index 48) and 9 (index 57) (case sensitive)
# \s matches any whitespace character (equivalent to [\r\n\t\f\v ])
# Global pattern flags 
# g modifier: global. All matches (don't return after first match)

print(re.search(r"[^a-zA-Z]", "This is sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is sentence with spaces.")) # to exlude space just add white space inside square bracket

## Use pipe syntax [ | ] to compare between regex expressions
print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I like tiger and dogs"))
print(re.search(r"cat|dog", "I like cats and dogs")) # re.search will return the first occurence of matching

# use re.findall() to return any matches | it will return a LIST of strings.
print(re.findall(r"cat|dog", "I like both cats and dogs"))
# output: ['cat', 'dog']

## Repeated Qualifiers [.*]

print(re.search(r"Py.*n", "Pygmalion"))

print(re.search(r"Py.*n", "Python Programming"))
# <re.Match object; span=(0, 17), match='Python Programmin'> # -> Greedy Behavior

print(re.search(r"Py[a-z]*n", "Python Programming")) # use character class to just only word mathes
# <re.Match object; span=(0, 6), match='Python'>

print(re.search(r"Py[a-z]*n", "Pyn")) # (*) is mean 0 or 1 or more occurences

# (+) is mean mathing character one or more occurences of the character that comes before it
print(re.search(r"o+l+", "goldfish"))
# <re.Match object; span=(1, 3), match='ol'>
















