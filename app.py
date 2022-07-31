teams = ["Human", "Dragon", "Slave", "Unicorn", "Orc", "Magician", "Fruit Slayer"]

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

