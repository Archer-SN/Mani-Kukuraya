from app import app
from models import *
from fasthtml.common import *
from lucide_fasthtml import Lucide

@app.post("/update-delivery")
def update_delivery(order_id:str, delivery: str):
    order = controller.get_order_by_id(order_id)
    order.select_delivery_option(delivery)
    return  Div(P("Selected: " + str(order.get_delivery_option_by_name(delivery))), id="delivery-summary"),  # Display selection dynamically
