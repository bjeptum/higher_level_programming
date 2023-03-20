#!/usr/bin/python3

"""
Lists all state objects that start with letter a from hbtn_0e_6_usa
Uses the module SQLAlchemy
"""


from sqlalchemy import Column, Integer, String, create_engine, MetaData
from sqlalchemy.engine import result
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == '__main__':

    # Connect to MySQL server running on localhost at port 3306
    username, password, database = argv[1], argv[2], argv[3]

    # Create a MySQL engine and connect to database
    engine = create_engine(f'mysql+mysqldb://{username}:\
                             {password}@localhost:3306/{database}')
    Base.metadata.create_all(engine)

    # Create a session to query the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for state  objects that start with a
    states = session.query(State).filter(State.name.like('%a%'))

    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
