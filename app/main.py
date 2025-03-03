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
    order = Order(user_kaka, kfc_cart, kaka_location, saver_delivery, cash_payment, kfc_promotion)
    print(order)

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

@rt("/selectedFood")
def get():
    product = {
        "name": "ส้มตำไทย ไข่เค็ม",
        "description": "ส้มตำไทยไม่เผ็ดเป็นเมนูยอดนิยม...",
        "price": 99,
        "image": "https://media.istockphoto.com/id/478186916/th/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%96%E0%B9%88%E0%B8%B2%E0%B8%A2/%E0%B8%A2%E0%B9%8D%E0%B8%B2%E0%B8%A1%E0%B8%B0%E0%B8%A5%E0%B8%B0%E0%B8%81%E0%B8%AD%E0%B8%AA%E0%B9%84%E0%B8%95%E0%B8%A5%E0%B9%8C%E0%B9%84%E0%B8%97%E0%B8%A2.jpg?s=612x612&w=0&k=20&c=BsKuToHcvJ_2HAcI3DuZi9V_P8gAR2bvNd1dZeyjtOc="
    }

    form = Form(
        # รูปภาพและรายละเอียดสินค้า
         Card(
            Img(src=product["image"], style="width: 120px; height: 120px; object-fit: cover; border-radius: 10px;"),
            Div(
                H2(product["name"]),
                P(product["description"]),
                H3(f"{product['price']} บาท", style="color: #ff5722;"),
            ),
            style="display: flex; align-items: center; gap: 15px;"
        ),

        # ตัวเลือกปริมาณ
        Fieldset(
            Legend("ปริมาณ (Pick 1)"),
            Div(
                Input(type="radio", name="size", value="normal", id="size-normal", checked=True),
                Label("ธรรมดา (+0 บาท)", for_="size-normal"),
            ),
            Div(
                Input(type="radio", name="size", value="extra", id="size-extra"),
                Label("พิเศษ (+10 บาท)", for_="size-extra"),
            )
        ),

        # ตัวเลือกระดับรสชาติ
        Fieldset(
            Legend("รสเผ็ด (Pick 1)"),
            Div(
                Input(type="radio", name="spicy", value="mild", id="spicy-mild", checked=True),
                Label("เผ็ดน้อย (+0 บาท)", for_="spicy-mild"),
            ),
            Div(
                Input(type="radio", name="spicy", value="medium", id="spicy-medium"),
                Label("เผ็ดกลาง (+10 บาท)", for_="spicy-medium"),
            ),
            Div(
                Input(type="radio", name="spicy", value="hot", id="spicy-hot"),
                Label("เผ็ดมาก (+20 บาท)", for_="spicy-hot"),
            )
        ),

        # ความคิดเห็นเพิ่มเติม
        Fieldset(
            Legend("ความคิดเห็นถึงร้านค้า (Optional)"),
            Textarea(name="comment", placeholder="ใส่ข้อความถึงร้านค้า...")
        ),

        # ปุ่มเพิ่ม-ลดจำนวนสินค้า
        Div(
            Button("-", type="button", id="decrease", hx_post="/update-quantity", hx_target="#quantity", hx_vals='{"action":"decrease"}'),
            Span("1", id="quantity", style="font-size: 28px; font-weight: bold; position: relative; top: -5px; margin: 0 20px;"),
            Button("+", type="button", id="increase", hx_post="/update-quantity", hx_target="#quantity", hx_vals='{"action":"increase"}'),
            style="display: flex; justify-content: center; align-items: center; margin: 10px 0;"
        ),

        # ปุ่มเพิ่มลงตะกร้า
        Button("+ เพิ่มลงตะกร้า", type="submit",style="border: none; background-color: #ff5722; color: white;",
               hx_post="/add-to-cart", hx_target="#cart-message", hx_swap="outerHTML"),

        # ข้อความแสดงผลหลังจากกดเพิ่มลงตะกร้า
        Div(id="cart-message")
    )

    return Titled("ส้มตำไทย",  
        Div(
            AX("⬅ กลับ", "/", "body", style="text-decoration: none; font-size: 18px; color: black; display: inline-block;"),
            style="position: absolute; top: 10px; left: 10px;"
        ),
        form
    )

@rt("/update-quantity", methods=["POST"])
def update_quantity(quantity: int = 1, action: str = "increase"):
    """ ฟังก์ชันอัปเดตจำนวนสินค้า """
    try:
        quantity = int(quantity)  # แปลงค่าให้เป็นตัวเลขแน่นอน
    except ValueError:
        quantity = 1  # ถ้าค่าไม่ใช่ตัวเลขให้เริ่มที่ 1

    if action == "increase":
        new_quantity = quantity + 1
    elif action == "decrease":
        new_quantity = max(1, quantity - 1)  # ไม่ให้ค่าต่ำกว่า 1
    else:
        new_quantity = quantity  # ถ้าค่า action ไม่ถูกต้อง

    return str(new_quantity)  # ส่งค่ากลับไปอัปเดต HTML


# เพิ่มสินค้าลงตะกร้า
@rt("/add-to-cart", methods=["POST"])
def add_to_cart():
    return Span("เพิ่มสินค้าลงตะกร้าแล้ว!", cls="success")

@rt("/validate-field")
def post(field: str, value: str):
    if not value.strip():  # ถ้าเว้นว่าง
        return Span("กรุณากรอกข้อมูลให้ครบถ้วน", cls="error")
    return ""  # ถ้าไม่มีปัญหา ให้ส่งค่าเป็นค่าว่าง (ลบข้อความแจ้งเตือนออก)

