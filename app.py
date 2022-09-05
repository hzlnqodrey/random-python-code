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

### Repeated Qualifiers [.*]

print(re.search(r"Py.*n", "Pygmalion"))

print(re.search(r"Py.*n", "Python Programming"))
# <re.Match object; span=(0, 17), match='Python Programmin'> # -> Greedy Behavior

print(re.search(r"Py[a-z]*n", "Python Programming")) # use character class to just only word mathes
# <re.Match object; span=(0, 6), match='Python'>

print(re.search(r"Py[a-z]*n", "Pyn")) # (*) is mean 0 or 1 or more occurences

## (+) is mean mathing character one or more occurences of the character that comes before it
print(re.search(r"o+l+", "goldfish"))
# <re.Match object; span=(1, 3), match='ol'>

print(re.search(r"o+l+", "woolly"))
# <re.Match object; span=(1, 5), match='ooll'>

print(re.search(r"o+l+", "boil"))
# None

# Short Quiz

# Question
# The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice. For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False. Fill in the code to make this work. 

import re
def repeating_letter_a(text):
  result = re.search(r"a.*a", text, re.IGNORECASE)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

# Here is your output:
# True
# False
# True
# True

# You get an A! See how handy the repetition qualifiers can
# be, when we're working with lots of different text!


## (?) is mean matching character ZERO or ONE occurences of the character that comes before it

print(re.search(r"p?each", "To each of their own")) # it means it might be ZERO P or ONE P is matches
# <re.Match object; span=(3, 7), match='each'>

print(re.search(r"p?each", "I like the peaches")) # IT HAS ONE P, so it will matches
# <re.Match object; span=(11, 16), match='peach'>

## Escaping Characters [if we wanna match the SPECIAL CHARACTERS/RESERVED CHARACTERS]

# If we don't use escape characters
print(re.search(r".com", "Welcome"))
# <re.Match object; span=(2, 6), match='lcom'>

# If we use escaping characters
print(re.search(r"\.com", "Welcome"))
# None. Nice!

print(re.search(r"\.com", "temandisabilitas.com"))
# <re.Match object; span=(16, 20), match='.com'>

## Special String Characters

# [\n] is new line
# [\t] is tab

# [\w] will match any ALPHANUMERIC character including letters, numbers and underscores
print(re.search(r"\w*", "This is an example"))
# <re.Match object; span=(0, 4), match='This'>
print(re.search(r"\w*", "And_this_is_example"))
# <re.Match object; span=(0, 19), match='And_this_is_example'>

# [\d] for matching number
# [\s] for matching whitespaces
# [\b] for word boundaries (the location of word the word in the substring or subsentence)

# Short Quiz: Escaping Characters
# Question
# Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace characters.

