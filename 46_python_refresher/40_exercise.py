# Exercise 40 — Mixed Revision
# Write a number-guessing program that:
# 1. Generates a random number between 1 and 20.
# 2. Repeatedly asks the user to guess the number.
# 3. If the guess is too high, display "Too high".
# 4. If it's too low, display "Too low".
# 5. If correct, display "Correct! You guessed it." and stop the loop.
# 6. Count and display the number of attempts.
# Concepts tested: while loops, conditionals, user input, type casting, comparison operators, variables and the random module.

import random

def guess(number):
    result = random.randint(1, 20)
    count = 0
    while result != number:
        if number > result:
            print("Too high")
        if number < result:
            print("Too low")
        number = int(input("Enter a number from 1 to 20: "))
        count += 1
    print(f"You guessed it correctly!!!\nYour Answer: {number}\nNumber of times guessed: {count}")

print("Guess the number from 1 to 20!!!!")
guess(number = int(input("Enter number: ")))