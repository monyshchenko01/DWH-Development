import csv
import uuid
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Define file paths
cities_file = 'cities.csv'
customers_file = 'customers.csv'
cars_file = 'cars.csv'
drivers_file = 'drivers.csv'
rides_file = 'rides.csv'
payments_file = 'payments.csv'
reviews_file = 'reviews.csv'
couriers_file = 'couriers.csv'
deliveries_file = 'deliveries.csv'
shifts_file = 'shifts.csv'
donations_file = 'donations.csv'

# CITIES
print("Generating Cities data...")
with open(cities_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'oblast'])
    for _ in range(100000):
        writer.writerow([fake.city(), fake.country()])
print(f"Data written to {cities_file}")

# CUSTOMERS
print("Generating Customers data...")
with open(customers_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['customer_id', 'first_name', 'last_name', 'email', 'phone', 'password', 'city_id', 'created_at'])
    for _ in range(100000):
        writer.writerow([str(uuid.uuid4()), fake.first_name(), fake.last_name(), fake.unique.email(), fake.unique.phone_number(), fake.password(),
                         random.randint(1, 100), fake.date_time_between(start_date='-2y', end_date='now').strftime('%Y-%m-%d')])
print(f"Data written to {customers_file}")

# CARS
print("Generating Cars data...")
brends = ['Ford', 'Nissan', 'Toyota', 'Volkswagen', 'Bugatti', 'BMW', 'Audi', 'Mercedes', 'Jaguar', 'Subaru', 'Honda', 'Hyundai',
          'Tesla', 'Skoda', 'Suzuki', 'Volvo', 'Kia', 'Mazda', 'Lifan', 'Opel', 'Mitsubishi', 'Fiat', 'Lexus', 'Ferrari', 'Reno',
          'Bentley', 'Scania', 'Seat', 'Infiniti', 'Chevrolet']
car_type = ['Standard', 'Comfort', 'Business', 'Delivery', 'Prime', 'Express', 'Inclusive', 'Green', 'Wagon', 'Kids', 'Minibus']

with open(cars_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['car_number', 'car_brend', 'car_model', 'license_plate', 'color', 'car_type', 'year_produced'])
    for _ in range(100000):
        writer.writerow([fake.license_plate(), random.choice(brends), fake.word(), fake.unique.license_plate(),
                         fake.color_name(), random.choice(car_type), fake.random_int(min=1980, max=2023)])
print(f"Data written to {cars_file}")

# DRIVERS
print("Generating Drivers data...")
existing_cars_ids = list(range(1, 100001))  # Simulate car IDs for the example

with open(drivers_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['driver_id', 'first_name', 'last_name', 'phone', 'email', 'license_number', 'car_id', 'city_id', 'password', 'created_at'])
    for _ in range(100000):
        writer.writerow([str(uuid.uuid4()), fake.first_name(), fake.last_name(), fake.unique.phone_number(), fake.unique.email(), fake.unique.license_plate(),
                         random.choice(existing_cars_ids), random.randint(1, 100), fake.password(),
                         fake.date_time_between(start_date='-2y', end_date='now').strftime('%Y-%m-%d')])
print(f"Data written to {drivers_file}")

# RIDES
print("Generating Rides data...")
existing_customer_ids = list(range(1, 100001))  # Simulate customer IDs for the example
existing_driver_ids = list(range(1, 100001))  # Simulate driver IDs for the example

