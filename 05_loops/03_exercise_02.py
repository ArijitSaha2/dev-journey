# Create a while loop that asks the user to guess a number between 1 and 10
# Keep asking until they guess correctly
# Print how many attempts it took

attempts = 0

numb_to_guess = 7

num = int(input("enter your number to guess between 1 to 10: "))

while True:
    attempts += 1
    
    if num == numb_to_guess:
        print(f"Nice you guessed correctly = {num}")
        break

    else:
        print(f"please try again your guess is wrong = {num}")
        num = int(input("enter your number: "))
    

print(f"It took {attempts} tries for you to guess the number correctly")