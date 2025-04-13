# for loop
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)


# Reversed loop
for i in range(5, 0, -1):
    print(i)


# while loop
coun = 1
while count <= 1:
    print(count)
    count += 1


#reversed while loop
count = 5
while count >= 1:
    print(count)
    count -= 1

#Looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#reversing a list
fruits = ["apple", "banana", "cherry"]
for fruit in reversed(fruits):
    print(fruit)

#Loop with enumerate
for index,fruit in enumerate(fruits):
    # index is the index of the item in the list  
    print(f"{index}: {fruit}")


#lOOP with dictionaries
person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

#list comprehension 
squares = [x**2 for x in range(1,6)]
print(squares)

#list comprehension with condition
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)

#For loop with zip()
meyve = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "pink"]
for fruit,color in zip(meyve, colors):
    print(f"{fruit} is {color}.")
#Output:

#break and contunie
for i in range(1, 11):
    if i == 5:
        break
    print(i)

for i in range(1, 11):
    if i == 5:
        continue
    print(i)