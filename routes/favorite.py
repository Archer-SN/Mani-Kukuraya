from app import *
from models import *  # Ensure this correctly imports User and Restaurant
from fasthtml.common import *


@app.get("/favorite/{user_id:str}")
def favorite_view(user_id: str):

    # ✅ ดึงค่าร้านอาหารจาก `user.favorite_restaurant`
    favorite_restaurants = user.favorite_restaurants  # ✅ List ของ Object Restaurant

    # ✅ สร้างรายการร้านค้าที่ถูก Favorite
    restaurant_list = []
    for restaurant in favorite_restaurants:
        restaurant_card = Div(
            Div(
                Img(src=f"/static/{restaurant.get_image()}", alt="Restaurant Image", 
                    style="width: 200px; height: 150px; margin-right: 20px; border-radius: 10px;"),
                style="flex-shrink: 0; display: inline-block;"
            ),
            Div(
                H2(restaurant.get_name()),  # ✅ ชื่อร้าน
                P(restaurant.get_description(), style="color: grey;"),  # ✅ คำอธิบาย
                P(f"Rating: {restaurant.get_score()} ⭐", style="font-weight: bold;"),  # ✅ คะแนนร้าน
                A("View Restaurant", href=f"/restaurant/{user_id}/{restaurant.get_id()}",
                  style="display: inline-block; margin-top: 10px; padding: 10px 20px; background-color: #4CAF50; color: white; border-radius: 5px; text-decoration: none;"),
                style="display: inline-block; vertical-align: top;"
            ),
            style="display: flex; align-items: center; margin-bottom: 20px; border: 1px solid #ddd; padding: 10px; border-radius: 10px; background-color: #f9f9f9;"
        )
        restaurant_list.append(restaurant_card)  # ✅ เพิ่มข้อมูลร้านค้าเข้าไปใน List

    # ✅ ปุ่มย้อนกลับไปหน้า Home
    back_button = A(
        Img(src='/static/arrow.jpeg', alt="back", style="width: 30px; height: 30px; margin-right: 20px;"),  
        href="/home"
    )

    # ✅ Navbar
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

    # ✅ รวมทุกองค์ประกอบเข้า Container หลัก
    page_content = Container(
        navbar,
        Section(
            H1("Your Favorite Restaurants", cls="text-center", style="margin-top: 20px;"),  
            Div(*restaurant_list, cls="restaurant-list")  # ✅ แสดงรายการร้านค้า
        ),
        Section(
            Div("Looking for something else? Try searching or explore another category!", 
                style="font-size: 14px; color: grey; text-align: center;")
        )
    )
    
    return page_content