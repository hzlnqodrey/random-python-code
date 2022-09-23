import unittest
import sys
import subprocess
import re
import csv
import datetime
import os
import psutil
import shutil
from dataclasses import field
import requests as req
import pandas as pd

response = req.get("http://instagram.com")

print(response)

visitors = [1234, 5232, 9223, 8856, 7752]
errors = [23, 52, 62, 89, 12]

df = pd.DataFrame({"visitors": visitors, "errors": errors},
                  index=["Mon", "Tue", "Wed", "Thu", "Fri"])

print(df)

# DataFrame operator method [Mean, Average, Sum, etc]
errors_mean = df["errors"].mean()
print(errors_mean)


"hello " * 10  # print on interactive interpreter CLI

du = shutil.disk_usage("/")
print(du)
# -> usage(total=269490393088, used=1470783488, free=254258937856)

du.free/du.total*100
# -> 94.34805261238893

psutil.cpu_percent(.1)
psutil.cpu_percent(.1)
0.0
psutil.cpu_percent(.1)
0.0

# Health Check (of a PC) Script's

#!/usr/bin/env python3

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


# Reading Files

file = open("spider.txt")
# print(file.readline()) # read the first line
# print(file.readline()) # read the second line
# print(file.readlines()) # read the second line
print(file.read())  # read the second line

file.close()  # open-use-close: is a typical way of working with files in most prog lang

# with 'with block' Python will automatically close the file
with open("spider.txt") as file1:
    print(file1.read())

# Both methods read from the current position. The readline() method reads one line, while read() reads until the end of the file.

# file object can be iterated the same way as other Python sequences (string, list, dict, set)

# you can do this to uppercase ur text lines:

with open("spider.txt") as file:
    for line in file:
        # this will create a weird a empty line before read the next line
        print(line.upper())

# how to avoid a empty new line?
# we can use string method: strip() to remove  all surrounding white spaces [including: tabs and new lines]

with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())

# Good work! Here, we are iterating line by line, and the strip() command is used to remove extra whitespace.

# store file line to list (the element is line by line (each line))

file = open("spider.txt")
lines = file.readlines()  # list
file.close()  # eventhough we close it, the lines has the all the infos from file
print(lines)

# Write content to file
# by default the 'open()' use "r" mode to read-only the file
# the "w" argument is to write-only mode, if the file doesn't exist then Python will create it
# then if the file does exist, the current content will be overwritten by whatever we decide to write using our script
# remember you can't read if the argument is write-only mode, u need to "r+" [read-write] mode
# if you want to add content at the end of an existing content in file, use "a" (to append)
with open("novel.txt", "w") as file:
    file.write("It was a dark and stormy night")

# You nailed it! When using write mode, the old contents get deleted as soon as the file is opened.


# OS MODULE
# Delete, Rename, or modified time or else, use os module

# Remove File

os.remove("novel.txt")

# If you try to remove file that you already remove or file that's not even created in the first hand, it will raise an Error
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# FileNotFoundError: [Errno 2] No such file or directory: 'novel.txt'

# os.rename(arg1, arg2)
# arg1 -> the old name
# arg2 -> the new name

os.rename("spider.txt", "tarantula.txt")  # it changed!

# how do we check if the file is exist or not?
# submodule of OS [os.path sub-module]
os.path.exists("tarantula.txt")
os.path.exists("spider.txt")

# >>> with open("sayagila.txt", "w") as newFile:
# ...   newFile.write("sayaaaaaaaaaaa")
# ...
# 14
# >>> os.path.exists("sayagila.txt")
# True


# os.path.[module]

# [1] getsize -> to check how big the size of the file in bytes
os.path.getsize("sayagila.txt")
# >>> os.path.getsize("sayagila.txt")
# 14

# [2] gettime -> to check when the file was last modified
os.path.getmtime("sayagila.txt")
# >>> os.path.getmtime("sayagila.txt")
# 1661339935.40045 -> # Issa UNIX TIMESTAMP and hard to read, convert it to datestamp module

time_stamp = os.path.getmtime("sayagila.txt")
datetime.datetime.fromtimestamp(time_stamp)
# datetime.datetime(2022, 8, 24, 18, 18, 55, 400450) -> output

# in os.path we can work with absolute and relative paths
# .abspath() -> to locate where exactly located on dir
os.path.abspath("sayagila.txt")
# 'C:\\Users\\<user>\\AppData\\Local\\Programs\\Python\\Python38\\sayagila.txt'

# How to work with | DIRECTORIES | or folders(?)

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


# Practice Quiz

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


def new_directory(directory, filename):
    # Before creating a new directory, check to see if it already exists
    if os.path.isdir(directory) == False:
        os.mkdir(directory)

    # Create the new file inside of the new directory
    os.chdir(directory)
    with open(filename, "w") as file:
        pass

    # Return the list of files in the new directory
    return os.listdir(os.getcwd())


print(new_directory("PythonPrograms", "script.py"))


# Q4: Question 4
# The file_date function creates a new file in the current working directory, checks the date that the file was modified, and returns just the date portion of the timestamp in the format of yyyy-mm-dd. Fill in the gaps to create a file called "newfile.txt" and check the date that it was modified.


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


def parent_directory():
    # Create a relative path to the parent
    # of the current working directory
    relative_parent = os.path.join(os.getcwd(), os.pardir)

    # Return the absolute path of the parent directory
    return os.path.abspath(relative_parent)


print(parent_directory())


# CSV Files

# Parsing
# -> Analyzing a file's content to correctly structure the data

# CSV module

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
hosts = [["workstation.local", "192.168.25.46"],
         ["webserver.cloud", "10.2.5.6"]]

with open("hosts.csv", "w") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)


# Dict Reader
# -> This reader turn each row of the data in CSV file into a dictionary

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
    {"name": "Lio Nelson", "username": "lion",
        "departement": "User Experience Research"},
    {"name": "Charlie Grey", "username": "greyc", "departement": "Development"}
]

# define keys/column
keys = ["name", "username", "departement"]

# writing them to csv file
with open("by_departement.csv", "w") as by_departement:
    writer = csv.DictWriter(by_departement, fieldnames=keys)
    # will create the first line on csv based on keys we passed in fieldnames
    writer.writeheader()
    writer.writerows(users)

##########################################################################################

# Regular Expression [REGEX  or REGEXP]
# so what are these expression and why are they regular? (lol)

