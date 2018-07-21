#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities of that
state, using the database hbtn_0e_4_usa
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
    c.execute("""SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name LIKE %s
    ORDER BY cities.id ASC""", (sys.argv[4],))
    result = c.fetchall()
    res_len = len(result)
    for i in range(res_len):
        if i < res_len - 1:
            print(result[i][0], end=", ")
        else:
            print(result[i][0])
