# Use a nested loop to print a 4x4 number grid
# Each row prints numbers 1 to 4
# Expected output:
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

for i in range(1, 5):
    for j in range(1, 5):
        print(j, end=" ")
    print()