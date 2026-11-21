# Exercise 024 — API Requests (Query Parameters)
# Fetch posts belonging to a specific user using the JSONPlaceholder API.

# Your task:
# - Send a GET request to https://jsonplaceholder.typicode.com/posts.
# - Retrieve only posts belonging to user ID 1 using query parameters.
# - Check whether the request succeeded.
# - Convert the response into Python data.
# - Print the title of each returned post.
# API reference:

# The response contains a list of dictionaries. Each post has these fields:
# - userId
# - id
# - title
# - body

import requests

base_url = "https://jsonplaceholder.typicode.com/posts"

def get_info(user_id):
    response = requests.get(base_url, params={"userId": user_id})

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        print(f"Failed to retrieve data {response.status_code}")

uid = int(input("Enter user id(A number): "))
data = get_info(uid)

if data:
    for post in data:
        print(f"UserId: {post['userId']}")
        print(f"ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("-" * 40)