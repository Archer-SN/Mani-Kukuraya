from app import *
from models import *  # Ensure this correctly imports Controller
from fasthtml.common import *

@app.get("/favorite/{id:str}")
def favorite_view(id:str):
    # Fetch restaurant by id
    restaurant = controller.get_restaurant_by_id(id)

    # Container to hold all food items
    food_list = []
    # Add "For You" section with "+" button to the right for other food items
    for food in restaurant.get_menu():
        food_item = Div(
            Div(
                Img(src=f"/static/{restaurant.get_image()}", alt="Food Image", style="width: 150px; height: 110px; margin-right: 20px; margin-left: 40px; border-radius: 10px;"),
                style="flex-shrink: 0; display: inline-block;"
            ),
            Div(
                H3(restaurant.get_name()),
                P(restaurant.get_description()),
                P(f"Price: {restaurant.get_score()} บาท"),
                style="display: inline-block; vertical-align: top;",
            ),
            style="display: flex; margin-bottom: 20px; align-items: center;"
        )
        food_list.append(food_item)

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
            A("Favorites", href="/favorite/1", style="margin-right: 20px;"),
            A("Promotions", href="/promotion", style="margin-right: 20px;"),
            A("Carts", href="/cart", style="margin-right: 20px;"),
            style="display: flex; justify-content: center; align-items: center; flex-grow: 1;"
        ),
        style="display: flex; align-items: center; margin-top: 10px; width: 100%;"
    )

    # Combine all parts into one container
    page_content = Container(
        navbar,
        Section(
            H1("Favourite Restaurants", cls="text-center", style="margin-top: 20px;"),  
            Div(*food_list, cls="food-list")
        ),
        Section(
            Div("Looking for something else? Try searching or explore another category!", style="font-size: 14px; color: grey; text-align: center;")
        )
    )
    
    # Return the complete page content
    return page_content