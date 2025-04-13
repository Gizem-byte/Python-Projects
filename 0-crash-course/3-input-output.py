# name = input("Enter your name: ")
# print("Hello ", name)

# age = int(input("Enter your age: "))
# years_to_100 = 100 - age
# print(f"You will be 100 years old in {years_to_100} years.")


# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# result = num1 + num2
# print(f"The sum of {num1} and {num2} is {result}")

#working with multiple inputs on one line
# x,y = input("Enter two numbers separated by a space: ").split()
# print(f"First number: {x}, Second number: {y}")


user_choice=  input("Choose a color or press Enter for default:")

if user_choice == "":
    user_choice = "blue"
print(f"Your choice is {user_choice}")