# -> is essentially a search query for text that's expressed by STRING PATTERN


log = "July 31 mycomputer bad_processes[12345]: ERROR Performing package upgrade"

# this means: d means integer - "\[...\]" means marked by square brackets
regex = r"\[(\d+)\]"
# full meaning of the regex symbol: As long as there's a single sequence of number in the string marked by square brackets
# the regex will extract those numbers for us

result = re.search(regex, log)

print(result[0])

# Basic Matching with grep
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

# Basic Regular Expression

# Simple Mathing

# 'r' indicates RAWSTRING [No Special Characters (!*&@%$!^*@#*!@#^)]
result = re.search(r"aza", "plaza")
print(result)

# substring in different location
# 'r' indicates RAWSTRING [No Special Characters (!*&@%$!^*@#*!@#^)]
result = re.search(r"aza", "bazaar")
print(result)

# no matching
# 'r' indicates RAWSTRING [No Special Characters (!*&@%$!^*@#*!@#^)]
result = re.search(r"aza", "Turmoil")
print(result)  # None

# Simple Matching with Special Character

# Circumflex (^)

print(re.search(r"^x", "xenon"))
# <re.Match object; span=(0, 1), match='x'>

# Dot (.)
word = ["penguin", "ping", "Absolutely",
        "Holy ping", "Clapping", "Sponge", "Rapping"]
print(re.search(r"p.ng", word[1]))

for w in word:
    comp = re.search(r"p.ng", w)
    if comp:
        print(comp)

# Short Quiz: Simple Matching in Python
# Fill in the code to check if the text passed contains the vowels a, e and i, with exactly one occurrence of any other character in between.


def check_aei(text):
    result = re.search(r"a.e.i.", text)  # another solution: r"([aei]).\1"
    return result != None


print(check_aei("academia"))  # True
print(check_aei("aerial"))  # False
print(check_aei("paramedic"))  # True

# Here is your output:
# True
# False
# True

# Great work! You've written your first regular expression!

# to Ignore the case use -> re.IGNORECASE
word = ["Pangaea", "penguin", "ping", "Absolutely",
        "Holy ping", "Clapping", "Sponge", "Rapping"]
print(re.search(r"p.ng", word[1]))

for w in word:
    comp = re.search(r"p.ng", w, re.IGNORECASE)
    if comp:
        print(comp)


# Wildcards and Character Classes

# Wildcards like dot syntax is WILD, if you want more stricter matches use: CHARACTER CLASSES
# Characters Classes: Written in Square Brackets [], and let us list the character we want to match inside of those brackets.
# example:
print(re.search(r"[Pp]ython", "Python"))

# to range a character alphabetically use dash (-) -> REGEX TOKEN: [a-z]
print(re.search(r"[a-z]way", "What a way to go"))  # hway

# combine a lower/upper case alpha and numeric
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))

# Short Quiz: Wildcards and Character Classes
# Fill in the code to check if the text passed contains punctuation symbols: commas, periods, colons, semicolons, question marks, and exclamation points.


def check_punctuation(text):
    result = re.search(r"[^a-zA-Z0-9\s]+", text)
    return result != None


print(check_punctuation("This is a sentence that ends with a period."))  # True
print(check_punctuation("This is a sentence fragment without a period"))  # False
print(check_punctuation("Aren't regular expressions awesome?"))  # True
print(check_punctuation("Wow! We're really picking up some steam now!"))  # True
print(check_punctuation("End of the line"))  # False

# Here is your output:
# True
# False
# True
# True
# False

# Right on! You're seeing the flexibility of character classes in regular expressions!

# [^a-zA-Z0-9\s]+ Explanation (from regex101.com):
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
# to exlude space just add white space inside square bracket
print(re.search(r"[^a-zA-Z ]", "This is sentence with spaces."))

# Use pipe syntax [ | ] to compare between regex expressions
print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I like tiger and dogs"))
# re.search will return the first occurence of matching
print(re.search(r"cat|dog", "I like cats and dogs"))

# use re.findall() to return any matches | it will return a LIST of strings.
print(re.findall(r"cat|dog", "I like both cats and dogs"))
# output: ['cat', 'dog']

# Repeated Qualifiers [.*]

print(re.search(r"Py.*n", "Pygmalion"))

print(re.search(r"Py.*n", "Python Programming"))
# <re.Match object; span=(0, 17), match='Python Programmin'> # -> Greedy Behavior

# use character class to just only word mathes
print(re.search(r"Py[a-z]*n", "Python Programming"))
# <re.Match object; span=(0, 6), match='Python'>

print(re.search(r"Py[a-z]*n", "Pyn"))  # (*) is mean 0 or 1 or more occurences

# (+) is mean mathing character one or more occurences of the character that comes before it
print(re.search(r"o+l+", "goldfish"))
# <re.Match object; span=(1, 3), match='ol'>

print(re.search(r"o+l+", "woolly"))
# <re.Match object; span=(1, 5), match='ooll'>

print(re.search(r"o+l+", "boil"))
# None

# Short Quiz

# Question
# The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice. For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False. Fill in the code to make this work.


def repeating_letter_a(text):
    result = re.search(r"a.*a", text, re.IGNORECASE)
    return result != None


print(repeating_letter_a("banana"))  # True
print(repeating_letter_a("pineapple"))  # False
print(repeating_letter_a("Animal Kingdom"))  # True
print(repeating_letter_a("A is for apple"))  # True

# Here is your output:
# True
# False
# True
# True

# You get an A! See how handy the repetition qualifiers can
# be, when we're working with lots of different text!


# (?) is mean matching character ZERO or ONE occurences of the character that comes before it

# it means it might be ZERO P or ONE P is matches
print(re.search(r"p?each", "To each of their own"))
# <re.Match object; span=(3, 7), match='each'>

# IT HAS ONE P, so it will matches
print(re.search(r"p?each", "I like the peaches"))
# <re.Match object; span=(11, 16), match='peach'>

# Escaping Characters [if we wanna match the SPECIAL CHARACTERS/RESERVED CHARACTERS]

# If we don't use escape characters
print(re.search(r".com", "Welcome"))
# <re.Match object; span=(2, 6), match='lcom'>

# If we use escaping characters
print(re.search(r"\.com", "Welcome"))
# None. Nice!

print(re.search(r"\.com", "temandisabilitas.com"))
# <re.Match object; span=(16, 20), match='.com'>

# Special String Characters

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


