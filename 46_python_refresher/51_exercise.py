# Exercise 51 — Mixed Collections Revision
# Create a function that accepts a list of student names and does the following:
# 1. Convert the list into a tuple and display it.
# 2. Convert the list into a set to remove duplicates and display it.
# 3. Create a new 2D list containing the names in groups of two.
# 4. Display each group using a loop.
# Requirements:
# - Take 6 names as user input.
# - Use functions and loops.
# - Don't hardcode the names.

def func(names):

    t = tuple(names)
    print(f"List converted to Tuple = {t}")

    l = []
    for row in names:
        for name in row:
            l.append(name)
    s = set(l)
    print(f"List convert to Set = {s}")
    
    for row in names:
        print(row, end="")
        print("")

student_names = []

for r in range(3):
    row = []
    for x in range(2):
        y = input("Enter student names: ")
        row.append(y)

    student_names.append(row)

func(student_names)