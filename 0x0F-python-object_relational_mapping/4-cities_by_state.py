#!/usr/bin/python3
"""
Lists all cities from database hbtn_0e_0_usa
Ordered by cities.id in ASC order
Used the module MySQLdb
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connecting to hbtn_0e_0_usa d
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    curx = db.cursor()
    query = ("SELECT cities.id, cities.name, states.name \
             FROM cities \
             INNER JOIN states ON cities.state_id = states.id \
             ORDER BY cities.id ASC")
    curx.execute(query)
    rows = curx.fetchall()
    for row in rows:
        print(row)
        # Close  cursor and db
    curx.close()
    db.close()
