# modules
from pathlib import Path
import pandas as pd
import mysql.connector
from mysql.connector import errorcode


conn = mysql.connector.connect(read_default_file=str(Path.home() / ".my.cnf"))


query = (
    "SELECT year, title, genre "
    "FROM `u479841347_sql_course`.`imdb_movies` "
    "LIMIT 5"
)

df = pd.read_sql(query, conn)
print(df)

conn.close()