#!/usr/bin/python3
""" New engine """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity

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
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ Query on the current database session all objects """
        l = []
        if cls is not None:
            r = self.__session.query(cls).all()
        else:

            pass
            """
            print(self.__engine.table_names())
            for e in Base.metadata.tables.keys():
                r = self.__session.query(Base.metadata.tables[e]).all()
                for j in r:
                    print(j)
                    print(type(j))
                    """
        for obj in r:
            l.append(obj.__str__())
        return(l)

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fact)
        self.__session = Session()

    def close(self):
        """ Close session """
        self.__session.close()
