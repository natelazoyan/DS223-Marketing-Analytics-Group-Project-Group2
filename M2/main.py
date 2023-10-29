from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from etl.data_preparation.schema import Sale, Property, Customer, Agent, Transaction, Date
from models import (
    SalesFactCreate, SalesFactUpdate,
    PropertyCreate, PropertyUpdate,
    CustomerCreate, CustomerUpdate,
    AgentCreate, AgentUpdate,
    TransactionCreate, TransactionUpdate,
    DateCreate, DateUpdate
)

app = FastAPI()

DATABASE_URL = "sqlite:///temp.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        

###############################################################################################################

@app.post("/sales_fact/")
async def create_sales_fact(sales_fact: SalesFactCreate, db: Session = Depends(get_db)):
    db_sales_fact = Sale(**sales_fact.dict())
    db.add(db_sales_fact)
    db.commit()
    db.refresh(db_sales_fact)
    return db_sales_fact

@app.get("/sales_fact/")
async def read_sales_facts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sales_facts = db.query(Sale).offset(skip).limit(limit).all()
    return sales_facts

@app.get("/sales_fact/{sales_fact_id}")
async def read_sales_fact(sales_fact_id: int, db: Session = Depends(get_db)):
    sales_fact = db.query(Sale).filter(Sale.sales_id == sales_fact_id).first()
    if sales_fact is None:
        raise HTTPException(status_code=404, detail="Sales Fact not found")
    return sales_fact

@app.put("/sales_fact/{sales_fact_id}")
async def update_sales_fact(sales_fact_id: int, sales_fact: SalesFactUpdate, db: Session = Depends(get_db)):
    db_sales_fact = db.query(Sale).filter(Sale.sales_id == sales_fact_id).first()
    if db_sales_fact is None:
        raise HTTPException(status_code=404, detail="Sales Fact not found")
    for var, value in vars(sales_fact).items():
        setattr(db_sales_fact, var, value) if value is not None else None
    db.commit()
    db.refresh(db_sales_fact)
    return db_sales_fact

@app.delete("/sales_fact/{sales_fact_id}")
async def delete_sales_fact(sales_fact_id: int, db: Session = Depends(get_db)):
    db_sales_fact = db.query(Sale).filter(Sale.sales_id == sales_fact_id).first()
    if db_sales_fact is None:
        raise HTTPException(status_code=404, detail="Sales Fact not found")
    db.delete(db_sales_fact)
    db.commit()
    return {"message": "Sales Fact deleted successfully"}


###############################################################################################################

@app.post("/property/")
async def create_property(property: PropertyCreate, db: Session = Depends(get_db)):
    db_property = Property(**property.dict())
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property

@app.get("/property/")
async def read_properties(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    properties = db.query(Property).offset(skip).limit(limit).all()
    return properties

@app.get("/property/{property_id}")
async def read_property(property_id: int, db: Session = Depends(get_db)):
    property = db.query(Property).filter(Property.property_id == property_id).first()
    if property is None:
        raise HTTPException(status_code=404, detail="Property not found")
    return property

@app.put("/property/{property_id}")
async def update_property(property_id: int, property: PropertyUpdate, db: Session = Depends(get_db)):
    db_property = db.query(Property).filter(Property.property_id == property_id).first()
    if db_property is None:
        raise HTTPException(status_code=404, detail="Property not found")
    for var, value in vars(property).items():
        setattr(db_property, var, value) if value is not None else None
    db.commit()
    db.refresh(db_property)
    return db_property

@app.delete("/property/{property_id}")
async def delete_property(property_id: int, db: Session = Depends(get_db)):
    db_property = db.query(Property).filter(Property.property_id == property_id).first()
    if db_property is None:
        raise HTTPException(status_code=404, detail="Property not found")
    db.delete(db_property)
    db.commit()
    return {"message": "Property deleted successfully"}

###############################################################################################################

@app.post("/customer/")
async def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    db_customer = Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@app.get("/customer/")
async def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    customers = db.query(Customer).offset(skip).limit(limit).all()
    return customers

@app.get("/customer/{customer_id}")
async def read_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@app.put("/customer/{customer_id}")
async def update_customer(customer_id: int, customer: CustomerUpdate, db: Session = Depends(get_db)):
    db_customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    for var, value in vars(customer).items():
        setattr(db_customer, var, value) if value is not None else None
    db.commit()
    db.refresh(db_customer)
    return db_customer

@app.delete("/customer/{customer_id}")
async def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(db_customer)
    db.commit()
    return {"message": "Customer deleted successfully"}

###############################################################################################################

@app.post("/agent/")
async def create_agent(agent: AgentCreate, db: Session = Depends(get_db)):
    db_agent = Agent(**agent.dict())
    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)
    return db_agent

