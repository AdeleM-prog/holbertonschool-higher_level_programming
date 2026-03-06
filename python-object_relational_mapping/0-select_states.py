#!/usr/bin/python3
""" MySQL imported to connect to the server and execute the SQL query
sys imported to catch the command arguments
"""
import MySQLdb
import sys

"""to manage file execution"""
if __name__ == "__main__":

    """storing arguments in variables"""
    User = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    """connexion to the server"""
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=User,
        password=passwd,
        database=db
        )

    """cursor interpreting the command and executing the SQL query"""
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    rows = cur.fetchall()

    """catching the lines from the result in order to print them"""
    for row in rows:
        print(row)

    """closing cursor and connexion"""
    cur.close()
    db.close()
