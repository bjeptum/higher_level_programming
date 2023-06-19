#!/usr/bin/python3
"""
Changes the name of a State object  wher id = 2 to New Mexico
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

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query database and print results
    state = session.query(State).filter(State.id == '2').first()

    if state:
        state.name = "New Mexico"
        session.commit()

    # Close session
    session.close()
