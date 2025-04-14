print("CHARACTER TYPE CHECKER: ")

user_input = input("Enter a single character: ")

if user_input.isalpha():
    print("This is a letter")

elif user_input.isdigit():
    print("This is a number.")

else:
    print("This is a special character")