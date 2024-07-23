WITH cleaned AS (
    SELECT
        review_id,
        ride_id,
        user_id,
        driver_id,
        CAST(rating as int),
        comment,
        CAST(created_at AS DATE)
    FROM {{ ref('raw_reviews') }}
    WHERE
        review_id IS NOT NULL
        AND ride_id IS NOT NULL
        AND user_id IS NOT NULL
        AND driver_id IS NOT NULL
        AND rating IS NOT NULL
        AND created_at IS NOT NULL
)

SELECT * from cleaned