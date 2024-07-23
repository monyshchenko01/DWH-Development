WITH cleaned AS (
    SELECT
        payment_id,
        ride_id,
        CAST(amount as DECIMAL(10, 2)),
        payment_method,
        card_number,
        CAST(paid_at AS DATE)
    FROM {{ ref('raw_payments') }}
    WHERE
        payment_id IS NOT NULL
        AND ride_id IS NOT NULL
        AND amount IS NOT NULL
        AND payment_method IS NOT NULL
        AND card_number IS NOT NULL
        AND paid_at IS NOT NULL
)

SELECT * FROM cleaned