import random

words = ["python","coding","game","computer","fun","learn"]


while True:

    original_words = random.choice(words)

    letters = list(original_words)
    random.shuffle(letters)
    scrambled = "".join(letters)

    print(f"\nScrambled word: {scrambled}")


    guess = input("What is the word ? ").lower()

    if guess == original_words:
        print("Congrats")

    else:
        print("Sorry you lost")

    again = input("Play again ? (y/n)").lower()
    if not again.startswith("y"):
        print("Good bye")
        break

