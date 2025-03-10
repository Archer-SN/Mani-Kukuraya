from app import *
from models import *  # Ensure this correctly imports Controller
from fasthtml.common import *

@app.get("/favorite")
def favorite_view(auth):
    """ แสดงรายการร้านอาหารที่ผู้ใช้กด Favorite ทั้งหมด """
    
    # ดึง user object จากระบบ
    user = controller.get_user(auth)  # ต้องแน่ใจว่าฟังก์ชันนี้มีอยู่ใน controller
    
    # ดึงรายการร้านอาหารที่ผู้ใช้ favorite ไว้
    favorite_restaurants = [controller.get_restaurant_by_id(rid) for rid in user.restaurant_ids]

    # Container สำหรับรายการร้านอาหารทั้งหมด
    restaurant_list = []
    for restaurant in favorite_restaurants:
        restaurant_item = Div(
            Div(
                Img(src=f"/static/{restaurant.get_image()}", alt="Restaurant Image", 
                    style="width: 150px; height: 110px; margin-right: 20px; margin-left: 40px; border-radius: 10px;"),
                style="flex-shrink: 0; display: inline-block;"
            ),
            Div(
                H3(restaurant.get_name()),
                P(restaurant.get_description()),
                P(f"Score: {restaurant.get_score()}"),
                A("View Details", href=f"/restaurant/{restaurant.get_id()}", 
                  style="display: block; margin-top: 5px; color: blue; text-decoration: underline;"),
                style="display: inline-block; vertical-align: top;",
            ),
            style="display: flex; margin-bottom: 20px; align-items: center;"
        )
        restaurant_list.append(restaurant_item)

    # ปุ่มกลับไปหน้า Home
    back_button = A(
        Img(src='/static/arrow.jpeg', alt="back", 
            style="width: 30px; height: 30px; margin-right: 20px;"),  
        href="/home"
    )

    # Navbar
    navbar = Div(
        Div(back_button, style="flex: 0 0 auto;"),  
        Div(
            A("Home", href="/home", style="margin-right: 20px;"),
            A("Favorites", href="/favorite", style="margin-right: 20px;"),
            A("Promotions", href="/promotion", style="margin-right: 20px;"),
            A("Carts", href="/cart", style="margin-right: 20px;"),
            style="display: flex; justify-content: center; align-items: center; flex-grow: 1;"
        ),
        style="display: flex; align-items: center; margin-top: 10px; width: 100%;"
    )

    # รวมส่วนประกอบของหน้า
    page_content = Container(
        navbar,
        Section(
            H1("Favourite Restaurants", cls="text-center", style="margin-top: 20px;"),  
            Div(*restaurant_list, cls="restaurant-list")
        ),
        Section(
            Div("Looking for something else? Try searching or explore another category!", 
                style="font-size: 14px; color: grey; text-align: center;")
        )
    )
    
    return page_content