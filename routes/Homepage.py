from app import *
from models import *
from fasthtml.common import *

@app.get("/home")
def ShowHomepage():
    # Categories from the controller
    catagories = Controller.get_numbers_catagories()
    
    # Create category elements (using A and Div to structure the categories)
    catagory_element = [
        A(
            Div(
                Img(src=category[1], style="width:100%;height:50%;"),
                P(category[0], style="text-align:center; margin-top: 10px;"),
                style="text-align:center;"
            ),
            href=f"/category/{category[0]}",  # Navigate to a category-specific page
            style="display:block; text-align:center; margin: 10px;"
        )
        for category in catagories
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
        style="width:30%;height:20%;margin-top:10px;"
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

    # recent_order = Controller.get_recent_order()
    # recent_order_element = [
    #     Card(
    #         Img(src=order["image"], style="width:100%;height:50%;"),
    #         P(order["name"], style="text-align:center;"),
    #         style="text-align:center; margin: 10px;"
    #     )
    #     for order in recent_order
    # ]

    
    #Recommended food
    recommended_food = Controller.get_recommended_food()
    recommended_food_element = [
        Div(
            Img(src=food[1], style="width:300px;height:200px;"),
            P(food[0]),
            style="text-align:left; margin: 10px;"
        )
        for food in recommended_food
    ]

    #recommended restaurant
    # recommended_restaurant = Controller.get_recommended_restaurant()
    # recommended_food_element = [

    # ]



    # Return the entire page with navbar, search, categories, and promotions
    return Container(
        navbar,  # Add the navigation bar at the top
        Div(
            search_bar_element
        ),
        Div(

            H2("หมวดหมู่", style="width: 100%; text-align: left; margin-top: 20px;"),
            Div(
                *catagory_element,
                style="display:flex;flex-direction:row;justify-content:space-around;margin-top:40px;"
            ),
        ),
        promotion_element,
        Div(
            H2("อาหารแนะนำ", style="width: 100%; text-align: left; margin-bottom: 20px;"),  # Custom style for H2
            Div(
                *recommended_food_element,
                style="display:flex;flex-direction;justify-content:flex-start;"
            ),
            style="margin-top:30px;"
        ),


        # Div(
        #     H2("อาหารล่าสุด"),
        #     *recent_order_element,
        #     style="display:flex;flex-wrap:wrap;justify-content:space-around;margin-top:200px;"
        # ),

        style="text-align:center;"
    )

@app.get("/search")
def SearchResults(query: str):
    # Implement your search logic here
    search_results = Controller.search_food(query)
    
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