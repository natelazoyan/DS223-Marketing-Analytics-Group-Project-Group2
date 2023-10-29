from pydantic import BaseModel
from typing import Optional
from datetime import datetime



# Pydantic models for database entities
class PropertyCreate(BaseModel):
    property_type: str
    country: str
    city: str
    street: str
    building_number: int
    square_footage: int
    number_of_bedrooms: int
    number_of_bathrooms: int
    year_built: int

class PropertyUpdate(BaseModel):
    property_type: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    street: Optional[str] = None
    building_number: Optional[int] = None
    square_footage: Optional[int] = None
    number_of_bedrooms: Optional[int] = None
    number_of_bathrooms: Optional[int] = None
    year_built: Optional[int] = None

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

class AgentCreate(BaseModel):
    agent_name: str
    agent_surname: str
    email: str
    phone: str
    experience_years: int

class AgentUpdate(BaseModel):
    agent_name: Optional[str] = None
    agent_surname: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    experience_years: Optional[int] = None

class TransactionCreate(BaseModel):
    transaction_amount: float
    transaction_date: datetime
    payment_method: str

class TransactionUpdate(BaseModel):
    transaction_amount: Optional[float] = None
    transaction_date: Optional[datetime] = None
    payment_method: Optional[str] = None

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
    property_id: int
    customer_id: int
    agent_id: int
    date_id: int

class SalesFactUpdate(BaseModel):
    transaction_id: Optional[int] = None
    property_id: Optional[int] = None
    customer_id: Optional[int] = None
    agent_id: Optional[int] = None
    date_id: Optional[int] = None