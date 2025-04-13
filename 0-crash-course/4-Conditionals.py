temp =  28
if temp > 30:
    print("It's a hot day.")
elif temp < 10:
    print("It's a cold day.")
else:
    print("It's a nice day.")




#Cheking multiple conditions with logical operators
age =  25
has_license =  True

if age >= 18 and has_license:
    print("You can drive.") 
elif age >= 18 and not has_license:
    print("You need to get a license.")
else:
    print("You are not old enough to drive.")



#Nested conditionals
score = 85

if score >= 60:
    print("You passed!")
    if score >= 90:
        print("You got an A!")
    elif score >= 80:
        print("You got a B!")   
    elif score >= 70:
        print("You got a C!")
    else:
        print("You got a D!")
else:
    print("You failed.")



#using in operator with conditionals
fruit = "apple"
if fruit in ["apple", "banana", "orange"]:
    print(f"{fruit} is in the list.")


#comparing strings
password = "secret123"

if password == "secret123":
    print("Access granted.")
else:
    print("Access denied.")

#Chaining comparisons
x = 15
if 10<x<20:
    print("x is between 10 and 20.")

