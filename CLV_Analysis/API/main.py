from fastapi import FastAPI, HTTPException
from ..DB import sql_interactions
from .models import (
    SalesFactCreate, SalesFactUpdate,
    ProductCreate, ProductUpdate,
    CustomerCreate, CustomerUpdate,
    TransactionCreate, TransactionUpdate,
    DateCreate, DateUpdate
)

app = FastAPI()

# Sales Fact API Methods


@app.post("/sales_fact/")
async def create_sales_fact(insert_values: SalesFactCreate):
    try:
        db_sales = sql_interactions.SqlHandler.insert_by_id(
            insert_values,
            db_name="temp.db", table_name="sales_fact"
        )
        return db_sales
    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}"}


@app.get("/sales_fact/")
async def select_sales_facts(start_id: int, head: int):
    try:
        db_sales_fact = sql_interactions.SqlHandler.select_many(
            start_id, head,
            db_name="temp.db", table_name="sales_fact", table_id="sales_id"
        )
        return db_sales_fact
    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}"}


@app.get("/sales_fact/{sales_fact_id}")
async def select_sales_fact(sales_fact_id: int):
    try:
        db_sales_fact = sql_interactions.SqlHandler.select_by_id(
            sales_fact_id,
            db_name="temp.db", table_name='sales_fact', table_id="sales_id"
        )
        return db_sales_fact
    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}"}


@app.put("/sales_fact/{sales_fact_id}")
async def update_sales_fact(row_id: int, update_data: SalesFactUpdate):
    try:
        result = sql_interactions.SqlHandler.update_by_id(
            row_id, update_data,
            db_name="temp.db", table_name="sales_fact", table_id="sales_id"
        )
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error: {str(e)}"
        )


@app.delete("/sales_fact/{sales_fact_id}")
async def delete_sales_fact(sales_fact_id: int):
    try:
        db_sales_fact = sql_interactions.SqlHandler.delete_by_id(
            sales_fact_id,
            db_name="temp.db", table_name='sales_fact', table_id="sales_id"
        )
        return db_sales_fact
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error: {str(e)}"
        )

# Product API Methods


@app.post("/product/")
async def create_product(insert_values: ProductCreate):
    try:
        db_product = sql_interactions.SqlHandler.insert_by_id(
            insert_values,
            db_name="temp.db", table_name="product"
        )
        return db_product
    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}"}


@app.get("/product/")
async def select_products(start_id: int, head: int):
    try:
        db_products = sql_interactions.SqlHandler.select_many(
            start_id, head,
            db_name="temp.db", table_name="product", table_id="product_id"
        )
        return db_products
    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}"}


@app.get("/product/{product_id}")
async def select_product(product_id: int):
    try:
        db_product = sql_interactions.SqlHandler.select_by_id(
            product_id,
            db_name="temp.db", table_name='product', table_id="product_id"
        )
        return db_product
    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}"}


@app.put("/product/{product_id}")
async def update_product(row_id: int, update_data: ProductUpdate):
    try:
        result = sql_interactions.SqlHandler.update_by_id(
            row_id, update_data,
            db_name="temp.db", table_name="product", table_id="product_id"
        )
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error: {str(e)}"
        )


@app.delete("/product/{product_id}")
async def delete_product(product_id: int):
    try:
        db_product = sql_interactions.SqlHandler.delete_by_id(
            product_id,
            db_name="temp.db", table_name='product', table_id="product_id"
        )
        return db_product
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error: {str(e)}"
        )

# Customer API Methods


@app.post("/customer/")
async def create_customer(insert_values: CustomerCreate):
    try:
        db_customer = sql_interactions.SqlHandler.insert_by_id(
            insert_values,
            db_name="temp.db", table_name="customer"
        )
        return db_customer
    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}"}


@app.get("/customer/")
async def select_customers(start_id: int, head: int):
    try:
        db_customers = sql_interactions.SqlHandler.select_many(
            start_id, head,
            db_name="temp.db", table_name="customer", table_id="customer_id"
        )
        return db_customers
    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}"}


