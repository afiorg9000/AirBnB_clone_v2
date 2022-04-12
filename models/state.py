#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade="all, delete")
    

    @property
    def cities(self):
        """ Will return list of cities with state_id """
        res = []
        for city in self.cities:
            if city.state_id == self.id:
                res.append(city)
        return res
