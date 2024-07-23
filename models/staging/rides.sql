WITH cleaned AS (
    SELECT
        ride_id,
        customer_id,
        driver_id,
        pickup_location,
        CAST(pickup_city_id as int),
        dropoff_location,
        CAST(dropoff_city_id as int),
        CAST(requested_at AS DATE),
        CAST(completed_at AS DATE)
    FROM {{ ref('raw_rides') }}
    WHERE
        ride_id IS NOT NULL
        AND customer_id IS NOT NULL
        AND driver_id IS NOT NULL
        AND pickup_city_id IS NOT NULL
        AND dropoff_city_id IS NOT NULL
        AND requested_at IS NOT NULL
        AND completed_at IS NOT NULL
)

SELECT * FROM cleaned