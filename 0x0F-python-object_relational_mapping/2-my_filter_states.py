#!/usr/bin/python3
"""displays all values in the states table of hbtn_0e_0_usa where
name matches the argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    c = db.cursor()
    c.execute("""SELECT * FROM states
    WHERE name LIKE BINARY "{:s}"
    ORDER BY id ASC""".format(sys.argv[4]))
    result = c.fetchall()
    for row in result:
        print(row)
