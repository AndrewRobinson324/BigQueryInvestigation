# BigQuery Investigation

Python utilities for a learning ETL flow: extract data from **MySQL**, transform with **pandas**, and load or query **Google BigQuery**.

## Prerequisites

- Python **3.12** (`.python-version` is set for pyenv).
- MySQL options file **`~/.my.cnf`** used by `mysql.connector.connect(read_default_file=...)`.
- Google Cloud credentials with BigQuery access for BigQuery scripts (`gcloud auth application-default login` or a service account).

```bash
pip install -r requirements.txt
```

## Scripts

| Script | Purpose |
|--------|---------|
| `mysql-connect.py` | Test MySQL using `~/.my.cnf`. |
| `mysql-query.py` | Sample query against `imdb_movies`. |
| `mysql-export-imdb-csv.py` | Export `imdb_movies` with computed `movie_rating` from `avg_vote`. |
| `pandas-dtypes.py` | Example `pandas.read_sql`. |
| `pandas-new-col-sql.py` | CSV export with SQL-side `movie_rating`. |
| `pandas-transform.py` | Export `city_house_prices` for **1988–1999** to `housing_1988-1999.csv`. |
| `full-etl.py` | Aggregate movies by year, add `year_rating`, export CSV, load BigQuery `annual_movie_summary`. |
| `bq-conn.py` | Sample query against `sample_dataset.imdb_movies_with_ratings`. |
| `bq-load.py` | Load housing CSV into `sample_dataset.city_house_prices1988-1999`. |

Update database names and BigQuery `project.dataset.table` ids inside each script to match your environment.

## Notes

- Generated CSV outputs are gitignored; reproduce them with the scripts above.
- Do not commit secrets (`~/.my.cnf`, service-account JSON).
