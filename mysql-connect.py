# modules
from pathlib import Path

import mysql.connector
from mysql.connector import errorcode

try:
    conn = mysql.connector.connect(read_default_file=str(Path.home() / ".my.cnf"))
    print("Connected to MySQL database")
    conn.close()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Check Credentials")
    else:
        print(err)
    