@rt("/new-address")
def get():
    form = Form(
        Label("ชื่อ-นามสกุล"),
        Input(id="full_name", name="full_name", required=True, placeholder="กรอกชื่อ-นามสกุล",
              hx_post="/validate-field", hx_target="#err_full_name", hx_trigger="blur"),
        Span("", cls="error", id="err_full_name"),

        Label("เบอร์โทรศัพท์มือถือ"),
        Input(id="phone", name="phone", type="tel", required=True, placeholder="กรอกเบอร์โทรศัพท์",
              hx_post="/validate-field", hx_target="#err_phone", hx_trigger="blur"),
        Span("", cls="error", id="err_phone"),

        Label("จังหวัด/เขต(อำเภอ)/รหัสไปรษณีย์/แขวง(ตำบล)"),
        Input(id="location", name="location", required=True, placeholder="กรอกข้อมูลพื้นที่",
              hx_post="/validate-field", hx_target="#err_location", hx_trigger="blur"),
        Span("", cls="error", id="err_location"),

        Label("ถนน/ชื่ออาคาร"),
        Input(id="street", name="street", required=True, placeholder="กรอกถนน/ชื่ออาคาร",
              hx_post="/validate-field", hx_target="#err_street", hx_trigger="blur"),
        Span("", cls="error", id="err_street"),

        Label("เลขที่ยูนิต/ชั้น"),
        Input(id="unit", name="unit", placeholder="ระบุเลขที่ยูนิต/ชั้น"),

        Label("ข้อมูลที่อยู่เพิ่มเติม (ถ้ามี)"),
        Textarea(id="extra_info", name="extra_info", placeholder="รายละเอียดเพิ่มเติม"),

        Div(
            Button("บันทึก", type="submit", style="border: none; background-color: #ff5722; color: white;",
                hx_post="/submit-address", hx_target="#form-msg", hx_swap="outerHTML"),
            style="margin-top: 20px;"
        ),

        Div(id="form-msg")  # สำหรับแสดงผลลัพธ์
    )

    return Titled(
        "เพิ่มที่อยู่ใหม่",
        Div(
            AX("⬅ กลับ", "/", "body", style="text-decoration: none; font-size: 18px; color: black; display: inline-block;"),
            style="position: absolute; top: 10px; left: 10px;"
        ),
        form
    )

@rt("/submit-address", methods=["POST"])
def submit_address(full_name: str, phone: str, location: str, street: str, unit: str = "", extra_info: str = ""):
    print(f"ข้อมูลที่ได้รับ: {full_name}, {phone}, {location}, {street}, {unit}, {extra_info}")  

    if not full_name or not phone or not location or not street:
        return Span("กรุณากรอกข้อมูลให้ครบถ้วน", cls="error")

    return Span("บันทึกที่อยู่สำเร็จ!", cls="success")

@rt("/update-address", methods=["POST"])
def update_address(sess, full_name: str, phone: str, location: str, street: str, unit: str = "", extra_info: str = ""):
    print(f"ข้อมูลที่ได้รับ: {full_name}, {phone}, {location}, {street}, {unit}, {extra_info}")

    # ตรวจสอบว่ามีค่าว่างหรือไม่
    if not full_name or not phone or not location or not street:
        return Span("กรุณากรอกข้อมูลให้ครบถ้วน", cls="error")

    # บันทึกการแก้ไขลง session
    sess["address_data"] = {
        "full_name": full_name,
        "phone": phone,
        "location": location,
        "street": street,
        "unit": unit,
        "extra_info": extra_info
    }

    return Span("บันทึกการแก้ไขสำเร็จ!", cls="success")

@rt("/edit-address")
def get_edit(sess):
    # ถ้ายังไม่มีข้อมูลใน session ให้กำหนดค่าเริ่มต้น
    if "address_data" not in sess:
        sess["address_data"] = {
            "full_name": "มหาเทพกาก้า",
            "phone": "66629",
            "location": "กรุงเทพมหานคร เขตลาดกระบัง 10502 แขวงลำปลาทิว",
            "street": "ตึก ECC",
            "unit": "-",
            "extra_info": "รถคันนี้สีขาว"
        }

    address_data = sess["address_data"]  # ดึงข้อมูลจาก session

    form = Form(
        Label("ชื่อ-นามสกุล"),
        Input(id="full_name", name="full_name", value=address_data["full_name"], required=True),
        Span("", cls="error", id="err_full_name"),

        Label("เบอร์โทรศัพท์มือถือ"),
        Input(id="phone", name="phone", type="tel", value=address_data["phone"], required=True),
        Span("", cls="error", id="err_phone"),

        Label("จังหวัด/เขต(อำเภอ)/รหัสไปรษณีย์/แขวง(ตำบล)"),
        Input(id="location", name="location", value=address_data["location"], required=True),
        Span("", cls="error", id="err_location"),

        Label("ถนน/ชื่ออาคาร"),
        Input(id="street", name="street", value=address_data["street"], required=True),
        Span("", cls="error", id="err_street"),

        Label("เลขที่ยูนิต/ชั้น"),
        Input(id="unit", name="unit", value=address_data["unit"]),

        Label("ข้อมูลที่อยู่เพิ่มเติม (ถ้ามี)"),
        Textarea(id="extra_info", name="extra_info", value=address_data["extra_info"]),

         Div(
            Button("บันทึกการแก้ไข", type="submit", style="border: none; background-color: #ff5722; color: white;",
                hx_post="/update-address", hx_target="#form-msg", hx_swap="outerHTML"),
        ),
        
        Div(id="form-msg")  # สำหรับแสดงผลลัพธ์
    )

    return Titled(
        "เเก้ไขที่อยู่ใหม่",
        Div(
            AX("⬅ กลับ", "/", "body", style="text-decoration: none; font-size: 18px; color: black; display: inline-block;"),
            style="position: absolute; top: 10px; left: 10px;"
        ),
        form
    )

serve()