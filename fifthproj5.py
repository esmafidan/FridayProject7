# Define functions to format text in different colors

def redText(text):
    # ANSI code for red text
    return f"\033[31m{text}\033[0m"

def blueText(text):
    # ANSI code for blue text
    return f"\033[34m{text}\033[0m"

def greenText(text):
    # ANSI code for green text
    return f"\033[32m{text}\033[0m"

def yellowText(text):
    # ANSI code for yellow text
    return f"\033[33m{text}\033[0m"

def brownText(text):
    # ANSI code for brown text (often represented by ANSI as yellow)
    return f"\033[33m{text}\033[0m"

# Main Program Logic
print("Here are some examples of colored text:")
print(redText("This is red text."))
print(blueText("This is blue text."))
print(greenText("This is green text."))
print(yellowText("This is yellow text."))
print(brownText("This is brown text (or similar color)."))

# Prompt the user to choose a color and input a string of text
color_choice = input("\nChoose a color (red, blue, green, yellow, brown): ").strip().lower()
user_text = input("Enter the text you'd like to display in that color: ").strip()

# Display the user's text in the chosen color
if color_choice == "red":
    print(redText(user_text))
elif color_choice == "blue":
    print(blueText(user_text))
elif color_choice == "green":
    print(greenText(user_text))
elif color_choice == "yellow":
    print(yellowText(user_text))
elif color_choice == "brown":
    print(brownText(user_text))
else:
    print("Invalid color choice.")