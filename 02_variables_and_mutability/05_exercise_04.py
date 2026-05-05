# Create a tuple of 5 colors
# Try to change a value (comment it out and explain why it fails)
# Create a new tuple with one color replaced
# Check if a color exists using 'in'
# Print both tuples

t = ("red", "green", "blue", "yellow", "pink")

# t[0] = "navy blue" # Values in tuple cannot be changed. Since they are immutable. Create a new tuple change not possible

rt = ("red", "green", "blue", "purple", "pink")

print("purple" in t)
print("purple" in rt)

print(t)
print(rt)