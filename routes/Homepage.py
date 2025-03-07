from app import *
from models import *
from fasthtml.common import *

@app.get("/home")
def ShowHomepage():
    catagories = Controller.get_numbers_catagories()
    catagory_element = [
        A(
<<<<<<< HEAD
            Img(src="catagory[img]",alt="catagory[name]",style="width:100%;height:100%;"
                ,href="catagory[herf]"),
=======
            Img(src=category[1],alt=category[0],style="width:5%;height:40%;"),
>>>>>>> 8e98389cd44e815b94eb34f70724dbc503072dd4
        )
        for category in catagories
    ]
    numbers_promotion = 10
    promotion_element = Card(
        H3("โปรโมชั่น",style="text-align:left;"),
        Div(
            *[
                P("โปรโมชั่นที่ ",str(i+1),style="text-align:left;")
                for i in range(numbers_promotion)
            ],
            style="text-align:left;"
        ),
        style="width:30%;height:20%;"

    )
    search_bar = Input("ค้นหาอาหาร",placeholder="ค้นหา",style="width:100%;height:100%;")
    search_button = Button("ค้นหา",style="width:100%;height:100%;")
    search_bar_element = Form(
        search_bar,
        search_button,
        style="width:100%;height:100%;"
    )

    return Container(
        H1("หน้าหลัก"),
        Div(
            *catagory_element,
            style="display:flex;flex-wrap:wrap;justify-content:space-around;"
        ),
        Div(
            search_bar_element
        ),
        promotion_element,
        
        style="text-align:center;"
    )
    
        