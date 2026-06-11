# Lambda Exercise 2
# Create a list of names = ["alice", "bob", "charlie", "diana", "eve"]
# Use map and lambda to capitalize every name
# Use filter and lambda to keep only names longer than 3 characters
# Print both results

names = ["alice", "bob", "charlie", "diana", "eve"]

result_1 = list(map(lambda name: name.capitalize(), names))
result_2 = list(filter(lambda name: len(name) > 3, names))

print(result_1)
print(result_2)