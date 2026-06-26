# Revision Exercise 19
# Create a function using **kwargs
# It should print every key and value
# Call the function with:
# name="Alex"
# age=20
# city="Mumbai"

def keywords(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

keywords(name = "Alex",
         age = 20,
         city = "Mumbai")