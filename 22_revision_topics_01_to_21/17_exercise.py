# Revision - List Comprehensions
# Create a list of squares for numbers 1 to 10
# Filter only the odd squares from that list
# Print both lists

all_squares = [i*i for i in range(1, 11)]
all_odd = [num for num in all_squares if num % 2 != 0]
print(f"All squares from 1 to 10: {all_squares}")
print(f"Only odd squares : {all_odd}")

# Revision - Modules
# Import the math module
# Print the square root of 256
# Print the value of pi rounded to 4 decimal places
# Print the ceiling of 7.2

import math 

n = 256
result = math.sqrt(n)

print(result)
print(f"{math.pi:.4f}")
print(math.ceil(7.2))