from app import app
from models import *
from fasthtml.common import *

@app.get("/locations")
def saved_locations_page(user_id: str):
    user = controller.get_user_by_id(user_id)
        
    if not user:
        return Span("ไม่พบผู้ใช้ โปรดเข้าสู่ระบบ", cls="error")

    locations = user.get_locations() 

    if not locations:
        return Redirect(f"/address?user_id={user_id}")
    
    return Container(
        H2("สถานที่ที่บันทึกไว้", style="margin-top: 20px; border-bottom: 1px solid #ccc; padding-bottom: 10px;"),

        Div(
            Div(
                A("⬅ กลับ", href=f"/profile?user_id={user_id}", style="text-decoration: none; font-size: 18px; color: black; display: inline-block;"),
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
                            onclick=f"window.location.href='/edit-address/{location.id}?user_id={user_id}';"),

                    style="display: flex; align-items: center; gap: 10px; padding: 15px; border-bottom: 1px solid #ddd;"
                )
                for location in locations
            ]
        ),

        Div(
            A("+", href=f"/address?user_id={user_id}", cls="button outline circle large"),
            P("เพิ่มสถานที่ใหม่", cls="add-location-text"),
            cls="grid center"
        )
    )
