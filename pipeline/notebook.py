#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.__file__
"""This pandas is coming from the virtual environment in the host machine 
: /workspaces/docker-workshop/pipeline/.venv/lib/python3.13/site-packages/pandas/__init__.py"""


# In[3]:


import pandas as pd

# Read a sample of the data
"""github url link where files are available : https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/yellow/ """
prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
df = pd.read_csv(prefix + '/yellow_tripdata_2021-01.csv.gz', nrows=100)

# Display first rows
df.head()


# In[11]:


# Check data types
df.dtypes


# In[12]:


# Check data shape
df.shape


# In[13]:


#Check number of records
len(df)


# In[14]:


df['tpep_pickup_datetime']


# In[4]:


dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

df = pd.read_csv(
    prefix + '/yellow_tripdata_2021-01.csv.gz',
    nrows=100,
    dtype=dtype,
    parse_dates=parse_dates
)


# In[5]:


# Display first rows
df.head()


# In[2]:


"""install the sqlalchemy"""
"""using pandas to interact with different databases (mysql,postgresql), insert data etc this library sqlalchemy will be used"""
get_ipython().system('uv add sqlalchemy')


# In[4]:


get_ipython().system('uv add sqlalchemy psycopg2-binary')
""" If this is not installed , then you will get an error when create_engine is executed for sql_alchemy """


# In[6]:


"""Using sql alchemy connect to postgre SQL database"""
from sqlalchemy import create_engine
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')


# In[17]:


"""Get the DDL Schema for the database """
print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))


# In[18]:


"""Create an empty table with the name yello_taxi_data but without any data , empty dataframe/table"""
df.head(0).to_sql(name="yellow_taxi_data",con=engine,if_exists="replace")


# In[8]:


"""Instead of inserting all the data at once, where the data is stored in the memory and then retrieved, iterate the data chunk by chunk and insert it"""
"""df_iter is an iterator object"""
df_iter=pd.read_csv(prefix + '/yellow_tripdata_2021-01.csv.gz',dtype=dtype,parse_dates=parse_dates,iterator=True,chunksize=100000)
df_iter 


# In[20]:


df=next(df_iter)
df
"""Get each row from the dataframe object"""


# In[22]:


for df in df_iter:
    print(len(df))
    """It will take 12 chunks of data for insert"""


# In[23]:


get_ipython().system('uv add tqdm')
"""to check the progress of insert via chunks"""


# In[9]:


from tqdm.auto import tqdm
for df_chunk in tqdm(df_iter):
    df_chunk.to_sql(name="yellow_taxi_data",con=engine,if_exists="append")
    """It will take 12 chunks of data for insert"""


# In[ ]:




