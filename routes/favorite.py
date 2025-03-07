from app import *
from models import *
from fasthtml.common import *

# Sample restaurant data
restaurants = [
    {"name": "ไข่ข้นป้า - ตลาดกระบัง 46", "food": "อาหารตามสั่ง", "rating": 4.8, "distance": 5.7, "image": "egg.jpeg"},
    {"name": "ไข่ข้นป้า - ตลาดกระบัง 46", "food": "อาหารตามสั่ง", "rating": 4.8, "distance": 5.7, "image": "egg.jpeg"}
]

@app.get("/favorite")
def get():
    # Create list of restaurants
    items = []
    for restaurant in restaurants:
        items.append(
            Div(
                Div(
                    Img(src=f'/static/{restaurant["image"]}', alt=restaurant["name"], style="width: 100px; height: auto;"),
                    style="flex: 0 0 auto; margin-right: 15px;"
                ),
                Div(
                    Div(f"{restaurant['name']} - {restaurant['food']}", style="font-weight: bold;"),
                    Div(f"คะแนน: {restaurant['rating']} | ระยะทาง: {restaurant['distance']} km"),
                    style="flex: 1;"
                ),
                style="display: flex; align-items: center; margin-bottom: 15px;"
            )
        )

    # Back button image that leads back to home
    back_button = A(
        Img(src='/static/arrow.jpeg', alt="back", style="width: 30px; height: 30px; margin-right: 20px;"),  # รูปลูกศรที่คลิกได้
        href="/home"  # Link to home page
    )

    # Create navbar for navigation with back button on the left and navbar in the center
    navbar = Div(
        Div(back_button, style="flex: 0 0 auto;"),  # Back button on the left side
        Div(
            A("Home", href="/home", style="margin-right: 20px;"),
            A("Favorites", href="/favorite", style="margin-right: 20px;"),
            A("Promotions", href="/promotion", style="margin-right: 20px;"),
            A("Carts", href="/cart", style="margin-right: 20px;"),
            style="display: flex; justify-content: center; align-items: center; flex-grow: 1;"
        ),
        style="display: flex; align-items: center; margin-top: 10px; width: 100%;"
    )

    # Main content with navbar, back button, restaurant list, and message
    return Container(
        navbar,  # Navbar at the top with back button aligned to the left and navbar centered
        H1("Favourite Restaurants", style="font-weight: normal; margin-top : 35px;"),  # Title for favorites
        Div(*items, cls="restaurant-list"),
        Div("Looking for something else? Try searching or explore another category!", style="font-size: 14px; color: grey; text-align: center;")
    )