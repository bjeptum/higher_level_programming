#!/usr/bin/python3

"""
Adds the State object “Louisiana” to the database hbtn_0e_6_usa
Uses the module SQLAlchemy
"""


from sqlalchemy import Column, Integer, String, create_engine, MetaData
from sqlalchemy.engine import result
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound
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

    # Add Louisiana to database
    new_state = State(name="Louisiana")
    def save_to_db(record):
        try:
            session.add(new_state)
            session.commit()
        except MultipleResultsFound as e:
            print(e)
        except NoResultFound as e:
            print(e)

    # Query the database with newly added state
    states = session.query(State).order_by(State.id)

    # Print the results
    for state in states:
        print(f"{state.id}")

    session.close()
