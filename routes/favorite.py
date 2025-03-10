from app import *
from models import *  # Ensure this correctly imports User and Restaurant
from fasthtml.common import *

@app.get("/favorite/{user_id:str}")
def favorite_view(user_id: str):
    # ดึงข้อมูล User จาก user_id
    user = controller.get_user_by_id(user_id)
    
    if not user:
        return Container(
            H1("User Not Found", cls="text-center", style="color: red; margin-top: 20px;")
        )

    # รายการร้านอาหารที่ถูกเพิ่มเป็น favorite
    favorite_restaurants = user.favorite_restaurant

    # Container เก็บรายการอาหารจากร้านที่ถูก Favorite
    food_list = []
    for restaurant in favorite_restaurants:
        food_item = Div(
            Div(
                Img(src=f"/static/{restaurant.get_image()}", alt="Food Image", 
                    style="width: 150px; height: 110px; margin-right: 20px; margin-left: 40px; border-radius: 10px;"),
                style="flex-shrink: 0; display: inline-block;"
            ),
            Div(
                H3(restaurant.get_name()),
                P(restaurant.get_description()),
                P(f"Rating: {restaurant.get_score()} ⭐"),
                style="display: inline-block; vertical-align: top;",
            ),
            style="display: flex; margin-bottom: 20px; align-items: center;"
        )
        food_list.append(food_item)

    # ปุ่มย้อนกลับ
    back_button = A(
        Img(src='/static/arrow.jpeg', alt="back", style="width: 30px; height: 30px; margin-right: 20px;"),  
        href="/home"
    )

    # Navbar
    navbar = Div(
        Div(back_button, style="flex: 0 0 auto;"),  
        Div(
            A("Home", href="/home", style="margin-right: 20px;"),
            A("Favorites", href=f"/favorite/{user_id}", style="margin-right: 20px;"),
            A("Promotions", href="/promotion", style="margin-right: 20px;"),
            A("Carts", href="/cart", style="margin-right: 20px;"),
            style="display: flex; justify-content: center; align-items: center; flex-grow: 1;"
        ),
        style="display: flex; align-items: center; margin-top: 10px; width: 100%;"
    )

    # รวมทุกองค์ประกอบเข้า Container หลัก
    page_content = Container(
        navbar,
        Section(
            H1("Favorite Restaurants", cls="text-center", style="margin-top: 20px;"),  
            Div(*food_list, cls="food-list")
        ),
        Section(
            Div("Looking for something else? Try searching or explore another category!", 
                style="font-size: 14px; color: grey; text-align: center;")
        )
    )
    
    return page_content