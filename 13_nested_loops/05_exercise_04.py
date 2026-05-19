# Use a nested loop to print a rectangle of stars
# Ask user for rows and columns
# Each row should be on a new line

rows = int(input("Enter number of rows: "))

columns = int(input("Enter number of columns: "))

for i in range(rows):
    for j in range(columns):
        print("*", end="")
    print()