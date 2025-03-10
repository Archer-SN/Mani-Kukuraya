from app import app
from models import *
from fasthtml.common import *
from lucide_fasthtml import Lucide


@app.get("/order")
def view_order(cart_id: dict):
    print(cart_id)
    loc = user.get_locations()[0]
    location = Card(
        f"- {loc.full_name}, {loc.address}, {loc.street}, {loc.unit}, {loc.extra_information}",
        cls="grid-item"
    )

    delivery_options = Card(
        H4("ตัวเลือกการจัดส่ง"),
        P("ระยะห่างประมาณ: 2.1 กม."),
        Div(
            Label(Input(type="radio", name="delivery", value="priority", 
                        hx_post="/update-delivery", hx_target="#delivery-summary"), 
                  " Priority < 25 นาที - 32 บาท"),
            Label(Input(type="radio", name="delivery", value="standard", 
                        hx_post="/update-delivery", hx_target="#delivery-summary"), 
                  " Standard 25 นาที - 32 บาท"),
            Label(Input(type="radio", name="delivery", value="saver", checked=True, 
                        hx_post="/update-delivery", hx_target="#delivery-summary"), 
                  " Saver 35 นาที - ฟรี"),
            cls="radio-group"
        ),
        Div(P("Selected: Saver (35 นาที - ฟรี)"), id="delivery-summary"),  # Display selection dynamically
        cls="grid-item"
    )
    cart = user.get_carts()[0]
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
        P(B(cart.calculate_price(), " บาท"), style="font-size:1.5rem; color:#FF6240;"),
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
            A("Use Now", hx_post="/promotion", cls="contrast button"),
            cls="grid"
        )
        for promotion in cart.get_user().get_promotions_by_restaurant(restaurant)
    ]

    offers = Card(
        H4("Offers"),
        P("ใช้ส่วนลดหรือใส่รหัสโปรโมชั่น"),
        *available_promotions,
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


@app.post("/order")
def create_order():
    
    return Redirect("/order_confirmation")

