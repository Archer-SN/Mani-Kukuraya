from app import *
from models import *
from fasthtml.common import *

@app.get("/selectedFood/{id:str}")
def get(id: str):
    food = controller.get_food_by_id(id)

    form = Form(
        Input(id="food-id", name="food_id", type="hidden", value=f"{food.get_food_id()}"),
        # รูปภาพและรายละเอียดสินค้า
         Card(
            Img(src=food.get_image(), style="width: 120px; height: 120px; object-fit: cover; border-radius: 10px;"),
            Div(
                H2(food.get_name()),
                P(food.get_description()),
                H3(f"{food.get_price()} บาท", style="color: #ff5722;"),
            ),
            style="display: flex; align-items: center; gap: 15px;"
        ),
        # ตัวเลือกเพิ่มเติมจาก foodOption และ foodOptionChoices
        *[
            Div(
                H4(option.get_name()),
                *[
                    Div(
                        Input(type="checkbox", name=f"choices", value=choice.get_id(), id=f"option_{option.get_id()}_{choice.get_id()}"),
                        Label(choice.get_name(), for_=f"option_{option.get_id()}_{choice.get_id()}")
                    )
                    for choice in option.get_choices()
                ]
            )
            for option in food.get_food_options()
        ],
        # ความคิดเห็นเพิ่มเติม
        Fieldset(
            Legend("ความคิดเห็นถึงร้านค้า (Optional)"),
            Textarea(name="comment", placeholder="ใส่ข้อความถึงร้านค้า...")
        ),
        # ปุ่มเพิ่ม-ลดจำนวนสินค้า
        Div(
            Button("-", 
                hx_post="/update-quantity",  
                hx_target="#counter",  
                hx_swap="innerHTML",  
                hx_include="#counter-value"  # Include hidden input data
            ),

            Span("1", id="counter", style="margin: 0 10px; font-size: 1.5rem;"),  # Displays the number
            
            Button("+", 
                hx_post="/update-quantity",  
                hx_target="#counter",  
                hx_swap="innerHTML",  
                hx_include="#counter-value"  # Include hidden input data
            ),

    Input(id="counter-value", name="value", type="hidden", value="0"),  # Stores the current value
    Input(id="restaurant-id", name="restaurant_id", type="hidden", value=f"{food.get_restaurant().get_restaurant_id()}"),
    Script("""
        document.querySelectorAll('button').forEach(button => {
            button.addEventListener('click', () => {
                let counter = document.getElementById('counter');
                let counterInput = document.getElementById('counter-value');

                if (button.innerText === '+') {
                    counter.innerText = parseInt(counter.innerText) + 1;
                    counterInput.value = parseInt(counterInput.value) + 1;
                } else {
                    if (counterInput.value > 1) {
                        counter.innerText = parseInt(counter.innerText) - 1;
                        counterInput.value = parseInt(counterInput.value) - 1;
                    }
                }
            });
        });
    """),  # Updates the hidden input value before sending the request

    style="display: flex; justify-content: center; align-items: center; margin-top: 20px;"
),

        # ปุ่มเพิ่มลงตะกร้า
        Button("+ เพิ่มลงตะกร้า", type="submit",style="border: none; background-color: #ff5722; color: white;",
               hx_post="/add-to-cart", hx_target="#cart-message", hx_swap="outerHTML"),

        # ข้อความแสดงผลหลังจากกดเพิ่มลงตะกร้า
        Div(id="cart-message")
    )

    return Titled(
        "",
        Div(
            A("⬅ กลับ", href =f"/restaurant/{food.get_restaurant().get_restaurant_id()}", style="text-decoration: none; font-size: 18px; color: black; display: inline-block;"),
            style="position: absolute; top: 10px; left: 10px;"
    
        ),
        form
    )


@app.post("/update-quantity")
def update_quantity(value: int):
    if (value < 1):
        value = 1
    return Span(value, id="counter", style="margin: 0 10px; font-size: 1.5rem;")  # Displays the number

# If you want to check the request, just use request: dict

@app.post("/add-to-cart")
# def add_to_cart(req: dict):
def add_to_cart(food_id: str, choices: list[str], comment: str, value: str, restaurant_id: str):
    # print(req)
    food = controller.get_food_by_id(food_id)
    restaurant = controller.get_restaurant_by_id(restaurant_id)
    cart = user.get_cart_by_restaurant_id(restaurant_id)
    selected_food = SelectedFood(food, int(value))
    if cart == None:
        for choice_id in choices:
            choice = controller.get_choice_by_id(choice_id)
            selected_food.add_choice(choice)
        cart = Cart(restaurant)
        user.add_cart(cart)
    cart.add_to_cart(selected_food)
    return Response(headers={"HX-Redirect": f"/restaurant/{restaurant_id}"})

