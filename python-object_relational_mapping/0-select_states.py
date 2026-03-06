#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    User = sys.argv[1]
    Passwd = sys.argv[2]
    Db = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=User, password=Passwd, database=Db)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
