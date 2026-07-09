# Exercise 5
# Import requests and create the base URL: https://jsonplaceholder.typicode.com/
# Ask the user to enter a post ID.
# Build the URL for that post using /posts/{post_id}.
# Send a GET request and check if the status code is 200.
# If successful, convert the response to Python data and print the post's Title and Body.
# Otherwise, print "Post not found".

import requests

base_url = "https://jsonplaceholder.typicode.com/"

user = input("Enter a post ID: ")

url = f"{base_url}/posts/{user}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if data:
        print(f"Title: {data['title']}")
        print(f"Body: {data['body']}")
else:
    print("Post not found")