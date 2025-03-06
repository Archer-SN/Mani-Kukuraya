from app import *
from models import *
from fasthtml.common import *

@app.get("/selectedFood")
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

    return Titled(
        "",
        Div(
            A("⬅ กลับ", href ="/food", style="text-decoration: none; font-size: 18px; color: black; display: inline-block;"),
            style="position: absolute; top: 10px; left: 10px;"
    
        ),
        form
    )


@app.post("/update-quantity")
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
@app.post("/add-to-cart")
def add_to_cart():
    return Span("เพิ่มสินค้าลงตะกร้าแล้ว!", cls="success")

@app.get("/validate-field")
def post(field: str, value: str):
    if not value.strip():  # ถ้าเว้นว่าง
        return Span("กรุณากรอกข้อมูลให้ครบถ้วน", cls="error")
    return ""  # ถ้าไม่มีปัญหา ให้ส่งค่าเป็นค่าว่าง (ลบข้อความแจ้งเตือนออก)