def check_character_groups(text):
    result = re.search(r"[\w*]\s", text)
    return result != None


print(check_character_groups("One"))  # False
print(check_character_groups("123  Ready Set GO"))  # True
print(check_character_groups("username user_01"))  # True
print(check_character_groups("shopping_list: milk, bread, eggs."))  # False

# Here is your output:
# False
# True
# True
# False

# You got it! There's no escaping your regular expression
# expertise!


# Regular Expression in Real World Cases [in Action!]

# if we wanna match the Country with start A and end a
print(re.search(r"A.*a", "Argentina"))
# <re.Match object; span=(0, 9), match='Argentina'>
print(re.search(r"A.*a", "Ajerbaizan"))
# <re.Match object; span=(0, 9), match='Ajerbaiza'>

# we need to more stricter about our pattern, add ^ and $
print(re.search(r"^A.*a$", "Ajerbaizan"))  # None
# <re.Match object; span=(0, 9), match='Argentina'>
print(re.search(r"^A.*a$", "Argentina"))
# <re.Match object; span=(0, 9), match='Australia'>
print(re.search(r"^A.*a$", "Australia"))

# example: the variable rule in python (no number in the beginning, only underspaces and letters)

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"

print(re.search(pattern, "_this_is_a_valid_variable_name_"))
# <re.Match object; span=(0, 31), match='_this_is_a_valid_variable_name_'>

# None. Whitespaces is not in the pattern
print(re.search(pattern, "This isn't a valid variable"))
print(re.search(pattern, "my_variable01"))  # Valid
# <re.Match object; span=(0, 13), match='my_variable01'>
print(re.search(pattern, "2my_variable01"))  # None. Invalid

# Short Quiz: Regular Expressions in Action
# Question
# Fill in the code to check if the text passed looks like a standard sentence, meaning that it starts with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point.


def check_sentence(text):
    result = re.search(r"___", text)
    return result != None


print(check_sentence("Is this is a sentence?"))  # True
print(check_sentence("is this is a sentence?"))  # False
print(check_sentence("Hello"))  # False
print(check_sentence("1-2-3-GO!"))  # False
print(check_sentence("A star is born."))  # True

# Here is your output:
# True
# False
# False
# False
# True

# Awesome! You're becoming a regular "regular expression"
# writer!


# Practice Quiz: Basic Regular Expressions

# Q1
# The check_web_address function checks if the text passed qualifies as a top-level web address, meaning that it contains alphanumeric characters (which includes letters, numbers, and underscores), as well as periods, dashes, and a plus sign, followed by a period and a character-only top-level domain such as ".com", ".info", ".edu", etc. Fill in the regular expression to do that, using escape characters, wildcards, repetition qualifiers, beginning and end-of-line characters, and character classes.


def check_web_address(text):
    pattern = r"[a-zA-Z0-9_]+[\.\+\-][\.\w*]*[^\/]$"
    result = re.search(pattern, text)
    return result != None


print(check_web_address("gmail.com"))  # True
print(check_web_address("www@google"))  # False
print(check_web_address("www.Coursera.org"))  # True
print(check_web_address("web-address.com/homepage"))  # False
print(check_web_address("My_Favorite-Blog.US"))  # True

# True
# False
# True
# False
# True


# Q2
# Question 2
# The check_time function checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12, with no leading zero, followed by a colon, then minutes between 00 and 59, then an optional space, and then AM or PM, in upper or lower case. Fill in the regular expression to do that. How many of the concepts that you just learned can you use here?


def check_time(text):
    pattern = r"^(?:1[0-2]|[0-9]):(?:[0-5][0-9])(?:\s?[AaPp][Mm])"
    result = re.search(pattern, text)
    return result != None


print(check_time("12:45pm"))  # True
print(check_time("9:59 AM"))  # True
print(check_time("6:60am"))  # False
print(check_time("five o'clock"))  # False

# True
# True
# False
# False


# Question 3
# The contains_acronym function checks the text for the presence of 2 or more characters or digits surrounded by parentheses, with at least the first character in uppercase (if it's a letter), returning True if the condition is met, or False otherwise. For example, "Instant messaging (IM) is a set of communication technologies used for text-based communication" should return True since (IM) satisfies the match conditions." Fill in the regular expression in this function:


def contains_acronym(text):
    pattern = r"[\(\)][a-zA-Z0-9]*"
    result = re.search(pattern, text)
    return result != None


print(contains_acronym(
    "Instant messaging (IM) is a set of communication technologies used for text-based communication"))  # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication"))  # True
print(contains_acronym("Please do NOT enter without permission!"))  # False
print(contains_acronym(
    "PostScript is a fourth-generation programming language (4GL)"))  # True
print(contains_acronym(
    "Have fun using a self-contained underwater breathing apparatus (Scuba)!"))  # True

# True
# True
# False
# True
# True

# Question 6
# Fill in the code to check if the text passed includes a possible U.S. zip code, formatted as follows: exactly 5 digits, and sometimes, but not always, followed by a dash with 4 more digits. The zip code needs to be preceded by at least one space, and cannot be at the start of the text.


def check_zip_code(text):
    result = re.search(r" \d{5}(?:-\d{4})?", text)
    return result != None


print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code(
    "The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False

# True
# False
# True
# False


# Advanced Regular Expressions

# Capturing Group () - Literal Parentheses

# example:
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
# <re.Match object; span=(0, 13), match='Lovelace, Ada'>

# Let's look up into groups method of re
print(result.groups())
# ('Lovelace', 'Ada') # Apparently it will return Tuple of matches elements.

# Accessing the Elements
print(result[0])  # return strings of all elements
# Lovelace, Ada
print(result[1])  # return string of the first element
# Lovelace
print(result[2])  # return string of the second element, and so on
# Ada

# More Example:


def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])


rearrange_name("Lovelace, Ada")  # 'Ada Lovelace'
rearrange_name("Qodrey, Hazlan")  # 'Hazlan Qodrey'
rearrange_name("Hansel, Timotius")  # 'Timotius Hansel'


# Short Quiz: Capturing Groups
# Question
# Fix the regular expression used in the rearrange_name function so that it can match middle names, middle initials, as well as double surnames.


def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])


name = rearrange_name("Kennedy, John F.")
print(name)

# Here is your output:
# John F. Kennedy

# Nice work! You're doing well using regular expressions to
# capture groups.


