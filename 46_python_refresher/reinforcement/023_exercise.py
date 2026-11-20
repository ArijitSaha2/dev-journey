# Exercise 023 — API Requests (GET Request)
# Write a Python program that fetches information about a random user from a public API.

# Requirements:
# - Make a GET request to https://randomuser.me/api/.
# - Retrieve the response.
# - Check the HTTP status code.
# - Convert the response into Python data.
# - Extract and print the user's first name, last name, and country.
# Expected output: A randomly generated user's details.

import requests

base_url = "https://randomuser.me/api/"

def get_info():
    response = requests.get(base_url)
    if response.status_code == 200:
        result = response.json()
        return result
    else:
        print(f"Failed to retrieve: {response.status_code}")

data = get_info()

if data:
    first_name = data["results"][0]["name"]["first"]
    last_name = data["results"][0]["name"]["last"]
    country = data["results"][0]["location"]["country"]

    print(f"First name: {first_name}")
    print(f"Last name: {last_name}")
    print(f"Country: {country}")