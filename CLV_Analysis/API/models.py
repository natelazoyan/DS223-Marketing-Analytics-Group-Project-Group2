from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Pydantic models for database entities


class ProductCreate(BaseModel):
    SKU: str
    product_category: str
    producer_country: str
    price: float


class ProductUpdate(BaseModel):
    SKU: Optional[str] = None
    product_category: Optional[str] = None
    producer_country: Optional[str] = None
    price: Optional[float] = None


class CustomerCreate(BaseModel):
    customer_name: str
    customer_surname: str
    email: str
    phone: str
    country: str
    city: str
    address: str
    zip_code: str
    birthday: datetime
    gender: str


class CustomerUpdate(BaseModel):
    customer_name: Optional[str] = None
    customer_surname: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    address: Optional[str] = None
    zip_code: Optional[str] = None
    birthday: Optional[datetime] = None
    gender: Optional[str] = None


class TransactionCreate(BaseModel):
    date: datetime
    payment_method: str
    customer_id: int


class TransactionUpdate(BaseModel):
    date: Optional[datetime] = None
    payment_method: Optional[str] = None
    customer_id: Optional[int] = None


class DateCreate(BaseModel):
    date: datetime
    month: int
    month_name: str
    year: int
    quarter: int
    day_of_month: int
    day_of_year: int
    day_of_week_number: int
    day_of_week_name: str
    week_of_year: int
    week_of_month: int


class DateUpdate(BaseModel):
    date: Optional[datetime] = None
    month: Optional[int] = None
    month_name: Optional[str] = None
    year: Optional[int] = None
    quarter: Optional[int] = None
    day_of_month: Optional[int] = None
    day_of_year: Optional[int] = None
    day_of_week_number: Optional[int] = None
    day_of_week_name: Optional[str] = None
    week_of_year: Optional[int] = None
    week_of_month: Optional[int] = None


class SalesFactCreate(BaseModel):
    transaction_id: int
    product_id: int
    customer_id: int
    quantity: int
    date_id: int


class SalesFactUpdate(BaseModel):
    transaction_id: Optional[int] = None
    product_id: Optional[int] = None
    customer_id: Optional[int] = None
    quantity: Optional[int] = None
    date_id: Optional[int] = None
