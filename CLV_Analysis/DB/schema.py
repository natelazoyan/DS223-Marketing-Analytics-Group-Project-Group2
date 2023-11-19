import logging
from ..Logger.logger import CustomFormatter
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

engine = create_engine('sqlite:///temp.db')
Base = declarative_base()


class Product(Base):
    """Represents a product in the company."""
    __tablename__ = "product"

    product_id = Column(Integer, primary_key=True)
    SKU = Column(String)
    product_category = Column(String)
    producer_country = Column(String)
    price = Column(Float)


class Customer(Base):
    """Represents a customer in the company."""
    __tablename__ = "customer"

    customer_id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    customer_surname = Column(String)
    email = Column(String)
    phone = Column(String)
    country = Column(String)
    city = Column(String)
    address = Column(String)
    zip_code = Column(String)
    birthday = Column(DateTime)
    gender = Column(String)


class Transaction(Base):
    """Represents a transaction in the company."""
    __tablename__ = "transactions"

    transaction_id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    payment_method = Column(String)

    customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    customers = relationship("Customer", backref="transactions")


class Date(Base):
    """Represents a date in the company."""
    __tablename__ = "date"

    date_id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    month = Column(Integer)
    month_name = Column(String)
    year = Column(Integer)
    quarter = Column(Integer)
    day_of_month = Column(Integer)
    day_of_year = Column(Integer)
    day_of_week_number = Column(Integer)
    day_of_week_name = Column(String)
    week_of_year = Column(Integer)
    week_of_month = Column(Integer)


class Sale(Base):
    """Represents a sale in the company."""
    __tablename__ = "sales_fact"

    sales_id = Column(Integer, primary_key=True)
    transaction_id = Column(Integer, ForeignKey('transactions.transaction_id'))
    product_id = Column(Integer, ForeignKey('product.product_id'))
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    quantity = Column(Integer)
    date_id = Column(Integer, ForeignKey('date.date_id'))

    transaction = relationship("Transaction")
    product = relationship("Product")
    customer = relationship("Customer")
    date = relationship("Date")


Base.metadata.create_all(engine)
