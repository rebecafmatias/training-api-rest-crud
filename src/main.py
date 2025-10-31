from core.db import initialize_db
from seeds.pokemon import catch_pokemon_data, check_pokemon_data, seed_pokemons

def main():
    print("Initializing database...")
    initialize_db()
    print("Database initialized.")

    pokemons_to_seed = 10  # Number of Pokemons to seed
    print(f"Seeding {pokemons_to_seed} Pokemons...")
    for pokemon_id in range(1, pokemons_to_seed + 1):
        pokemon_data = catch_pokemon_data(pokemon_id)
        pokemon_schema = check_pokemon_data(pokemon_data)
        seed_pokemons(pokemon_data)
        print(f"Seeded: {pokemon_schema}")
    print("Seeding completed.")
if __name__ == "__main__":
    main()