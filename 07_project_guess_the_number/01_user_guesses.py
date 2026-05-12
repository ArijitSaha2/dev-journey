# Computer picks a number between 1 and 10 (hardcode it)
# Ask user to keep guessing until correct
# Tell them if their guess is too high or too low
# Print how many attempts it took



def guess(n = 7):
    counts = 1
    while True:
        user_guess = int(input("try to guess the number: "))
        if user_guess == n:
            print("Guess is Correct")
            print(f"It took {counts} attempt to guess the number")
            break
        elif user_guess > n:
            print("The number you picked is high")
        elif user_guess < n:
            print("The number you picked is low")
        counts += 1
        
guess()