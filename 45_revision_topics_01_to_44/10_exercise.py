# Create a tuple containing five numbers.
# Write a function that accepts the tuple.
# Loop through it and print each number.
# Return the total sum.
# Print the returned value.

numbers = (1, 2, 3, 4, 5)

def func(num):
    total_sum = 0
    print("Five Numbers: ")
    for loop in num:
        total_sum += loop
        print(loop)
    return f"Total Sum: {total_sum}"

print(func(numbers))