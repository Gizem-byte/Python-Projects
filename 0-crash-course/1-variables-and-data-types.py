print("Hello world")

#String
name = "Gizem"

#integers (Whole numbers)
age = 25

#float (Decimal numbers)
height = 1.70

#boolean (True or False)
is_student = True

print("Hello my name is " + name)
print("Hello my names is ", name)
print(f"Hello my name is {name}")


message = "heLLo world"
print(message.upper())
print(message.lower())
print(message.capitalize())
print(message.replace("L","l"))

#Python is case sensitive so world and World are different
print("World" in message) #false
print("world" in message) #true

greeting1 = "Hello"
greeting2 = "hello"

if greeting1 == greeting2:
    print("The same")
else:
    print("Different")

#Type conversion
age_str = "33" #string
age_num = int(age_str) #convert to integer  

print(age_str, type(age_str))
print(age_num, type(age_num))
