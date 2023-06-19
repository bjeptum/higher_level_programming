#!/usr/bin/python3
"""
State module
"""

from sys import argv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, create_engine


Base = declarative_base()


class State(Base):
    """Class definition of State"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
