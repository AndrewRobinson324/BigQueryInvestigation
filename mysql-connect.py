# modules
from pathlib import Path

import mysql.connector
from mysql.connector import errorcode

cnf = Path.home() / ".my.cnf"
if not cnf.is_file():
    raise SystemExit(f"Missing MySQL options file: {cnf}")

conn = None
try:
    conn = mysql.connector.connect(read_default_file=str(cnf))
    print("Connected to MySQL database")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
finally:
    if conn is not None and conn.is_connected():
        conn.close()
        print("MySQL connection is closed")
