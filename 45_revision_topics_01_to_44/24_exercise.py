# Read the contents of names.txt.
# Print the contents.
# Handle FileNotFoundError.

try: 
    file_path = "names.txt"
    with open(file_path, "r") as file:
        reader = file.read()
        print(reader)
except FileNotFoundError:
    print("Unfortunately file is not found")