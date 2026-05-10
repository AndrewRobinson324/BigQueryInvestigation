#modules
import os 
import pandas as pd
import mysql.connector
from google.cloud import bigquery
from mysql.connector import errorcode
from pathlib import Path

#variables 
cur_path = os.getcwd()
load_file = 'mysql_export.csv'
load_file_path = os.path.join(cur_path, load_file)

proj = 'etl-pipeline-495914'
dataset = 'sample_dataset'
target_table = 'annual_movie_summary'
table_id = f'{proj}.{dataset}.{target_table}'

# data connections
conn = mysql.connector.connect(read_default_file=str(Path.home() / ".my.cnf"))
client = bigquery.Client(project=proj)

# create our sql extract query 
sql = """
SELECT year,count(imdb_title_id) as movie_count, avg(duration) as avg_movie_duration,avg(avg_vote) as avg_rating
FROM `u479841347_sql_course`.`imdb_movies`
GROUP BY year
"""

# extract data

df = pd.read_sql(sql, conn)

# transform data 

def year_rating(row):
    if row['avg_rating'] <= 5.8:
        return 'bad movie year'
    elif row['avg_rating'] <= 6.3:
        return 'okay movie year'
    elif row['avg_rating'] <= 10:
        return 'good movie year'

    else:
        return 'not rated'

df['year_rating'] = df.apply(year_rating, axis=1)

df.to_csv(load_file_path, index=False)
print(f"Wrote {len(df)} rows to {load_file_path}")

# load data to bigquery

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=True,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
)

with open(load_file_path, 'rb') as source_file:
    job = client.load_table_from_file(source_file, table_id, job_config=job_config)

job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)
print(f"Loaded {destination_table.num_rows} rows to {table_id}")