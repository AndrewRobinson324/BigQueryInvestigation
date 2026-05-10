# BigQuery Investigation

A small project I put together while learning how data moves from a traditional database into the cloud. I wanted to see the whole picture, not just write queries, but actually **pull data**, **shape it**, and **land it somewhere I could analyze it again**, which is how I ended up wiring MySQL, Python/pandas, and Google BigQuery into one flow.

## What I set out to do

I was curious what it feels like to build a **real-ish ETL pipeline** without a fancy orchestration tool: connect to the database I use for coursework, run transformations that mean something to me (like summarizing movies by year or tagging ratings), and finally **load the results into BigQuery** so I could query them like any other dataset.

Along the way I wanted to get comfortable with **BigQuery itself** projects, datasets, tables, load jobs, and how CSV exports behave once they hit the cloud.

## How the pieces fit together

**Extract:** I used Python with `mysql.connector`, reading connection defaults from my local MySQL options file (`~/.my.cnf`), so I wasn’t hard-coding passwords into the repo.

**Transform:** I used **pandas** for some basic transformations (was not the aim of my project) for example aggregating or enriching data before export. Some transformations live in SQL (`GROUP BY`, averages), and others live in Python (bucketing years into rough “good / okay / bad” labels). Experimenting in both places helped me see where each approach feels natural.

**Load:** I used the **Google Cloud BigQuery** Python client to load CSV files into tables under my project (for example datasets like `sample_dataset`). Figuring out **load job config**—CSV format, header rows, `autodetect`, and write disposition—was where a lot of the learning clicked.

```mermaid
flowchart LR
  subgraph extract [Extract]
    MySQL[(MySQL)]
  end
  subgraph transform [Transform]
    Pandas[pandas_and_SQL]
  end
  subgraph load [Load]
    BQ[(BigQuery)]
  end
  MySQL --> Pandas --> BQ