with open(rides_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ride_id', 'customer_id', 'driver_id', 'pickup_location', 'pickup_city_id', 'dropoff_location', 'dropoff_city_id', 'status', 'requested_at', 'completed_at'])
    for _ in range(100000):
        writer.writerow([str(uuid.uuid4()), random.choice(existing_customer_ids), random.choice(existing_driver_ids), fake.address(),
                         random.randint(1, 100), fake.address(), random.randint(1, 100), random.choice(['requested', 'completed']),
                         fake.date_time_between(start_date='-2y', end_date='now').strftime('%Y-%m-%d'),
                         fake.date_time_between(start_date='-2y', end_date='now').strftime('%Y-%m-%d')])
print(f"Data written to {rides_file}")

# PAYMENTS
print("Generating Payments data...")
existing_ride_ids = list(range(1, 100001))  # Simulate ride IDs for the example

with open(payments_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['payment_id', 'ride_id', 'amount', 'payment_method', 'card_number', 'paid_at'])
    for _ in range(100000):
        writer.writerow([str(uuid.uuid4()), random.choice(existing_ride_ids), round(random.uniform(10.0, 100.0), 2),
                         random.choice(['Credit Card', 'PayPal']), fake.credit_card_number(),
                         fake.date_time_between(start_date='-2y', end_date='now').strftime('%Y-%m-%d')])
print(f"Data written to {payments_file}")

# REVIEWS
print("Generating Reviews data...")
with open(reviews_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['review_id', 'ride_id', 'user_id', 'driver_id', 'rating', 'comment', 'created_at'])
    for _ in range(100000):
        writer.writerow([str(uuid.uuid4()), random.choice(existing_ride_ids), random.choice(existing_customer_ids), random.choice(existing_driver_ids),
                         random.randint(1, 5), fake.text(max_nb_chars=200), fake.date_time_between(start_date='-2y', end_date='now').strftime('%Y-%m-%d')])
print(f"Data written to {reviews_file}")

# COURIERS
print("Generating Couriers data...")
existing_city_ids = list(range(1, 101))  # Simulate city IDs for the example

with open(couriers_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['courier_id', 'first_name', 'last_name', 'phone', 'email', 'city_id', 'car_id', 'created_at'])
    for _ in range(100000):
        writer.writerow([str(uuid.uuid4()), fake.first_name(), fake.last_name(), fake.unique.phone_number(), fake.unique.email(),
                         random.choice(existing_city_ids), random.choice(existing_cars_ids), fake.date_time_between(start_date='-2y', end_date='now').strftime('%Y-%m-%d')])
print(f"Data written to {couriers_file}")

# DELIVERIES
print("Generating Deliveries data...")
existing_couriers_ids = list(range(1, 100001))  # Simulate courier IDs for the example

with open(deliveries_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['delivery_id', 'customer_id', 'courier_id', 'pickup_location', 'pickup_city_id', 'dropoff_location', 'dropoff_city_id', 'status', 'requested_at', 'completed_at'])
    for _ in range(100000):
        writer.writerow([str(uuid.uuid4()), random.choice(existing_customer_ids), random.choice(existing_couriers_ids), fake.address(),
                         random.randint(1, 100), fake.address(), random.randint(1, 100), random.choice(['requested', 'completed']),
                         fake.date_time_between(start_date='-2y', end_date='now').strftime('%Y-%m-%d'),
                         fake.date_time_between(start_date='-2y', end_date='now').strftime('%Y-%m-%d')])
print(f"Data written to {deliveries_file}")

# SHIFTS
print("Generating Shifts data...")
with open(shifts_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['shift_id', 'driver_id', 'courier_id', 'start_time', 'end_time'])
    for _ in range(100000):
        writer.writerow([str(uuid.uuid4()), random.choice(existing_driver_ids), random.choice(existing_couriers_ids),
                         fake.date_time_between(start_date='-2y', end_date='now').strftime('%Y-%m-%d'),
                         fake.date_time_between(start_date='-2y', end_date='now').strftime('%Y-%m-%d')])
print(f"Data written to {shifts_file}")

# DONATIONS
print("Generating Donations data...")
with open(donations_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['donation_id', 'customer_id', 'amount', 'payment_method', 'card_number', 'comment', 'donated_at'])
    for _ in range(100000):
        writer.writerow([str(uuid.uuid4()), random.choice(existing_customer_ids), round(random.uniform(10.0, 1000.0), 2),
                         random.choice(['Credit Card', 'PayPal']), fake.credit_card_number(),
                         fake.text(max_nb_chars=200), fake.date_time_between(start_date='-2y', end_date='now').strftime('%Y-%m-%d')])
print(f"Data written to {donations_file}")

print("Data generation complete.")
