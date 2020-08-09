#!/usr/bin/python3
"""
a python file that contains the class definition of a State
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class City(Base):
    """ creating the state table via python"""
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True,
                primary_key=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))
