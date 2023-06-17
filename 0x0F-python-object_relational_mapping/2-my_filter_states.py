#!/usr/bin/python3
"""
Displays values of the state entered as argument
From database hbtn_0e_0_usa
Ordered by states.id
Used the module MySQLdb
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":

    # Connecting to hbtn_0e_0_usa db
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    # Create cursor
    curx = db.cursor()
    # Query data as per user input
    u_input = argv[4]
    query = ("SELECT * FROM states WHERE name LIKE '%{}%' ORDER BY id ASC")
    curx.execute(query.format(u_input))
    rows = curx.fetchall()
    for row in rows:
        print(row)
        # Close  cursor and db
    curx.close()
    db.close()