@app.get("/agent/")
async def read_agents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    agents = db.query(Agent).offset(skip).limit(limit).all()
    return agents

@app.get("/agent/{agent_id}")
async def read_agent(agent_id: int, db: Session = Depends(get_db)):
    agent = db.query(Agent).filter(Agent.agent_id == agent_id).first()
    if agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent

@app.put("/agent/{agent_id}")
async def update_agent(agent_id: int, agent: AgentUpdate, db: Session = Depends(get_db)):
    db_agent = db.query(Agent).filter(Agent.agent_id == agent_id).first()
    if db_agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    for var, value in vars(agent).items():
        setattr(db_agent, var, value) if value is not None else None
    db.commit()
    db.refresh(db_agent)
    return db_agent

@app.delete("/agent/{agent_id}")
async def delete_agent(agent_id: int, db: Session = Depends(get_db)):
    db_agent = db.query(Agent).filter(Agent.agent_id == agent_id).first()
    if db_agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    db.delete(db_agent)
    db.commit()
    return {"message": "Agent deleted successfully"}

###############################################################################################################

@app.post("/transaction/")
async def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    db_transaction = Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@app.get("/transaction/")
async def read_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    transactions = db.query(Transaction).offset(skip).limit(limit).all()
    return transactions

@app.get("/transaction/{transaction_id}")
def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@app.put("/transaction/{transaction_id}")
async def update_transaction(transaction_id: int, transaction: TransactionUpdate, db: Session = Depends(get_db)):
    db_transaction = db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    for var, value in vars(transaction).items():
        setattr(db_transaction, var, value) if value is not None else None
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@app.delete("/transaction/{transaction_id}")
async def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    db_transaction = db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    db.delete(db_transaction)
    db.commit()
    return {"message": "Transaction deleted successfully"}

###############################################################################################################

@app.post("/date/")
async def create_date(date: DateCreate, db: Session = Depends(get_db)):
    db_date = Date(**date.dict())
    db.add(db_date)
    db.commit()
    db.refresh(db_date)
    return db_date

@app.get("/date/")
async def read_dates(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dates = db.query(Date).offset(skip).limit(limit).all()
    return dates

@app.get("/date/{date_id}")
async def read_date(date_id: int, db: Session = Depends(get_db)):
    date = db.query(Date).filter(Date.date_id == date_id).first()
    if date is None:
        raise HTTPException(status_code=404, detail="Date not found")
    return date

@app.put("/date/{date_id}")
async def update_date(date_id: int, date: DateUpdate, db: Session = Depends(get_db)):
    db_date = db.query(Date).filter(Date.date_id == date_id).first()
    if db_date is None:
        raise HTTPException(status_code=404, detail="Date not found")
    for var, value in vars(date).items():
        setattr(db_date, var, value) if value is not None else None
    db.commit()
    db.refresh(db_date)
    return db_date

@app.delete("/date/{date_id}")
async def delete_date(date_id: int, db: Session = Depends(get_db)):
    db_date = db.query(Date).filter(Date.date_id == date_id).first()
    if db_date is None:
        raise HTTPException(status_code=404, detail="Date not found")
    db.delete(db_date)
    db.commit()
    return {"message": "Date deleted successfully"}

###############################################################################################################
