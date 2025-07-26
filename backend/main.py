from fastapi import FastAPI, Query
from data_loader import get_top_products, get_order_status, get_stock_count

app = FastAPI()

@app.get("/top-products")
def top_products(limit: int = 5):
    return get_top_products(limit)

@app.get("/order-status")
def order_status(order_id: str = Query(...)):
    return get_order_status(order_id)

@app.get("/stock")
def stock(product_name: str = Query(...)):
    return get_stock_count(product_name)
