from fasthtml.common import *
from utils import *
from fa6_icons import svgs
from models import *

app, rt = fast_app(live=True, debug=True)

@app.get("/")
def home():
    return P("Hello World")

@app.get("/order")
def view_order():
    location = Card(
        # svgs.location_dot.solid.width(25),
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
        Label(Input(type="radio", name="payment", value="qr"), svgs.qrcode.solid, " สแกน QR Code"),
        Label(Input(type="radio", name="payment", value="cash", checked=True), svgs.money_bill_wave.solid, " เงินสด"),
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
    order = Order()

@app.get("/confirm")
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
        svgs.location_dot.solid.width(10),
        Div(
            P(B("ตึก ECC ฉลองกรุง 1 เฟส 5"), style="margin: 0;"),
            P("ฉลองกรุง แขวงลำปลาทิว เขตลาดกระบัง กรุงเทพมหานคร", cls="text-muted"),
        ),
        svgs.chevron_right.solid.width(10),
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
        Button(svgs.chevron_left.solid, style="border: none; background: none; font-size: 1.5rem;", onclick="window.history.back()"),
        tracking_section,
        location_section,
        order_summary,
        pricing_section
    )


serve()