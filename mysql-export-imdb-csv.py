# modules
from pathlib import Path

import mysql.connector
import pandas as pd

DB = "u479841347_sql_course"
TABLE = "imdb_movies"
OUT = Path(__file__).resolve().parent / "imdb_movies_with_rating.csv"
# No ALTER: movie_rating exists only in this export (not in MySQL).

conn = mysql.connector.connect(read_default_file=str(Path.home() / ".my.cnf"))

query = f"""
SELECT title, year, genre, avg_vote,
CASE
    WHEN `avg_vote` IS NULL THEN NULL
    WHEN `avg_vote` < 3 THEN 'bad'
    WHEN `avg_vote` < 6 THEN 'okay'
    ELSE 'good'
END AS `movie_rating`
FROM `{DB}`.`{TABLE}`
"""

df = pd.read_sql(query, conn)
conn.close()

df.to_csv(OUT, index=False)
print(f"Wrote {len(df)} rows to {OUT}")
