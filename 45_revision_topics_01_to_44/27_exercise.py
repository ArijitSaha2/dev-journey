# Exercise 27 — API Requests

# Send a GET request to:
# https://jsonplaceholder.typicode.com/users/1
#
# If the request is successful:
# - Print the user's Name.
# - Print the user's Email.
#
# Otherwise, print "Request failed".

import requests

base_url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(base_url)

if response.status_code == 200:
    data = response.json()
    print(f"Name: {data['name']}")
    print(f"Email: {data['email']}")
else:
    print("Request Failed")