# Recursion Exercise 9  
# Write a recursive function that calculates the sum of a list
# numbers = [1, 2, 3, 4, 5]

def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])

print(sum_list([1, 2, 3, 4, 5]))