from app import *
from models import *
from fasthtml.common import *

@app.get("/home")
def ShowHomepage():
    catagories = Controller.get_numbers_catagories()
    catagory_element = [
        A(
            Div(
                Img(src=category[1], style="width:100%;height:50%;"),
                P(category[0], style="text-align:center; margin-top: 10px;"),
                style="text-align:center;"
            ),
            style="display:block; text-align:center; margin: 10px;"
        )
        for category in catagories
    ]
    numbers_promotion = 10
    promotion_element = Card(
        H3("โปรโมชั่น",style="text-align:left;"),
        Div(
            *[
                P(f"โปรโมชั่นที่คุณมี {numbers_promotion}",style="text-align:left;")
            ],
            style="text-align:left;"
        ),
        style="width:30%;height:20%;margin-top:10px;"

    )
    search_bar = Input(type="text",name = "query", placeholder="ค้นหาอาหาร", style="width: 80%; height: 100%; display: inline-block;margin-right:10px;")
    search_button = Button("ค้นหา",type="submit", style="width: 30%; height: 100%; display: inline-block;")
    search_bar_element = Form(
        search_bar,
        search_button,
        action="/search",
        method="get",
        style="position: absolute; top: 20px; right: 20px; width: 300px; height: 40px; display: flex;"
    )

    return Container(
        Div(
            search_bar_element
        ),
        Div(
            *catagory_element,
            style="display:flex;flex-wrap:wrap;justify-content:space-around;margin-top:200px;"
        ),
        promotion_element,
        
        style="text-align:center;"
    )
@app.get("/search")
def SearchResults(query: str):
    # Implement your search logic here
    search_results = Controller.search_food(query)
    search_results_elements = [
        Div(
            P(result["name"], style="text-align:center;"),
            Img(src=result["image"], style="width:100%;height:50%;"),
            style="text-align:center; margin: 10px;"
        )
        for result in search_results
    ]
    return Container(
        H1(f"ผลการค้นหาสำหรับ '{query}'"),
        Div(
            *search_results_elements,
            style="display:flex;flex-wrap:wrap;justify-content:space-around;margin-top:20px;"
        ),
        style="text-align:center;"
    )
    
        