import enum
import random

teams = ["Human", "Dragon", "Slave", "Unicorn"]

for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)


#####################################################

friends = ["Rivano", "Fauzan", "Hazlan", "Cemilik", "Gilang",
           "Bintang", "Mas Pram", "Najma", "Julio", "Regularity", "Singularity"]

for friend in friends:
    print("Hi " + friend)

#####################################################


for i in range(10):
    print("Hello, World!")

#####################################################

for i in range(5):
    print("This is fun!")

#####################################################

seconds_in_a_day = 86400
seconds_in_a_week = seconds_in_a_day*7
print(seconds_in_a_week)

#####################################################

base = 5
height = 3
area = (base*height)/2
print("The area of the triangle is: " + str(area))

#####################################################

bill = 47.28
tip = bill * (0.15)
total = bill + tip
share = total / 2
print("Each person needs to pay: " + str(share))

#####################################################

numerator = 10
denominator = 10
result = numerator / denominator
print(int(result))

#####################################################

word1 = "How "
word2 = "do "
word3 = "you "
word4 = "like "
word5 = "Python "
word6 = "so "
word7 = "far?"

print(word1+word2+word3+word4+word5+word6+word7)

#####################################################

# define a function


def greeting(name, department):
    print("Welcome, " + name)
    print("You are part of " + department + " department")


greeting("Hazlan Muhammad Qodri", "Software Engineering")

#####################################################

# seconds convertion calc


def print_to_seconds(day, hours, minutes, seconds):
    print(str(day) + " day, " + str(hours) + " hours, " + str(minutes) +
          " minutes, and " + str(seconds) + " seconds is same as ")
    print(str((day*24*3600)+(hours*3600)+(minutes*60)+seconds) + " seconds")


print_to_seconds(7, 5, 15, 0)

#####################################################

# calculate the area of triangle


def area_triangle(base, height):
    return int(base*height/2)


print(area_triangle(10, 5))

area_a = area_triangle(4, 6)
print("Area A: ", area_a)
area_b = area_triangle(90, 8)
print("Area B: ", area_b)
sum_area = area_a + area_b
print("The sum of areas is: ", sum_area)

#####################################################

# seconds convertion calc return value


def get_seconds(hours, minutes, seconds):
    return 3600*hours + 60*minutes + seconds


amount_a = get_seconds(2, 30, 0)
amount_b = get_seconds(0, 45, 15)
result = amount_a + amount_b
print(result)

#####################################################

# remaining seconds func


def convert_to_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


hours, minutes, remaining_seconds = convert_to_seconds(7841)
print(hours, minutes, remaining_seconds)

#####################################################

# lucky number func


def lucky_number(name):
    number = len(name) * 8
    print("Hello " + name + ". Your lucky number is: " + str(number))


lucky_number("Qodrey")

#####################################################

# month_days func


def month_days(month, days):
    print(month + " has " + str(days) + " days.")


month_days("June", 30)
month_days("July", 31)

#####################################################

# area of a circle ( 𝝅r^2 )


def area_of_circle(radius):
    𝝅 = 3.14
    area = 𝝅 * (radius ** 2)
    print("The area of circle, by given radius " +
          str(radius) + " is: " + str(area))


area_of_circle(5)

#####################################################

# refactoring area of a rectangle ( base * height )


def rectangle_area(base, height):
    area = base*height  # the area is base*height
    print("The area is " + str(area))


rectangle_area(5, 6)

#####################################################

# 1) Complete the function to return the result of the conversion


def convert_distance(miles):
    km = miles * 1.6  # approximately 1.6 km in 1 mile
    return km


my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(my_trip_km*2))

#####################################################

# This function compares two numbers and returns them
# in increasing order.


def order_numbers(number1, number2):
    if number2 > number1:
        return number1, number2
    else:
        return number2, number1


# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

#####################################################

# user feeling function checking by emoji


