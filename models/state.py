#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import Base

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade="all, delete")
    else:
        name = ""

    @property
    def cities(self):
        """ Will return list of cities with state_id """
        res = []
        for city in self.cities:
            if city.state_id == self.id:
                res.append(city)
        return res
