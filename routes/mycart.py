from app import *
from models import *
from fasthtml.common import *

cart_items = [
    {"name": "ไข่ข้นป้า - ตลาดกระบัง 46", "food": "อาหารตามสั่ง", "rating": 4.8, "distance": 5.7, "image": "egg.jpeg"},
    {"name": "ไข่ข้นป้า - ตลาดกระบัง 46", "food": "อาหารตามสั่ง", "rating": 4.8, "distance": 5.7, "image": "egg.jpeg"},
    {"name": "ราเมงร้อน - ตลาดกระบัง 45", "food": "อาหารตามสั่ง", "rating": 4.2, "distance": 5.7, "image": "rice.jpeg"}
]

@app.get("/cart")
def get():
    
    items = []
    for cart in user.get_carts():
        restaurant = cart.get_restaurant()
        items.append(
            A(
                Card(
                    Div(
                        Img(src=f'{restaurant.get_restaurant_image()}', alt=f"{restaurant.get_name()}", style="width: 100px; height: 70px;"),
                        style="flex: 0 0 auto; margin-right: 15px;"
                    ),
                    Div(f"{len(cart.get_foods())} items"),
                    Div(f"คะแนน: {restaurant.get_score()} | ระยะทาง: 100 km"),
                    style="display: flex;  flex-direction: column; align-items: center; margin-bottom: 15px; border: 1px solid #ccc; padding: 10px; margin-bottom: 10px;",
                    cls="hover-effect"
                ),
                Input(id="cart-id", name="cart_id", type="hidden", value=f"{cart.get_cart_id()}"),
                href=f"/order?cart_id={cart.get_cart_id()}",
            )
        )

    # รูปลูกศรย้อนกลับที่คลิกได้
    back_button = A(
        Img(src='/static/arrow.jpeg', alt="back", style="width: 30px; height: 30px; margin-right: 20px;"),  # รูปลูกศรที่คลิกได้
        href="/home"  # ลิงก์ไปยังหน้า home
    )

    # สร้าง navbar สำหรับการนำทาง โดยที่ลูกศรย้อนกลับอยู่ทางซ้ายและ navbar อยู่กลาง
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

    # สร้างหน้าเว็บหลักที่มีปุ่ม "Manage" อยู่ในแถวเดียวกับ "My Cart"
    return Container(
        navbar,  # แสดง navbar ที่จัดตำแหน่งให้ลูกศรย้อนกลับอยู่ทางซ้ายและแถบการนำทางอยู่ตรงกลาง
        Div(
            H1("My Cart", style="font-weight: normal; margin-right: 20px; margin-top: 20px;"),  # ขยับ "My Cart" ลง 20px
            Div(A("Manage", href="#", style="font-size: 14px; color: #f1a22a;"), cls="manage-button"),
            style="display: flex; justify-content: space-between; align-items: center; width: 100%;"
        ),
        Div(*items, cls="cart-list")
    )