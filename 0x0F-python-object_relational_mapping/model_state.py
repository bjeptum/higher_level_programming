#!/usr/bin/python3

"""
Class definition of State
Use the module SQLAlchemy
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sys import argv

Base = declarative_base()


class State(Base):
    """Derived class from Base"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
