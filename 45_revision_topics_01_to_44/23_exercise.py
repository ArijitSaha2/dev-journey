# Ask the user to enter their name.
# Write the name to a file called names.txt.
# Print "Saved successfully".

name = input("Enter your name: ")

file_path = "names.txt"

with open(file_path, 'w') as file:
    file.write(name)
    print("Saved successfully")