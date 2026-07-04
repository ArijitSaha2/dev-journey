# Exercise 2
# Create a list of four programming languages.
# Create a file called language.txt using write mode.
# Write each language on a new line using a loop.
# After writing is complete, print "language.txt was created".

languages = ["Python", "Javascript", "Typescript", "C++"]

file_path = "language.txt"

with open(file_path, 'w') as file:
    for language in languages:
        file.write(language + "\n")
    print(f"{file_path} was created")