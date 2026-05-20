# Use a nested loop to print a times table
# Ask user for a number
# Print the table from 1 to 10
# Format: "5 x 1 = 5"

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i:2} x {j:1} = {i*j:<5}", end="  ")
    print()