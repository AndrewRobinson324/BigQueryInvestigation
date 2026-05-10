# modules
from google.cloud import bigquery

client = bigquery.Client(project='etl-pipeline-495914')

query = "SELECT * FROM `etl-pipeline-495914.sample_dataset.imdb_movies_with_ratings` LIMIT 5"

query_job = client.query(query)

results = query_job.result()

for r in results:
    print(r.year, r.title, r.genre,r.avg_vote,r.movie_rating)
