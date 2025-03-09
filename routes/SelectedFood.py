from app import *
from models import *
from fasthtml.common import *

@app.get("/selectedFood/{id:str}")
def get(id: str):
    food = controller.get_food_by_id(id)

    form = Form(
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
                        Input(type="radio", name=f"option_{option.get_id()}", value=choice.get_id(), id=f"option_{option.get_id()}_{choice.get_id()}"),
                        Label(choice.get_name(), for_=f"option_{option.get_id()}_{choice.get_id()}")
                    )
                    for choice in option.get_choices()
                ]
            )
            for option in food.get_food_options()
        ],
        # # ตัวเลือกเพิ่มเติมจาก foodOption และ foodOptionChoices
        # Fieldset(
        #     Legend("ตัวเลือกเพิ่มเติม"),
        #     *[
        #     Div(
        #         Input(type="radio", name=f"option_{option.get_id()}", value=choice.get_id(), id=f"option_{option.get_id()}_{choice.get_id()}"),
        #         Label(choice.get_name(), for_=f"option_{option.get_id()}_{choice.get_id()}")
        #     )
        #     for option in food.get_food_options()
        #     for choice in option.get_choices()
        #     ]
        # ),
        # # ตัวเลือกปริมาณ
        # Fieldset(
        #     Legend("ปริมาณ (Pick 1)"),
        #     Div(
        #         Input(type="radio", name="size", value="normal", id="size-normal", checked=True),
        #         Label("ธรรมดา (+0 บาท)", for_="size-normal"),
        #     ),
        #     Div(
        #         Input(type="radio", name="size", value="extra", id="size-extra"),
        #         Label("พิเศษ (+10 บาท)", for_="size-extra"),
        #     )
        # ),

        # # ตัวเลือกระดับรสชาติ
        # Fieldset(
        #     Legend("รสเผ็ด (Pick 1)"),
        #     Div(
        #         Input(type="radio", name="spicy", value="mild", id="spicy-mild", checked=True),
        #         Label("เผ็ดน้อย (+0 บาท)", for_="spicy-mild"),
        #     ),
        #     Div(
        #         Input(type="radio", name="spicy", value="medium", id="spicy-medium"),
        #         Label("เผ็ดกลาง (+10 บาท)", for_="spicy-medium"),
        #     ),
        #     Div(
        #         Input(type="radio", name="spicy", value="hot", id="spicy-hot"),
        #         Label("เผ็ดมาก (+20 บาท)", for_="spicy-hot"),
        #     )
        # ),

        # ความคิดเห็นเพิ่มเติม
        Fieldset(
            Legend("ความคิดเห็นถึงร้านค้า (Optional)"),
            Textarea(name="comment", placeholder="ใส่ข้อความถึงร้านค้า...")
        ),

        # ปุ่มเพิ่ม-ลดจำนวนสินค้า
        Div(
            Button("-", type="button", id="decrease", hx_post="/update-quantity", hx_target="#quantity", hx_vals='{"value": -1}'),
            Span("1", id="quantity", style="font-size: 28px; font-weight: bold; position: relative; top: -5px; margin: 0 20px;"),
            Button("+", type="button", id="increase", hx_post="/update-quantity", hx_target="#quantity", hx_vals='{"value": +1}'),
            style="display: flex; justify-content: center; align-items: center; margin: 10px 0;"
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
            A("⬅ กลับ", href ="/restaurant/1", style="text-decoration: none; font-size: 18px; color: black; display: inline-block;"),
            style="position: absolute; top: 10px; left: 10px;"
    
        ),
        form
    )


@app.post("/update-quantity")
def update_quantity(value: int):
    selected_food = ""
    return str(new_quantity)  



@app.post("/add-to-cart")
def add_to_cart():
    return Span("เพิ่มสินค้าลงตะกร้าแล้ว", cls="success")

