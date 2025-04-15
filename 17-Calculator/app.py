
def addition(x,y):
  return x+y

def substract(x,y):
  return x-y

def multiply(x,y):
  return x*y

def divide(x,y):
  if y == 0:
    return "Error divison by sero is not allowed"
  return x/y


def main():

    print("SIMPLE CALCULATOR")

    print("Select operation:")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4-Division")
  


    while True:


     choice = input("\nEnter your choice(1-4): ")

     if choice not in ["1","2","3","4"]:
        print("Invalid input,Please enter number between 1 and 4")
     else:
        break
     


    try:
       
       num1= float(input("\nEnter your first number: "))
       num2 = float(input("\nEnter your second number: "))

    except ValueError:

        print("Error,please enter a valid number")

        return
     
    if choice == "1":
       print(f"{num1} + {num2} = {addition(num1,num2)}")

    elif choice == "2":
       print(f"{num1} - {num2} = {substract(num1,num2)}")
 
    elif choice == "3":
        print(f"{num1} * {num2} = {multiply(num1,num2)}")

    elif choice == "4":
        print(f"{num1} / {num2} = {divide(num1,num2)}")


    again = input("Do you want to perform antother calculation ? ( y/n): ").lower()

    if not again.startswith("y"):
        print("Good bye")
        return
    else:
       main()

main()
       




 
   
