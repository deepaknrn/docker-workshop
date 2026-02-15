from tokenize import String
import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm
import click

"""ingest the data from the following 
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
Filename : Taxi Zone Lookup Table (CSV)
The file is placed in the path /SQL-refresher/taxi_zone_lookup.csv
"""

def ingest_data(url: str, engine, target_table: str, chunksize: int = 100000):
    """Ingest data into Postgres database"""

    dtype = {
    "LocationID": "int64",
    "Borough": "object",
    "Zone": "object",
    "service_zone": "object",
    }

    
    df = pd.read_csv(url,dtype=dtype)

    """Get the DDL Schema for the database """
    print(pd.io.sql.get_schema(df, name=target_table, con=engine))

    """Create an empty table with the name yellow_taxi_data but without any data , empty dataframe/table"""
    df.head(0).to_sql(name=target_table,con=engine,if_exists="replace")

    """Instead of inserting all the data at once, where the data is stored in the memory and then retrieved, iterate the data chunk by chunk and insert it"""
    """df_iter is an iterator object"""
    df_iter=pd.read_csv(url,dtype=dtype,iterator=True,chunksize=chunksize)

    for df_chunk in tqdm(df_iter):
       df_chunk.to_sql(name=target_table,con=engine,if_exists="append")
       

@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL username')
@click.option('--pg-password', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default='5432', help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--target-table', default='zones', help='Target table name')
@click.option('--chunksize', type=int, default=100000, help='Chunk size for data ingestion')

def main(pg_user, pg_password, pg_host, pg_port, pg_db, target_table, chunksize):
    """Ingest NYC taxi zone lookup data into PostgreSQL"""

    engine = create_engine(f'postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}')
    url = './taxi_zone_lookup.csv'

    ingest_data(
        url=url,
        engine=engine,
        target_table=target_table,
        chunksize=chunksize
    )

if __name__=="__main__":
    main()