# Revision - Sets
# Create a set of 5 numbers with 2 duplicates
# Print the set — what do you notice?
# Add a number and remove a number
# Print the final set

set_ = {1, 1, 2, 3, 4} # Duplicates aren't stored at all and python sees them as the same value
# After print we saw only 1 instance of value 1 from the set was printed instead of 2 instances.

set_.add(5)
set_.remove(3)

print(set_)


# Revision - Dictionaries
# Create a dictionary with 3 student names as keys and their grades as values
# Print one student's grade
# Add a new student
# Update an existing student's grade
# Print the final dictionary

students = {"Jess": "A", "Angela": "A+", "Grace": "A+"}

print(f"Grace's Grade: {students["Grace"]}")

students["Angela"] = "B"
students["Kayleigh"] = "B+"
print(students)