def express_emoji(emoji):
    if (emoji == "😃"):
        return "😃 Happy 😃"
    elif (emoji == "😒"):
        return "😒 Annoyed 😒"
    elif (emoji == "😡"):
        return "😡 Angry 😡"
    elif (emoji == "😭"):
        return "😭 Sad 😭"
    else:
        return "Flat"


def user_feeling(name, get_feeling):
    print("This user: " + name + " is feeling " + get_feeling + " today.")


get_feeling = express_emoji("😡")
user_feeling("Qodri", get_feeling)

#####################################################

# validation username < 3


def hint_username(username):
    if len(username) < 3:
        print("Invalid username, Must be at least 3 characters long")
    else:
        print("Valid username. You ready to go")


hint_username("Qodrey")

#####################################################

# the basic even or odd number function


def is_even(number):
    if number % 2 == 0:
        return True
    return False


is_even(165242342)

#####################################################

# validation username < 3 and not long than 15


def hint_username(username):
    if len(username) < 3:
        print("Invalid username, Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username, Must be at most 15 characters long")
    else:
        print("Valid username. You ready to go")


hint_username("Hazlan Muhammad Qodri")

#####################################################

# The number_group function should return "Positive" if the number received is positive, "Negative" if it's negative, and "Zero" if it's 0.


def number_group(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


print(number_group(10))  # Should be Positive
print(number_group(0))  # Should be Zero
print(number_group(-5))  # Should be Negative

#####################################################

# Question 5
# If a filesystem has a block size of 4096 bytes,
# this means that a file comprised of only one byte will
# still use 4096 bytes of storage. A file made up of 4097 bytes
# will use 4096*2=8192 bytes of storage. Knowing this,
# can you fill in the gaps in the calculate_storage function below,
# which calculates the total number of bytes needed to store a file of a given size?


def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return (full_blocks+1) * block_size
    return full_blocks * block_size


print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096))  # Should be 4096
print(calculate_storage(4097))  # Should be 8192
print(calculate_storage(6000))  # Should be 8192

#####################################################

# exam grade score test cases


def exam_grade(score):
    if score > 95:
        grade = "Top Score"
    elif score >= 60:
        grade = "Passed"
    else:
        grade = "Failed"
    return grade


print(exam_grade(65))  # Should be Pass
print(exam_grade(55))  # Should be Fail
print(exam_grade(60))  # Should be Pass
print(exam_grade(95))  # Should be Pass
print(exam_grade(100))  # Should be Top Score
print(exam_grade(0))  # Should be Fail

#####################################################

# format_name function


def format_name(first_name, last_name):
    if first_name != "" and last_name != "":
        string = "Name: " + last_name + ", " + first_name
        return string
    elif first_name == "" and last_name != "":
        string = "Name: " + last_name
        return string
    elif first_name != "" and last_name == "":
        string = "Name: " + first_name
        return string
    else:
        string = ""
        return string


print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string

#####################################################

# Function in Calling Function


def sum(x, y):
    return(x+y)


print(sum(sum(1, 2), sum(3, 4)))

#####################################################

# The fractional_part function divides the numerator by the denominator, and returns just the fractional part (a number between 0 and 1). Complete the body of the function so that it returns the right number.
# Note: Since division by 0 produces an error, if the denominator is 0, the function should return 0 instead of attempting the division.


def fractional_part(numerator, denominator):
    # Operate with numerator and denominator to
    # keep just the fractional part of the quotient
    if denominator == 0:
        return 0
    else:
        c = (numerator/denominator) % 1
        return c


print(fractional_part(5, 5))  # Should be 0
print(fractional_part(5, 4))  # Should be 0.25
print(fractional_part(5, 3))  # Should be 0.66...
print(fractional_part(5, 2))  # Should be 0.5
print(fractional_part(5, 0))  # Should be 0
print(fractional_part(0, 5))  # Should be 0

#####################################################

# while loops
x = 0
while x < 5:
    print("Not there yet, x = ", x)
    x = x + 1
