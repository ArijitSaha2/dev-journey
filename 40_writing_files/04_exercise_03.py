# Exercise 3
# Ask the user to enter their name and favorite game.
# Create a file called profile.txt using write mode.
# Write the name and favorite game on separate lines with labels.
# After writing is complete, print "profile.txt was created".

name = input("Enter your name: ")
game = input("Enter your favourite game: ")

file_path = "profile.txt"

with open(file_path, "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Fav Game: {game}")
    print(f"{file_path} was created")