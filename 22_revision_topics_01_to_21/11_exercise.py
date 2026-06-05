# Revision - Nested Loops
# Print a multiplication table for numbers 1 to 5
# Format: "1 x 1 = 1", "1 x 2 = 2" etc.

for x in range(1, 6):
    for y in range(1, 6):
        print(f"{x} x {y} = {x*y}")