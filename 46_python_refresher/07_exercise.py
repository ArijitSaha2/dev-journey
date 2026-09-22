def get_even_positives(numbers):
    result = []
    for num in numbers:
        if num > 0 and num % 2 == 0:
            result.append(num)
    return result

print(get_even_positives([-4, -2, 0, 3, 6, 8, -10, 5]))