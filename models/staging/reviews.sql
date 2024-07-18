WITH cleaned AS (
    SELECT
        review_id,
        ride_id,
        user_id,
        driver_id,
        CAST(rating as int) AS rating,
        comment,
        CAST(created_at AS DATE) AS created_at
    FROM {{ ref('reviews') }}
    WHERE
        review_id IS NOT NULL
        AND ride_id IS NOT NULL
        AND user_id IS NOT NULL
        AND driver_id IS NOT NULL
        AND rating IS NOT NULL
        AND created_at IS NOT NULL
)

SELECT * from cleaned