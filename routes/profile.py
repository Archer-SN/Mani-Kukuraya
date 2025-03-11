from app import app
from models import *
from fasthtml.common import *

@app.get("/profile")
def profile():
    user = controller.get_user_by_id("1")

    if not user:
        return Span("ไม่พบผู้ใช้ โปรดเข้าสู่ระบบ", cls="error")

    return Container(
        A("⬅ กลับ", href=f"/home", style="font-size: 24px; color: #333; text-decoration: none; position: absolute; top: 20px; left: 20px;"),

        Div(
            Img(
                src="https://img.freepik.com/free-vector/blue-circle-with-white-user_78370-4707.jpg",
                alt="Profile Picture",
                style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover;"
            ),
            H2(user.name, style="margin-top: 10px; color: #222; font-weight: 600;"),
            P("เเกร็ปยังต้องกลัว", style="color: #777; font-size: 14px;"),
            style="display: flex; flex-direction: column; align-items: center; margin-top: 40px;"
        ),

        Div(
            A(
                Div(
                    Img(src="https://cdn-icons-png.flaticon.com/512/1077/1077035.png", width="40px"),  
                    P("รายการโปรด", style="font-size: 14px; margin-top: 5px; color: #444;"),
                    style="display: flex; flex-direction: column; align-items: center;"
                ),
                href=f"/favorite",
                cls="profile-menu-item"
            ),

            A(
                Div(
                    Img(src="https://cdn-icons-png.flaticon.com/512/747/747376.png", width="40px"),
                    P("จัดการบัญชี", style="font-size: 14px; margin-top: 5px; color: #444;"),
                    style="display: flex; flex-direction: column; align-items: center;"
                ),
                href=f"/account",
                cls="profile-menu-item"
            ),

            A(
                Div(
                    Img(src="https://cdn-icons-png.flaticon.com/512/684/684908.png", width="40px"),
                    P("ที่อยู่ของฉัน", style="font-size: 14px; margin-top: 5px; color: #444;"),
                    style="display: flex; flex-direction: column; align-items: center;"
                ),
                href=f"/locations",
                cls="profile-menu-item"
            ),

            style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; max-width: 400px; margin: auto; margin-top: 30px;"
        ),
        Style("""
            .profile-menu-item {
                text-align: center;
                padding: 15px;
                background: white;
                border-radius: 12px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
                transition: transform 0.2s ease-in-out;
                text-decoration: none;
            }
            .profile-menu-item:hover {
                transform: translateY(-3px);
                box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
            }
        """)
    )
