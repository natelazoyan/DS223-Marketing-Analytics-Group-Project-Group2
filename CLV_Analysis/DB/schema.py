import logging
import os

from ..Logger.logger import CustomFormatter

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
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

class Property(Base):
    """Represents a property in the real estate system."""
    __tablename__ = "property"

    property_id = Column(Integer, primary_key=True)
    property_type = Column(String)
    country = Column(String)
    city = Column(String)
    street = Column(String)
    building_number = Column(Integer)
    square_footage = Column(Integer)
    number_of_bedrooms = Column(Integer)
    number_of_bathrooms = Column(Integer)
    year_built = Column(Integer)

class Customer(Base):
    """Represents a customer in the real estate system."""
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

class Agent(Base):
    """Represents an agent in the real estate system."""
    __tablename__ = "agent"

    agent_id = Column(Integer, primary_key=True)
    agent_name = Column(String)
    agent_surname = Column(String)
    email = Column(String)
    phone = Column(String)
    experience_years = Column(Integer)

class Transaction(Base):
    """Represents a transaction in the real estate system."""
    __tablename__ = "transactions"

    transaction_id = Column(Integer, primary_key=True)
    transaction_amount = Column(Float)
    transaction_date = Column(DateTime)
    payment_method = Column(String)

class Date(Base):
    """Represents a date in the real estate system."""
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
    """Represents a sale in the real estate system."""
    __tablename__ = "sales_fact"

    sales_id = Column(Integer, primary_key=True)
    transaction_id = Column(Integer, ForeignKey('transactions.transaction_id'))
    property_id = Column(Integer, ForeignKey('property.property_id'))
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    agent_id = Column(Integer, ForeignKey('agent.agent_id'))
    date_id = Column(Integer, ForeignKey('date.date_id'))

    transaction = relationship("Transaction")
    propertyy = relationship("Property")
    customer = relationship("Customer")
    agent = relationship("Agent")
    date = relationship("Date")

Base.metadata.create_all(engine)