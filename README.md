# Training: Simple Pokémon Seeder (SQLAlchemy)

## Overview
This small project demonstrates using SQLAlchemy to define a model and persist data to a SQLite database. The provided script fetches Pokémon data from the public PokeAPI and seeds the local database with one record per Pokémon-type combination (for example, a dual-type Pokémon will produce two records).

This repository is a learning exercise and not a full web API server.

## Features
- SQLAlchemy model for `pokemons` (id, name, type, created_at)
- Creates the SQLite database file (`pokemons.db`) automatically
- Fetches data from the PokeAPI and seeds the database with Pokémon names and types

## Requirements
- Python 3.8+
- Poetry (recommended) or install dependencies manually

## Installation
1. Clone the repository:

```powershell
git clone https://github.com/rebecafmatias/training-api-rest-crud.git
cd aula-18-api-crud
```

2. Create/activate a virtual environment and install dependencies with Poetry:

```powershell
# Create venv (optional) and activate, or rely on Poetry's virtualenv
poetry install
poetry shell
```

If you prefer pip, create a virtualenv and install packages listed in `pyproject.toml`.

## Usage
Run the main script to initialize the database and seed Pokémon data:

```powershell
python src/main.py
```

What this does:
- Initializes the SQLite database and SQLAlchemy metadata (creates `pokemons.db`)
- Fetches Pokémon data from the PokeAPI
- Inserts one database row per (name, type) combination

## Database file
After running the script, a `pokemons.db` SQLite file will be created in the project root. You can inspect it with any SQLite client.

Examples:

Inspect with the sqlite3 CLI (PowerShell):

```powershell
# Open DB
sqlite3.exe pokemons.db
# In sqlite prompt, run:
# SELECT id, name, type, created_at FROM pokemons LIMIT 10;
```

Quick Python snippet to read first rows:

```python
import sqlite3
conn = sqlite3.connect('pokemons.db')
cur = conn.cursor()
for row in cur.execute('SELECT id, name, type, created_at FROM pokemons LIMIT 10'):
	print(row)
conn.close()
```

## Notes / Implementation details
- Models: `src/core/models.py` defines `Pokemon` (SQLAlchemy) and a Pydantic schema for validation.
- Database setup: `src/core/db.py` creates the engine and calls `Base.metadata.create_all(...)` during initialization.
- Seeding: `src/seeds/pokemon.py` fetches types for each Pokémon and stores each type as a separate record so dual-type Pokémon are saved twice (one row per type).
- The seeder currently commits results directly and may create duplicate records if run multiple times for the same Pokémon names (the `name` column is defined as unique in the model, so duplicates may cause insert errors).

## Contributing
Feel free to open issues or submit pull requests. Ideas for improvement:
- Add an API layer (FastAPI) to serve the stored pokémons
- Make seeding idempotent (upsert behavior)
- Add tests and CI

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
If you have questions or want guidance on next steps (API, tests, idempotent seeding), open an issue or reach out via the repository.