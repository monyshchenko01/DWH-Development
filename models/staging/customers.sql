with cleaned as (
    SELECT
        customer_id,
        first_name,
        last_name,
        email,
        phone,
        password,
        CAST(city_id as int) AS city_id,
        CAST(created_at AS DATE) AS created_at
    FROM {{ ref('customers') }}
    WHERE
        customer_id IS NOT NULL
        AND email IS NOT NULL
        AND phone IS NOT NULL
        AND city_id IS NOT NULL
        AND created_at IS NOT NULL
)

SELECT * FROM cleaned