print("x = ", x)

#####################################################


def count_down(start_number):
    current = start_number
    while (current > 0):
        print(current)
        current -= 1
    print("Zero!")


count_down(3)

#####################################################

# Infinite Loops and How to Break Them

while x != 0 and x % 2 == 0:
    x = x / 2

#####################################################
# The following code causes an infinite loop. Can you figure out what’s missing and how to fix it?


def print_range(start, end):
    # Loop through the numbers from start to end
    n = start
    while n <= end:
        print(n)


print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)

# possible solution:


def print_range(start, end):
    # Loop through the numbers from start to end
    n = start
    while n <= end:
        print(n)
        n += 1


print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)

# Here is your output:
# 1
# 2
# 3
# 4
# 5

# Great work! You've managed to fix the error in the code that
# was causing an infinite loop!

#####################################################

# the print_prime_factors function print all the prime factors of a number. A prime factor is a number that is prime and divides another without a remainder.

# def print_prime_factors(number):
#   # Start with two, which is the first prime
#   factor = 2
#   # Keep going until the factor is larger than the number
#   while factor <= number:
#     # Check if factor is a divisor of number
#     if number % factor == 0:
#       # If it is, print it and divide the original number
#       print(factor)
#       number = number / factor
#     else:
#       # If it's not, increment the factor by one
#       factor += 1
#   return "Done"

# print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT

#####################################################

#  is_power_of_two division and remainder program


def is_power_of_two(n):
    # Check if the number can be divided by two without a remainder
    while n % 2 == 0 and n != 0:
        n = n / 2
    # If after dividing by two the number is 1, it's a power of two
    if n == 1:
        return True
    return False


print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False

#####################################################

# Question 4
# Fill in the empty function so that it returns the sum of all the divisors of a number, without including it. A divisor is a number that divides into another without a remainder.


def sum_divisors(n):
    sum = 0
    x = 1
    # Return the sum of all divisors of n, not including n
    while n != 0 and x < n:
        if n % x == 0:
            sum = sum + x
        x += 1
    return sum


print(sum_divisors(0))
# 0
print(sum_divisors(3))  # Should sum of 1
# 1
print(sum_divisors(36))  # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102))  # Should be sum of 2+3+6+17+34+51
# 114


#####################################################

# The multiplication_table function prints the results of a number passed to it multiplied by 1 through 5. An additional requirement is that the result is not to exceed 25, which is done with the break statement. Fill in the blanks to complete the function to satisfy these conditions.

def multiplication_table(number):
    # Initialize the starting point of the multiplication table
    multiplier = 1
    # Only want to loop through 5
    while multiplier <= 5:
        result = number
        # What is the additional condition to exit out of the loop?
        result = number * multiplier
        if result > 26:
            break

        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the variable for the loop
        multiplier += 1


multiplication_table(3)
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5)
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)
# Should print: 8x1=8 8x2=16 8x3=24


#####################################################

for x in range(5):
    print(x)


# Fill in the gaps of the sum_squares function, so that it returns the sum of all the squares of numbers between 0 and x (not included). Remember that you can use the range(x) function to generate a sequence of numbers from 0 to x (not included).
def square(n):
    return n*n


def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum


print(sum_squares(10))  # Should be 285

values = [23, 46, 65, 20, 91, 73, 28, 54]

length = 0
sum = 0
for value in values:
    sum += value
    length += 1

print("The total sum of values is " + str(sum) +
      " and the average of values is " + str(sum/length))

#####################################################

# Factorial
product = 1
for n in range(1, 1000000):
    product = product * n

print(product)


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result


print(factorial(4))  # should return 24
print(factorial(5))  # should return 120

#####################################################

# Convert Fahrenheit to Celcius


def convert_to_celcius(x):
    return (x-32)*5/9


for x in range(0, 101, 10):
    print(x, convert_to_celcius(x))

print("F   C")

#####################################################

# Domino's Bracket

for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    # print newline
    print()

