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

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=db_name, port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities WHERE state_id = (SELECT
                id FROM states WHERE name='%s')""" % argv[4])
    rows = cur.fetchall()
        print(", ".join(row[0] for row in rows)
    cur.close()
    db.close()
