#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    mysql_database = argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_database,
        charset="utf8mb4"
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    for query in cursor.fetchall():
        print(query)

    cursor.close()
    db.close()
