# Exercise 1
# Create a list of three game names.
# Create a file called games.txt using write mode.
# Use a loop to write each game name on a new line in the file.
# Print "games.txt was created" after writing is complete.

games = ["Grand Theft Auto V", "Cyberpunk 2077", "Forza Horizon 6"]

file_path = "games.txt"

with open(file_path, "w") as file:
    for game in games:
        file.write(game + "\n")
    print(f"{file_path} file was created")