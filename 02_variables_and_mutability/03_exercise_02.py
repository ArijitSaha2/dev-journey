# Create a dictionary of 3 students with names as keys and grades as values
# Print the full dictionary
# Add a new student
# Remove one student using pop()
# Check if a student name exists using 'in'
# Print the final dictionary

d = {"Robin": "A", "Rose": "O", "Natasha": "A"}

print(d)

d["Carla"] = "A"

d.pop("Robin")

print("Robin" in d)
print("Carla" in d)

print(d)