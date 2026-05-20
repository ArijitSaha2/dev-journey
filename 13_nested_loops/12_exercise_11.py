# Create a list of 3 students, each student has a list of 3 marks
# Use a nested loop to print each student's marks
# Print the student number before their marks
# Calculate and print the average mark for each student

stud1 = [77, 89, 90]
stud2 = [66, 99, 99]
stud3 = [100, 100, 79]

l = [stud1, stud2, stud3]

counter = 1

for i in (l):
    total = 0
    print(f"Student {counter}")
    counter += 1
    for j in i:
        total += j
        print(f"{j:<3}", end=" ")
    print(f"Average Marks = {total/len(i):.2f}")
    print()
    print()