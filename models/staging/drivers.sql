WITH cleaned AS (
    SELECT
        driver_id,
        first_name,
        last_name,
        phone,
        email,
        license_number,
        CAST(car_id as int),
        CAST(city_id as int),
        password,
        CAST(created_at AS DATE)
    FROM {{ ref('raw_drivers') }}
    WHERE
        driver_id IS NOT NULL
        AND phone IS NOT NULL
        AND email IS NOT NULL
        AND car_id IS NOT NULL
        AND city_id IS NOT NULL
        AND created_at IS NOT NULL
)

SELECT * FROM cleaned