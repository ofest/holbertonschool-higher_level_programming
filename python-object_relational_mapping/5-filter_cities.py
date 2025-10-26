#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
Safe from SQL injection.
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
    cur.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
    """, (state_name,))
    rows = cur.fetchall()

    print(", ".join([r[0] for r in rows]))

    cur.close()
    db.close()
