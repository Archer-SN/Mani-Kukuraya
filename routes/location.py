from app import app
from models import *
from fasthtml.common import *


@app.get("/locations")
def saved_locations_page():
    locations = user.get_locations() 
    return Container(
        H2("สถานที่ที่บันทึกไว้", style="margin-top: 20px; border-bottom: 1px solid #ccc; padding-bottom: 10px;"),

        Div(
            Div(
                  A("⬅ กลับ", href ="/profile", style="text-decoration: none; font-size: 18px; color: black; display: inline-block;"),
                style="position: absolute; top: 10px; left: 10px;"
                ),
            *[
                Div(
                    Img(src="https://cdn-icons-png.flaticon.com/512/684/684908.png",
                        style="width: 40px; height: 40px; margin-right: 15px;"),

                    Div(
                        Div(
                            H3(location.full_name, style="margin: 0; font-weight: bold; display: inline-block;"),
                            Span(location.phone_number, style="margin-left: 10px; color: gray; font-size: 14px;"),
                            style="display: flex; align-items: center;"
                        ),
                        P(f"{location.address} {location.street} {location.unit} {location.extra_information}",
                          style="color: gray; font-size: 14px; margin: 0; line-height: 1.5;"),
                        style="flex: 1;"
                    ),

                    Button("⋮", type="button", 
                            style="background: none; border: none; font-size: 20px; cursor: pointer; color: gray;",
                            onclick=f"window.location.href='/edit-address/{location.id}';"),

                    style="display: flex; align-items: center; gap: 10px; padding: 15px; border-bottom: 1px solid #ddd;"
                )
                for location in locations
            ]
        ) if locations else P("ไม่มีสถานที่ที่บันทึกไว้", style="color: gray; text-align: center;"),

        Div(
            Button("+", type="button",
                   style="width: 40px; height: 40px; border-radius: 50%; font-size: 24px; background: none; border: 2px solid gray; color: gray; cursor: pointer;",
                   onclick="window.location.href='/address';"),
            P("เพิ่มสถานที่ใหม่", style="color: gray; font-size: 16px;"),
            style="display: flex; align-items: center; gap: 10px; padding: 15px; cursor: pointer;",
        ),
    )
