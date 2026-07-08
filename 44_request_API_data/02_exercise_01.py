# Exercise 1
# Import requests and Create the PokéAPI base URL.
# Create a function called get_pokemon() that accepts a Pokémon name.
# Build the URL for that Pokémon.
# Send a GET request to the URL.
# If the status code is 200: Convert the response from JSON into Python data and return it.
# Otherwise: Print "Pokemon not found".
# Ask the user to enter a Pokémon name.
# Call get_pokemon() using the entered name.
# If data was returned, print the Pokémon's: Name, ID, Height

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print("Pokemon Not found")

pokemon_name = input("Enter your pokemon: ")
pokemon_info = get_pokemon(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"Id: {pokemon_info['id']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")