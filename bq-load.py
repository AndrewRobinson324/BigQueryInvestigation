# modules
from google.cloud import bigquery
import os

client = bigquery.Client(project='etl-pipeline-495914')
target_table = 'etl-pipeline-495914.sample_dataset.city_house_prices1988-1999'

job_config = bigquery.LoadJobConfig(

    skip_leading_rows=1,
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE

)

# file vars
cur_path = os.getcwd()
file = 'housing_1988-1999.csv'
file_path = os.path.join(cur_path, file)


with open(file_path, 'rb') as source_file:
    job = client.load_table_from_file(source_file, target_table, job_config=job_config)

job.result()  # Waits for the job to complete.



destination_table = client.get_table(target_table)
print(f"Loaded {destination_table.num_rows} rows to {target_table}")