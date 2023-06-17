#!/usr/bin/python3
"""
Lists all cities in the state inputted by user
From database hbtn_0e_0_usa
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
    # Query data as per user input
    u_input = argv[4]
    query = ("SELECT cities.name \
             FROM cities \
             INNER JOIN states ON cities.state_id = states.id \
             WHERE states.name = %s \
             ORDER BY cities.id ASC")
    curx.execute(query, (u_input,))
    cities = curx.fetchall()

    # Convert the tuple to list
    cities_list = []
    for city in cities:
        # Append only the first element of the tuple
        cities_list.append(city[0])
    # Join elemenents with a comma
    cities_list = ", ".join(cities_list)
    print(cities_list)

    # Close  cursor and db
    curx.close()
    db.close()
