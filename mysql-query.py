# modules
from pathlib import Path

import mysql.connector
from mysql.connector import errorcode


conn = mysql.connector.connect(read_default_file=str(Path.home() / ".my.cnf"))

cursor = conn.cursor()

query = (
    "SELECT year, title, genre "
    "FROM `u479841347_sql_course`.`imdb_movies` "
    "LIMIT 5"
)

cursor.execute(query)

for (year, title, genre) in cursor:
    print(f"{year}: {title}: {genre}")

cursor.close()
conn.close()
  
    