#####################################################


def validate_users(users):
    for user in users:
        if len(users) > 3:
            print(user + " is valid")
        else:
            print(user + " is invalid")


validate_users(["purplecat"])

#####################################################

# Fill in the blanks to make the factorial function return the factorial of n. Then, print the first 10 factorials (from 0 to 9) with the corresponding number. Remember that the factorial of a number is defined as the product of an integer and all integers before it. For example, the factorial of five (5!) is equal to 1*2*3*4*5=120. Also recall that the factorial of zero (0!) is equal to 1.


def factorial(n):
    result = 1
    for x in range(1, n):
        result = result + result * (x-1)
    return result


for n in range(0, 1):
    print(n, factorial(n+1))


#####################################################

# Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and ending with x=10.

for x in range(1, 11):
    print(x**3)

# Write a script that prints the multiples of 7 between 0 and 100. Print one multiple per line and avoid printing any numbers that aren't multiples of 7. Remember that 0 is also a multiple of 7.

for x in range(0, 101):
    if x % 7 == 0:
        print(x)


def factorial(n):
    result = 1
    for x in range(1, n):
        result = result * x
    return result


for n in range(0, 10):
    print(n, factorial(n+1))

#####################################################

# recursion


def factorial(n):
    if n < 2:  # base case
        return 1
    return n * factorial(n-1)  # recursive case

#####################################################


def is_power_of(number, base):
    # Base case: when number is smaller than base.
    if number < base:
        # If number is equal to 1, it's a power (base**0).
        if number == 1:
            return True
        return False

    # Recursive case: keep dividing number by base.
    return is_power_of(number/base, base)


print(is_power_of(8, 2))  # Should be True
print(is_power_of(64, 4))  # Should be True
print(is_power_of(70, 10))  # Should be False
print(is_power_of(100, 10))  # Should be False
print(is_power_of(625, 5))  # Should be False

#####################################################

# Module 3 Graded Assessment

# Question 1
# Fill in the blanks of this code to print out the numbers 1 through 7.
number = 1
while number <= 7:
    print(number, end=" ")
    number += 1

    # output: 1 2 3 4 5 6 7

# Question 2
# The show_letters function should print out each letter of a word on a separate line. Fill in the blanks to make that happen.


def show_letters(word):
    for x in word:
        print(x)


show_letters("Hello")
# Should print one line per letter
# output: H
# e
# l
# l
# o

# Question 3
# Complete the function digits(n) that returns how many digits the number has. For example: 25 has 2 digits and 144 has 3 digits. Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left.


def digits(n):

    count = 0

    if n == 0:  # only 0 can through this, so
        return count+1  # 0 is digit, we count them 1

    while (n >= 1):
        count += 1
        n = n / 10

    return count


print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000))  # Should print 4
print(digits(0))    # Should print 1

# Question 4
# This function prints out a multiplication table (where each number is the result of multiplying the first number of its row by the number at the top of its column). Fill in the blanks so that calling multiplication_table(1, 3) will print out:

# 1 2 3

# 2 4 6

# 3 6 9


def multiplication_table(start, stop):
    for x in range(start, stop+1):
        for y in range(start, stop+1):
            print(str(x*y), end=" ")
        print()


multiplication_table(1, 3)
# Should print the multiplication table shown above

# Question 5
# The counter function counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise. Fill in the blanks to make this work correctly.


def counter(start, stop):
    x = start
    if start > stop:
        return_string = "Counting down: "
        while x >= stop:
            return_string += str(x)
            if x != stop:
                return_string += ","
            x -= 1
    else:
        return_string = "Counting up: "
        while x <= stop:
            return_string += str(x)
            if x != stop:
                return_string += ","
            x += 1
    return return_string


print(counter(1, 10))  # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1))  # Should be "Counting down: 2,1"
print(counter(5, 5))  # Should be "Counting up: 5"

# Counting up: 1,2,3,4,5,6,7,8,9,10
# Counting down: 2,1
# Counting up: 5

