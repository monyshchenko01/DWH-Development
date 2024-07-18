with car_usage as (
    select
        cr.car_id,
        count(ri.ride_id) over (partition by cr.car_id) as number_of_rides
    from cars cr
    left join rides ri on cr.car_id = ri.driver_id
),
car_reviews as (
    select
        cr.car_id,
        avg(rv.rating) over (partition by cr.car_id) as avg_rating
    from cars cr
    left join drivers dr on cr.car_id = dr.car_id
    left join reviews rv on dr.driver_id = rv.driver_id
)
select
    cr.car_id,
    cr.car_brend,
    cr.car_model,
    car_usage.number_of_rides,
    car_reviews.avg_rating
from cars cr
left join car_usage on cr.car_id = car_usage.car_id
left join car_reviews on cr.car_id = car_reviews.car_id;
