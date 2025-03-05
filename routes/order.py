from app import app
from models import *
from fasthtml.common import *


@app.get("/order")
def order_view():
    pass

@app.post("/order")
def create_order():
    pass