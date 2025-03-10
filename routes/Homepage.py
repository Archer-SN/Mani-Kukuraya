from app import *
from models import *
from fasthtml.common import *

@app.get("/home")
def ShowHomepage(user_id: str = "1"):
    user = controller.get_user_by_id(user_id)

    if not user:
        return Span("ไม่พบผู้ใช้ โปรดเข้าสู่ระบบ", cls="error")

    dataforhomepage = controller.dataforhomepage("1")

    # User Profile
    user_profile = Div(
        Img(
            src="https://upload.wikimedia.org/wikipedia/en/c/c2/Peter_Griffin.png" if hasattr(user, "profile_picture") else "https://images.ctfassets.net/h6goo9gw1hh6/2sNZtFAWOdP1lmQ33VwRN3/24e953b920a9cd0ff2e1d587742a2472/1-intro-photo-final.jpg?w=1200&h=992&q=70&fm=webp",
            alt="User Profile Picture",
            style="width: 50px; height: 50px; border-radius: 50%; margin-right: 10px;"
        ),
        A(
            f"{user.name}",
            href=f"/profile?user_id={user_id}",
            style="display:block; text-decoration:none; color:#ff6600; text-align:center; font-size:16px; margin-top: 5px;"
        ),
        style="display: flex; align-items: center; position: absolute; top: 10px; left: 10px;"
    )

    # Navigation Bar
    navbar = Div(
        A("Home", href=f"/home?user_id={user_id}", style="margin-right: 20px;"),
        A("Favorites", href=f"/favorite?user_id={user_id}", style="margin-right: 20px;"),
        A("Promotions", href=f"/promotion?user_id={user_id}", style="margin-right: 20px;"),
        A("Carts", href=f"/cart?user_id={user_id}", style="margin-right: 20px;"),
        A("Categories", href=f"/categories?user_id={user_id}", style="margin-right: 20px;"),
        style="text-align:center; margin-top: 10px;"
    )

    # Search Bar
    search_bar_element = Form(
        Input(type="text", name="query", placeholder="ค้นหาอาหาร", style="width: 80%; height: 100%; display: inline-block; margin-right:10px;"),
        Button("ค้นหา", type="submit", style="width: 30%; height: 100%; display: inline-block;"),
        action=f"/search?user_id={user_id}",
        method="get",
        style="position: absolute; top: 20px; right: 20px; width: 300px; height: 40px; display: flex;"
    )

    # Recommended Food
    recommended_food = dataforhomepage[1]
    recommended_food_element = [
        Div(
            Img(
                src=food.get_image(), 
                style="width:320px; height:200px; object-fit:cover; display:block; margin-bottom: 5px;"
            ),
            A(
                f"{food.get_name()}",
                href=f"/food/{food.get_food_id()}",
                style="display:block; text-decoration:none; color:#ff6600; text-align:center; font-size:16px; margin-top: 5px;"
            ),
            style="text-align:center; margin: 10px; display:flex; flex-direction:column; align-items:center;"
        )
        for food in recommended_food
    ]

    # Recommended Restaurants
    recommended_restaurant = dataforhomepage[2]
    recommended_restaurant_element = [
        Div(
            Img(
                src=restaurant.get_image(),
                style="width:300px; height:200px; object-fit:cover; display:block; margin-bottom: 5px;"
            ),
            A(  
                f"{restaurant.get_name()}",
                href=f"/restaurant/{restaurant.get_restaurant_id()}",
                style="display:block; text-decoration:none; color:#ff6600; text-align:center; font-size:16px; margin-top: 5px;"
            ),
            style="text-align:center; margin: 10px; display:flex; flex-direction:column; align-items:center;"
        )
        for restaurant in recommended_restaurant
    ]

    return Container(
        navbar,  
        user_profile,
        search_bar_element,
        Div(
            H2("อาหารแนะนำ", style="width: 100%; text-align: left; margin-bottom: 20px;"),  
            Div(
                *recommended_food_element,
                style="display:flex;flex-wrap:row;justify-content:flex-start;"
            ),
            style="margin-top:100px;"
        ),
        Div(
            H2("ร้านอาหารแนะนำ", style="width: 100%; text-align: left; margin-bottom: 20px;"),  
            Div(
                *recommended_restaurant_element,
                style="display:flex;flex-direction:row;justify-content:flex-start;"
            ),
            style="margin-top:100px;"
        )
    )

@app.get("/search")
def SearchResults(user_id: str, query: str):
    # Implement your search logic here
    search_results = controller.search_food(query)
    
    # Display search results
    search_results_elements = [
        Div(
            P(result["name"], style="text-align:center;"),
            Img(src=result["image"], style="width:100%;height:50%;"),
            style="text-align:center; margin: 10px;"
        )
        for result in search_results
    ]
    
    return Container(
        H1(f"ผลการค้นหาสำหรับ '{query}'"),
        Div(
            *search_results_elements,
            style="display:flex;flex-wrap:wrap;justify-content:space-around;margin-top:20px;"
        ),
        A("กลับหน้าหลัก", href=f"/home?user_id={user_id}", style="display:block; text-align:center; margin-top:20px; color:#ff6600;"),
        style="text-align:center;"
    )