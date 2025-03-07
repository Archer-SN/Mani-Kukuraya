from app import *
from models import *
from fasthtml.common import *

@app.get("/home")
def ShowHomepage():
    catagories = catagory_from_controller
    catagory_element = [
        A(
            Img(src="catagory[img]",alt="catagory[name]",style="width:100%;height:100%;"
                ,herf="catagory[herf]",style="display:block; text-align:center;"),
        )
        for category in catagories
    ]
    numbers_promotion = numbers_promotion_from_controller
    promotion_element = Card(
        H3("โปรโมชั่น{numbers_promotion}",style="text-align:center;"),
        style="width:100%;height:100%;"
    )
    search_bar = Input("text",placeholder="ค้นหา",style="width:100%;height:100%;")
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
        promotion_element,
        search_bar_element,
        style="text-align:center;"
    )
    
        