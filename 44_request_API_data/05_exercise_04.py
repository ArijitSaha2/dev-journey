# Exercise 4
# Import requests and create the PokéAPI base URL.
# Ask the user to enter two Pokémon names.
# Create a function called get_pokemon() that accepts a name, sends a GET request, and returns the converted JSON data if successful.
# Call the function once for each Pokémon.
# If both were found, print each Pokémon's Name and Weight.
# Print which Pokémon is heavier, or print "Both have the same weight" if their weights are equal.

import requests

base_url = "https://pokeapi.co/api/v2/"

poke_name1 = input("Enter 1st Pokemon name: ")
poke_name2 = input("Enter 2nd Pokemon name: ")

def get_pokemon(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        poke_data = response.json()
        return poke_data
    else:
        print("Pokemon not found")
    
info1 = get_pokemon(poke_name1)
info2 = get_pokemon(poke_name2)

if info1 and info2:
    print(f"Name: {info1['name']}")
    print(f"Weight: {info1['weight']}")

    print(f"Name: {info2['name']}")
    print(f"Weight: {info2['weight']}")

if info1['weight'] > info2['weight']:
    print(f"{poke_name1} is heavier")

elif info1['weight'] == info2['weight']:
    print("Both have same weight")

else:
    print(f"{poke_name2} is heavier")