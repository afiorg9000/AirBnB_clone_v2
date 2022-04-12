#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String

class State(BaseModel, base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False
