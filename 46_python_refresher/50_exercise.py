# Exercise 50 — 2D Lists
# Write a program that:
# 1. Creates a 2D list containing three rows, with three numbers in each row.
# 2. Displays the complete 2D list.
# 3. Displays the element at the second row and third column.
# 4. Displays each row using nested loops.
# Requirements:
# - Use a function.
# - Use nested loops.
# - Don't hardcode the individual numbers; collect them from the user.

def two_d_list(matrix):
    print(f"Complete 2D list: {matrix}")

    # Second row, third column
    print(f"Second row, third column: {matrix[1][2]}")

    # Display each row using nested loops
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()


matrix = []

for r in range(3):
    row = []

    for c in range(3):
        value = int(input("Enter value: "))
        row.append(value)

    matrix.append(row)

two_d_list(matrix)