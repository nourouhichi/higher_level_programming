#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv
if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    city = argv[4]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=db_name, port=3306)
    cur = db.cursor()
    cur.execute("SELECT  cities.name FROM cities WHERE\
                states.name = %s ORDER BY cities.id ASC", (city,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
