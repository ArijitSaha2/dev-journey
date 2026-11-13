# Exercise 75 — Fetch a Todo

# API endpoint

# https://jsonplaceholder.typicode.com/todos/1

# The API returns JSON containing:
# - userId
# - id
# - title
# - completed
# Your task:
# 1. Send a GET request.
# 2. Check for HTTP errors.
# 3. Convert the response into Python data.
# 4. Print the todo's title and completed status.
# 5. Handle request exceptions.

import requests

base_url = "https://jsonplaceholder.typicode.com/todos/"

try: 

    user_id = int(input("Enter user id number: "))

    def get_info(_id):
        url = f"{base_url}{_id}"
        response = requests.get(url)

        if response.status_code == 200:
            user_data = response.json()
            return user_data
        else:
            print(f"Failed to retrieve data {response.status_code}")
            return None

    todo_info = get_info(user_id)
    if todo_info is not None:
        print(f"Title: {todo_info['title']}")
        print(f"Completed: {todo_info['completed']}")

except ValueError:
    print(f"Come on man your suppose to enter numerical values for user id!!")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")