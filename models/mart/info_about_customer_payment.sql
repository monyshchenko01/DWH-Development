with customer_orders as (
    select
        c.customer_id,
        r.ride_id,
        count(r.ride_id) as number_of_rides
    from customers c
    left join rides r on c.customer_id = r.customer_id
    group by c.customer_id, r.ride_id
),
customer_payments as (
    select
        co.customer_id,
        p.amount,
        sum(p.amount) over (partition by co.customer_id order by p.amount) as total_amount_paid,
        lead(p.amount) over (partition by co.customer_id order by p.amount) as next_amount,
        lag(p.amount) over (partition by co.customer_id order by p.amount) as previous_amount
    from customer_orders co
    left join payments p on p.ride_id = co.ride_id
),
final as (
    select
        c.customer_id,
        c.first_name,
        c.last_name,
        co.number_of_rides,
        cp.amount,
        cp.total_amount_paid,
        cp.next_amount,
        cp.previous_amount
    from customers c
    left join customer_orders co on c.customer_id = co.customer_id
    left join customer_payments cp on c.customer_id = cp.customer_id
)
select * from final;
