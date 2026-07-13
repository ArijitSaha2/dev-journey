# Exercise 5
# Create a tuple containing five fruits.
# Use a for loop to display each fruit.
# Print:
# - The first letter.
# - The last letter.

t = ("Apple", "Banana", "Kiwi", "Dragon", "Strawberry")

print("-" * 25) # Only prints once at the top; the others are printed inside the loop.
for fruits in t:
    print(f"{fruits}")
    print(f"First letter: {fruits[0]}\nLast letter: {fruits[-1]}")
    print("-" * 25)