from app import app
from models import *
from fasthtml.common import *

@app.get("/account")
def account_management(user_id, sess):
    user = controller.get_user_by_username(sess["auth"])

    if not user:
        return Span("ไม่พบผู้ใช้ โปรดเข้าสู่ระบบ", cls="error")

    return Container(
        Div(
            A("⬅ กลับ", href=f"/profile", style="text-decoration: none; font-size: 18px; color: black; display: inline-block;"),
            style="position: absolute; top: 10px; left: 10px;"
        ),
        H2("การจัดการบัญชี", style="margin-top: 20px;"),

        Card(
            H4("ชื่อผู้ใช้", style="color: gray;"),
            Div(
                P(user.name, id="username_display", style="font-size: 18px; margin-left: 25px;"),
                style="display: flex;"
            ),
            H4("รหัสผ่าน", style="color: gray; margin-top: 20px;"),
            Div(
                P("●●●●●●●●", id="password_display", style="font-size: 18px;margin-left: 25px;"),
            ),
            style="padding: 20px; margin-top: 20px;"
        ),

        Form(
            H3("แก้ไขชื่อผู้ใช้"),
            Input(type="text", name="new_username", placeholder="ชื่อผู้ใช้ใหม่", required=True),
            Input(type="hidden", name="user_id", value=user_id),  # ส่ง user_id ไปด้วย
            Button("บันทึก", type="submit",
                   hx_post="/update-username", hx_target="#username_display", hx_swap="outerHTML"),
        ),
        Dialog(id="editUsername"),

        Form(
            H3("เปลี่ยนรหัสผ่าน"),
            Input(type="password", name="new_password", placeholder="รหัสผ่านใหม่", required=True),
            Input(type="hidden", name="user_id", value=user_id),  # ส่ง user_id ไปด้วย
            Button("บันทึก", type="submit",
                   hx_post="/update-password", hx_target="#password_display", hx_swap="outerHTML"),
        ),
        Dialog(id="editPassword"),
    )

@app.post("/update-username")
def update_username(user_id: str, new_username: str, ses):
    user = controller.get_user_by_username(sess["auth"])
    
    if not user:
        return Span("ไม่พบผู้ใช้ โปรดเข้าสู่ระบบ", cls="error")

    if not new_username:
        return Span("กรุณากรอกชื่อผู้ใช้ใหม่", cls="error")

    user.set_name(new_username)
    
    return P(new_username, id="username_display", style="font-size: 18px; margin-left: 25px;")

@app.post("/update-password")
def update_password(user_id: str, new_password: str, sess):
    user = controller.get_user_by_username(sess["auth"])
    
    if not user:
        return Span("ไม่พบผู้ใช้ โปรดเข้าสู่ระบบ", cls="error")

    if not new_password:
        return Span("กรุณากรอกรหัสผ่านใหม่", cls="error")

    user.set_password(new_password)

    return P("●●●●●●●●", id="password_display", style="font-size: 18px; color: red; margin-left: 25px;")
