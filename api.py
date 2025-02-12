from fastapi import FastAPI
import pandas as pd
from database import get_db_connection

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Sales Data API is running!"}

@app.get("/total_revenue")
def total_revenue():
    conn = get_db_connection()
    query = "SELECT SUM(total_price) as revenue FROM sales_data"
    result = pd.read_sql(query, conn)
    return {"total_revenue": result["revenue"][0]}

@app.get("/top_products")
def top_products():
    conn = get_db_connection()
    query = "SELECT product_name, COUNT(*) as sales FROM sales_data GROUP BY product_name ORDER BY sales DESC LIMIT 5"
    result = pd.read_sql(query, conn)
    return result.to_dict(orient="records")
