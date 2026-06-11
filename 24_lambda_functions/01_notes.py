# Lambda Function can have multiple parameters
# Must be written on a single line
# Have different syntax for the regular functions
# No need for an explicit Return statement
# Lambda functions don't have a name and they are also known as anonymous functions
# EXAMPLE:
# square = lambda num: num ** 2
# addition = lambda num1, num2: (num1 + num2)
# print(square(5))
# print(addition(2, 2))


def transform_list(nums_list, transform_item): 
    transformed_0 = transform_item(nums_list[0])
    transformed_1 = transform_item(nums_list[1])
    return [transformed_0, transformed_1]

print(transform_list([2, 3], lambda num: num ** 2))
print(transform_list([2, 3], lambda num: num ** 3))


# map() = applies a function to each item in a list/tuple/etc and returns the modified items
# filter() = goes through a list/tuple/etc and returns only items where the condition is True
nums_list = [2, 3, 4, 5, 6]
print(list(map(lambda num: num ** 3, nums_list))) # map function

print(list(filter(lambda num: num % 2 == 0, nums_list))) # filter function