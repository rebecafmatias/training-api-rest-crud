def catch_pokemon_data(pokemon_id: int):

    import requests

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url=url)
    data = response.json()
    data_types = data['types']
    type_dict = {}
    type_list = []

    for i in data_types:
        type_dict['name'] = data['name']
        type_dict['type'] = i['type']['name']
        type_list.append(type_dict)

        print(type_list)
    return type_list  

def check_pokemon_data(pokemons_data_list: list): 
    from core.models import PokemonSchema   
    
    for pokemon_data_dict in pokemons_data_list:
        return PokemonSchema(name=pokemon_data_dict['name'], type=pokemon_data_dict['type'])
  
    
def seed_pokemons(pokemons_data_list: list):
    from core.db import session
    from core.models import Pokemon

    pokemons_to_add = []

    for pokemon_data in pokemons_data_list:
        pokemon = Pokemon(name=pokemon_data['name'], type=pokemon_data['type'])
        pokemons_to_add.append(pokemon)

    with session as s:
        s.add_all(pokemons_to_add)
        s.commit()
