SELECT * FROM yellow_taxi_data;
SELECT * FROM zones;

SELECT * FROM yellow_taxi_data limit 100;

SELECT 
tpep_pickup_datetime,
tpep_dropoff_datetime,
total_amount,
CONCAT(zpu."Borough",'/', zpu."Zone") AS "pick_up_loc",
CONCAT(zdo."Borough",'/', zdo."Zone") AS "drop_off_loc"
FROM 
yellow_taxi_data t,
zones zpu,
zones zdo
WHERE 
t."PULocationID"=zpu."LocationID" AND
t."DOLocationID"=zdo."LocationID"
LIMIT 100;