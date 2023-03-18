#!/usr/bin/python3

"""
Returns all states from the database hbtn_0e_0_usa
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
    cur.execute("SELECT * FROM states ORDER BY %s ASC", (id,))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
