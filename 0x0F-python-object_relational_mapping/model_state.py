#!/usr/bin/python3
"""
a python file that contains the class definition of a State
"""


from SQLAlchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class state(Base):
    """ creating the state table via python"""
    __tablename__ = 'state'

    id = column(Integer, autoincrement=True,
                primary_key=True,
                nullable=False, unique=True)
    name = column(String(128), nullable=False)
