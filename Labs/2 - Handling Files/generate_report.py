#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
  keys = ["Full Name", "Username", "Departement"]
  with open(csv_file_location) as filename:
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(filename, fieldnames=keys, dialect='empDialect')

    employee_list = []

    for data in employee_file:
        employee_list.append(data)
    
  return employee_list

employee_list = read_employees('/home/student-04-2675d58b4395/user/data/employees.csv')
print(employee_list)