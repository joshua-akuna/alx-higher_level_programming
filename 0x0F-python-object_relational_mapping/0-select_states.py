#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa using MySQLdb
"""
import MySQLdb
import sys

if __name__ == "__main__":
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
        cur.execute('SELECT * FROM states ORDER BY states.id ASC')
        result_set = cur.fetchall()

        for row in result_set:
            print(row)

        cur.close()
        conn.close()
