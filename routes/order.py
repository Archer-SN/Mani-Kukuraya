from app import app
from models import *
from fasthtml.common import *
from lucide_fasthtml import Lucide


@app.get("/order")
def view_order():
    location = Card(
        P(B("ตึก ECC ลองกรุง 1 เฟส 5"), style="margin: 0;"),
        P("ลองกรุง แขวงลาดกระบัง เขตลาดกระบัง กรุงเทพมหานคร", cls="text-muted"),
        cls="grid-item"
    )

    delivery_options = Card(
        H4("ตัวเลือกการจัดส่ง"),
        P("ระยะห่างประมาณ: 2.1 กม."),
        Form(
            Div(
                Label(Input(type="radio", name="delivery", value="priority"), " Priority < 25 นาที - 32 บาท"),
                Label(Input(type="radio", name="delivery", value="standard"), " Standard 25 นาที - 32 บาท"),
                Label(Input(type="radio", name="delivery", value="saver", checked=True), " Saver 35 นาที - ฟรี"),
                cls="radio-group"
            ),
            cls="grid-item"
        )
    )

    order_summary = Card(
        H4("สรุปคำสั่งซื้อ"),
        P("1x กระเพราหมูสับ", B("99 บาท")),
        P(Small("ไม่เผ็ด • พิเศษ • เพิ่มขนม")),
        cls="grid-item"
    )

    total_cost = Card(
        H4("รวมทั้งหมด"),
        P(B("113 บาท"), style="font-size:1.5rem; color:#FF6240;"),
        cls="grid-item"
    )

    payment_methods = Card(
        H4("รายละเอียดการชำระเงิน"),
        Label(Input(type="radio", name="payment", value="qr"), Lucide("qr-code"), " สแกน QR Code"),
        Label(Input(type="radio", name="payment", value="cash", checked=True), Lucide("banknote"), " เงินสด"),
        cls="grid-item"
    )

    offers = Card(
        H4("Offers"),
        P("ใช้ส่วนลดหรือใส่รหัสโปรโมชั่น"),
        cls="grid-item"
    )

    summary = Form(
        Card(
            Button("สั่งซื้อ", type="submit", style="background-color:#FF6240; color:white; font-size:1.2rem; padding: 10px; width: 100%;"),
            cls="grid-item"
        ),
        action="/order", method="post"
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
    order = Order(user_kaka, kfc_cart, kaka_location, saver_delivery, cash_payment, kfc_promotion)
    print(order)
    return Redirect("/order-confirmation")

