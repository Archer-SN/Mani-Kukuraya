from app import *
from models import *
from fasthtml.common import *

@app.get("/side-dish")
def show_side_dish():
    # ดึงอาหารที่เป็น Side Dish ทั้งหมด
    side_dishes = [
        food for restaurant in controller.get_restaurants()
        for food in restaurant.get_menu()
        if food.get_category().lower() == "side"
    ]

    if not side_dishes:
        return Main(
            Container(
                H1("Side Dish Menu 🍟"),
                P("ยังไม่มีเมนูเครื่องเคียง", style="text-align:center; font-size:18px; color:gray;"),
                style="text-align:center; padding:20px;"
            )
        )

    # สร้างรายการเครื่องเคียง
    side_dish_elements = [
        Div(
            Img(
                src=food.get_image(),
                style="width:100%; height:180px; object-fit:cover; border-radius:10px;"
            ),
            H3(
                food.get_name(),
                style="color:#ff6600; text-align:center; font-size:18px; padding:0 10px; white-space:normal; overflow:hidden; text-overflow:ellipsis; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; min-height:48px;"
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
                style="width:90%; padding:10px; margin-top:auto; text-align:center; font-weight:bold; font-size:16px;"
            ),
            style="display:flex; flex-direction:column; justify-content:space-between; align-items:center; text-align:center; padding:15px; border:1px solid #ddd; border-radius:10px; background:#fff; box-shadow:0 4px 6px rgba(0,0,0,0.1); min-height:350px;"
        )
        for food in side_dishes
    ]

    return Main(
        Container(
            H1("Side Dish Menu 🍟", style="text-align:center; margin-bottom:20px;"),
            Div(
                *side_dish_elements,
                style="display:grid; grid-template-columns:repeat(auto-fill, minmax(250px, 1fr)); gap:20px; justify-content:center; align-items:stretch; margin-top:20px;"
            ),
            style="padding:30px; max-width:1200px; margin:auto;"
        ),
        style="background:#f8f8f8;"
    )
