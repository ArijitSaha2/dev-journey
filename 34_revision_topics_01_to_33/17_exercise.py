# Revision Exercise 17
# Create a function called introduce()
# It should take name, age, city
# Call it once using positional arguments
# Call it again using keyword arguments

def introduce(name, age, city):
    return name, age, city

print(introduce("John Winchester", 40, "California")) # Positional
print(introduce(age=21, name="Cassie", city="Texas")) # Keyword