# More of Repetition Qualifiers
# {} -> specifying a range of repetition

# example:
# Match the first occurence of 5 letter of word
print(re.search(r"[a-zA-Z]{5}", "A ghost, a tales, and folklore"))
# <re.Match object; span=(2, 7), match='ghost'>
# use findall method to return all the matches
# Match all of word that have 5 or more letter
print(re.findall(r"[a-zA-Z]{5}", "A ghost, a tales, and folklore kills"))
# ['ghost', 'tales', 'folkl', 'kills']

# Hmm, seems folkl is getting involved, how to match exactly 5 letters?
# use \b [Word Boundaries]
# example:
print(re.findall(
    r"\b[a-zA-Z]{5}\b", "A scary ghost appeared, and the story of the saint folklore happened"))
# ['scary', 'ghost', 'story', 'saint'] | Nice!

# Curly Brackets Ranges { from , to [can be null or open ended] }
print(re.findall(r"\w{5,10}", "I really like strowberry shortcake!"))
# ['really', 'strowberry', 'shortcake']

# Open ended upper bracket
print(re.findall(
    r"\w{5,}", "I really like strowberry shortcake sooooooooo muchhhhhhhhhhhhhhhhh!"))
# ['really', 'strowberry', 'shortcake', 'sooooooooo', 'muchhhhhhhhhhhhhhhhh']

# More example: We search a pattern of the letter S followed by up to 20 alphanumeric characters
print(re.findall(
    r"s\w{,20}", "I really like strowberry shortcake sooooooooo muchhhhhhhhhhhhhhhhh!"))
# ['strowberry', 'shortcake', 'sooooooooo']
print(re.search(
    r"s\w{,20}", "I really like strowberry shortcake sooooooooo muchhhhhhhhhhhhhhhhh!"))
# <re.Match object; span=(14, 24), match='strowberry'>


# Short Quiz: More of Repetition Qualifiers
# Question
# The long_words function returns all words that are at least 7 characters. Fill in the regular expression to complete this function.


def long_words(text):
    pattern = r"[a-zA-Z]{7,}"  # another solution: "\w{7,}"
    result = re.findall(pattern, text)
    return result


print(long_words("I like to drink coffee in the morning."))  # ['morning']
# ['chocolate', 'afternoon']
print(long_words("I also have a taste for hot chocolate in the afternoon."))
print(long_words("I never drink tea late at night."))  # []


# Here is your output:
# ['morning']
# ['chocolate', 'afternoon']
# []

# Nice job! Your regular expressions are getting more and more
# sophisticated!


# Extracting a PID [Process ID] Using regexes in Python

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = "\[(\d+)\]"
result = re.search(regex, log)
print(result[1])  # 12345

# Extract PID function (return PID if matched, return None if not matched)


def extract_pid(log_lines):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_lines)
    if result is None:
        return ""
    return result[1]


log = extract_pid("saya siapa kamu dimana dia siapa [popo]")
print(log)
log1 = extract_pid(
    "99 Matters of time like the hilling tree as we used before [32456]")
print(log1)  # 32456

# Short Quiz: Extracting a PID Using regexes in Python
# Question
# Add to the regular expression used in the extract_pid function, to return the uppercase message in parenthesis, after the process id.


def extracting_pid(logging_lines):
    regex = r"\[(\d+)\]: (\b[A-Z]+\b)"
    result = re.search(regex, logging_lines)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])


print(extracting_pid(
    "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"))  # 12345 (ERROR)
print(extracting_pid("99 elephants in a [cage]"))  # None
print(extracting_pid(
    "A string that also has numbers [34567] but no uppercase message"))  # None
# 67890 (RUNNING)
print(extracting_pid(
    "July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup"))

# Here is your output:
# 12345 (ERROR)
# None
# None
# 67890 (RUNNING)

# You nailed it! You're using the tools you've learned in the
# previous lessons, and it shows!


# More of Re Modules (Splitting and Replacing)

re.split(r"[.?!]", "One Sentence. Another one? And the last one!")
# ['One Sentence', ' Another one', ' And the last one', ''] # The notation mark that we putting in the matches table were not in

# if we want to include the notation mark -> use capturing parentheses
re.split(r"([.?!])", "One Sentence. Another one? And the last one!")
# ['One Sentence', '.', ' Another one', '?', ' And the last one', '!', ''] | Good

# SUB method (replacing the matches string to subtitute string)
# example:

re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]",
       "Received an email from hazlanqodri2020work@gmail.com")
# 'Received an email from [REDACTED]'

# more example: [fam name, first name case]:
re.sub(r"([\w .-]*), ([\w .-]*)", r"\2 \1", "Lovelace, Ada")
# Explanation:
# First Parameter is the pattern we look up for
# Second Parameter is the subtitute matches we gonna change for the Third Parameter
# Second Parameter: when we used capturing group in first param,
# a number in second param indicates the corresponding captured group in first param
# 'Ada Lovelace'

# more example: [Change Date Format]
re.sub(r"([0-9]{4})-([0-9]{2})-([0-9]{2})", r"\3/\2/\1", "2022-09-05")
# '05/09/2022'

# Short Quiz: Splitting and Replacing

# Question
# We want to split a piece of text by either the word "a" or "the", as implemented in the following code. What is the resulting split list?

re.split(r"the|a", "One sentence. Another one? And the last one!")

# Correct
# Well done! This regular expression uses "the" and "a" as delimiters, no matter where they are in the text, even in the middle of other words like "Another" and "last".


# Practice Quiz: Advanced Regular Expressions

# Question 1
# We're working with a CSV file, which contains employee information. Each record has a name field, followed by a phone number field, and a role field. The phone number field contains U.S. phone numbers, and needs to be modified to the international format, with "+1-" in front of the phone number. Fill in the regular expression, using groups, to use the transform_record function to do that.


def transform_record(record):
    new_record = re.sub(r"([\w ]+),([\w -]+),([\w ]+)", r"\1,+1-\2,\3", record)
    return new_record


print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist"))
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer"))
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer"))
# Charlie Rivera,+1-698-746-3357,Web Developer

# Sabrina Green,+1-802-867-5309,System Administrator
# Eli Jones,+1-684-3481127,IT specialist
# Melody Daniels,+1-846-687-7436,Programmer
# Charlie Rivera,+1-698-746-3357,Web Developer


# Question 2
# The multi_vowel_words function returns all words with 3 or more consecutive vowels (a, e, i, o, u). Fill in the regular expression to do that


