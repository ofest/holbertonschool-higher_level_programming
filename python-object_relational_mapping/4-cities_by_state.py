#!/usr/bin/python3
""" Write a script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name \
    FROM cities as c \
    INNER JOIN states as s \
    ON c.state_id = s.id \
    ORDER BY c.id")
    [print(city) for city in cur.fetchall()]
    cur.close()
    db.close()
