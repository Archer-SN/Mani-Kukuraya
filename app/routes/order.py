from app import app
from models import models

@app.get("/order")
def order_view():
    pass

@app.post("/order")
def create_order():
    pass