#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128))
    
    cities = relationship("City", cascade = "all, delete, delete-orphan", back_populates="state")

    @property
    def cities(self):
        """ cities model docs """
        from models import storage
        city_list = []
        city_dict = storage.all(City)
        for city_objs in city_dict.values():
            if city_objs['state_id'] == self.id:
                city_list.append(city_objs)
        return city_list
        
