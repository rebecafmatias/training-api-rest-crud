from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///pokemons.db')

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

def initialize_db():
    import core.models  
    Base.metadata.create_all(bind=engine)   