# Define a dictionary with trivia questions as keys and their correct answers as values
questions_and_answers = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our Solar System?": "Jupiter",
    "What is the chemical symbol for water?": "H2O",
    "Who wrote 'Romeo and Juliet'?": "Shakespeare",
    "How many continents are there on Earth?": "7"
}

# Display a greeting message
print("Welcome to the Trivia Study Program!")

# Loop through each question and answer in the dictionary
for question, correct_answer in questions_and_answers.items():
    # Display the question to the user
    print("\n" + question)
    
    # Prompt the user to input their answer
    user_answer = input("Your answer: ").strip()

    # Check if the user's answer matches the correct answer (case-insensitive)
    if user_answer.lower() == correct_answer.lower():
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")

# Display a farewell message after all questions are answered
print("\nThanks for studying with us! Good luck!")