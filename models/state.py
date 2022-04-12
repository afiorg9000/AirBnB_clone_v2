#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class State(BaseModel, Base):
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
