with cleaned as (
    SELECT
        name,
        oblast
    FROM {{ ref('raw_cities') }}
    WHERE
        name IS NOT NULL
        AND oblast IS NOT NULL
)

SELECT * FROM cleaned
