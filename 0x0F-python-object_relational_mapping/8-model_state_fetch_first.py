#!/usr/bin/python3

"""
Prints the first state object from the database hbtn_0e_6_usa
No fetching of all states before dislaying results
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

    # Query the database for first state object in db
    try:
        first_state = session.query(State).first()
    except NoResultFound:
        print("Nothing")

    # Print the results
    print(f"{first_state.id}: {first_state.name}")
