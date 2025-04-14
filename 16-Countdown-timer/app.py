import time
print("COUNTDOWN TIMER")

while True:

    user_input = int(input("Enter seconds to countdown from:"))

    if user_input <= 0:
        print("Please enter a positive number")
        continue

    print(f"Starting countdown from {user_input} seconds!")

    for i in range(user_input, 0, -1):
        print(f"{i} seconds remaining...")
        time.sleep(1)

    print("COUNTDOWN COMPLETED")

    user_choice = input("Start another countdown?(y/n):")

    if not user_choice.lower().startswith("y"):
        print("Thanks for using countdown timer")
        break