import re
def check_character_groups(text):
  result = re.search(r"[\w*]\s", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

# Here is your output:
# False
# True
# True
# False

# You got it! There's no escaping your regular expression
# expertise!


### Regular Expression in Real World Cases [in Action!]

## if we wanna match the Country with start A and end a
print(re.search(r"A.*a", "Argentina"))
# <re.Match object; span=(0, 9), match='Argentina'>
print(re.search(r"A.*a", "Ajerbaizan"))
# <re.Match object; span=(0, 9), match='Ajerbaiza'>

## we need to more stricter about our pattern, add ^ and $
print(re.search(r"^A.*a$", "Ajerbaizan")) # None
print(re.search(r"^A.*a$", "Argentina")) # <re.Match object; span=(0, 9), match='Argentina'>
print(re.search(r"^A.*a$", "Australia")) # <re.Match object; span=(0, 9), match='Australia'>

## example: the variable rule in python (no number in the beginning, only underspaces and letters)

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"

print(re.search(pattern, "_this_is_a_valid_variable_name_"))
# <re.Match object; span=(0, 31), match='_this_is_a_valid_variable_name_'>

print(re.search(pattern, "This isn't a valid variable")) # None. Whitespaces is not in the pattern
print(re.search(pattern, "my_variable01")) # Valid
# <re.Match object; span=(0, 13), match='my_variable01'>
print(re.search(pattern, "2my_variable01")) # None. Invalid

# Short Quiz: Regular Expressions in Action
# Question
# Fill in the code to check if the text passed looks like a standard sentence, meaning that it starts with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point.  

import re
def check_sentence(text):
  result = re.search(r"___", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True

# Here is your output:
# True
# False
# False
# False
# True

# Awesome! You're becoming a regular "regular expression"
# writer!


## Practice Quiz: Basic Regular Expressions

# Q1
# The check_web_address function checks if the text passed qualifies as a top-level web address, meaning that it contains alphanumeric characters (which includes letters, numbers, and underscores), as well as periods, dashes, and a plus sign, followed by a period and a character-only top-level domain such as ".com", ".info", ".edu", etc. Fill in the regular expression to do that, using escape characters, wildcards, repetition qualifiers, beginning and end-of-line characters, and character classes.
import re
def check_web_address(text):
  pattern = r"[a-zA-Z0-9_]+[\.\+\-][\.\w*]*[^\/]$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

# True
# False
# True
# False
# True


# Q2
# Question 2
# The check_time function checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12, with no leading zero, followed by a colon, then minutes between 00 and 59, then an optional space, and then AM or PM, in upper or lower case. Fill in the regular expression to do that. How many of the concepts that you just learned can you use here?
import re
def check_time(text):
  pattern = r"^(?:1[0-2]|[0-9]):(?:[0-5][0-9])(?:\s?[AaPp][Mm])"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False

# True
# True
# False
# False


# Question 3
# The contains_acronym function checks the text for the presence of 2 or more characters or digits surrounded by parentheses, with at least the first character in uppercase (if it's a letter), returning True if the condition is met, or False otherwise. For example, "Instant messaging (IM) is a set of communication technologies used for text-based communication" should return True since (IM) satisfies the match conditions." Fill in the regular expression in this function: 
import re
def contains_acronym(text):
  pattern = r"[\(\)][a-zA-Z0-9]*"
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

# True
# True
# False
# True
# True

# Question 6
# Fill in the code to check if the text passed includes a possible U.S. zip code, formatted as follows: exactly 5 digits, and sometimes, but not always, followed by a dash with 4 more digits. The zip code needs to be preceded by at least one space, and cannot be at the start of the text.
import re
def check_zip_code (text):
  result = re.search(r" \d{5}(?:-\d{4})?", text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False

# True
# False
# True
# False


################ Advanced Regular Expressions

### Capturing Group () - Literal Parentheses

# example: 
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
# <re.Match object; span=(0, 13), match='Lovelace, Ada'>

## Let's look up into groups method of re
print(result.groups()) 
# ('Lovelace', 'Ada') # Apparently it will return Tuple of matches elements.

# Accessing the Elements
print(result[0]) # return strings of all elements
# Lovelace, Ada
print(result[1]) # return string of the first element
# Lovelace
print(result[2]) # return string of the second element, and so on
# Ada

# More Example:

def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

rearrange_name("Lovelace, Ada") # 'Ada Lovelace'
rearrange_name("Qodrey, Hazlan") # 'Hazlan Qodrey'
rearrange_name("Hansel, Timotius") # 'Timotius Hansel'


### Short Quiz: Capturing Groups
# Question
# Fix the regular expression used in the rearrange_name function so that it can match middle names, middle initials, as well as double surnames.
import re
def rearrange_name(name):
  result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)

# Here is your output:
# John F. Kennedy

# Nice work! You're doing well using regular expressions to
# capture groups.


## More of Repetition Qualifiers
# {} -> specifying a range of repetition

# example:
print(re.search(r"[a-zA-Z]{5}", "A ghost, a tales, and folklore")) # Match the first occurence of 5 letter of word
# <re.Match object; span=(2, 7), match='ghost'>
# use findall method to return all the matches
print(re.findall(r"[a-zA-Z]{5}", "A ghost, a tales, and folklore kills")) # Match all of word that have 5 or more letter
# ['ghost', 'tales', 'folkl', 'kills']

# Hmm, seems folkl is getting involved, how to match exactly 5 letters?
# use \b [Word Boundaries]
# example:
print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared, and the story of the saint folklore happened"))
# ['scary', 'ghost', 'story', 'saint'] | Nice!

# Curly Brackets Ranges { from , to [can be null or open ended] } 
print(re.findall(r"\w{5,10}", "I really like strowberry shortcake!"))
# ['really', 'strowberry', 'shortcake']

# Open ended upper bracket
print(re.findall(r"\w{5,}", "I really like strowberry shortcake sooooooooo muchhhhhhhhhhhhhhhhh!"))
# ['really', 'strowberry', 'shortcake', 'sooooooooo', 'muchhhhhhhhhhhhhhhhh']

# More example: We search a pattern of the letter S followed by up to 20 alphanumeric characters
print(re.findall(r"s\w{,20}", "I really like strowberry shortcake sooooooooo muchhhhhhhhhhhhhhhhh!"))
# ['strowberry', 'shortcake', 'sooooooooo']
print(re.search(r"s\w{,20}", "I really like strowberry shortcake sooooooooo muchhhhhhhhhhhhhhhhh!"))
# <re.Match object; span=(14, 24), match='strowberry'>


## Short Quiz: More of Repetition Qualifiers
# Question
# The long_words function returns all words that are at least 7 characters. Fill in the regular expression to complete this function.
import re
def long_words(text):
  pattern = r"[a-zA-Z]{7,}" # another solution: "\w{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []


# Here is your output:
# ['morning']
# ['chocolate', 'afternoon']
# []

# Nice job! Your regular expressions are getting more and more
# sophisticated!


## Extracting a PID [Process ID] Using regexes in Python

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = "\[(\d+)\]"
result = re.search(regex, log)
print(result[1]) # 12345

# Extract PID function (return PID if matched, return None if not matched)

def extract_pid(log_lines):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_lines)
    if result is None:
        return ""
    return result[1]

log = extract_pid("saya siapa kamu dimana dia siapa [popo]")
print(log) # 
log1 = extract_pid("99 Matters of time like the hilling tree as we used before [32456]")
print(log1) # 32456