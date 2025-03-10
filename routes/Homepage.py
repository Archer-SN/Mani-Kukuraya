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

    numbers_promotion = len(dataforhomepage[3])

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
            style="position: absolute; top: 15px; right: 17px; width: 25%;"
        ),
        className="navbar bg-body-tertiary"
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
                className="card-img-top",
                alt=food.get_name(),
                style="border-radius: 15px;"
            ),
            Div(
                H5(food.get_name(), className="card-title"),
                P("Some quick example text to build on the card title and make up the bulk of the card's content.", className="card-text"),
                Button(
                    "ดูสินค้า",
                    onclick="window.location.href='/review'",
                    className="btn btn-primary"
                ),
                className="card-body"
            ),
            className="card",
            style="width: 18rem; margin: 10px;"
        )
        for food in recommended_food
    ]
    # recommended restaurant
    recommended_restaurant = dataforhomepage[2]
    recommended_restaurant_element = [
        Div(
            Img(
                src=restaurant.get_image(),
                className="card-img-top",
                alt=restaurant.get_name(),
                style="border-radius: 15px;"
            ),
            Div(
                H5(restaurant.get_name(), className="card-title"),
                P("Some quick example text to build on the card title and make up the bulk of the card's content.", className="card-text"),
                Button(
                    "ดูสินค้า",
                    onclick="window.location.href='/review'",
                    className="btn btn-primary"
                ),
                className="card-body"
            ),
            className="card",
            style="width: 18rem; margin: 10px;"
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
        ),

        style="text-align:center;"
    )

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