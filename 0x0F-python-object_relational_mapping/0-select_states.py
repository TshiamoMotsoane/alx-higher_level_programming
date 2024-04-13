#!/usr/bin/python3
""" Script to list all states from the database htbn_0e_0_usa."""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
            passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT *FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()

