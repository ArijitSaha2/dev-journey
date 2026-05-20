# Use a nested loop to print a diagonal pattern
# 4 rows
# Expected output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4

for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end=" ")
    print()