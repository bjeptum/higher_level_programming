#!/usr/bin/python3

"""
Return lists all states with a name starting with N
Takes 4 arguments mysql username, mysql password, database name a
and state name searched
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to the database
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         password=argv[2],
                         port=3306,
                         db=argv[3])

    # create a cursor to execute queries
    cur = db.cursor()

    # lists all states where name matches user input
    user_input = argv[4]
    query = "SELECT * FROM states WHERE name LIKE '%{}%' ORDER BY id ASC"
    cur.execute(query.format(user_input))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
