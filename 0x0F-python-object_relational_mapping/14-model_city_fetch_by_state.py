#!/usr/bin/python3

"""
Lists all city objects from database hbtn_0e_14_usa
"""

from sqlalchemy import Column, Integer, String, create_engine, MetaData
from sqlalchemy.engine import result
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City


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

    # Query the database for all City  objects
    cities_query = session.query(City.id, City.name, State.name) \
            .join(State).order_by(City.id)

    # Print the results
    for city_id, city_name, state_name  in cities_query:
        print(f"{state_name}: ({city_id}) {city_name}")

    session.close()
