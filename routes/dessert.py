from app import *
from models import *
from fasthtml.common import *

@app.get("/category/{category_name}")
def show_category(category_name: str):
    # ดึงอาหารทั้งหมดจากร้านอาหารทุกแห่งที่ตรงกับ category
    category_foods = [
        food for restaurant in controller.get_restaurants()
        for food in restaurant.get_menu()
        if food.get_category().lower() == category_name.lower()
    ]

    if not category_foods:
        return Main(
            Container(
                H1(f"หมวดหมู่: {category_name.capitalize()}",style="color:black"),
                P("ยังไม่มีอาหารในหมวดนี้", style="text-align:center; font-size:18px; color:black;"),
                style="text-align:center; padding:20px ;"
            )
        )

    # สร้างรายการอาหารของหมวดหมู่ที่เลือก
    category_food_elements = [
        Div(
            Img(
                src=food.get_image(),
                style="width:100%; height:180px; object-fit:cover; border-radius:10px;margin-bottom:20px"
            ),
            H3(
                food.get_name(),
                style="color:#ff6600; text-align:center; font-size:18px; padding:0 10px; white-space:normal; overflow:hidden; text-overflow:ellipsis; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; min-height:48px;margin-bottom:10px"
            ),
            P(
                food.get_description(),
                style="text-align:center; color:#555; font-size:14px; padding:0 10px; min-height:40px;"
            ),
            P(
                f"ราคา: {food.get_price():.2f} ฿",
                style="text-align:center; font-weight:bold; font-size:16px;"
            ),
            A(
                "สั่งซื้อ",
                href=f"/selectedFood/{food.get_food_id()}",
                cls="btn flash-slide flash-slide--blue",
                style="width:90%; padding:10px; margin-top:auto; text-align:center; font-weight:bold; font-size:16px;border: none; background-color: #ff5722; color: white;"
            ),
            style="display:flex; flex-direction:column; justify-content:space-between; align-items:center; text-align:center; padding:15px; border:1px solid #ddd; border-radius:10px; background:#fff; box-shadow:0 4px 6px rgba(0,0,0,0.1); min-height:350px;margin-top:20px"
        )
        for food in category_foods
    ]

    return Main(
        Container(
            H1(f"{category_name.capitalize()}", style="text-align:center; margin-bottom:50px; margin-top:20px;color:black"),
            Div(
                *category_food_elements,
                style="display:grid; grid-template-columns:repeat(auto-fill, minmax(250px, 1fr)); gap:20px; justify-content:center; align-items:stretch; margin-top:20px;"
            ),
            style="padding:30px; max-width:1200px; margin:auto;"
        ),
        style="background:#f8f8f8;"
    )
