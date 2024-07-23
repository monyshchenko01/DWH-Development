WITH cleaned AS (
    SELECT
        car_number,
        car_brend,
        car_model,
        license_plate,
        color,
        car_type,
        CAST(year_produced as int)
    FROM {{ ref('raw_cars') }}
    WHERE
        car_number IS NOT NULL
        AND car_brend IS NOT NULL
        AND license_plate IS NOT NULL
        AND car_type IS NOT NULL
        AND year_produced IS NOT NULL
)

SELECT * FROM cleaned
