# Import the random module to use the randint function for generating random numbers
import random

# Display a greeting message to the user
print("Welcome to the PowerBall Number Generator!")

# Generate five random numbers between 1 and 69 for the white balls
white_ball1 = random.randint(1, 69)
white_ball2 = random.randint(1, 69)
white_ball3 = random.randint(1, 69)
white_ball4 = random.randint(1, 69)
white_ball5 = random.randint(1, 69)

# Generate a random number between 1 and 26 for the red PowerBall
power_ball = random.randint(1, 26)

# Format the output with spaces between the numbers
# First five numbers have one space between them, followed by three spaces before the PowerBall number
print(f"Your PowerBall numbers are: {white_ball1} {white_ball2} {white_ball3} {white_ball4} {white_ball5}   {power_ball}")

# Display a farewell message to the user
print("Good luck! Thanks for using the PowerBall Number Generator.")