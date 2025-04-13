try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Execution completed.This piece always works.")
