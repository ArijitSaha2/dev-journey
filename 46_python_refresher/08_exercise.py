def double_odd_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 != 0:
            num = num + num
            result.append(num)
    return result

print(double_odd_numbers([1, 2, 3, 4, 5, 6, 7]))