from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import func
from core.db import Base
from pydantic import BaseModel

class PokemonSchema(BaseModel):  # data validation
    name: str
    type: str

    class Config:
        orm_mode = True

class Pokemon(Base):
    __tablename__ = 'pokemons'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False, index=True, nullable=False)
    type = Column(String, index=False, nullable=False)
    created_at = Column(String, default=func.now())