def multi_vowel_words(text):
    pattern = r"[\w]*[aiueo]{3,}[\w]*"
    result = re.findall(pattern, text)
    return result


print(multi_vowel_words("Life is beautiful"))
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious."))
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words(
    "The rambunctious children had to sit quietly and await their delicious dinner."))
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)"))
# ['queue']

print(multi_vowel_words("Hello world!"))
# []

# ['beautiful']
# ['Obviously', 'queen', 'courageous', 'gracious']
# ['rambunctious', 'quietly', 'delicious']
# ['queue']
# []


# Question 4
# The transform_comments function converts comments in a Python script into those usable by a C compiler. This means looking for text that begins with a hash mark (#) and replacing it with double slashes (//), which is the C single-line comment indicator. For the purpose of this exercise, we'll ignore the possibility of a hash mark embedded inside of a Python command, and assume that it's only used to indicate a comment. We also want to treat repetitive hash marks (##), (###), etc., as a single comment indicator, to be replaced with just (//) and not (#//) or (//#). Fill in the parameters of the substitution method to complete this function:


def transform_comments(line_of_code):
    result = re.sub(r"[#]+", r"//", line_of_code)
    return result


print(transform_comments("### Start of program"))
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable"))
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable"))
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)"))
# Should be "  return(number)"

# // Start of program
#   number = 0   // Initialize the variable
#   number += 1   // Increment the variable
#   return(number)

# Question 5
# The convert_phone_number function checks for a U.S. phone number format: XXX-XXX-XXXX (3 digits followed by a dash, 3 more digits followed by a dash, and 4 digits), and converts it to a more formal format that looks like this: (XXX) XXX-XXXX. Fill in the regular expression to complete this function.


def convert_phone_number(phone):
    result = re.sub(
        r"([0-9]{3})-([0-9]{3})-(\b[0-9]{4}\b)", r"(\1) \2-\3", phone)
    return result


# My number is (212) 345-9999.
print(convert_phone_number("My number is 212-345-9999."))
# Please call (888) 555-1234
print(convert_phone_number("Please call 888-555-1234"))
print(convert_phone_number("123-123-12345"))  # 123-123-12345
# Phone number of Buckingham Palace is +44 303 123 7300
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300"))

# My number is (212) 345-9999.
# Please call (888) 555-1234
# 123-123-12345
# Phone number of Buckingham Palace is +44 303 123 7300

# Qwiklabs

#!/usr/bin/env python3


def contains_domain(address, domain):
    """Returns True if the email address contains the given,domain,in the domain position, false if not."""
    domain = r'[\w\.-]+@'+domain+'$'
    if re.match(domain, address):
        return True
    return False


def replace_domain(address, old_domain, new_domain):
    """Replaces the old domain with the new domain in the received address."""
    old_domain_pattern = r'' + old_domain + '$'
    address = re.sub(old_domain_pattern, new_domain, address)
    return address


def main():
    """Processes the list of emails, replacing any instances of the old domain with the new domain."""
    old_domain, new_domain = 'abc.edu', 'xyz.edu'
    csv_file_location = '<csv_file_location>'
    report_file = '<path_to_home_directory>' + '/updated_user_emails.csv'
    user_email_list = []
    old_domain_email_list = []
    new_domain_email_list = []
    with open(csv_file_location, 'r') as f:
        user_data_list = list(csv.reader(f))
        user_email_list = [data[1].strip() for data in user_data_list[1:]]
        for email_address in user_email_list:
            if contains_domain(email_address, old_domain):
                old_domain_email_list.append(email_address)
                replaced_email = replace_domain(
                    email_address, old_domain, new_domain)
                new_domain_email_list.append(replaced_email)
        email_key = ' ' + 'Email Address'
        email_index = user_data_list[0].index(email_key)
        for user in user_data_list[1:]:
            for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
                if user[email_index] == ' ' + old_domain:
                    user[email_index] = ' ' + new_domain
    f.close()
    with open(report_file, 'w+') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(user_data_list)
        output_file.close()


main()

################################################################

# Subprocess Module

# inside ../September/../main.py

#!/usr/bin/env python3

subprocess.run(["date"])
subprocess.run(["sleep", "5"])  # this will blocked out CLI for 5 sec

result = subprocess.run(['ls', 'this_file_does_not_exist'])
print(result.returncode)

# WHO command
# -> which prints the users currently logged into a computer
# -> To be able to process the output of the command,
# -> We'll set a parameter called [capture_output] to True when calling the run function

# HOST command
# -> which can convert a host name to an IP address, pass a parameter capture_output to True

#!/usr/bin/env python3

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)
# the result was a raw array of bytes, because we don't decode the encoding utf-8 parse
print(result.stdout)

# so use DECODE method
# this method applies an encoding to transform the bytes into a string
# by default, it uses a UTF-8 encoding
print(result.stdout.decode().split())

# Short Quiz
# Which of the following is a Unicode standard used to convert an array of bytes into a string?

# UTF-8

# Correct
# Woohoo! This encoding is part of the Unicode standard that can transform an array of bytes into a string.

# What if there is any error in capture_output parameter? use STDERR

# example: use RM command to remove non-existing file

result = subprocess.run(["rm", "saya_gila.txt"], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stderr)
print(result.stderr.decode())


# Advanced Subprocess Management

# ENV command

#!/usr/bin/env python3


my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)

# CWD command
# -> change the Current Working Directory

# timeout parameter on .run() method
# -> this will cause the run function to kill the process if it takes longer than a given number of seconds to finish

# Shell parameter on .run() method [True/False]
# -> python will first execute an instance of the default system shell and then run the given command inside of it

# Which method do you use to prepare a new environment to modify environment variables?

# Correct answer: copy

# Correct
# Awesome! Calling this method of the os.environ dictionary will copy the current environment variables to store and prepare a new environment.


# Processing Log Files

# use REGEX to extract info in text based file

# Filtering log files with Regular Expressions

#!/usr/bin/env python3


logfile = sys.argv[1]  # to get the second argument in CLI

with open(logfile) as f:
    for line in f:
        # Check whether "CRON" letter is in logfile
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        print(result[1])  # the first capturing group
        print(line.strip())

# CRON JOB is used to schedule scripts on UNIX-based OS

# Short Quiz: Filtering Log Files with Regular Expressions

