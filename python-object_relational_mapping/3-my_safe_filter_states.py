#!/usr/bin/python3
"""
Safe search: lists all states with a given name (protected from SQL injection)
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:

        print("Usage: {} <user> <passwd> <db> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=user,
                         passwd=passwd,
                         db=db_name)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
