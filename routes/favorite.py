from app import *
from models import *
from fasthtml.common import *

restaurants = [
    {"name": "ไข่ข้นป้า - ตลาดกระบัง 46", "food": "อาหารตามสั่ง", "rating": 4.8, "distance": 5.7, "image": "egg.jpeg"},
    {"name": "ไข่ข้นป้า - ตลาดกระบัง 46", "food": "อาหารตามสั่ง", "rating": 4.8, "distance": 5.7, "image": "egg.jpeg"}
]

@app.get("/favorite")
def get():
    # สร้างรายการของร้านอาหาร
    items = []
    for restaurant in restaurants:
        items.append(
            Div(
                Div(
                    Img(src=f'/static/{restaurant["image"]}', alt=restaurant["name"], style="width: 100px; height: auto;"),
                    style="flex: 0 0 auto; margin-right: 15px;"
                ),
                Div(
                    Div(f"{restaurant['name']} - {restaurant['food']}", style="font-weight: bold;"),
                    Div(f"คะแนน: {restaurant['rating']} | ระยะทาง: {restaurant['distance']} km"),
                    style="flex: 1;"
                ),
                style="display: flex; align-items: center; margin-bottom: 15px;"
            )
        )

    # สร้างรูปภาพที่สามารถกดย้อนกลับไปหน้า home
    back_button = A(
        Img(src='/static/arrow.jpeg', alt="back", style="width: 30px; height: 30px; margin-bottom: 20px;"),  # รูปลูกศรที่คลิกได้
        href="/home"  # ลิงก์ไปยังหน้า home
    )

    # สร้างหน้าเว็บหลัก
    return Container(
        back_button,  # รูปลูกศรที่สามารถกดกลับ
        H1("Favourite Restaurants", style="font-weight: normal;"),  # หัวข้อเป็นข้อความธรรมดา
        Div(*items, cls="restaurant-list"),
        Div("Looking for something else? Try searching or explore another category!", style="font-size: 14px; color: grey; text-align: center;")
    )