#!/usr/bin/python3
"""
Returns the first state object from database
"""

from sys import argv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import Column, Integer, String, create_engine, MetaData
from sqlalchemy.engine import result
from model_state import Base, State


if __name__ == '__main__':

    # Connect to MySQL server running on localhost
    username, password, database = argv[1], argv[2], argv[3]

    # Create engine and connect to db
    engine = create_engine(f'mysql+mysqldb://{username}:\
                             {password}@localhost:3306/{database}')
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query database and print results
    state_1 = session.query(State).first()

    if state_1 is None:
        print("Nothing")
    else:
        print(f"{state_1.id}: {state_1.name}")

    session.close()
