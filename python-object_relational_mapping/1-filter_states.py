#!/usr/bin/python3
""" lists all states with a name starting with N from the hbtn_0e_0_usa:
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * \
    FROM states \
    WHERE name like BINARY 'N%' \
    ORDER BY id ASC")
    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()