# We're using the same syslog, and we want to display the date, time, and process id that's inside the square brackets. We can read each line of the syslog and pass the contents to the show_time_of_pid function. Fill in the gaps to extract the date, time, and process id from the passed line, and return this format: Jul 6 14:01:23 pid:29440.


def show_time_of_pid(line):
    pattern = r"(\w+ \d+ [\d:]+).*\[(\d+)\]"
    result = re.search(pattern, line)
    return "{} pid:{}".format(result[1], result[2])


# Jul 6 14:01:23 pid:29440
print(show_time_of_pid(
    "Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)"))

# Jul 6 14:02:08 pid:29187
print(show_time_of_pid(
    "Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)"))

# Jul 6 14:02:09 pid:29187
print(show_time_of_pid(
    "Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)"))

# Jul 6 14:03:01 pid:29440
print(show_time_of_pid(
    "Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)"))

# Jul 6 14:03:40 pid:29807
print(show_time_of_pid(
    "Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\""))

# Jul 6 14:04:01 pid:29440
print(show_time_of_pid(
    "Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)"))

# Jul 6 14:05:01 pid:29440
print(show_time_of_pid(
    "Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)"))

# Here is your output:
# Jul 6 14:01:23 pid:29440
# Jul 6 14:02:08 pid:29187
# Jul 6 14:02:09 pid:29187
# Jul 6 14:03:01 pid:29440
# Jul 6 14:03:40 pid:29807
# Jul 6 14:04:01 pid:29440
# Jul 6 14:05:01 pid:29440

# You got it! You're parsing the syslog and extracting just
# the information that we need, with nothing extra!


# Making Sense out of the Data

# use dictionary to store specific log data we want

usernames = {}

name = "jinx_user"

usernames[name] = usernames.get(name, 0) + 1

print(usernames)
usernames[name] = usernames.get(name, 0) + 1
print(usernames)


logfile = sys.argv[1]  # to get the second argument in CLI
usernames = {}

with open(logfile) as f:
    for line in f:
        # Check whether "CRON" letter is in logfile
        if "CRON" not in line:
            continue

        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)

        # check whether result value is None, if it's None then Continue
        if result is None:
            continue
        name = result[1]
        # Increment The Name Value, it the key has same value
        usernames[name] = usernames.get(name, 0) + 1

print(usernames)

# Intro to Module 5: Testing in Python

# Software Testing
# -> The process of evaluating computer code to determine whether or not it does what you expect it to do

# When you test software, what are you really looking for?


# Correct Answer: Defects

# Correct
# Right on! You want to find errors and defects when testing software.

# Unit Test
# -> Used to verify that small, isolated parts of a program are correct

# An important characteristic of a unit test is ___.


# Correct Answer: Isolation.

# Correct
# Nice job! Unit tests test the piece of code they target.

# Python has a test module. It's unittest

#!/usr/bin/env python3
from rearrange import rearrange_name
import unittest
# inherit the TestCase class
class TestRearrange(unittest.TestCase):
    # ready to write first test case
    def test_basic(self):
        # we setting up our expected inputs and outputs
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)
        # assertEqual to verify what we expected is exactly what we got

unittest.main()

# Short Quiz: Writing Unit Tests in Python

# Question
# What module can you load to use a bunch of testing methods for your unit tests?


# Correct Answer: unittest


# Correct
# Nice job! This module provides a TestCase class with a bunch of testing methods.

## Edge Cases
# -> Inputs to our code that produce unexpected results, and are found at the extreme ends,
# -> of the ranges of input we imagine our programs will typically work with
# -> Edge case need special "handling" in scripts in order for the code to continue to behave correctly

# you want your program to crash most likely, rather then nothing happened/error silently

#!/usr/bin/env python3
from rearrange import rearrange_name
import unittest
# inherit the TestCase class
class TestRearrange(unittest.TestCase):
    # ready to write first test case
    def test_basic(self):
        # we setting up our expected inputs and outputs
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)
        # assertEqual to verify what we expected is exactly what we got

    # we test empty string
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
        
unittest.main()

#!/usr/bin/env python3

import re

def rearrange_name(name):
        result = re.search(r"^([\w .]*), ([\w .]*)$", name)
        # add this block to basically check whether result is None or not
        if result is None:
            return ""
        return "{} {}".format(result[2], result[1])


### Additional Test Cases
# we need to check further check of our regex, function, etc


#!/usr/bin/env python3
from rearrange import rearrange_name
import unittest
# inherit the TestCase class
class TestRearrange(unittest.TestCase):
    # ready to write first test case
    def test_basic(self):
        # we setting up our expected inputs and outputs
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)
        # assertEqual to verify what we expected is exactly what we got

    # we test empty string
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
    
    # In this case, we're testing that someone with more than one given name still gets their name properly rearranged, Let's test it! 
    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()

# 4th Cases - Check Only One Name

#!/usr/bin/env python3
from rearrange import rearrange_name
import unittest
# inherit the TestCase class
class TestRearrange(unittest.TestCase):
    # ready to write first test case
    def test_basic(self):
        # we setting up our expected inputs and outputs
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)
        # assertEqual to verify what we expected is exactly what we got

    # we test empty string
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
    
    # In this case, we're testing that someone with more than one given name still gets their name properly rearranged, Let's test it! 
    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()

# Debugging - Change return empty string value to the user name itself

#!/usr/bin/env python3

import re

def rearrange_name(name):
        result = re.search(r"^([\w .]*), ([\w .]*)$", name)
        # add this block to basically check whether result is None or not
        if result is None:
            return name
        return "{} {}".format(result[2], result[1])

##### White vs Black Box Test

## White Box Test
# -> the test is made along by development by developer that know exactly what is going in the code

## Black Box Test
# -> is based on requirement of test, mainly written before the application even coded yet


# Which of the following is descriptive of a black-box test case?


# Correct Ansswer: Code is opaque.


# The code is open-source.


# Tests are created alongside the code development.


# The tester is familiar with the code.

# Correct
# You got it! Black-box tests have no knowledge of the code.

############# TEST SUITE

### Integration Test
# -> Basically Whole Software Testing, group of unit test packed up in test environment

### Regression Test
# -> Debug the only bug line

### Smoke Test
# -> [ironically] check whether our hardware output smokes out of it (lol)

### Load Test
# -> Generate Traffic

## Short Quiz

# Running a piece of software code as-is to see if it runs describes what type of testing?


# Regression test


# Load test


# Integration test


