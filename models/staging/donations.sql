WITH cleaned AS (
    SELECT
        donation_id,
        customer_id,
        CAST(amount as DECIMAL(10, 2)),
        payment_method,
        card_number,
        comment,
        CAST(donated_at AS DATE)
    FROM {{ ref('raw_donations') }}
    WHERE
        donation_id IS NOT NULL
        AND customer_id IS NOT NULL
        AND amount IS NOT NULL
        AND payment_method IS NOT NULL
        AND card_number IS NOT NULL
        AND donated_at IS NOT NULL
)

SELECT * FROM cleaned