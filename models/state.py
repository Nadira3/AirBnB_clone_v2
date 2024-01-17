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
        city_list = storage.__session.query(City, State).\
                filter(City.state_id == self.id).Order_by(City.id).all()
        return city_list
        
