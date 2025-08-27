import requests
import json

def create_pokemon(name, height, weight, abilities):
    pokemon = {
        'Name': name,
        'Height': height,
        'Weight': weight,
        'Abilities': abilities,
    }
    return pokemon


try:
    with open('pokemons.json', 'r') as file:
        pokemons = json.load(file)
except FileNotFoundError:
    pokemons = []

main_url = 'https://pokeapi.co/api/v2/pokemon'
response = requests.get(main_url, params={'limit':5})
pokemon_main_data = response.json().get('results')

for pokemon in pokemon_main_data:
    detail_url = pokemon['url']

    detail_response = requests.get(detail_url)
    detail_data = detail_response.json()
    abilities = [ability['ability']['name'] for ability in detail_data['abilities']]
    pokemons.append(create_pokemon(detail_data['name'], detail_data['height'], detail_data['weight'], abilities))

print(pokemons)

with open('pokemons.json', 'w') as file:
    json.dump(pokemons, file, indent=4)
