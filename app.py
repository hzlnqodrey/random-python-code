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
psutil.cpu_percent(1)
psutil.cpu_percent(1)
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