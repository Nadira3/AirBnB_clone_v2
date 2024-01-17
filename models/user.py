#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base, String, Column, ForeignKey
import os


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128))
        password = Column(String(128))
        first_name = Column(String(128))
        last_name = Column(String(128))
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
