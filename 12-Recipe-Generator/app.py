import random

print("RANDOM RECIPE GENERATOR")


while True:


  recipe = {

        "flavor": ["spicy", "tangy", "sweet", "savory", "herby", "smoky", "umami", "citrusy"],
        "method": ["grilled", "roasted", "stir-fried", "braised", "steamed", "baked", "fried", "raw"],
        "protein": ["chicken", "tofu", "shrimp", "salmon", "beef", "lentils", "eggs", "pork"],
        "veggie": ["bell peppers", "broccoli", "spinach", "zucchini", "mushrooms", "carrots", "kale", "eggplant"],
        "carb": ["rice", "quinoa", "pasta", "potatoes", "couscous", "bread", "noodles", "farro"]
    }

  random_recipe = (
       
    f"{random.choice(recipe['flavor'])} "
    f"{random.choice(recipe['method'])} "
    f"{random.choice(recipe['protein'])} with "
    f"{random.choice(recipe['veggie'])} and "
    f"{random.choice(recipe['carb'])}."
)

  print(f"Your random recipe is {random_recipe}")

  user_input = input("Generate another recipe?(y/n):")

  if user_input.lower() == "y":
        
        print(f"Your random recipe is {random_recipe}")
        continue
  else:
        print("Have a good day ")
        break
