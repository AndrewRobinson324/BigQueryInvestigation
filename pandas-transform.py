from pathlib import Path
import mysql.connector
import pandas as pd


DB = "u479841347_sql_course"
TABLE = "city_house_prices"
YEAR_COL = "Date"  # change if your column is sale_year, yr, etc.
OUT = Path(__file__).resolve().parent / "housing_1988-1999.csv"

conn = mysql.connector.connect(read_default_file=str(Path.home() / ".my.cnf"))
query = f"""
SELECT *
FROM `{DB}`.`{TABLE}`
WHERE `{YEAR_COL}` BETWEEN 1988 AND 1999
"""

df = pd.read_sql(query, conn)
conn.close()
df.to_csv(OUT, index=False)
print(f"Wrote {len(df)} rows to {OUT}")