# Question 6
# The even_numbers function returns a space-separated string of all positive numbers that are divisible by 2, up to and including the maximum that's passed into the function. For example, even_numbers(6) returns “2 4 6”. Fill in the blank to make this work.


def even_numbers(maximum):
    return_string = ""
    for x in range(1, maximum+1):
        if x % 2 == 0:
            return_string += str(x) + " "
    return return_string.strip()


print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10))  # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed

# 2 4 6
# 2 4 6 8 10
#
# 2
#

# Question 7
# The following code raises an error when executed. What's the reason for the error?


def decade_counter():
    while year < 50:
        year += 10
    return year
# answer: Failure to initialize variables


# Question 8
# What is the value of x at the end of the following code?
for x in range(1, 10, 3):
    print(x)

# output :
# 1
# 4
# 7

# Question 9
# What is the value of y at the end of the following code?
for x in range(10):
    for y in range(x):
        print(y)

# output: 8

# Question 10
# How does this function need to be called to print yes, no, and maybe as possible options to vote for?


def votes(params):
    for vote in params:
        print("Possible option:" + vote)

# output: votes(['yes', 'no', 'maybe'])

#####################################################

# string indexing - string start index at 0


name = "Jaylen"
print(name[0])
print(name[len(name)-1])  # how to search the last character in the strings
# or use negative indexes
print(name[-1])  # output: n


def first_and_last(message):
    if len(message) == 0:
        return True
    else:
        if message[0] == message[-1]:
            return True
        else:
            return False


print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))


# slice method

fruit = "Orange"
fruit[1:-1]  # output 'rang'

# slice one side is onward

fruit = "Pineapple"
print(fruit[:4])  # output: 'Pine'
# output: 'apple', Accessing 4 to NOTHING takes everything from index four onward.
print(fruit[4:])

# string in Python is immutable/can't be modified

# STRING METHOD

word = "supercalifragilisticexpialidocious"
print(word.index("x"))  # Should be 21

# 'in' substring in a string
pets = "Cats & Dogs"
"Dragon" in pets  # Should be False
"Cats" in pets  # Should be True

# STRING: Real World Problem - Convert old email domain to the new one


def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:  # if user still using the old domain, change them
        # index to find what index is contained by '@', so we can start slicing without @ + old_domain
        index = email.index("@" + old_domain)
        new_email = email[:index] + new_domain
        return new_email
    return email  # if use alrd using the new domain, just return the current value

# Another String Method Example:

# 1. Lower and Upper Method


answer = "YES"

if answer.lower() == "yes":
    print("User said yes")

# 2. Strip Method - To get rid of whitespaces
    # strip combination
    # .lstrip() - get rid of left whitespaces
    # .rstrip() - get rid of right whitespaces

" yes ".strip()

# 3. Count - returns how many times a given substring appears within a string

"The number of times e occurs in this string is 4".count('e')

# 3. Endswith - returns a boolean whether string have the specific requested substring

"Forest".endswith("rest")

# 4. isnumeric

"Forest".isnumeric()  # False

"12345".isnumeric()  # True

int("12345") + int("54321")  # 66666

# 5. Join - to concatinate string

" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"])

# 6. Split - returns array/list of string that splitted into indexes

"This is another example".split()  # ['This', 'is', 'another', 'example']

# Short Quiz in More String Methods


def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[:1]
    return result.upper()


print(initials("Universal Serial Bus"))  # Should be: USB
print(initials("local area network"))  # Should be: LAN
print(initials("Operating system"))  # Should be: OS


##############################################################################

# String Format

name = "Hazlan"
number = len(name) * 9 - 7 + 28
print("Hello {}!. Your lucky number is {}...".format(name, number))


# name = req.body.name
# tokenizer = auth.token.generator() #contohnya

print("Your token is {tokenizer}, {name}".format(
    name=name, tokenizer="tokenizer"))

# another example


