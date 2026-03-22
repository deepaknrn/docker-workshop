{{ config(
    materialized='table'
) }}

with green_tripdata as (
    select *,'Green' as service_type from {{ ref('stg_greentrip_data_1') }}
),

yellow_tripdata as (
    select *,'Yellow' as service_type from {{ ref('stg_yellowtrip_data')}}
),

trips_union as 
(select * from green_tripdata 
--union all
--select * from yellow_tripdata
--Removing due to error 
--Database Error in model fact_trips (models/core/fact_trips.sql)
  --Queries in UNION ALL have mismatched column count; query 1 has 23 columns, query 2 has 18 columns at [27:1]
  --compiled code at target/run/taxi_rides_ny/models/core/fact_trips.sql
),

dim_zones as (
select * from {{ref('dim_zones')}}
where borough!='Unknown'
)


select trips_union.* from trips_union 
Inner join dim_Zones pickup_zone
on trips_union.pickup_location_id=pickup_zone.LocationID
inner join dim_zones dropoff_zone
on trips_union.dropoff_location_id=dropoff_zone.LocationID

