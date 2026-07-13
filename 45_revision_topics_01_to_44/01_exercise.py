# Exercise 1
# Ask the user to enter five numbers separated by spaces.
# Convert them into integers.
# Use a list comprehension to create a new list containing only the even numbers.
# Create a function that accepts the filtered list and returns the sum.
# Print the filtered list and the total sum.

user = input("Enter 5 numbers separated by space: ").split()

numbers = []
total = 0
for nums in user:
    total += int(nums)
    numbers.append(int(nums))
print(f"Converted: {numbers}")

ev = [num for num in numbers if num % 2 == 0]
print(f"Even: {ev}")

def filter(num_list=ev):
    return (sum(num_list))
print(f"Sum: {filter()}")

print(f"Total Sum of list: {total}")