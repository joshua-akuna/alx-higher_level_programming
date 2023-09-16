#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N' from
the database 'hbtn_0e_0_usa'
"""
import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) == 4:
        conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3],
                charset='utf8'
        )
        cur = conn.cursor()
        st = 'SELECT * FROM states WHERE name LIKE "N%" ORDER BY states.id ASC'
        cur.execute(st)
        rs = cur.fetchall()

        for row in rs:
            print(row)

        cur.close()
        conn.close()
