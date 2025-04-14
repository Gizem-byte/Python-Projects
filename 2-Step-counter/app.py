print("🏃🏽 STEP COUNTER 🏃🏽")

print("What is your daily step goal? ❓ ")
daily_step_goal = int(input("Enter your daily step goal: "))

print("How many steps did you take today? ❓ ")
steps_today = int(input("Enter the number of steps you took today: "))

required_steps = daily_step_goal - steps_today

if required_steps > 0:
    print(f"You need {required_steps} more steps to reach your goal!")
elif required_steps < 0:
    print(f"You have exceeded your goal by {abs(required_steps)} steps!")
