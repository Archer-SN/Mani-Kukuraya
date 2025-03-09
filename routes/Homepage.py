from app import *
from models import *
from fasthtml.common import *

@app.get("/home")
def ShowHomepage():
    
    dataforhomepage = controller.dataforhomepage()
    # Categories from the controller
    user_profile = Div(
    Img(
        src="https://upload.wikimedia.org/wikipedia/en/c/c2/Peter_Griffin.png" if hasattr(user, "profile_picture") else "https://images.ctfassets.net/h6goo9gw1hh6/2sNZtFAWOdP1lmQ33VwRN3/24e953b920a9cd0ff2e1d587742a2472/1-intro-photo-final.jpg?w=1200&h=992&q=70&fm=webp",
        alt="User Profile Picture",
        style="width: 50px; height: 50px; border-radius: 50%; margin-right: 10px;"
    ),
    A(
        f"{user.name}",
        href="/profile",
        style="display:block; text-decoration:none; color:#ff6600; text-align:center; font-size:16px; margin-top: 5px;"
    ),
    
    style="display: flex; align-items: center; position: absolute; top: 10px; left: 10px;"
)
    categories = dataforhomepage[0]
    
    # Create category elements (using A and Div to structure the categories)
    category_element = [
        A(
            Div(
                P(category, style="text-align:center; margin-top: 10px;"),
                style="text-align:center;"
            ),
            href=f"/category/{category[0]}",  # Navigate to a category-specific page
            style="display:block; text-align:center; margin: 10px;"
        )
        for category in categories
    ]

    
    # Promotion element

    numbers_promotion = 35

    promotion_element = Card(
        H3("โปรโมชั่น", style="text-align:left;"),
        Div(
            *[
                P(f"โปรโมชั่นที่คุณมี {numbers_promotion}", style="text-align:left;")
            ],
            style="text-align:left;"
        ),
        style="width:30%;height:20%;margin-top:50px;"
    )

    # Search bar
    search_bar = Input(type="text", name="query", placeholder="ค้นหาอาหาร", style="width: 80%; height: 100%; display: inline-block; margin-right:10px;")
    search_button = Button("ค้นหา", type="submit", style="width: 30%; height: 100%; display: inline-block;")
    search_bar_element = Form(
        search_bar,
        search_button,
        action="/search",
        method="get",
        style="position: absolute; top: 20px; right: 20px; width: 300px; height: 40px; display: flex;"
    )

    
    # Navbar with links to different pages
    navbar = Div(
        A("Home", href="/home", style="margin-right: 20px;"),

        A("Favorites", href="/favorite", style="margin-right: 20px;"),
        A("Promotions", href="/promotion", style="margin-right: 20px;"),
        A("Carts", href="/cart", style="margin-right: 20px;"),

        A("Categories", href="/categories", style="margin-right: 20px;"),
        A("Promotions", href="/promotion", style="margin-right: 20px;"),

        style="text-align:center; margin-top: 10px;"
    )

    # recent_order = controller.get_recent_order()
    # recent_order_element = [
    #     Card(
    #         Img(src=order["image"], style="width:100%;height:50%;"),
    #         P(order["name"], style="text-align:center;"),
    #         style="text-align:center; margin: 10px;"
    #     )
    #     for order in recent_order
    # ]

    
    # Recommended food
    recommended_food = dataforhomepage[1]
    recommended_food_element = [
    Div(
        Img(
            src=food.get_image(), 
            style="width:320px; height:200px; object-fit:cover; display:block; margin-bottom: 5px;"
        ),
        A(
            f"{food.get_name()}",
            href=f"/",
            style="display:block; text-decoration:none; color:#ff6600; text-align:center; font-size:16px; margin-top: 5px;"
        ),
        style="text-align:center; margin: 10px; display:flex; flex-direction:column; align-items:center;"
    )
    for food in recommended_food
]
    #recommended restaurant
    recommended_restaurant = dataforhomepage[2]
    recommended_restaurant_element = [
    Div(
        Img(
            src=restaurant.get_image(),
            style="width:300px; height:200px; object-fit:cover; display:block; margin-bottom: 5px;"
        ),
        A(  
            f"{restaurant.get_name()}",
            href = f"/restaurant/{restaurant.get_restaurant_id()}",
            style="display:block; text-decoration:none; color:#ff6600; text-align:center; font-size:16px; margin-top: 5px;"
        ),
        style="text-align:center; margin: 10px; display:flex; flex-direction:column; align-items:center;"
    )
    for restaurant in recommended_restaurant
]



    # Return the entire page with navbar, search, categories, and promotions
    return Container(
        navbar,  # Add the navigation bar at the top
        user_profile,
        Div(
            search_bar_element
        ),
        Div(

            H2("หมวดหมู่", style="width: 100%; text-align: left; margin-top: 20px;"),
            Div(
                *category_element,
                style="display:flex;flex-direction:row;justify-content:space-around;margin-top:40px;"
            ),
        ),
        promotion_element,
        Div(
            H2("อาหารแนะนำ", style="width: 100%; text-align: left; margin-bottom: 20px;"),  # Custom style for H2
            Div(
                *recommended_food_element,  # Show only the first 5 items initially
                id="recommended-food-container",
                style="display:flex;flex-wrap:row;justify-content:flex-start;"
            ),
            style="margin-top:100px;"
        ),

        Div(
            H2("ร้านอาหารแนะนำ", style="width: 100%; text-align: left; margin-bottom: 20px;"),  # Custom style for H2
            Div(
                *recommended_restaurant_element,
                style="display:flex;flex-direction:row;justify-content:flex-start;"
            ),
            style="margin-top:100px;"
        )

        # style="text-align:center;"
    )

@app.get("/search")
def SearchResults(query: str):
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
        style="text-align:center;"
    )