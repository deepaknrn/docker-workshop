from tokenize import String
import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm
import click

"""ingest the data from the following sources:
https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet
https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv
The file is placed in the path /homework1_docker_sql/
"""

def ingest_data1(url: str, engine, target_table: str, chunksize: int = 100000):
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

    """Create an empty table with the name taxi_zone_data but without any data , empty dataframe/table"""
    df.head(0).to_sql(name=target_table,con=engine,if_exists="replace")

    """Instead of inserting all the data at once, where the data is stored in the memory and then retrieved, iterate the data chunk by chunk and insert it"""
    """df_iter is an iterator object"""
    df_iter=pd.read_csv(url,dtype=dtype,iterator=True,chunksize=chunksize)

    for df_chunk in tqdm(df_iter):
       df_chunk.to_sql(name=target_table,con=engine,if_exists="append")

def ingest_data2(url: str, engine, target_table: str, chunksize: int = 100000):
    """Ingest data into Postgres database"""

    dtype = {
    'VendorID': 'Int32',
    'store_and_fwd_flag': 'string',
    'RatecodeID': 'float64',
    'PULocationID': 'Int32',
    'DOLocationID': 'Int32',
    'passenger_count': 'float64',
    'trip_distance': 'float64',
    'fare_amount': 'float64',
    'extra': 'float64',
    'mta_tax': 'float64',
    'tip_amount': 'float64',
    'tolls_amount': 'float64',
    'ehail_fee': 'float64',
    'improvement_surcharge': 'float64',
    'total_amount': 'float64',
    'payment_type': 'float64',
    'trip_type': 'float64',
    'congestion_surcharge': 'float64',
    'cbd_congestion_fee': 'float64'
    }

    df = pd.read_parquet(url)
    df = df.astype(dtype)

    df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'], errors='coerce')
    df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'], errors='coerce')

    """Get the DDL Schema for the database """
    print(pd.io.sql.get_schema(df, name=target_table, con=engine))

    """Create an empty table with the name green_trip_data but without any data , empty dataframe/table"""
    df.head(0).to_sql(name=target_table,con=engine,if_exists="replace")

    """Instead of inserting all the data at once, where the data is stored in the memory and then retrieved, iterate the data chunk by chunk and insert it"""
    """df_iter is an iterator object"""
    df_iter = (df[i:i+chunksize] for i in range(0, len(df), chunksize))

    for df_chunk in tqdm(df_iter):
       df_chunk.to_sql(name=target_table,con=engine,if_exists="append") 

@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL username')
@click.option('--pg-password', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default='5432', help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--target-table1', default='taxi_zone_data', help='Target table name')
@click.option('--target-table2', default='green_trip_data', help='Target table name')
@click.option('--chunksize', type=int, default=100000, help='Chunk size for data ingestion')

def main(pg_user, pg_password, pg_host, pg_port, pg_db, target_table1, target_table2, chunksize):
    """Ingest data into PostgreSQL from multiple sources"""

    engine = create_engine(f'postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}')
    url1 = './taxi_zone_lookup.csv'
    url2 = './green_tripdata_2025-11.parquet'

    ingest_data1(
        url=url1,
        engine=engine,
        target_table=target_table1,
        chunksize=chunksize
    )

    ingest_data2(
        url=url2,
        engine=engine,
        target_table=target_table2,
        chunksize=chunksize
    )

if __name__=="__main__":
    main()