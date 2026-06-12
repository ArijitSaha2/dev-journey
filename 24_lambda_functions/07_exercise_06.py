# Lambda Exercise 6
# Create a list of students = [("Alice", 85), ("Bob", 42), ("Charlie", 91), ("Diana", 58)]
# Use filter and lambda to keep only students who passed (score above 50)
# Use map and lambda to add 5 bonus marks to every passing student's score
# Print both results

students = [("Alice", 85), ("Bob", 42), ("Charlie", 91), ("Diana", 58)]

above_50 = list(filter(lambda stud: stud[1] > 50, students))

bonus_5 = list(map(lambda stud: (stud[0], stud[1] + 5), above_50))

print(above_50)
print(bonus_5)