teams = ["Human", "Dragon", "Slave", "Unicorn"]

for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)


#####################################################

friends = ["Rivano" , "Fauzan", "Hazlan", "Cemilik", "Gilang", "Bintang", "Mas Pram", "Najma", "Julio", "Regularity", "Singularity"]

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
    print(str(day) + " day, " + str(hours) + " hours, " + str(minutes) + " minutes, and " + str(seconds) + " seconds is same as ")
    print(str((day*24*3600)+(hours*3600)+(minutes*60)+seconds) + " seconds")

print_to_seconds(7, 5, 15, 0)

#####################################################

# calculate the area of triangle
def area_triangle(base, height):
    return int(base*height/2)

print(area_triangle(10,5))

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
    print("The area of circle, by given radius " + str(radius) + " is: " + str(area))

area_of_circle(5)

#####################################################

# refactoring area of a rectangle ( base * height )
def rectangle_area(base, height):
	area = base*height  # the area is base*height
	print("The area is " + str(area))

rectangle_area(5,6)

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

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative

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
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192

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

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail

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
print(sum(sum(1,2), sum(3,4)))

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
		
print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0

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

#Here is your output:
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
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False

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
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
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

print(sum_squares(10)) # Should be 285

values = [23, 46, 65, 20, 91, 73, 28, 54]

length = 0
sum = 0
for value in values:
    sum += value
    length += 1

print("The total sum of values is " + str(sum) + " and the average of values is " + str(sum/length))

#####################################################

# Factorial
product = 1
for n in range(1, 1000000):
    product = product * n

print(product)

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

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
    for x in range(1,n):
        result = result + result * (x-1)
    return result

for n in range(0,1):
    print(n, factorial(n+1))


#####################################################

# Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and ending with x=10.

for x in range(1,11):
  print(x**3)

# Write a script that prints the multiples of 7 between 0 and 100. Print one multiple per line and avoid printing any numbers that aren't multiples of 7. Remember that 0 is also a multiple of 7.

for x in range(0, 101):
    if x % 7 == 0:
        print(x)

def factorial(n):
    result = 1
    for x in range(1,n):
        result = result * x
    return result

for n in range(0,10):
    print(n, factorial(n+1))

#####################################################

# recursion

def factorial(n):
    if n < 2: # base case
        return 1
    return n * factorial(n-1) # recursive case

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

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False
print(is_power_of(100,10)) # Should be False
print(is_power_of(625,5)) # Should be False