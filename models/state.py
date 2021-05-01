#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import os
from models.engine.file_storage import FileStorage
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    db_type = os.environ.get('HBNB_TYPE_STORAGE')
    if db_type == "db":
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete")
    else:
        @property
        def cities(self):
            l = []
            for elem in FileStorage.all(City).values():
                if elem.id == self.id:
                    l.append(elem)
            return (l)