@app.get("/customer/{customer_id}")
async def select_customer(customer_id: int):
    try:
        db_customer = sql_interactions.SqlHandler.select_by_id(
            customer_id,
            db_name="temp.db", table_name='customer', table_id="customer_id"
        )
        return db_customer
    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}"}


@app.put("/customer/{customer_id}")
async def update_customer(row_id: int, update_data: CustomerUpdate):
    try:
        result = sql_interactions.SqlHandler.update_by_id(
            row_id, update_data,
            db_name="temp.db", table_name="customer", table_id="customer_id"
        )
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error: {str(e)}"
        )


@app.delete("/customer/{customer_id}")
async def delete_customer(customer_id: int):
    try:
        db_customer = sql_interactions.SqlHandler.delete_by_id(
            customer_id,
            db_name="temp.db", table_name='customer', table_id="customer_id"
        )
        return db_customer
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error: {str(e)}"
        )

# Transaction API Methods


@app.post("/transaction/")
async def create_transaction(insert_values: TransactionCreate):
    try:
        db_transaction = sql_interactions.SqlHandler.insert_by_id(
            insert_values,
            db_name="temp.db", table_name="transactions"
        )
        return db_transaction
    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}"}


@app.get("/transaction/")
async def select_transactions(start_id: int, head: int):
    try:
        db_transactions = sql_interactions.SqlHandler.select_many(
            start_id, head,
            db_name="temp.db", table_name="transactions",
            table_id="transaction_id"
        )
        return db_transactions
    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}"}


@app.get("/transaction/{transaction_id}")
async def select_transaction(transaction_id: int):
    try:
        db_transaction = sql_interactions.SqlHandler.select_by_id(
            transaction_id,
            db_name="temp.db", table_name='transactions',
            table_id="transaction_id"
        )
        return db_transaction
    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}"}


@app.put("/transaction/{transaction_id}")
async def update_transaction(row_id: int, update_data: TransactionUpdate):
    try:
        result = sql_interactions.SqlHandler.update_by_id(
            row_id, update_data,
            db_name="temp.db", table_name="transactions",
            table_id="transaction_id"
        )
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error: {str(e)}"
        )


@app.delete("/transaction/{transaction_id}")
async def delete_transaction(transaction_id: int):
    try:
        db_transaction = sql_interactions.SqlHandler.delete_by_id(
            transaction_id,
            db_name="temp.db", table_name='transactions',
            table_id="transaction_id"
        )
        return db_transaction
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error: {str(e)}"
        )

# Date API Methods


@app.post("/date/")
async def create_date(insert_values: DateCreate):
    try:
        db_date = sql_interactions.SqlHandler.insert_by_id(
            insert_values,
            db_name="temp.db", table_name="date"
        )
        return db_date
    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}"}


@app.get("/date/")
async def select_dates(start_id: int, head: int):
    try:
        db_dates = sql_interactions.SqlHandler.select_many(
            start_id, head,
            db_name="temp.db", table_name="date", table_id="date_id"
        )
        return db_dates
    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}"}


@app.get("/date/{date_id}")
async def select_date(date_id: int):
    try:
        db_date = sql_interactions.SqlHandler.select_by_id(
            date_id,
            db_name="temp.db", table_name='date', table_id="date_id"
        )
        return db_date
    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}"}


@app.put("/date/{date_id}")
async def update_date(row_id: int, update_data: DateUpdate):
    try:
        result = sql_interactions.SqlHandler.update_by_id(
            row_id, update_data,
            db_name="temp.db", table_name="date", table_id="date_id"
        )
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error: {str(e)}"
        )


@app.delete("/date/{date_id}")
async def delete_date(date_id: int):
    try:
        db_date = sql_interactions.SqlHandler.delete_by_id(
            date_id,
            db_name="temp.db", table_name='date', table_id="date_id"
        )
        return db_date
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error: {str(e)}"
        )
