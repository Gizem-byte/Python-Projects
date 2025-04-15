print("REVERSE NAME GENERATOR")


while True:
    user_name = input("Enter a name:")

    reversed_name =user_name[::-1]

    print(f"Your reversed name is {reversed_name}")
    print(f"In a parallel universe, they call you {reversed_name.capitalize()}")

    user_choice = input("Try another name ? (y/n)")

    if user_choice.lower() =="y":
        continue
    else:
        break

