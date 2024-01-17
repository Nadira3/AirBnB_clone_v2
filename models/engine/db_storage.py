#!/usr/bin/python3
""" City Module for HBNB project """
from models.class_find import classFind
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
import os

    

class DBStorage:
    """ DB storage class documentation """
    __engine = None
    __session = None

    def __init__(self):
        env = os.getenv('HBNB_ENV')
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database =  os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, database), pool_pre_ping=True)

        if env == 'test':
            DBStorage.__table__.drop(self.__engine)
    
    def all(self, cls=None):
        """ all method documentation """
        result = {}
        if cls:
            rows = self.__session.query(cls).all()
            for res in rows:
                value = res.to_dict()
                key = value['__class__'] + '.' + res.id
                result.update({key: res})
        else:
            tables = Base.__subclasses__()
            for t in tables:
                rows = self.__session.query(t).all()
                for res in rows:
                    value = res.to_dict()
                    key = value['__class__'] + '.' + res.id
                    result.update({key: res})
        return result

    def new(self, obj):
        """ new method documentation """
        self.__session.add(obj)

    def save(self, obj):
        """ save method documentation """
        self.__session.commit()

    def delete(self, obj):
        """ delete method documentation """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ reload method documentation """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