# Correct Answer: Smoke test

# Correct
# Keep it up! This test finds out if the program can run in its basic form before undergoing more refined test cases.

### Test-Driven Development [TDD]

# -> Calls for creating the test before writing the code
# -> First Writing a test then running the development code to make sure it fails
# -> Once it fails, you write the actual code to satisfy the test run, and run the TDD again

## Short Quiz : Test-Driven Development

# Which of the following is NOT an advantage of test-driven development (TDD)?


# Correct Answer: Faster development of code


# Test cases written before writing code


# A problem is well thought out


# Test while you develop code

# Correct
# Nailed it! Testing while developing code may increase the code completion time.

### Continuous Integration [CI]
# -> When engineers submit their code, it's integrated to main repository
# -> and tests are automatically run againts it to spot bugs and error in a process

## Practice Quiz: Other Test Concepts

# Congratulations! You passed!
# Grade received 100%
# To pass 80% or higher
# 1.
# Question 1
# In what type of test is the code not transparent?

# 1 / 1 point

# Correct Answer: Black-box test


# White-box test


# Test-driven development


# Smoke test

# Correct
# Nice work! This type of test relies on the tester having no knowledge of the code.

# 2.
# Question 2
# Verifying an automation script works well with the overall system and external entities describes what type of test?

# 1 / 1 point

# Correct Answer:  Integration test


# Smoke test


# Load test


# Regression test

# Correct
# Great job! This test verifies that the different parts of the overall system interact as expected. 

# 3.
# Question 3
# _____ ensures that any success or failure of a unit test is caused by the behavior of the unit in question, and doesn't result from some external factor.

# 1 / 1 point

# Regression testing


# Integration


# Correct Answer:  Isolation


# White-box testing

# Correct
# Right on! By ensuring the unit of code we are testing is isolated, we can ensure we know where the bug originated.

# 4.
# Question 4
# A test that is written after a bug has been identified in order to ensure the bug doesn't show up again later is called _____

# 1 / 1 point

# Load test


# Black-box test


# Smoke test


# Correct Answer:  Regression test

# Correct
# Excellent! Regression testing is a type of software test used to confirm that a recent program or code change has not adversely affected existing features, by re-executing a full or partial selection test cases.

# 5.
# Question 5
# What type of software testing is used to verify the software’s ability to behave well under significantly stressed testing conditions?

# 1 / 1 point

# Correct Answer:  Load test


# Black-box test


# Smoke test


# Regression test

# Correct
# Way to go! Load testing verifies the behavior of the software remains consistent under conditions of significant load.

## To count characters frequency with try-except block

#!/usr/bin/env python3

def character_frequency(filename):
        """Counts the frequence of each character in the given file."""
        # First try to open the file
        try:
                f = open(filename)
        except OSError:
                return None

        # Now process the file
        characters = {}
        for line in f:
                for char in line:
                        characters[char] = characters.get(char, 0) + 1
        f.close()
        return characters

# Validating Username

#!/usr/bin/env python3

def validate_user(username, minlen):
        # add Assertion checking
        assert type(username) == str, "username must be as string"

        if minlen < 1:
            raise ValueError("minlen must be at least 1")
        # mininum required characters
        if len(username) < minlen:
                return False
        # is username alphanumerice?
        if not username.isalnum():
                return False
        return True


## Short Quiz: Raising Errors

# What keyword can help provide a reason an error has occurred in a function?


# raise


# Correct Ansewer assert


# return


# minlen

# Correct
# Right on! This keyword is used to produce a message when a conditional is false.

## Test the raised errors

#!/usr/bin/env python3

import unittest

from validations import validate_user

class TestValidateUser(unittest.TestCase):
        def test_valid(self):
                self.assertEqual(validate_user("validuser", 3), True)

        def test_too_short(self):
                self.assertEqual(validate_user("inv", 5), False)

        def test_invalid_characters(self):
                self.assertEqual(validate_user("invalid_user", 1),  False)

        def test_invalid_minlen(self):
                self.assertRaises(ValueError, validate_user, "user", -1)

# Run The Test
unittest.main()

## Short Quiz: Testing for Expected Errors

# When using the assertRaises method, what is passed first?


# Function name


# Conditional


# Parameters


# Correct Answer: Error

# Correct
# Way to go! The expected error is passed first.


################################################# Intro to Module 6: Bash Scripting

## bash is to simplify the complex script in  modern prog-lang
## you are using bash scripting to automate a few lines of codes

## Basic Linux Commands | other resource: https://devhints.io/bash

# echo      : is a command to used to print messages to the screen
# cat       : is a command for showing contents of files
# ls        : is a command to list contents of a directory
# chmod     : is a command to change a permission of a file
# mkdir     : is a command to make a directory
# cd        : is a command to change a directory
# pwd       : is a command to checking currect working directory
# cp        : is a command to copy a file (using a dot)
#           : -> dot is the current directory (./) like that
#           : -> dot dot is the parent directory (../)
# touch     : is a command to create a empty file
# mv        : is a command to RENAME and MOVE file
# rm        : is a command to delete file (delete all using asterisk (*))
# rmdir     : is a command to delete directory [ONLY WORKS IN EMPTY DIRECTORIES]

## Short Quiz: Basic Linux Commands

# Which of the following Linux commands will create an empty file?


# Correct Answer: touch


# pwd


# mkdir


# cd

# Correct
# Right on! The touch command will create an empty file.


###### Redirecting Streams | I/O streams with Bash

## Redirection (>)
#  -> the process of sending a stream to different destinatiion

# STDOUT [File Descriptor: 1]
## > is overwritten the file
## >> is to append the new content of the file in the end of line

# STDIN [File Descriptor: 0]
## < is to read the input

## Short Quiz: Redirecting Streams

# How do you append the output of a command to a .txt file?


# user@ubuntu:~$ ./calculator.py > result.txt


# CORRECT ANSWER: user@ubuntu:~$ ./calculator.py >> result.txt


# user@ubuntu:~$ ./calculator.py < result.txt


# user@ubuntu:~$ print("This will append")

# Correct
# Great work! A double greater than sign will append a command output to a file.

# STD_ERROR [File Descriptor: 2]
## 2> redirected of error value to error file

########## Pipes and Pipelines

## Pipes [Represented by pipe character ( | )]
#  -> connect the output of one program to the input of another in order to pass data between programs.

