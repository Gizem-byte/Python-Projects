import random

random_number = random.randint(1, 100) # generate a random number between 1 and 100, 1 and 100 included
print(f"Random number: {random_number}") # print the random number

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
random_fruit = random.choice(fruits) # choose a random fruit from the list
print(f"Random fruit: {random_fruit}") # print the random fruit


random_float = random.random() # generate a random float between 0 and 1
print(f"Random float: {random_float}") # print the random float


random.shuffle(fruits) # shuffle the list of fruits
print(f"Shuffled fruits: {fruits}") # print the shuffled list of fruits


import math 

print(math.pi) # 3.141592653589793 # print the value of pi
print(math.sqrt(16)) # 4.0 # print the square root of 16
print(math.factorial(5)) # 120 # print the factorial of 5
print(math.pow(2, 3)) # 8.0 # print 2 raised to the power of 3
print(math.sin(math.pi/2)) # 1.0 # print the sine of pi/2
print(math.cos(math.pi)) # -1.0 # print the cosine of pi
print(math.tan(math.pi/4)) # 1.0 # print the tangent of pi/4
print(math.log(100)) # 4.605170185988092 # print the natural logarithm of 100
print(math.floor(4.7)) # 4 # print the floor of 4.7
print(math.ceil(4.7)) # 5 # print the ceiling of 4.7
print(math.degrees(math.pi)) # 180.0 # print pi in degrees
print(math.radians(180)) # 3.141592653589793 # print 180 degrees in radians
print(math.isqrt(16)) # 4 # print the integer square root of 16
print(math.gcd(12, 15)) # 3 # print the greatest common divisor of 12 and 15
print(math.lcm(12, 15)) # 60 # print the least common multiple of 12 and 15
print(math.dist((1, 2), (4, 6))) # 5.0 # print the distance between two points in 2D space
print(math.hypot(3, 4)) # 5.0 # print the hypotenuse of a right triangle with sides 3 and 4
print(math.comb(5, 2)) # 10 # print the number of combinations of 5 items taken 2 at a time
print(math.perm(5, 2)) # 20 # print the number of permutations of 5 items taken 2 at a time
print(math.prod([1, 2, 3, 4])) # 24 # print the product of a list of numbers
print(math.isclose(0.1 + 0.2, 0.3)) # True # check if two floating-point numbers are close to each other
print(math.trunc(4.7)) # 4 # truncate a floating-point number to an integer
print(math.remainder(5, 2)) # 1.0 # print the remainder of 5 divided by 2
print(math.copysign(3, -1)) # -3.0 # print the absolute value of 3 with the sign of -1


#Datetime module
import datetime

current_time = datetime.datetime.now() # get the current date and time
print(f"Current date and time: {current_time}") # print the current date and time

current_date = datetime.date.today() # get the current date
print(f"Current date: {current_date}") # print the current date

current_time = datetime.time(12, 34, 56) # create a time object
print(f"Current time: {current_time}") # print the time object

import os

current_directory = os.getcwd() # get the current working directory
print(f"Current directory: {current_directory}") # print the current working directory
print(f"List of files in the current directory: {os.listdir(current_directory)}") # print the list of files in the current directory
print(f"Check if a file exists: {os.path.exists('test.txt')}") # check if a file exists

