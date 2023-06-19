#!/usr/bin/python3
"""
Prints state values as per name inputted by user
"""

from sys import argv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import Column, Integer, String, create_engine, MetaData
from sqlalchemy.engine import result
from model_state import Base, State


if __name__ == '__main__':

    # Connect to MySQL server running on localhost
    username, password, database, name = argv[1], argv[2], argv[3], argv[4]

    # Create engine and connect to db
    engine = create_engine(f'mysql+mysqldb://{username}:\
                             {password}@localhost:3306/{database}')

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query database and print results
    results = session.query(State).filter(State.name == name).first()

    if results is None:
        print("Not found")
    else:
        print(f"{results.id}")

    session.close()
