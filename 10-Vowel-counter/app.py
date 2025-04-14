print("VOWEL COUNTER")

#Simple syntax
# while True:

#     user_input = input("\nEnter some text (or 'quit'):")

#     if user_input.lower() == "quit":
#         print("Good Bye")
#         break

#     vowels = ["a","e","i","o","u"]
#     vowels_count = 0

    
#     for vowel in user_input.lower():
#         if vowel in vowels:
#             vowels_count += 1

#     print(f"That text has {vowels_count}vowels")


#Advanced syntax

while True:

     user_input = input("\nEnter some text (or 'quit'):")

     if user_input.lower() == "quit":
         print("Good Bye")
         break
     
     vowels = sum (1 for char in user_input.lower() if char in "aeiou")
     print(f"That text has {vowels} vowels")