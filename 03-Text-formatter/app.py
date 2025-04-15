print(" 🔈TEXT FORMATTER 🔈")

user_text = input("Enter some text :")

print("Here are some options to format your text:")
print("1. Uppercase")
print("2. Lowercase")
print("3. Titlecase")
print("4. Capitalize")


user_format = int(input("Choose a format (1-4):"))

if user_format == 1:
    formatted_text = user_text.upper()
elif user_format == 2:
    formatted_text = user_text.lower()
elif user_format == 3:
    formatted_text = user_text.title()
elif user_format == 4:
    formatted_text = user_text.capitalize()

print("Formatted text:")
print(formatted_text)






