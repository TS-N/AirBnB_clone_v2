#!/usr/bin/python3
""" New engine """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.base_model import BaseModel
from os import getenv


class DBStorage:
    """ The engine linked to the MySQL """
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of the DBstorage"""

        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=engine)

    def all(self, cls=None):
        """ Query on the current database session all objects """
        if cls is not None:
            l = self.__session.query(cls).all()
        else:
            l = self.__session.all()
        print(l)

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def reload(self):
        """ create all tables in the database"""
        from models.city import City
        from models.state import State
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine)()
