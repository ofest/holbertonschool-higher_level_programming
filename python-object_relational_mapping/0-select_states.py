#!/user/bin/python3

""" Lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # Create a cursor and execute the query
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print all results
    for state in cur.fetchall():
        print(state)

    # Close cursor and connection
    cur.close()
    db.close()
