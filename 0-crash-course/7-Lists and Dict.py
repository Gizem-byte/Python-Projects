# numbers = [1, 2, 3, 4, 5]
# things = [9, 2, 3, 4, 5,"hello",True,3.14]

# print(numbers[0]) # 1
# print(things[0]) # 9
# print(things[1]) # 2

# numbers [1] = 10 # change the second element to 10
# print(numbers[1]) # 10

# numbers.append(55) # add 55 to the end of the list
# print(numbers) # [1, 10, 3, 4, 5, 55]

# numbers.remove(10) # remove 10 from the list
# print(numbers) # [1, 3, 4, 5, 55]

# print(len(numbers)) # 5
# print(len(things)) # 8


#Slicing Lists
numbers = [1, 2, 3, 4, 5,6,7,8,9,10,5,5]
print(numbers[0:3]) # [1, 2, 3] # first three elements
print(numbers[3:]) # [4, 5, 6, 7, 8, 9, 10] # from the fourth element to the end
print(numbers[:3]) # [1, 2, 3] # first three elements
print(numbers[3:6]) # [4, 5, 6] # next three elements
print(numbers[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] # reverse the list
print(numbers + [11, 12, 13]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] # concatenate two lists together
print(numbers * 2) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # repeat the list twice
print(numbers.index(5)) # 4 # index of the first occurrence of 5



#Dictionaries
# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.
# Dictionaries are mutable, meaning you can change their contents after creation.
# They are unordered, meaning the order of the key-value pairs is not guaranteed.
# You can access the values in a dictionary using their keys.
# You can also add, remove, and modify key-value pairs in a dictionary.
# Dictionaries are defined using curly braces {} and key-value pairs separated by colons.
# You can also use the dict() constructor to create a dictionary.

student = { "name": "Alice", "age": 20, "major": ["Computer Science", "Mathematics"] }
print(student["name"]) # Alice
print(student["age"]) # 20
print(student["major"]) # ['Computer Science', 'Mathematics']
print(student["name"],student["age"]) # Alice 20

student["grade"] = "A" # add a new key-value pair
student["age"] = 21 # modify an existing key-value pair
print(student) # {'name': 'Alice', 'age': 21, 'major': ['Computer Science', 'Mathematics'], 'grade': 'A'}
print(student.keys()) # dict_keys(['name', 'age', 'major', 'grade'])
print(student.values()) # dict_values(['Alice', 21, ['Computer Science', 'Mathematics'], 'A'])  
print(student.items()) # dict_items([('name', 'Alice'), ('age', 21), ('major', ['Computer Science', 'Mathematics']), ('grade', 'A')])
print(len(student)) # 4 # number of key-value pairs in the dictionary

for key,value in student.items():
    print(f"{key}: {value}") # name: Alice, age: 21, major: ['Computer Science', 'Mathematics'], grade: A       




