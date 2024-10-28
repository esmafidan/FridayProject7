# Import the random module to generate a random number for the secret number
import random

# Display a greeting message and ask the user if they want to play
print("Welcome to the Number Guessing Game!")
play_game = input("Would you like to play? (yes or no): ").strip().lower()

# Check if the user wants to play the game
if play_game == "yes":
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    
    # Initialize the guess variable
    guess = None
    
    # Start a loop that continues until the user guesses correctly
    while guess != secret_number:
        # Ask the user for their guess and convert it to an integer
        guess = int(input("Guess a number between 1 and 10: "))
        
        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You've guessed the number!")
        else:
            print("Try again!")  # Prompt to try again if the guess is incorrect
    
    # Farewell message after the correct guess
    print("Thanks for playing! Goodbye!")

# If the user says no, print a message and end the program
else:
    print("Maybe next time!")