from app import app
from models import *
from fasthtml.common import *
from lucide_fasthtml import Lucide

@app.get("/promotion")
def view_promotion():
    # Fetch promotions (assuming `user.get_promotions()` returns a list of promotions)
    promotions = user.get_promotions()
    
    # Create back button to go back to the previous page
    back_button = A(
        Img(src='/static/arrow.jpeg', alt="back", style="width: 30px; height: 30px; margin-right: 20px;"),  # รูปลูกศรที่คลิกได้
        href="/home"  # ลิงก์ไปยังหน้า home
    )
    
    # Create navbar for navigation with back button on the left and navbar in the center
    navbar = Div(
        Div(back_button, style="flex: 0 0 auto;"),  # ลูกศรย้อนกลับอยู่ทางซ้าย
        Div(
            A("Home", href="/home", style="margin-right: 20px;"),
            A("Favorites", href="/favorite/1", style="margin-right: 20px;"),
            A("Promotions", href="/promotion", style="margin-right: 20px;"),
            A("Carts", href="/cart", style="margin-right: 20px;"),
            style="display: flex; justify-content: center; align-items: center; flex-grow: 1;"
        ),
        style="display: flex; align-items: center; margin-top: 10px; width: 100%;"
    )
    
    # Returning the page with navbar and promotion content
    return Container(
        navbar,  # Add the navbar at the top with back button and centered navigation
        Section(
            H1("Available Offers", cls="text-center", style="margin-top: 20px;"),  # ขยับหัวข้อ "Available Offers" ลง 20px
            Div(
                Input(placeholder="ใส่รหัสโปรโมชั่นที่นี่", cls="search", type="text"),
                cls="grid"
            )
        ),
        Section(
            *[
                Article(
                    Div(
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
                    ),
                    cls="card"
                )
                for promotion in promotions
            ]
        )
    )

@app.post("/promotion")
def use_promotion(promotion_code: str, order_id: str):
    promotion = user.get_promotion(promotion_code)
    order = controller.get_order_by_id(order_id)
    order.select_promotion(promotion)
    return order

