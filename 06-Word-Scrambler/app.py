import random

print(" WORD SCRAMBLER")

while True:
    user_input = input("Enter a word to scramble (or 'quit'):")

    if user_input.lower() == 'quit':
        print("Good Bye")
        break

    letters= list(user_input)
    random.shuffle(letters) 
    print(f"Scrambled : {"".join(letters)}") 