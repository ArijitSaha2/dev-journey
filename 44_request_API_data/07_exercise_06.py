# Exercise 6 — User Lookup
# Write a program that:
# Fetches user data from https://jsonplaceholder.typicode.com/users.
# Asks the user to enter a user ID.
# Finds the user with that ID.
# Prints: Name, Username, Email, Address
# If the ID does not exist, print User not found.

import requests

base_url = "https://jsonplaceholder.typicode.com/users"

id = input("Enter a user ID: ")

url = f"{base_url}/{id}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if data:
        print(f"Name: {data['name']}")
        print(f"Username: {data['username']}")
        print(f"Email: {data['email']}")
        print(f"Address: {data['address']}")
else:
    print(f"{id} does not exist, user not found")