# You have a list of names ["alice", "BOB", "Charlie", "diana", "EVE"]
# Use list comprehension to create a new list with all names capitalized properly
# Use list comprehension to filter only names longer than 4 characters
# Print both lists

List_of_names = ["alice", "BOB", "Charlie", "diana", "EVE"]

Capitalized = [List_of_names.capitalize() for List_of_names in List_of_names]
longer_4 = [List_of_names for List_of_names in List_of_names if len(List_of_names) > 4]

print(Capitalized)
print(longer_4)