# User thinks of a number between 1 and 10
# Computer guesses a number
# User tells computer if it's too high, too low, or correct (via input)
# Computer keeps guessing until it gets it right

def guess():
    computer_guesses = 5
    while True:
        print('computer guessed =',computer_guesses)
        user = input("Enter if too low or too high or correct: ").lower()

        if user == "low":
            computer_guesses += 1
            print(computer_guesses)

        elif user == "high":
            computer_guesses -= 1
            print(computer_guesses)
        
        elif user == "correct":
            print("Guessed Correctly didn't I!!!!!!")
            break


guess()