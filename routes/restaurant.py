from app import *
from models import *
from fasthtml.common import *
from lucide_fasthtml import Lucide

# ใช้ตัวแปรกลางเก็บรายการร้านที่ถูก Favorite
favorite_restaurants = set()  # ใช้ set() ป้องกันค่าซ้ำ

@app.get("/restaurant/{id:str}")
def restaurant_view(id: str):
    restaurant = controller.get_restaurant_by_id(id)

    food_list = []

    # ตรวจสอบว่าร้านนี้อยู่ในรายการโปรดหรือไม่
    is_favorite = id in favorite_restaurants

    # ปุ่มหัวใจ (เปลี่ยนสีตามสถานะรายการโปรด)
    favorite_button = A(
        Lucide("heart", 24, color="red" if is_favorite else "black"),
        hx_delete=f"/favorite/{id}" if is_favorite else None,
        hx_post=f"/favorite/{id}" if not is_favorite else None,
        style="position: absolute; top: 10px; right: 10px;",
        hx_target="this",
        hx_swap="outerHTML"
    )

    # การ์ดอาหารหลัก (Main Food Card)
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

    # รายการเมนูอาหาร
    food_list = []
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

    # ฟอร์มค้นหาอาหาร
    search_input = Input(id="search-query", name="search_query", placeholder="Search food...",
                         style="width: 200px; padding: 8px; margin-left: 10px;")
    confirm_button = Button("Confirm", type="submit",
                            style="padding: 8px 16px; font-size: 16px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; margin-left: 10px;")
    search_form = Form(
        search_input,
        confirm_button,
        action="/send_input",
        method="post"
    )

    # ส่วน "For You"
    for_you_section = Div(
        H3("For You"),
        search_form,
        style="display: flex; align-items: center; justify-content: space-between; margin-top: 20px; margin-right: 40px; margin-left: 40px;"
    )

    # รวมทุกส่วนเป็นหน้าเว็บ
    page_content = Container(
        main_food_card,
        favorite_button,  # ปุ่มหัวใจ
        for_you_section,
        *food_list
    )

    return page_content

@app.get("/search")
def SearchResults(query: str):
    # Implement your search logic here
    search_results = controller.search_result(query)
    # Display search results
    search_results_elements = [
        A(
            P(result.get_name(), style="text-align:center;"),
            Img(src=result.get_image(), style="width:70%;height:50%;"),
            href="/review",
            style="text-align:center; margin: 10px;"
        )
        for result in search_results
    ]
    
    return Container(
        H1(f"ผลการค้นหาสำหรับ '{query}'"),
        Div(
            *search_results_elements,
            style="display:flex;flex-wrap:wrap;flex-direction:row;justify-content:space-around;margin-top:20px;"
        ),
        style="text-align:center;"
    )
    

# 🟥 ฟังก์ชันเพิ่ม/ลบรายการโปรด (ใช้ตัวแปรกลาง favorite_restaurants)
@app.post("/favorite/{id:str}")
def add_favorite(id: str):
    """เพิ่มร้านอาหารลงในรายการโปรด"""
    favorite_restaurants.add(id)  # เพิ่มร้านลงใน set
    print(f"Added to favorites: {id}, Current Favorites: {list(favorite_restaurants)}")

    return A(
        Lucide("heart", 24, color="red"),
        hx_delete=f"/favorite/{id}",
        style="position: absolute; top: 10px; right: 10px;",
        hx_target="this",
        hx_swap="outerHTML"
    )

@app.delete("/favorite/{id:str}")
def remove_favorite(id: str):
    """ลบร้านอาหารออกจากรายการโปรด"""
    favorite_restaurants.discard(id)  # ลบออกจาก set (ไม่ error ถ้าไม่มี)
    print(f"Removed from favorites: {id}, Current Favorites: {list(favorite_restaurants)}")

    return A(
        Lucide("heart", 24, color="black"),
        hx_post=f"/favorite/{id}",
        style="position: absolute; top: 10px; right: 10px;",
        hx_target="this",
        hx_swap="outerHTML"
    )