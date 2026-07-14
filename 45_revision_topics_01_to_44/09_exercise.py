# Create a function called introduce().
# The function should accept name, age, and city.
# Call the function using keyword arguments in a different order than the parameters.
# Print the information using an f-string.

def introduce(name, age, city):
    return f"Name: {name}, Age: {age}, City: {city}"

print(introduce(age='21', city='New York', name='Ariana'))