def find_largest(numbers):
    largest = 0
    for num in numbers:
        if num > largest:
            largest = num
    return largest

print(find_largest(numbers = [4, 9, 2, 17, 6]))