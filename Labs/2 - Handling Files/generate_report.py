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

def process_data(employee_list):
    department_list = []

    for employee_data in employee_list:
        department_list.append(employee_data["department"])

# The department_list should now have a redundant list of all the department names. We now have to remove the redundancy and return a dictionary. We will return this dicationary in the format department:amount, where amount is the number of employees in that particular department.

    department_data = {}

    # This uses the set() method, which converts iterable elements to distinct elements.
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)

dictionary = process_data(employee_list)
print(dictionary)