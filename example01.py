import requests
from pydantic import BaseModel

# requests.get # select
# requests.post # create
# requests.put # update
# requests.delete # delete

class PokemonSchema(BaseModel): # data validation
    name: str
    type: list[str]

    class ConfigDict:
        orm_mode = True

def catch_pokemon(id: int):
    url = f"https://pokeapi.co/api/v2/pokemon/{id}"

    reponse = requests.get(url=url)
    data = reponse.json()
    data_types = data['types']
    type_list = []

    for i in data_types:
        type_list.append(i['type']['name'])
    types = ', '.join(type_list)
    
    return PokemonSchema(name=data['name'],type=type_list)

if __name__ == "__main__":
    pokemon = catch_pokemon(15)
    print(pokemon)