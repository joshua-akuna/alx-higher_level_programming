#!/usr/bin/python3
"""
The script takes in an argument and displays all values in the *state*
table of *hbtn_0e_0_usa* where *name* matches the argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) == 5:
        conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3],
                charset='utf8'
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM states WHERE name = %s", (sys.argv[4],))
        rs = cur.fetchall()

        for row in rs:
            print(row)

        cur.close()
        conn.close()