def student_grade(name, grade):
    return "{name} received {grade}% on the exam".format(name=name, grade=grade)


print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

# Formatting expression
price = 7.5
with_tax = price * 1.09  # 9% taxes lol
print(price, with_tax)

# -> example of formatting expression
print("Base price of the is ${:.2f}. With tax: ${:.2f}".format(
    price, with_tax))


# formatted the celc to fahrenheit
def convert_to_celcius(x):
    return (x-32)*5/9


for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C ".format(x, convert_to_celcius(x)))


##########################################################################################

# List

# check type
sentence = ["Now", "we", "are", "cooking!"]
type(sentence)  # class<list>

# print list
print(sentence)

# length of the list
len(sentence)

# to check if list contains a certain elements, use 'in'
"cooking!" in sentence  # True
"cooking" in sentence  # False

# Using the "split" string method from the preceding lesson, complete the get_word function to return the {n}th word from a passed sentence. For example, get_word("This is a lesson about lists", 4) should return "lesson", which is the 4th word in this sentence. Hint: remember that list indexes start at 0, not 1.


def get_word(sentence, n):
    # Only proceed if n is positive
    if n > 0:
        words = sentence.split()
        # Only proceed if n is not more than the number of words
        if n <= len(words):
            return(words[n-1])
    return("")


print(get_word("This is a lesson about lists", 4))  # Should print: lesson
print(get_word("This is a lesson about lists", -4))  # Nothing
print(get_word("Now we are cooking!", 1))  # Should print: Now
print(get_word("Now we are cooking!", 5))  # Nothing


# LIST METHOD

# [1] Append - will add element(s) in the end of index of a list
fruits = ["Manggo", "Banana", "Apple", "Orange"]
fruits.append("Watermelon")
print(fruits)  # ["Manggo", "Banana", "Apple", "Orange", "Watermelon"]

# [2] Insert - add element based index that specified choosen
fruits.insert(1, "Kiwi")  # will add 'Kiwi' after 'Manggo'
print(fruits)
# some note: if we use an index higher than the current length of the list, the elements just gets added to the end
fruits.insert(100, "Tomato")
print(fruits)

# [3] Remove - remove element return a new list that doesn't have the removed element(s)
fruits.remove("Banana")
print(fruits)

# [4] Pop - remove element and return a index that newly removed
fruits.pop(0)  # will remove 'Manggo'
print(fruits)

# Manually change/modifying the value of element by assign a new value to the specified index
fruits[2] = "Strawberry"
print(fruits)


def skip_elements(elements):
    # Initialize variables
    new_list = []
    i = 0

    # Iterate through the list
    for word in elements:
        # Does this element belong in the resulting list?
        if elements[i] == word:
            # Add this element to the resulting list
            new_list.append(word)
            # Increment i
            i += 2

    return new_list


# Should be ['a', 'c', 'e', 'g']
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
# Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))
print(skip_elements([]))  # Should be []


# List Slice Notation '[ : : ]'
# This notation [::2] allows you to select every second element in a sequence.

# [start:stop:step] - items from start to stop-1 by step.

# If you do not specify start, stop or step, then the default values will be applied instead.

# Deeper analysis here:

#   https://stackoverflow.com/questions/509211/understanding-slice-notation

##########################################################################################################

# Tuples - same as list, but immutable (can't be changed or modified), THE ORDERS of INDEX in tuple are matters

# remaining seconds func
def convert_to_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds  # this give us tuple


result = convert_to_seconds(7841)
type(result)
print(result)

# unpack tuples
hours, minutes, remaining_seconds = convert_to_seconds(5000)
print(hours, minutes, remaining_seconds)

# return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places.  with tuple


def file_size(file_info):
    file_name, file_type, file_size = file_info
    return("{:.2f}".format(file_size / 1024))


print(file_size(('Class Assignment', 'docx', 17875)))  # Should print 17.46
print(file_size(('Notes', 'txt', 496)))  # Should print 0.48
print(file_size(('Program', 'py', 1239)))  # Should print 1.21