# qodri123@DESKTOP-V1LR167:/mnt/c/WINDOWS/system32/programming_exercise/September/BashScripting$ cat capitalize.py
#!/usr/bin/env python3

import sys

for line in sys.stdin:
        print(line.strip().capitalize())

## Short Quiz: Pipes and Pipelines

# Which of the following is the correct way of using pipes?


# user@ubuntu:~$ cat sample.txt ./process.py


# user@ubuntu:~$ cat sample.txt || ./process.py


# user@ubuntu:~$ tr ' ' '\n' | sort | cat sample.txt


# Correct Answer: user@ubuntu:~$ cat sample.txt | tr ' ' '\n' | sort

# Correct
# Woohoo! The contents of the txt file are passed on to be placed in their own line and sorted in alphabetical order on the display.


######## Signalling Processes

## Signals
#  -> Tokens delivered to running process to indicate a desired action

## [SIGINT] ^C : is to Terminating Program cleanly
## [SIGSTOP] ^Z : is to stopped program
## fg : is to continued the stopped program

## Short Quiz: Signalling Processes

# What can you type in the terminal to stop the traceroute command from running cleanly?


# Correct Answer: Ctrl-C


# SIGINT


# Ctrl-Z


# SIGSTOP

# Correct
# Right on! This sends a SIGINT signal to the program to stop processing cleanly.

# [SIGTERM] kill : signal that tell program to terminate
# ps : which list the current running process

# # Basic Linux Commands Cheat-Sheet
# This list includes a bunch of different commands that are useful to know when working with Linux. Not all of these commands are covered in the videos, so feel free to investigate them on your own.

# Managing files and directories
# cd directory: changes the current working directory to the specified one

# pwd: prints the current working directory

# ls: lists the contents of the current directory

# ls directory: lists the contents of the received directory  

# ls -l: lists the additional information for the contents of the directory  

# ls -a: lists all files, including those hidden  

# ls -la: applies both the -l and the -a flags  

# mkdir directory: creates the directory with the received name

# rmdir directory: deletes the directory with the received name (if empty)

# cp old_name new_name: copies old_name into new_name

# mv old_name new_name: moves old_name into new_name

# touch file_name: creates an empty file or updates the modified time if it exists

# chmod modifiers files: changes the permissions for the files according to the provided modifiers; we've seen +x to make the file executable

# chown user files: changes the owner of the files to the given user

# chgrp group files: changes the group of the files to the given group

# Operating with the content of files
# cat file: shows the content of the file through standard output

# wc file: counts the amount of characters, words, and lines in the given file; can also count the same values of whatever it receives via stdin

# file file: prints the type of the given file, as recognized by the operating system

# head file: shows the first 10 lines of the given file

# tail file: shows the last 10 lines of the given file

# less file: scrolls through the contents of the given file (press "q" to quit)

# sort file: sorts the lines of the file alphabetically

# cut -dseparator -ffields file: for each line in the given file, splits the line according to the given separator and prints the given fields (starting from 1)

# Additional commands
# echo "message": prints the message to standard output

# date: prints the current date

# who: prints the list of users currently logged into the computer

# man command: shows the manual page of the given command; manual pages contain a lot of information explaining how to use each command (press "q" to quit)

# uptime: shows how long the computer has been running

# free: shows the amount of unused memory on the current system  


# # Redirections, Pipes and Signals Cheat Sheet
# Managing streams
# These are the redirectors that we can use to take control of the streams of our programs

# command > file: redirects standard output, overwrites file

# command >> file: redirects standard output, appends to file

# command < file: redirects standard input from file

# command 2> file: redirects standard error to file

# command1 | command2: connects the output of command1 to the input of command2

# Operating with processes
# These are some commands that are useful to know in Linux when interacting with processes. Not all of them are explained in videos, so feel free to investigate them on your own.

# ps: lists the processes executing in the current terminal for the current user

# ps ax: lists all processes currently executing for all users  

# ps e: shows the environment for the processes listed  

# kill PID: sends the SIGTERM signal to the process identified by PID

# fg: causes a job that was stopped or in the background to return to the foreground

# bg: causes a job that was stopped to go to the background

# jobs: lists the jobs currently running or stopped

# top: shows the processes currently using the most CPU time (press "q" to quit)  

################## BASH SCRIPTING

## Short Quiz: Creating Bash Scripts

# Which command will correctly run a bash script?


# user@ubuntu:~$ #!/bin/bash


# user@ubuntu:~$ ./bash.py 


# Correct Answer: user@ubuntu:~$ ./bash_sample.sh


# user@ubuntu:~$ ./sh.bash

# Correct
# Right on! A bash script is run with the .sh file extension.


###### Using Variables and Globs

## globs
#  -> use to create a list of files 
# * and ? is a common globs

### Conditional Execution in Bash

## Short Quiz: Conditional Execution in Bash

# A conditional block in Bash that starts with 'if', ends with which of the following lines?


# Correct Answer: fi


# if


# else


# grep

# Correct
# Right on! The if conditional ends with fi (a backwards "if").

## WHILE LOOP IN BASH

#   GNU nano 4.8                                                                            random-exit.py                                                                                      #!/usr/bin/env python

import sys
import random

value = random.randint(0, 3)
print("Returning: " + str(value))
sys.exit(value)

## FOR LOOP IN BASH

## basename index.HTM .HTM
## output: index

## Short Quiz: For Loops in Bash Scripts

# Which “for” conditional line will add users Paul and Jeremy to a user variable?


# for users in Paul Jeremy


# Correct Answer: for user in Paul Jeremy


# for Paul Jeremy in user


# for Paul & Jeremy in user

# Correct
# Nice job! The elements Paul and Jeremy are added to the user variable.

### Advanced Command Interaction

# Short Quiz: Advanced Command Interaction

# When using the following command, what would each line of the output start with?

# user@ubuntu:~$ tail /var/log/syslog | cut -d' ' -f3-


# CRON[257236]:


# October


# 31


# Correct Answer: 10:18:41

# Correct
# Woohoo! The time of the log will be shown with the -f3- or field three option of the cut command.

## Choosing Between Bash and Python

## Short Quiz: Choosing Between Bash and Python

# Which of the following statements would make it better to start using Python instead of Bash?


# Operate with system commands.


# Correct Answer: Use on multi-platforms.


# Operate with system files.


# Run a single process on multiple files.

# Correct
# Right on! It is better to use Python and its standard library to use when working across multiple platforms.
