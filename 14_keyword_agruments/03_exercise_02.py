# Create a function that takes name, age, and city as parameters
# Call it 3 times using keyword arguments in different orders each time

def crendentials(name, age, city):
    print(f"{name} {age} {city}")

crendentials(name="Addison", age=25, city="New York")
crendentials(age=27, name="Jessie", city="Texas")
crendentials(city="Manhatan", age=25, name="Clara")