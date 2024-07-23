WITH cleaned AS (
    SELECT
        shift_id,
        driver_id,
        courier_id,
        CAST(start_time AS TIMESTAMP),
        CAST(end_time AS TIMESTAMP)
    FROM {{ ref('raw_shifts') }}
    WHERE
        shift_id IS NOT NULL
        AND driver_id IS NOT NULL
        AND courier_id IS NOT NULL
        AND start_time IS NOT NULL
        AND end_time IS NOT NULL
)

SELECT * FROM cleaned