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
                Label(Input(type="radio", id="delivery", name="delivery", hx_vals={'order_id': order.get_order_id(), 'delivery': delivery_option.get_name()}, 
                        hx_post="/update-delivery", hx_target="#delivery-summary", checked=order.get_delivery_option() == delivery_option, ),
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
        P(B(cart.calculate_price(), " บาท"), hx_post="order/price", hx_vals={'order_id': order.get_order_id()}, hx_trigger="every 1s", hx_swap="innerHTML", style="font-size:1.5rem; color:#FF6240;"),
        cls="grid-item"
    )

    payment_methods = Card(
        H4("รายละเอียดการชำระเงิน"),
        Div(
            Label(Input(type="radio", hx_vals={'order_id': order.get_order_id(), 'payment': 'qr'},
                        hx_post="/update-payment", hx_target="#payment-summary", checked=isinstance(order.get_payment_method(), QRPayment)), 
                  Lucide("qr-code"), " สแกน QR Code"),
            Label(Input(type="radio", hx_vals={'order_id': order.get_order_id(), 'payment': 'cash'},
                        hx_post="/update-payment", hx_target="#payment-summary", checked=isinstance(order.get_payment_method(), CashPayment)), 
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
            A("Use Now", href=f"/restaurant/{promotion.get_restaurant()}", hx_post="/promotion", hx_target="#offer", hx_vals={'promotion_code': promotion.get_promotion_code(), 'order_id': order.get_order_id()}, hx_swap="innerHTML", cls="contrast button"),
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
            hx_target="#main",
            hx_vals={'order_id': cart_id},
            hx_swap="outerHTML"
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
        ),
        id="main"
    )

@app.post("/order/price")
def get_price(order_id: str):
    order = controller.get_order_by_id(order_id)
    print(controller.get_orders())
    return B(order.calculate_price(), " บาท")


@app.post("/order")
def confirm_order(order_id: str):
    order = controller.get_order_by_id(order_id)
    location = order.get_location()
    progress_bar = Div(
        Div(id='pb', style='width:122%', cls='progress-bar'),
        role='progressbar',
        aria_valuemin='0',
        aria_valuemax='100',
        aria_valuenow='122',
        aria_labelledby='pblabel',
        cls='progress'
    )

    progress_images = Div(
        Img(src="/static/chef.png", style="position: absolute; left: 27%; top: -40px; width: 40px;"),
        Img(src="/static/driver.png", style="position: absolute; left: 65%; top: -40px; width: 40px;"),
        Img(src="/static/home.png", style="position: absolute; left: 93%; top: -40px; width: 40px;"),
        style="position: relative; height: 40px; width: 100%;"
    )

    tracking_section = Card(
        H2("Preparing your orders"),
        P("Your order’s in the kitchen", cls="text-muted"),
        progress_images,
        progress_bar,
        style="padding: 20px;"
    )

    location_section = Card(
        Lucide("map-pin-house"),
        Div(
            P(B(location.full_name), style="margin: 0;"),
            P(location.address + location.street, cls="text-muted"),
        ),
        Lucide("cooking-pot"),
        style="display: flex; align-items: center; justify-content: space-between; padding: 15px;"
    )

    order_items = []
    for item in order.get_cart().get_foods():
        order_items.append(Li(f"{item.get_quantity()}x {item.get_name()}", B(f" {item.calculate_price()} บาท")))
        for option in item.get_selected_options():
            selected_choices = option.get_selected_choices()
            if selected_choices:
                choices = Ul(*[Li(choice.get_name()) for choice in selected_choices])
                order_items.append(choices)

    order_summary = Card(
        H4("Order Summary"),
        Ul(*order_items),
        style="padding: 15px;"
    )

    pricing_section = Card(
        Table(
            Tbody(
                Tr(Td("Subtotal"), Td(B(order.get_cart().calculate_price()))),
                Tr(Td("Delivery fee"), Td(B(order.get_delivery_option().get_price()))),
                Tr(Td("Discount"), Td(B(order.get_selected_promotion().get_discount()))) if order.get_selected_promotion() != None else "",
                Tr(Td(B("รวมทั้งหมด"), style="font-size: 1.2rem;"), Td(B(order.calculate_price()), style="font-size: 1.5rem; color: #FF6240;"))
            )
        ),
        style="padding: 15px;"
    )

    return Container(
        Button(Lucide("cooking-pot"), style="border: none; background: none; font-size: 1.5rem;", onclick="window.history.back()"),
        tracking_section,
        location_section,
        order_summary,
        pricing_section,
        id="main"
    )

