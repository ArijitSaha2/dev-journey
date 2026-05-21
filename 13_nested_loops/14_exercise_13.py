# Create a 3x3 grid of numbers
# Each cell should contain the product of its row and column number
# Print it like a grid
# Expected:
# 1 2 3
# 2 4 6
# 3 6 9

for i in range(1, 4):
    for j in range(1, 4):
        print(j*i, end=" ")
    print()