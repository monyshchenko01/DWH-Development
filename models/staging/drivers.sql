WITH cleaned AS (
    SELECT
        driver_id,
        first_name,
        last_name,
        phone,
        email,
        license_number,
        CAST(car_id as int) AS car_id,
        CAST(city_id as int) AS city_id,
        password,
        CAST(created_at AS DATE) AS created_at
    FROM {{ ref('drivers') }}
    WHERE
        driver_id IS NOT NULL
        AND phone IS NOT NULL
        AND email IS NOT NULL
        AND car_id IS NOT NULL
        AND city_id IS NOT NULL
        AND created_at IS NOT NULL
)

SELECT * FROM cleaned