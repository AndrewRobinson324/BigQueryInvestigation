# modules
import mysql.connector
from mysql.connector import errorcode

# connection
try:
    conn = mysql.connector.connect(read_default_file= 'Users/andrew/.my.cnf')
    print("Connected to MySQL database")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
finally:
    if conn.is_connected():
        conn.close()
        print("MySQL connection is closed")

conn.close()