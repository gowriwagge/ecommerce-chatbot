import pandas as pd

orders_df = pd.read_csv("https://raw.githubusercontent.com/recruit41/ecommerce-dataset/main/orders.csv")
products_df = pd.read_csv("https://raw.githubusercontent.com/recruit41/ecommerce-dataset/main/products.csv")

def get_top_products(limit=5):
    top = orders_df['product_id'].value_counts().head(limit)
    return [{"product_id": pid, "count": count} for pid, count in top.items()]

def get_order_status(order_id):
    order = orders_df[orders_df['order_id'] == order_id]
    if not order.empty:
        return order.iloc[0].to_dict()
    return {"error": "Order ID not found"}

def get_stock_count(product_name):
    product = products_df[products_df['name'].str.lower() == product_name.lower()]
    if not product.empty:
        return {"stock": int(product.iloc[0]['stock'])}
    return {"error": "Product not found"}
