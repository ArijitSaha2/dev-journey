# Exercise 3
# Import requests and create the PokéAPI base URL.
# Ask the user to enter a Pokémon name.
# Create a function called get_pokemon() that accepts the name, builds the URL, and sends a GET request.
# If successful, return the converted JSON data; otherwise print "Pokemon not found".
# Call the function and print the Pokémon's Name, Height, and Weight if data was returned.

import requests

base_url = "https://pokeapi.co/api/v2/"

user = input("Enter Pokemon name: ")

def get_pokemon(name=user):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        Poke_data = response.json()
        if Poke_data:
            print(f"Name: {Poke_data['name'].capitalize()}")
            print(f"Height: {Poke_data['height']}")
            print(f"Weight: {Poke_data['weight']}")
    else:
        print("Pokemon not found")

poke_info = get_pokemon()