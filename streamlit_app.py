import streamlit as st
import requests

st.title("📊 Sales Data Analysis Dashboard")

# API Endpoint
API_URL = "http://127.0.0.1:8000"

# Fetch Total Revenue
st.subheader("💰 Total Revenue")
revenue_response = requests.get(f"{API_URL}/total_revenue").json()
st.write(f"Total Revenue: ${revenue_response['total_revenue']}")

# Fetch Top Products
st.subheader("🔥 Top-Selling Products")
products_response = requests.get(f"{API_URL}/top_products").json()
for product in products_response:
    st.write(f"{product['product_name']} - {product['sales']} Sales")
