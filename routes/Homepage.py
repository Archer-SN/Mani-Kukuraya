from app import *
from models import *
from fasthtml.common import *

@app.get("/home")
def ShowHomepage():
    
    dataforhomepage = controller.dataforhomepage()
    promotions = user.get_promotions()
    # Categories from the controller
    user_profile = Div(
    Img(
        src="https://upload.wikimedia.org/wikipedia/en/c/c2/Peter_Griffin.png" if hasattr(user, "profile_picture") else "https://images.ctfassets.net/h6goo9gw1hh6/2sNZtFAWOdP1lmQ33VwRN3/24e953b920a9cd0ff2e1d587742a2472/1-intro-photo-final.jpg?w=1200&h=992&q=70&fm=webp",
        alt="User Profile Picture",
        style="width: 50px; height: 50px; border-radius: 50%; margin-right: 10px;"
    ),
    A(
        f"{user.name}",
        href=f"/profile",
        style="display:block; text-decoration:none; color:#ff6600; text-align:center; font-size:16px; margin-top: 5px;"
    ),
    
    style="display: flex; align-items: center; position: absolute; top: 10px; left: 10px;"
)
    categories = dataforhomepage[0]
    # Create category elements with links
    category_element = [
        A(
            Button(
                f"{category}",
                cls="btn btn-layered-3d btn-layered-3d--purple",
                style="display:block; text-align:center; margin:10px; width:200px; height:70px; line-height:30px;"
            ),
            href=f"/category/{category.lower()}",
            style="text-decoration:none;"
        )
        for category in categories
    ]

    
    # Promotion element

    promotion_element =Button(
                f"โปรโมชั่นที่คุณมี {len(promotions)}",cls="btn flash-slide flash-slide--green",style="margin-top:40px",
            ),
        
    

    # Search bar
    search_bar_element = Nav(
        Div(
            Form(
                Input(
                    type="search",
                    placeholder="Search",
                    name="query",
                    aria_label="Search",
                    className="form-control me-2"
                ),
                Button(
                    "Search",
                    type="submit",
                    className="btn btn-outline-success",
                ),
                className="d-flex",
                role="search",
                action="/search",
                method="get"
            ),
            className="container-fluid",
            style="position: absolute; top: 15px; right: 17px; width: 20%;"
        ),
        className="navbar bg-body-tertiary"
    )

    
    # Navbar with links to different pages
    navbar = Div(
        Div(
            A(
                Button("Favorite", cls="btn btn-moving-gradient btn-moving-gradient--blue"),
                style="text-decoration:none;",
                href=f"/favorite",
            ),
            style="margin: 10px;"
        ),
        Div(
            A(
                Button("Promotions", cls="btn btn-moving-gradient btn-moving-gradient--blue"),
                style="text-decoration:none;",
                href=f"/promotion",
            ),
            style="margin: 10px;"
        ),
        Div(
            A(
                Button("Carts", cls="btn btn-moving-gradient btn-moving-gradient--blue"),
                style="text-decoration:none;",
                href=f"/cart",
            ),
            style="margin: 10px;"
        ),     
        style="display:flex; flex-direction:row; justify-content:center; gap: 20px; margin-top: 10px;"
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
            A(
                Button(
                    "สั่งซื้อ",
                    cls="btn flash-slide flash-slide--blue",
                    style="display:block; text-decoration:none; color:#ffffff; text-align:center; font-size:16px; margin-top: 5px;"
                ),
                href=f"/selectedFood/{food.get_food_id()}",
            ),
            style="text-align:center; margin: 10px; display:flex; flex-direction:column; align-items:center; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);"
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
        P(f"{restaurant.get_name()}"),
        A(
            Button(  
            "ดูร้านค้า",
            cls="btn flash-slide flash-slide--red",
            style="display:block; text-decoration:none; color:#ffffff; text-align:center; font-size:16px; margin-top: 5px;"
            ),
            href = f"/restaurant/{restaurant.get_restaurant_id()}",
        ),
        style="text-align:center; margin: 10px; display:flex; flex-direction:column; align-items:center; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);"
    )
    for restaurant in recommended_restaurant
]



    # Return the entire page with navbar, search, categories, and promotions
    return Main(Container(
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
            ),
        ),
            style='background-color: #ffffff;'
    )

@app.get("/search")
def SearchResults(query: str):
    # Implement your search logic here
    search_results = controller.search_result(query)
    
    # Display search results
    search_results_elements = [
        Div(
            Img(
                src=result.get_image(), 
                style="width:320px; height:200px; object-fit:cover; display:block; margin-bottom: 5px;"
            ),
            A(
                f"{result.get_name()}",
                href=f"/restaurant/{result.get_restaurant_id()}" if isinstance(result, Restaurant) else f"/selectedFood/{result.get_food_id()}" if isinstance(result, Food) else "#",
                style="display:block; text-decoration:none; color:#ff6600; text-align:center; font-size:16px; margin-top: 5px;"
            ),
            A(
                Button(
                    "ดูร้านค้า" if isinstance(result, Restaurant) else "สั่งซื้อ" if isinstance(result, Food) else "ไม่ทราบประเภท",
                    cls="btn flash-slide flash-slide--red" if isinstance(result, Restaurant) else "btn flash-slide flash-slide--blue" if isinstance(result, Food) else "btn",
                    style="display:block; text-decoration:none; color:#ffffff; text-align:center; font-size:16px; margin-top: 5px;"
                ),
                href=f"/restaurant/{result.get_restaurant_id()}" if isinstance(result, Restaurant) else f"/selectedFood/{result.get_food_id()}" if isinstance(result, Food) else "#",
            ),
            style="text-align:center; margin: 10px; display:flex; flex-direction:column; align-items:center; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);"
        )
        for result in search_results
    ]
    
    if not search_results_elements:
        return Container(
            H1(f"ไม่พบ '{query}'", style="margin-bottom: 20px;"),
            A(
                Button(
                    "Go Home",
                    cls="btn flash-slide flash-slide--green",
                    style="padding: 10px 20px; font-size: 16px;"
                ),
                href="/home"
            ),
            style="text-align:center; margin-top: 100px;"
        )
    
    return Container(
        H1(f"ผลการค้นหาสำหรับ '{query}'"),
        Div(
            *search_results_elements,
            style="display:flex;flex-wrap:wrap;justify-content:space-around;margin-top:20px;"
        ),
        style="text-align:center;"
    )
