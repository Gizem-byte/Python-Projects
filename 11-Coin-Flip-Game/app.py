import random

print("COIN FLIP GAME")
print("Guess heads or tails!")


while True:

   user_input = input("Enter your guess (heads/tails):")

   coin = ["heads","tails"]
   result = random.choice(coin)

   print(f"The coin shows: {result}")

   if user_input.lower() == result :
      print("You guessed correctly! you win!")
      user_answer = input ("Play again ? (y/n)")

      if user_answer.lower() == "y":
         continue
      else:
         print("Thank you for playing")
         break

   else:
      
      
      print("Sorry wrong guess, Try again")
      user_answer = input ("Play again ? (y/n)")

      if user_answer.lower() == "y":
         continue
      else:
         print("Thank you for playing")
         break
