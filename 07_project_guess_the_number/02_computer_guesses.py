# User thinks of a number between 1 and 10
# Computer guesses a number
# User tells computer if it's too high, too low, or correct (via input)
# Computer keeps guessing until it gets it right using random

import random

def guess(x):
    low = 1 
    high = x
    computer_guesses = random.randint(low, high)

    while True:
        print('computer guessed =',computer_guesses)
        user = input("Enter if too low or too high or correct: ").lower()

        if user == "low":
            low = computer_guesses + 1
            computer_guesses = random.randint(low, high)

        elif user == "high":
            high = computer_guesses - 1
            computer_guesses = random.randint(low, high)
        
        elif user == "correct":
            print("Guessed Correctly didn't I!!!!!!")
            break


guess(10)