import random

print("MUSIC RECOMMENDER")

genres = { "rock":["AC/DC","Queen"],"pop":["Tylor swift","Britney Spears"],"hip-pop":["Drake","J.Cole"]}

choice = input("What genre do you like ? (rock/pop/hipi-hop):")

if choice not in genres:
    print("Sorry i dont know this genre")

else:
    print(f"Check out {random.choice(genres[choice])}")