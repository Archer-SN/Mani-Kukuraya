from app import *
from models import *
from fasthtml.common import *
from lucide_fasthtml import Lucide

# ใช้ตัวแปรกลางเก็บรายการร้านที่ถูก Favorite
favorite_restaurants = set()  # ใช้ set() ป้องกันค่าซ้ำ

@app.get("/restaurant/{id:str}")
def restaurant_view(id: str):
    restaurant = controller.get_restaurant_by_id(id)

    # ตรวจสอบว่าร้านนี้อยู่ในรายการโปรดหรือไม่
    is_favorite = id in favorite_restaurants

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

    # Container to hold all food items
    food_list = []

    Div(
        A("⬅ กลับ", href =f"/home", style="text-decoration: none; font-size: 18px; color: black; display: inline-block;"),
        style="position: absolute; top: 10px; left: 10px;"
    
    ),

    # Add main food item card at the top (with border for "ไข่ขนป้า")
    main_food_card = Div(
        Div(
            Img(src=f"/static/{restaurant.get_image()}", alt="Food Image", 
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

    # Add "For You" section with "+" button to the right for other food items
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

    # Search input and confirm button inside a form
    search_input = Input(id="search-query", name="search_query", placeholder="Search food...", 
                         style="width: 200px; padding: 8px; margin-left: 10px;")
    confirm_button = Button("Confirm", type="submit", 
                            style="padding: 8px 16px; font-size: 16px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; margin-left: 10px;")

    # Form that wraps the search input and button
    search_form = Form(
        search_input,
        confirm_button,
        action="/send_input",
        method="post"
    )

    # Div that contains "For You" and the search form
    for_you_section = Div(
        H3("For You"),
        search_form,
        style="display: flex; align-items: center; justify-content: space-between; margin-top: 20px; margin-right: 40px; margin-left: 40px;"
    )

    # Combine all parts into one container
    page_content = Container(
        main_food_card,  # การ์ดหลักของร้านอาหาร
        img_button,  # ปุ่มหัวใจ Favorite
        for_you_section,  # ส่วน For You
        *food_list  # รายการเมนูอาหาร
    )

    return page_content

@app.post("/send_input")
def send_input(search_query: str):
    print(f"User input: {search_query}")
    return RedirectResponse("/restaurant/1", status_code=303)

@app.post("/search_food")
def search_food(search_query: str):
    print(f"Received search query: {search_query}")

    # Fetch the restaurant data
    restaurant = controller.get_restaurant_by_id('1')
    
    found = False
    for food in restaurant.get_menu():
        print(f"Checking food item: {food.get_name()}")
        if search_query.lower().strip() == food.get_name().lower().strip():
            found = True
            print(f"Found: {food.get_name()}")
            break
    
    if not found:
        print("No match found.")

    return RedirectResponse(f"/restaurant/{restaurant.get_id()}", status_code=303)

# 🟥 ฟังก์ชันเพิ่ม/ลบรายการโปรด (Favorite)
@app.post("/favorite/{id:str}")
def add_favorite(id: str):
    """เพิ่มร้านอาหารลงในรายการโปรด"""
    restaurant = controller.get_restaurant_by_id(id)
    favorite_restaurants.add(restaurant)  # ลบออกจาก Set
    print(f"Added to favorites: {id}, Current Favorites: {list(favorite_restaurants)}")

    return A(
        Lucide("heart", 24, color="red"),
        hx_delete=f"/favorite/{id}",
        hx_trigger="click",
        style="position: absolute; top: 10px; right: 10px;",
        hx_target="this",
        hx_swap="outerHTML"
    )

@app.delete("/favorite/{id:str}")
def remove_favorite(id: str):
    """ลบร้านอาหารออกจากรายการโปรด"""
    restaurant = controller.get_restaurant_by_id(id)
    favorite_restaurants.discard(restaurant)  # ลบออกจาก Set
    print(f"Removed from favorites: {id}, Current Favorites: {list(favorite_restaurants)}")

    return A(
        Lucide("heart", 24, color="black"),
        hx_post=f"/favorite/{id}",
        hx_trigger="click",
        style="position: absolute; top: 10px; right: 10px;",
        hx_target="this",
        hx_swap="outerHTML"
    )
    