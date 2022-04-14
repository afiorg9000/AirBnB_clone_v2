#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = 'users'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(126), nullable=False)
        password = Column(String(126), nullable=False)
        first_name = Column(String(126), nullable=False)
        last_name = Column(String(126), nullable=False)
        places = relationship('Place', cascade="all, delete")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''

    def __init__(self, *args, **kwargs):
        """ instantiates a new city """
        super().__init__(self, *args, **kwargs)
