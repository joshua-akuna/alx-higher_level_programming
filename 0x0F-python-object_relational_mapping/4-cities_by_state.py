#!/usr/bin/python3
"""
The script lists all cities from the database hbtn_0e_4_usa
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
        cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities, states WHERE cities.state_id = states.id""")
        rs = cur.fetchall()

        for row in rs:
            print(row)

        cur.close()
        conn.close()
