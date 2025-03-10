from app import app
from models import *
from fasthtml.common import *
from lucide_fasthtml import Lucide


@app.get("/order")
def view_order(cart_id: str):
    print(cart_id)
    for cart in user.get_carts():
        print("User:" + cart.get_cart_id())
    # Note that cart_id is the same as order_id
    order = controller.get_order_by_id(cart_id)
    cart = user.get_cart_by_cart_id(cart_id)
    loc = user.get_locations()[0]
    if (order == None):
        order = controller.create_order(user, cart, loc)
    location = Card(
        f"- {loc.full_name}, {loc.address}, {loc.street}, {loc.unit}, {loc.extra_information}",
        cls="grid-item"
    )

    delivery_options = Card(
        H4("ตัวเลือกการจัดส่ง"),
        P("ระยะห่างประมาณ: 2.1 กม."),
        Div(
            *[
                Label(Input(type="radio", name="delivery", hx_vals={'order_id': order.get_order_id(), 'delivery': delivery_option.get_name()}, 
                        hx_post="/update-delivery", hx_target="#delivery-summary"), 
                  delivery_option)
                  for delivery_option in Order.delivery_options
            ],
            cls="radio-group"
        ),
        Div(P("Selected: " + str(order.get_delivery_option())), id="delivery-summary"),  # Display selection dynamically
        cls="grid-item"
    )
    cart_items = cart.get_foods()
    restaurant = cart.get_restaurant()
    order_summary_items = [
        P(f"{item.get_quantity()}x {item.get_name()}", B(f"{item.calculate_price()} บาท"))
        for item in cart_items
    ]

    order_summary = Card(
        H4("สรุปคำสั่งซื้อ"),
        *order_summary_items,
        cls="grid-item"
    )
    total_cost = Card(
        H4("รวมทั้งหมด"),
        P(B(cart.calculate_price(), " บาท"), hx_post="order/price", hx_vals={'order_id', order.get_order_id()}, hx_swap="innerHTML", hx_trigger="load", style="font-size:1.5rem; color:#FF6240;"),
        cls="grid-item"
    )

    payment_methods = Card(
        H4("รายละเอียดการชำระเงิน"),
        Div(
            Label(Input(type="radio", name="payment", value="qr", 
                        hx_post="/update-payment", hx_target="#payment-summary"), 
                  Lucide("qr-code"), " สแกน QR Code"),
            Label(Input(type="radio", name="payment", value="cash", checked=True, 
                        hx_post="/update-payment", hx_target="#payment-summary"), 
                  Lucide("banknote"), " เงินสด"),
            cls="radio-group"
        ),
        Div( P("Selected: เงินสด"), id="payment-summary"),  # Display selection dynamically
        cls="grid-item"
    )

    available_promotions = [
        Card(
            Img(src=promotion.get_image(), cls="avatar"),
            Div(
                Span("Just for you", cls="badge"),
                Hgroup(
                    H3(promotion.get_name()),
                    P(f"#Code {promotion.get_promotion_code()}"),
                )
            ),
            A("Use Now", hx_post="/promotion", hx_target="#offer", hx_vals={'promotion_code': promotion.get_promotion_code()}, hx_swap="innerHTML", cls="contrast button"),
            cls="grid"
        )
        for promotion in cart.get_user().get_promotions_by_restaurant(restaurant)
    ]

    offers = Card(
        H4("Offers"),
        P("ใช้ส่วนลดหรือใส่รหัสโปรโมชั่น"),
        *available_promotions,
        id="offer",
        cls="grid-item"
    )

    summary = Card(
        Button(
            "สั่งซื้อ",
            cls="contrast button",
            style="background-color:#FF6240; color:white; font-size:1.2rem; padding: 10px; width: 100%;",
            hx_post="/order",
            hx_target="#order-status"
        ),
        Div(id="order-status"),  # Display order confirmation dynamically
        cls="grid-item"
    )

    return Container(
        H2("ครัวสนามอาหารตามสั่ง - ข.ลาดกระบัง 21"),
        P("Delivery fee calculated at 14:08"),
        Grid(
            location,
            delivery_options,
            order_summary,
            total_cost,
            payment_methods,
            offers,
            summary,
            cls="order-grid"
        )
    )

@app.post("/order/price")
def get_price(order_id: str):
    order = controller.get_order_by_id(order_id)
    return B(cart.calculate_price(), " บาท")


@app.post("/order")
def create_order():
    
    return Redirect("/order_confirmation")

