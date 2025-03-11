from app import *
from models import *
from fasthtml.common import *
from lucide_fasthtml import Lucide

@app.get("/restaurant/{id:str}")
def restaurant_view(id: str):
    restaurant = controller.get_restaurant_by_id(id)

    # ตรวจสอบว่าร้านนี้อยู่ในรายการโปรดของ user1 หรือไม่
    is_favorite = restaurant in user.get_favorites()

    # ปุ่มกลับไปหน้า Home
    home_button = A(
        Img(src="/static/arrow.jpeg", alt="Home",
            style="width: 40px; height: 40px; position: absolute; top: 10px; left: 10px; cursor: pointer;"),
        href="/home"
    )

    # ปุ่มตะกร้าสินค้า (Cart Button)
    cart_button = A(
        Div(
            Lucide("shopping-cart", 36, color="orange"),
            Span(
                str(user.get_foods_incart()),  # จำนวนสินค้าที่อยู่ในตะกร้า
                style="position: absolute; top: -8px; right: -8px; background-color: red; color: white; border-radius: 50%; width: 20px; height: 20px; font-size: 12px; display: flex; align-items: center; justify-content: center; z-index: 1001;"
            ),
            style="position: relative; display: inline-block;"
        ),
        href="/cart",
        hx_get="/cart/count",
        hx_trigger="revealed, every 3s",
        hx_target="this",
        style="position: fixed; bottom: 20px; right: 20px; z-index: 1000; cursor: pointer; background-color: white; padding: 10px; border-radius: 50%; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);"
    )

    # ปุ่มหัวใจ (Favorite Button)
    img_button = A(
        Lucide("heart", 24, color="red" if is_favorite else "black"),
        hx_delete=f"/favorite/{id}" if is_favorite else None,
        hx_post=f"/favorite/{id}" if not is_favorite else None,
        hx_trigger="click",
        style="position: absolute; top: 10px; right: 10px;",
        hx_target="this",
        hx_swap="outerHTML"
    )
    food_list = []
    # การ์ดร้านอาหาร
    main_food_card = Div(
        Div(
            Img(src=f"{restaurant.get_image()}", alt="Food Image", 
                style="width: 200px; height: auto; margin-right: 40px; border-radius: 10px;"),
            style="flex-shrink: 0; display: inline-block;"
        ),
        Div(
            H2(restaurant.get_name()),
            P(restaurant.get_description()),
            P(f"Rating: {restaurant.get_score()} | Distance: "),
            style="display: inline-block; vertical-align: top;",
        ),
        style="display: flex; align-items: center; justify-content: center; margin-bottom: 20px; border: 2px solid orange; padding: 20px;", 
        cls="main-food-item-card"
    )
    for food in restaurant.get_menu():
            food_item = Div(
                Div(
                    Img(src=f"{food.get_image()}", alt="Food Image", 
                    style="width: 150px; height: 110px; margin-right: 20px; margin-left: 40px; border-radius: 10px;"),
                style="flex-shrink: 0; display: inline-block;"
                ),
                Div(
                    H3(food.get_name()),
                    P(food.get_description()),
                    P(f"Price: {food.get_price()} บาท"),
                    style="display: inline-block; vertical-align: top;",
                ),
                A("+", 
                    href=f"/selectedFood/{food.get_food_id()}",
                    style="padding: 10px; font-size: 17px; background-color: #4CAF50; color: white; border: none; margin-left: auto; margin-right: 130px; border-radius: 5px;"),
                style="display: flex; align-items: center; margin-bottom: 15px; justify-content: space-between;", 
                cls="food-item-card"
            )
            food_list.append(food_item)

    # รวมทุกอย่างเข้าไปในหน้าเว็บ
    page_content = Container(
        home_button, 
        main_food_card,  
        Div(*food_list, cls="food-list"),
        img_button,  
        cart_button
    )

    return page_content

@app.post("/favorite/{id:str}")
def add_favorite_restaurant(id: str):
    """เพิ่มร้านอาหารลงในรายการโปรดของ user1"""
    restaurant = controller.get_restaurant_by_id(id)

    # ✅ เพิ่มเข้า favorites
    user.add_favorite(restaurant)
    print(user.get_favorites())

    return A(
        Lucide("heart", 24, color="red"),
        hx_delete=f"/favorite/{id}",
        hx_trigger="click",
        style="position: absolute; top: 10px; right: 10px;",
        hx_target="this",
        hx_swap="outerHTML"
    )

@app.delete("/favorite/{id:str}")
def remove_favorite_restaurant(id: str):
    """ลบร้านอาหารออกจากรายการโปรดของ user1"""
    restaurant = controller.get_restaurant_by_id(id)

    # ✅ ลบออกจาก favorites
    user.remove_favorite(restaurant)
    print(user.get_favorites())

    return A(
        Lucide("heart", 24, color="black"),
        hx_post=f"/favorite/{id}",
        hx_trigger="click",
        style="position: absolute; top: 10px; right: 10px;",
        hx_target="this",
        hx_swap="outerHTML"
    )

@app.get("/cart/count")
def cart_count():
    return A(
        Div(
            Lucide("shopping-cart", 36, color="orange"),
            Span(
                str(user.get_foods_incart()),
                style="position: absolute; top: -8px; right: -8px; background-color: red; color: white; border-radius: 50%; width: 20px; height: 20px; font-size: 12px; display: flex; align-items: center; justify-content: center; z-index: 1001;"
            ),
            style="position: relative; display: inline-block;"
        ),
        href="/cart",
     )