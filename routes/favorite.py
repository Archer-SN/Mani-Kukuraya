from app import *
from models import *  # Import Controller class from models
from fasthtml.common import *

@app.get("/favorite")
def view_favorite():
    # Fetch restaurants from Controller
    restaurants = Controller.get_restaurants()
    
    # Create back button
    back_button = A(
        Img(src='/static/arrow.jpeg', alt="back", style="width: 30px; height: 30px; margin-right: 20px;"),  
        href="/home"  
    )
    
    # Create navbar with back button on the left and navigation in the center
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
    
    # Generate restaurant list
    items = [
        Div(
            Div(
                Img(src=f'/static/{restaurant.get_restaurant_image()}', alt=restaurant.get_name(), style="width: 100px; height: auto;"),
                style="flex: 0 0 auto; margin-right: 15px;"
            ),
            Div(
                Div(f"{restaurant.get_name()} - {restaurant.get_description()}", style="font-weight: bold;"),
                Div(f"คะแนน: {restaurant.get_score()} | ระยะทาง: {restaurant.get_reviews()} km"),
                style="flex: 1;"
            ),
            style="display: flex; align-items: center; margin-bottom: 15px;"
        )
        for restaurant in restaurants
    ]

    # Returning the page with navbar and favorite restaurant content
    return Container(
        navbar,  
        Section(
            H1("Favourite Restaurants", cls="text-center", style="margin-top: 20px;"),  
            Div(*items, cls="restaurant-list")
        ),
        Section(
            Div("Looking for something else? Try searching or explore another category!", style="font-size: 14px; color: grey; text-align: center;")
        )
    )