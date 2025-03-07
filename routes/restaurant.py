from app import *
from models import *
from fasthtml.common import *
from lucide_fasthtml import Lucide

@app.get("/restaurant/{id:str}")
def restaurant_view(id: str):
    restaurant = controller.get_restaurant_by_id(id)
    # Container to hold all food items
    food_list = []

    # Add main food item card at the top (with border for "ไข่ขนป้า")
    main_food_card = Div(
        Div(
            Img(src=f"/static/{restaurant.get_image()}", alt="Food Image", style="width: 200px; height: auto; margin-right: 40px; border-radius: 10px;"),
            style="flex-shrink: 0; display: inline-block;"
        ),
        Div(
            H2(restaurant.get_name()),
            P(restaurant.get_description()),
            P(f"Rating: {restaurant.get_score()} | Distance: "),
            style="display: inline-block; vertical-align: top;",
        ),
        style="display: flex; align-items: center; justify-content: center; margin-bottom: 20px; border: 2px solid orange; padding: 20px;",  # Added border, padding, and centered content
        cls="main-food-item-card"
    )

    # Adding an image button at the top (as requested)
    img_button = A(
        Lucide("heart", 24, color="black"),
        hx_post="/favorite/1",  # Define the action when the image is clicked
        style="position: absolute; top: 10px; right: 10px;",  # Position the image button at the top-right corner of the container
        hx_target="this"
    )

    # Add "For You" section with "+" button to the right for other food items
    for food in restaurant.get_menu():
        food_item = Div(
            Div(
                Img(src=f"{food.get_image()}", alt="Food Image", style="width: 150px; height: 110px; margin-right: 20px; margin-left: 40px; border-radius: 10px;"),
                style="flex-shrink: 0; display: inline-block;"
            ),
            Div(
                H3(food.get_name()),
                P(food.get_description()),
                P(f"Price: {food.get_price()} บาท"),
                style="display: inline-block; vertical-align: top;",
            ),
            Button("+", 
                hx_redirect="/log_input",
                hx_post="/log_input",  # Send data to the backend using HTMX
                hx_params=f"food_name={food.get_name()}&restaurant_name={food.get_name()}",  # Send food name and restaurant name
                style="padding: 10px; font-size: 17px; background-color: #4CAF50; color: white; border: none; margin-left: auto; margin-right: 130px; border-radius: 5px;"),
            style="display: flex; align-items: center; margin-bottom: 15px; justify-content: space-between;",  # Align "+" button to the right
            cls="food-item-card"
        )
        food_list.append(food_item)

    # Search input and confirm button inside a form
    search_input = Input(id="search-query", name="search_query", placeholder="Search food...", style="width: 200px; padding: 8px; margin-left: 10px;")
    confirm_button = Button("Confirm", type="submit", style="padding: 8px 16px; font-size: 16px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; margin-left: 10px;")

    # Form that wraps the search input and button
    search_form = Form(
        search_input,
        confirm_button,
        action="/send_input",  # The route to handle the form submission
        method="post"  # This makes the form use POST
    )

    # Div that contains "For You" and the search form
    for_you_section = Div(
        H3("For You"),
        search_form,  # Wrap the input and button in the form
        style="display: flex; align-items: center; justify-content: space-between; margin-top: 20px; margin-right: 40px; margin-left: 40px;"
    )

    # Combine all parts into one container
    page_content = Container(
        main_food_card,  # Display main food card with border around it
        img_button,  # Display the image button
        for_you_section,  # Display the "For You" section with search input and button
        *food_list  # Display other food items with "+" button
    )

    return page_content

@app.post("/send_input")
def send_input(search_query: str):
    # Print the text entered in the input box to the terminal
    print(f"User input: {search_query}")
    # Returning a response to clear the input (simulating the 'disappear' functionality)
    return RedirectResponse("/restaurant/1", status_code=303)

# Make the `log_input` function asynchronous
@app.post("/log_input")
async def log_input(request: Request):
    # Retrieve the form data from the request
    form_data = await request.form()
    food_name = form_data.get("food_name")
    restaurant_name = form_data.get("restaurant_name")
    
    # Log the captured information to the terminal
    print(f"Food Name: {food_name} from Restaurant: {restaurant_name}")  # This will print to the terminal
    
    # Return a simple redirect or empty response to the user
    return Response(headers={"HX-Redirect": "/selectedFood"})

@app.post("/favorite/{id}")
def add_favorite(id: int):
    # Add restaurant to favorites
    user.add_favorite(id)
    
    # Print the current list of favorites after adding
    print("Favorites after adding:", user.get_favorites())  # Assuming `get_favorites` is a method in `user` that returns the list of favorites
    
    # Return a red heart icon and set it for removal
    return A(
        Lucide("heart", 24, color="red"),
        hx_delete=f"/favorite/{id}",  # Use DELETE request to remove it when clicked
        style="position: absolute; top: 10px; right: 10px;",  # Position the image button at the top-right corner of the container
        hx_target="this",  # Update this element when the action is performed
        hx_swap="outerHTML"  # Swap the entire element with the response (so it changes the icon to red)
    )

@app.delete("/favorite/{id}")
def remove_favorite(id: int):
    # Remove restaurant from favorites
    user.remove_favorite(controller.get_restaurant_by_id(id))
    
    # Print the current list of favorites after removing
    print("Favorites after removing:", user.get_favorites())  # Assuming `get_favorites` is a method in `user` that returns the list of favorites
    
    # Return a black heart icon and set it for addition
    return A(
        Lucide("heart", 24, color="black"),
        hx_post=f"/favorite/{id}",  # Use POST request to add it back when clicked
        style="position: absolute; top: 10px; right: 10px;",  # Position the image button at the top-right corner of the container
        hx_target="this",  # Update this element when the action is performed
        hx_swap="outerHTML"  # Swap the entire element with the response (so it changes the icon to black)
    )