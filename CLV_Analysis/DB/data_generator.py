import faker
from faker import Faker
import faker_commerce
import numpy as np
import random
import logging
from ..Logger.logger import CustomFormatter
from datetime import datetime, timedelta
import os
faker.locale = "en_US"


logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)

fake = Faker()
fake.add_provider(faker_commerce.Provider)

# Data Models


def generate_product(product_id):
    return {
        "product_id": product_id,
        "SKU": fake.unique.hexify(text='^^^^^', upper=True),
        "product_category": fake.ecommerce_category(),
        "producer_country": fake.country(),
        "price": round(random.uniform(1, 100), 2)
    }


def generate_customer(customer_id):
    start_date = datetime(1923, 1, 1)
    end_date = datetime(2005, 12, 31)
    random_date = fake.date_time_between_dates(start_date, end_date)
    return {
        "customer_id": customer_id,
        "customer_name": fake.first_name(),
        "customer_surname": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "country": fake.country(),
        "city": fake.city(),
        "address": fake.street_address(),
        "zip_code":  fake.zipcode(),
        "birthday":  random_date.strftime("%Y-%m-%d"),
        "gender": fake.random_element(elements=("Female", "Male",
                                                "Prefer Not To Say", "Other"))
    }


def generate_transaction(transaction_id):
    # Generate a random date between a specific date range
    start_date = datetime(2000, 1, 1)
    end_date = datetime(2023, 12, 31)
    random_date = fake.date_between_dates(start_date, end_date)

    return {
        "transaction_id": transaction_id,
        "date": random_date,
        "payment_method": fake.random_element(
            elements=("Credit Card", "Debit Card",
                      "Cash", "Online Transfer", "Check", "Mobile Payment")),
        "customer_id": np.random.randint(0, 3000)
    }


def generate_date(date_id):

    start_date = datetime(2000, 1, 1)
    current_date = start_date + timedelta(days=date_id)

    # Extract date components
    return {
        "date_id": date_id,
        "date": current_date.strftime("%Y-%m-%d"),
        "month": current_date.month,
        "month_name": current_date.strftime("%B"),
        "year": current_date.year,
        "quarter": (current_date.month - 1) // 3 + 1,
        "day_of_month": current_date.day,
        "day_of_year": current_date.timetuple().tm_yday,
        "day_of_week_number": current_date.weekday() + 1,
        "day_of_week_name": current_date.strftime("%A"),
        "week_of_year": current_date.isocalendar()[1],
        "week_of_month": (current_date.day - 1) // 7 + 1
    }


def generate_sales():
    return {
        "product_id": np.random.randint(0, 5000),
        "quantity": np.random.randint(1, 20),
    }
