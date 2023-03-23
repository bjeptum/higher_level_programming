#!/usr/bin/python3

"""
Changes the name of a State object
Uses the module sqlalchemy
"""


from sqlalchemy import Column, Integer, String, create_engine, MetaData
from sqlalchemy.engine import result
from sqlalchemy import update
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == '__main__':

    # Connect to MySQL server running on localhost at port 3306
    username, password, database = argv[1], argv[2], argv[3]

    # Create a MySQL engine and connect to database
    engine = create_engine(f'mysql+mysqldb://{username}: \
            {password}@localhost:3306/{database}')
    Base.metadata.create_all(engine)

    # Create a session to query the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for state object inputted as argument
    state = session.query(State).filter(State.id == 2).first()

    # update and persist to db
    state.name = 'New Mexico'

    session.add(state)
    session.commit()

    session.close()
