# Revision - Lists
# Create a list of 5 fruits
# Add a fruit at the end
# Remove the second fruit
# Print the final list and its length

fruits = ["Apple", "Banana", "Coconut", "Dragon", "Watermelon"]
fruits.append("Mango")
fruits.remove("Dragon")
print(fruits)


# Revision - Tuples
# Create a tuple of 3 colors
# Print the second color
# Try to change the first color — what happens and why?
# Print the full tuple

colors = ("Red", "Blue", "Green")
print(colors[1])
# colors.remove("Red") Existing tuples cannot be changes they are immutable.
#                      Create an entire new tuple to assign values.

print(colors, len(colors))