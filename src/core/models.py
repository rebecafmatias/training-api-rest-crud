from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import func
from core.db import Base

class Pokemon(Base):
    __tablename__ = 'pokemons'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    type = Column(String, index=True, nullable=False)
    created_at = Column(String, default=func.now())



