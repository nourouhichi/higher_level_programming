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
    name = argv[4]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=db_name, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINZRY\
                states.name = %s ORDER BY states.id ASC"(name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
