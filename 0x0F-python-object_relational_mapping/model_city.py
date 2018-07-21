#!/usr/bin/python3
"""contains the class definition of a State and an instance
Base = declarative_base()
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base


class City(Base):
    """
    Creating a City object that inherits from Base
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
