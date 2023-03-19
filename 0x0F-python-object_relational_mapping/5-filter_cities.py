#!/usr/bin/python3

"""
Takes in the name of a state as an argument return list of its cities
Takes 3 arguments mysql username, mysql password and a database name
Code is SQL injection free
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to the database
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         password=argv[2],
                         port=3306,
                         db=argv[3])

    # create a cursor to execute queries
    cur = db.cursor()

    # lists all cities
    user_input = argv[4]
    query = "SELECT cities.name \
            FROM cities \
            INNER JOIN states ON cities.state_id = states.id \
            WHERE states.name LIKE '%{}%'"

    cur.execute(query.format(user_input))
    cities = cur.fetchall()

    comp_list = []
    for city in cities:
        comp_list += city

    comp_list = ", ".join(comp_list)
    print(comp_list)

    cur.close()
    db.close()
