#!/usr/bin/python3

"""
Return lists all states with a name starting with N
Take 3 arguments mysql username, mysql password and database name
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

    # lists all states with a name starting with N
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
