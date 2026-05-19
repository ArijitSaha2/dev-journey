# Use a nested loop to print a 3x3 countdown grid
# Each row counts down from 3 to 1
# Expected output:
# 3 2 1
# 3 2 1
# 3 2 1

for i in range(3):
    for j in reversed(range(1, 4)):
        print(j, end=" ")
    print()