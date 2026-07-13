# Exercise 6
# Ask the user to enter three students' names.
# Ask the user to enter each student's marks.
# Store the names and marks in a dictionary.
# Print a formatted report like this:
#
# Student         Marks
# ---------------------
# Alice           85
# Bob             91
# Charlie         78
#
# Print the average marks at the end.

name1 = input("Enter name1: ")
name2 = input("Enter name2: ")
name3 = input("Enter name3: ")

marks1 = int(input(f"Enter marks for {name1}: "))
marks2 = int(input(f"Enter marks for {name2}: "))
marks3 = int(input(f"Enter marks for {name3}: "))

marks = (marks1, marks2, marks3)

dictionary = {
    name1: marks1, 
    name2: marks2, 
    name3: marks3
}

print(f"{'Student':<10} {'Marks':>10}")
print("-" * 25)
for keys, values in dictionary.items():
    print(f"{keys:<10} {values:>7}")

average = sum(marks) / len(marks)
print(f"Average: {average}")