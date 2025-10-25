#!/usr/bin/python3
"""
Lists all states with a name given in arguments
from the database hbtn_0e_0_usa.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * \
    FROM states \
    WHERE BINARY name = '{}'\
    ORDER BY id ASC".format(argv[4]))
    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()
