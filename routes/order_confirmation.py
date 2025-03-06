from app import app
from models import *
from fasthtml.common import *
from lucide_fasthtml import Lucide


@app.get("/order_confirmation")
def view_order_confirmation():
    progress_bar = Div(
        Div(style="background-color: #4CAF50; width: 30%; height: 10px; border-radius: 5px;"),
        style="background-color: #E0E0E0; height: 10px; width: 100%; border-radius: 5px; margin-top: 10px;"
    )

    progress_images = Div(
        Img(src="/static/chef.png", style="position: absolute; left: 27%; top: -40px; width: 40px;"),
        Img(src="/static/delivery.png", style="position: absolute; left: 65%; top: -40px; width: 40px;"),
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
            P(B("ตึก ECC ฉลองกรุง 1 เฟส 5"), style="margin: 0;"),
            P("ฉลองกรุง แขวงลำปลาทิว เขตลาดกระบัง กรุงเทพมหานคร", cls="text-muted"),
        ),
        Lucide("cooking-pot"),
        style="display: flex; align-items: center; justify-content: space-between; padding: 15px;"
    )

    order_summary = Card(
        H4("1x กระเพราหมูสับ", B("99 บาท")),
        P(Small("ไข่ดาว • พิเศษ • เผ็ดมาก")),
        P(A("แก้ไข", href="/edit-order", cls="text-danger")),
        style="padding: 15px;"
    )

    pricing_section = Card(
        Table(
            Tbody(
                Tr(Td("Subtotal"), Td(B("99"))),
                Tr(Td("Delivery fee"), Td(B("14"))),
                Tr(Td(B("รวมทั้งหมด"), style="font-size: 1.2rem;"), Td(B("113 บาท"), style="font-size: 1.5rem; color: #FF6240;"))
            )
        ),
        style="padding: 15px;"
    )

    return Container(
        Button(Lucide("cooking-pot"), style="border: none; background: none; font-size: 1.5rem;", onclick="window.history.back()"),
        tracking_section,
        location_section,
        order_summary,
        pricing_section
    )