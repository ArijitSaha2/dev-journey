# Extra - Default & Keyword Arguments
# Create a function that takes item, price, and quantity (default 1)
# Print the total cost: "Total for [item]: ₹[price * quantity]"
# Call it 3 times: once with all args, once with just item and price, once using quantity as keyword argument

def func(item, price, quantity = 1):
    print(f"{item} = ₹{price * quantity}")

func("Apple", 60, 4)
func("Toy", 2000)
func("Smartphone", 35000, quantity = 2)

# Extra - List Comprehensions
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Use list comprehension to create a new list with only numbers greater than 5, squared
# Print the result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

greater = [greater*greater for greater in numbers if greater > 5]

print(greater)