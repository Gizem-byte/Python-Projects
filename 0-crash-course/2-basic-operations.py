# Basic Operations in Python
# Arithmetic Operations
x = 10
y = 5

print("Addition:", x + y)        # Addition
print("Subtraction:", x - y)     # Subtraction
print("Multiplication:", x * y)  # Multiplication
print("Division:", x / y)        # Division
print("Floor Division:", x // y)  # Floor Division
print("Modulus:", x % y)        # Modulus
print("Exponentiation:", x ** y)  # Exponentiation
print("Exponentiation:", x ** 2)  # Exponentiation
print("Exponentiation:", x ** 3)  # Exponentiation


x = x + 15
x += 15
print(x)

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)
# Concatenation of string
print(f"Hello my name is {first_name} and my last name is {last_name}")


i, j, k = 1, 2, 3
print(i, j, k)  # Multiple assignment

# swap values
m = 10
n = 20
m, n = n, m
print(m, n)  # 20 10

# comparison operators
a = 5
b = 10
print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to


# Logical operators
a = True
b = False
print(a and b)  # Logical AND 
print(a or b)   # Logical OR
print(not a)    # Logical NOT


#string slicing

text = "Python programming"

print(text[0:6])  # Python
print(text[7:])   # programming
print(text[::-1])   #reverse string


#string formatting with .format()
name = "Alice"
age = 30
msg = "Hello, my name is {} and I am {} years old.".format(name, age)
print(msg)

#using placeholders
msg2="Hello, my name is {0}} and I am {1} years old." .format{name, age}
print(msg2)

#math module operations
import math
print(math.sqrt(16))  # Square root
print(math.pow(2, 3))  # Power
print(math.pi)  # Pi constant
print(math.e)  # Euler's number
print(math.factorial(5))  # Factorial
print(math.floor(3.7))  # Floor value
print(math.ceil(3.7))  # Ceiling value
print(math.sin(math.pi/2))  # Sine value
