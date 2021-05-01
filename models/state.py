#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import os
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    db_type = os.environ.get('HBNB_TYPE_STORAGE')
    cities = relationship("City",
                          backref="state",
                          cascade="all, delete")
    if db_type != "db":
        @property
        def cities(self):
            """Getter for cities when using FileStorage mode"""
            l = []
            for elem in models.storage.all(City).values():
                if elem.state_id == self.id:
                    l.append(elem)
            return (l)