animals = ["Monkey", "Donkey", "Horse", "Zebra"]

chars = 0

for animal in animals:
    chars += len(animal)

print("The total characters in animal list: {}. The Average is {}".format(
    chars, chars/len(animals)))


# Enumerate Function - returns an tuple and useful for indexing a list

winners = ["Ashley", "Dylan", "Reese"]

for index, winner in enumerate(winners):
    print("{} - {}".format(index+1, winner))


# EXAMPLE: list of tuples

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result


print(full_emails([("hazlanqodri2020work@gmail.com", ["Hazlan Muhammad Qodri"]),
      ("geemde@gmail.com", ["Gilang Martadinata"])]))


# Skip elements but use enumerate function

def skip_elements(elements):
    # code goes here
    result = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            result.append(element)
    return result


# Should be ['a', 'c', 'e', 'g']
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
# Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))

# List comprehension - one line for loops iteration to add element(s) to a list

multiple = [x*7 for x in range(1, 11)]
print(multiple)

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]

len_language = [len(language) for language in languages]

# If conditional in List Comprehension
# let's say we want to know all number between 0 and 100 that can divide by 3

z = [i for i in range(0, 1001) if i % 3 == 0]
print(z)


def odd_numbers(n):
    return [x for x in range(0, n+1) if x % 2 != 0]


print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10))  # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11))  # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1))  # Should print []

# Practice Quiz: List and Tuple

# Question 1

filenames = ["program.c", "stdio.hpp",
             "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.

newfilenames = []
get_new_name = ""
for index, i in enumerate(filenames):
    if i.endswith('.hpp'):
        get_new_name = i[:-2]
        filenames[index] = get_new_name

newfilenames = filenames

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

# Question 2


def pig_latin(text):
    say = ""
    # Separate the text into words
    new_text = []
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        say = word[1:] + word[:1] + "ay"
        new_text.append(say)
        # Turn the list back into a phrase
    return " ".join(new_text)


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
# Should be "rogrammingpay niay ythonpay siay unfay"
print(pig_latin("programming in python is fun"))

# Question 3


def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]
    # Iterate over each of the digits in octal
    for i in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if i >= value:
                result += letter
                i -= value
            else:
                result += "-"
    return result


print(octal_to_string(755))  # Should be rwxr-xr-x
print(octal_to_string(644))  # Should be rw-r--r--
print(octal_to_string(750))  # Should be rwxr-x---
print(octal_to_string(600))  # Should be rw-------

# Question 5


def group_list(group, users):
    members = "{group}: {users}".format(group=group, users=", ".join(users))
    return members


# Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))
# Should be "Engineering: Kim, Jay, Tom"
print(group_list("Engineering", ["Kim", "Jay", "Tom"]))
print(group_list("Users", ""))  # Should be "Users:"

# Question 6


def guest_list(guests):
    for guest in guests:
        name, age, profession = guest
        print("{} is {} years old and works as {}".format(name, age, profession))


guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'),
           ('Amanda', 25, "Engineer")])

# Click Run to submit code
# """
# Output should match:
# Ken is 30 years old and works as Chef
# Pat is 35 years old and works as Lawyer
# Amanda is 25 years old and works as Engineer
# """

################################################################################################

# Dictionaries [Dict]

x = {}
type(x)  # <class 'dict'>

file_counts = {
    "jpg": 10,
    "txt": 14,
    "csv": 2,
    "py": 23
}

print(file_counts)

file_counts["txt"]  # 14

"jpg" in file_counts  # True

"html" in file_counts  # False

# add new key-value pair in dict

file_counts["cfg"] = 8
print(file_counts)  # add the newly added k-v to dict in the end of dict

# modified the value of existing key in dict
file_counts["csv"] = 17
print(file_counts)

# delete key in dict
del file_counts["cfg"]
print(file_counts)

# Short Quiz

