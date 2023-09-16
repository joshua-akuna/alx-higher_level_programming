#!/usr/bin/python3
"""
The script takes in the name of a state as an argument and lists all cities
of the state, using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
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
        cur.execute("""SELECT cities.name FROM cities, states
                WHERE cities.state_id = states.id
                AND states.name = %s""", (sys.argv[4],))

        rs = cur.fetchall()
        res = ''
        flag = 0

        for row in rs:
            if flag:
                res += ", "
            res += row[0]
            flag = 1

        print(res)
