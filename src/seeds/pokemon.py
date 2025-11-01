def catch_pokemon_data(pokemon_id: int):
    import requests

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url=url)
    data = response.json()
    data_types = data['types']
    type_list = []  
    print(f'Processing Pokemon ID: {pokemon_id}')
    
    i_types_list = []
    for i in data_types:
        i_types_list.append(i['type']['name'])
    
    pokemons_type = ', '.join(i_types_list)
    pokemons_type = str(pokemons_type)
    print(f'\n{pokemons_type}')
    type_dict = {  
        'name': data['name'],
        'type': pokemons_type
    }
    type_list.append(type_dict)

    return type_list

def check_pokemon_data(pokemons_data_list: list): 
    from core.models import PokemonSchema   
    
    for pokemon_data_dict in pokemons_data_list:
        return PokemonSchema(name=pokemon_data_dict['name'], type=pokemon_data_dict['type'])
  
    
def seed_pokemons(pokemons_data_list: list):
    from core.db import session
    from core.models import Pokemon

    for pokemon_data in pokemons_data_list:
        pokemon = Pokemon(
            name=pokemon_data['name'],
            type=pokemon_data['type']
        )
        session.add(pokemon)
    
    session.commit()
    
    return pokemons_data_list  


    