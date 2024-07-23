WITH cleaned AS (
    SELECT
        courier_id,
        first_name,
        last_name,
        phone,
        email,
        CAST(city_id as int),
        CAST(car_id as int),
        CAST(created_at AS DATE)
    FROM {{ ref('raw_couriers') }}
    WHERE
        courier_id IS NOT NULL
        AND phone IS NOT NULL
        AND email IS NOT NULL
        AND city_id IS NOT NULL
        AND car_id IS NOT NULL
        AND created_at IS NOT NULL
)

SELECT * FROM cleaned
