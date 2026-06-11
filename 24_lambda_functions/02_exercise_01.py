# Lambda Exercise 1
# Create a list of numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Use map and lambda to create a new list with each number doubled
# Use filter and lambda to create a new list with only odd numbers
# Print both results

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list_1 = (list(map(lambda nums: nums * 2, l)))

new_list_2 = (list(filter(lambda nums : nums % 2 != 0, l)))

print(new_list_1)
print(new_list_2)