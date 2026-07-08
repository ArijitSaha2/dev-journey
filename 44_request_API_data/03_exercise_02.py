# Exercise 2
# Import requests and create the PokéAPI base URL.
# Ask the user to enter a Pokémon name.
# Build the Pokémon URL directly, without using a function.
# Send a GET request and check if the status code is 200.
# If successful, convert the response to Python data and print the Pokémon's Name and Weight.
# Otherwise, print "Pokemon not found".

import requests
base_url = "https://pokeapi.co/api/v2/"

pokemon_name = input("Enter pokemon: ")
url = f"{base_url}/pokemon/{pokemon_name}"

response = requests.get(url)
if response.status_code == 200:
    poke_data = response.json()
    if poke_data:
        print(f"Name: {poke_data['name'].capitalize()}")
        print(f"Weight: {poke_data['weight']}")
else:
    print("Pokemon not found")