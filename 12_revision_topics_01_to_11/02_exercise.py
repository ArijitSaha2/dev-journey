# Create a dictionary of 5 countries and their capitals
# Ask user to enter a country name
# Check if it exists in the dictionary using 'in'
# If yes, print the capital
# If no, print "Country not found"

dictionary = {"America": "Washington", "England": "London", "Australia": "Sydney", "Indonesia": "Bali", "Canada": "Toronto"}

user = input("Enter a country: ").capitalize()

if user in dictionary:
    print("Capital is",dictionary[user])
else:
    print("Country not found")