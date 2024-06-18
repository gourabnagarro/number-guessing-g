import random
import json
from datetime import date

# Create a class for the Number Guessing Game
# The class should have the following functions and properties:
# 1. A constructor (__init__) with the following properties:
#    - lower_limit initialized to 1
#    - upper_limit initialized to 100
#    - random_number
#    - attempts as an empty array
#    - scores as empty array
class NumberGuessingGame:
    def __init__(self):
        self.lower_limit = 1
        self.upper_limit = 100
        self.random_number = self.generate_random_number()
        self.attempts = []
        self.scores = []

    # Create a function to generate a random number between a range of numbers
    # The range should be dynamic; the user can provide the range
    # If the user does not provide the range, the default range should be 1 to 100
    def generate_random_number(self):
        return random.randint(self.lower_limit, self.upper_limit)

    # Create a function to provide hints to the user after crossing half of the attempts of the range
    # Hints should be like "You are halfway there" or "You are close"
    # Print a range of numbers where the number lies (plus or minus 2) if the attempt is equal to half way 
    # Print a range of numbers where the number lies (plus or minus 1) if the attempt is more than half way and user is close to the number 
    def provide_hint(self):
        total_range = self.upper_limit - self.lower_limit + 1
        halfway = total_range // 2
        if len(self.attempts) == halfway:
            print("You are halfway there.")
            print(f"The number lies between {self.random_number - 2} and {self.random_number}.")
        elif len(self.attempts) > halfway and len(self.attempts) < total_range:
            print("You are close.")
            print(f"The number lies between {self.random_number - 1} and {self.random_number}.")

    # Prompt the user to guess the number
    # Ensure that the user input is a valid numeric input
    # Store the user input in a variable
    def prompt_user_for_guess(self):
        while True:
            try:
                user_guess = int(input("Guess the number: "))
                return user_guess
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Provide feedback for each guess, indicating if the guess is too high, too low, or correct
    # If the guess is too high, return "Too high. Try again."
    # If the guess is too low, return "Too low. Try again."
    # If the guess is correct, return "Correct"
    def provide_feedback_for_guess(self, user_guess):
        if user_guess > self.random_number:
            return "Too high. Try again."
        elif user_guess < self.random_number:
            return "Too low. Try again."
        else:
            return "Correct"

    # Create a function to implement a scoring system based on the number of attempts
    # The score should be a percentage, with more attempts reducing the score
    # The score should not be negative
    # If there is a single attempt, the score should be 100%
    def calculate_score(self):
        total_range = self.upper_limit - self.lower_limit + 1
        total_attempts = len(self.attempts)
        score = int(100 - ((total_attempts - 1) * 100 / total_range))
        return max(score, 0)


    # Play game will initialize the number guessing game and show a welcome message
    # It will ask the user to guess the range of numbers or continue with the default range of 1 to 100
    # It will call generate_random_number to generate a new number
    # It will call prompt_user_for_guess to prompt the user for a guess
    # Validate that the upper limit is greater than the lower limit; otherwise, show an error message and restart the game
    # It will call provide_feedback_for_guess to provide feedback for each guess
    # The game should track all attempts made by the user and store them in a list
    # Integrate the scoring system and show the score to the user once they guess the number
    # Prompt the user to play again or exit the game
    # Integrate provide_hint to provide a hint after crossing half of the attempts of the range
    # Store all score in the scores list and before exiting save the higest score in a json file
    def play_game(self):
        print("Welcome to the Number Guessing Game!")
        while True:
            while True:
                try:
                    self.lower_limit = int(input("Enter the lower limit of the number range: "))
                    self.upper_limit = int(input("Enter the upper limit of the number range: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            if self.upper_limit <= self.lower_limit:
                print("Upper limit should be greater than lower limit. Please try again.")
                continue
            self.random_number = self.generate_random_number()
            self.attempts = []
            while True:
                user_guess = self.prompt_user_for_guess()
                if user_guess > self.upper_limit or user_guess < self.lower_limit:
                    print(f"Please enter a number within the range of {self.lower_limit} and {self.upper_limit}.")
                    continue
                self.attempts.append(user_guess)
                feedback = self.provide_feedback_for_guess(user_guess)
                print(f"Feedback: {feedback}")
                if user_guess == self.random_number:
                    score = self.calculate_score()
                    self.scores.append(score)
                    print(f"Congratulations! You guessed the number in {len(self.attempts)} attempts.")
                    print(f"Your score is: {score}%")
                    play_again = input("Do you want to play again? (yes/no): ")
                    if play_again.lower() == "yes":
                        break
                    else:
                        highest_score = max(self.scores)
                        # Create a dictionary to store the highest score and date
                        score_data = {
                            "highestScore": highest_score,
                            "date": str(date.today())
                        }

                        # Write the score data to a JSON file
                        with open("highest_score.json", "w") as file:
                            json.dump(score_data, file)
                        print("Highest score saved to highest_score.json.")
                        print(f"Your highest score is: {highest_score}%")
                        print((f"All scores are: {self.scores}"))
                        return

                self.provide_hint()

game = NumberGuessingGame()
game.play_game()


