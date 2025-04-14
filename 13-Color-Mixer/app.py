print("COLOR MIXER")

color_mixer = {
    
    ("red", "blue"): "purple",
    ("red", "yellow"): "orange",
    ("blue", "yellow"): "green",
    ("purple", "red"): "magenta",
    ("purple", "blue"): "violet",
    ("orange", "red"): "vermilion",
    ("orange", "yellow"): "amber",
    ("green", "blue"): "teal",
    ("green", "yellow"): "lime", 
    ("red", "white"): "pink",
    ("blue", "white"): "light blue",
    ("black", "white"): "gray",
    ("red", "green"): "brown",
    ("blue", "orange"): "slate",  
}

while True:
    

    first_color = input("Enter your first color: ")
    second_color = input("Enter your second color: ")

    mix = None

    if (first_color,second_color) in color_mixer:
         mix = color_mixer[(first_color,second_color)]

        
    if mix:
         print(f"When you mix {first_color} and { second_color}, you get {mix}")
    else:
         print("I dont know what those colors make when mixed")

    if not input("mix more colors? (y/n):").lower().startswith("y"):
         print("Good Bye")
         break

    

 