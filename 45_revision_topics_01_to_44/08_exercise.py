# Create a list containing three names.
# For each name, print every character on a new line.
# Print "-----" after each name.

names = ["Alice", "Noelle", "Melanie"]

print("-" * 25)

for name in names:
    print(name)
    for nam in name:
        print(nam)
    print("-" * 25)