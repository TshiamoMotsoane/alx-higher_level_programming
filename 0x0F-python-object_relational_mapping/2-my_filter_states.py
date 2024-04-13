#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name_searched = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
            passwd=password, db=database)
    cursor = db.cursor()
    query = "SELEECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name_searched,))


    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    cursor.close()
    db.close()
