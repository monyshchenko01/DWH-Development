WITH cleaned AS (
    SELECT
        courier_id,
        first_name,
        last_name,
        phone,
        email,
        CAST(city_id as int) AS city_id,
        CAST(car_id as int) AS car_id,
        CAST(created_at AS DATE) AS created_at
    FROM {{ ref('couriers') }}
    WHERE
        courier_id IS NOT NULL
        AND phone IS NOT NULL
        AND email IS NOT NULL
        AND city_id IS NOT NULL
        AND car_id IS NOT NULL
        AND created_at IS NOT NULL
)

SELECT * FROM cleaned
