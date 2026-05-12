# Computer picks a number between 1 and 10 (use random)
# Ask user to keep guessing until correct
# Print how many attempts it took
# Uses random.randint() to generate the number
# while True loop runs until correct guess then breaks

import random

def guess(x):
    random_number = random.randint(1, 10)
    count = 1
    while True:
        if x == random_number:
            print(f"Correct Guess!!! = {random_number}")
            print(f"It took you {count} tries to guess correctly")
            break

        elif x!= random_number:
            user = int(input("Try to Guess the number again!! = "))
            x = user
        
        count += 1
    

user = int(input("Try to Guess the number = "))
guess(user)