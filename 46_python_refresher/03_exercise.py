def square_numbers(numbers):
    result = []
    for num in numbers:
        num = num*num
        result.append(num)
    return result
        
print(square_numbers([1, 2, 3, 4, 5]))