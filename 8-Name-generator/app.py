import random

print("FANTASY NAME GENERATOR")

first_name = ["Moon","Unicorn","Cat","Venus","Green","Miracle"]

last_name = ["Winds","Rain","Storm","Thunder","Fire","Sparkle"]

choice = int(input("How many names do you want?: "))


for i in range(choice):

    first = random.choice(first_name)
    Last = random.choice(first_name)

    print(f"{first}{Last}")