toc = {"Introduction": 1, "Chapter 1": 4,
       "Chapter 2": 11, "Chapter 3": 25, "Chapter 4": 30}
toc["Epilogue"] = 39  # Epilogue starts on page 39
toc["Chapter 3"] = 24  # Chapter 3 now starts on page 24
print(toc)  # What are the current contents of the dictionary?
print("Chapter 5" in toc)  # Is there a Chapter 5?

# https://stackoverflow.com/questions/20987485/what-are-the-differences-between-python-dictionaries-vs-javascript-objects

# Iterating to Dict

file_counts = {
    "jpg": 12,
    "txt": 2,
    "csv": 14,
    "py": 23
}

for extension in file_counts:
    print(extension)

# Iterating to Dict Value

for ext, amount in file_counts.items():  # items to get key-value pair
    print("There are {} files with the .{} extension".format(amount, ext))

# Dict base method [key/value]

file_counts.keys()  # return an array of key in file_counts

file_counts.values()  # return an array of values in file_counts

cool_beasts = {"octopuses": "tentacles", "dolphins": "fins", "rhinos": "horns"}
for beast, anatomy in cool_beasts.items():
    print("{} have {}".format(beast, anatomy))


def count_letter(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result


count_letter("aaaaaa")
count_letter("Hazlan Muhammad Qodri")

wardrobe = {
    "shirt": [
        "red",
        "blue",
        "white"
    ],
    "jeans": [
        "blue",
        "black"
    ]
}

for clothing, colors in wardrobe.items():
    for color in colors:
        print("{} {}".format(color, clothing))

print(file_counts)
{'jpg': 12, 'txt': 2, 'csv': 14, 'py': 23}
file_counts.get("jpg")
12
file_counts.get("py")
23
file_counts.values()
# dict_values([12, 2, 14, 23])
file_counts.keys()
# dict_keys(['jpg', 'txt', 'csv', 'py'])
file_counts.update(file_returning)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'file_returning' is not defined
file_returning = {}
file_counts.update(file_returning)
print(file_returning)
{}
file_returning.update(file_counts)
print(file_returning)
{'jpg': 12, 'txt': 2, 'csv': 14, 'py': 23}
file_returning.clear()
print(file_returning)
{}


def email_list(domains):
    emails = []
    for email, users in domains.items():
        for user in users:
            emails.append("{}@{}".format(user, email))
    return(emails)


print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": [
      "barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary
			user_groups[user] = user_groups.get(user, []) + [group]
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for items, price in basket.items():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += price
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44

# Module 4 Graded Assessment

# Q1

def format_address(address_string):
  # Declare variables
  number_address = ""
  # Separate the address string into parts
  split_string = address_string.split()
  # Traverse through the address parts
  for i in split_string:
    # Determine if the address part is the
    # house number or part of the street name
    if i.isnumeric():
      number_address += i
  # Does anything else need to be done 
  # before returning the result?
  street_address = " ".join(split_string[1:])
  # Return the formatted string  
  return "house number {} on street named {}".format(number_address, street_address)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

# Q2

def highlight_word(sentence, word):
	return(" ".join([x.replace(word, word.upper()) for x in sentence.split()]))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

# Q3

def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  Drews_list.extend(Jamies_list[::-1])
  return Drews_list
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

# Q4

def squares(start, end):
	return [ x*x for x in range(start,end+1) ]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Q5

def car_listing(car_prices):
  result = ""
  for car_model, car_price in car_prices.items():
    result += "{} costs {} dollars".format(car_model, car_price) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# Q6

def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
  guests2.update(guests1)
  return guests2

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

# Q7

def count_letters(text):
  result = {}
  # Go through each letter in the text
  for letter in text:
    letter = letter.lower()
    # Check if the letter needs to be counted or not
    if (letter not in result):
      result[letter] = 0
      if not letter.isalpha():
        del result[letter]
        continue
    # Add or increment the value in the dictionary
    result[letter] += 1
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}