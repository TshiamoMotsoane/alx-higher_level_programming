#!/usr/bin/python3
"""Module containing the class definition of a City."""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    """Class representing a city. Inherits from Base.Links to the MySQL table
    cities."""

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
