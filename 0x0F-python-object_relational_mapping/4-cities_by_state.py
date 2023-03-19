#!/usr/bin/python3

"""
Return list of all cities
Takes 3 arguments mysql username, mysql password and a database name
Code is safe from MySQL Injections
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
    query = "SELECT cities.id, cities.name, states.name \
             FROM cities \
             INNER JOIN states ON cities.state_id = states.id \
             ORDER BY cities.id ASC"
    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
