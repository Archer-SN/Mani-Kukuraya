from app import *
from models import *
from fasthtml.common import *

@app.get("/address")
def address_view():
    form = Form(
        Label("ชื่อ-นามสกุล"),
        Input(id="full_name", name="full_name", required=True, placeholder="กรอกชื่อ-นามสกุล",
              hx_post="/validate-field", hx_target="#err_full_name", hx_trigger="blur"),
        Span("", cls="error", id="err_full_name"),

        Label("เบอร์โทรศัพท์มือถือ"),
        Input(id="phone", name="phone", type="tel", required=True, placeholder="กรอกเบอร์โทรศัพท์",
              hx_post="/validate-field", hx_target="#err_phone", hx_trigger="blur"),
        Span("", cls="error", id="err_phone"),

        Label("จังหวัด/เขต(อำเภอ)/รหัสไปรษณีย์/แขวง(ตำบล)"),
        Input(id="location", name="location", required=True, placeholder="กรอกข้อมูลพื้นที่",
              hx_post="/validate-field", hx_target="#err_location", hx_trigger="blur"),
        Span("", cls="error", id="err_location"),

        Label("ถนน/ชื่ออาคาร"),
        Input(id="street", name="street", required=True, placeholder="กรอกถนน/ชื่ออาคาร",
              hx_post="/validate-field", hx_target="#err_street", hx_trigger="blur"),
        Span("", cls="error", id="err_street"),

        Label("เลขที่ยูนิต/ชั้น"),
        Input(id="unit", name="unit", placeholder="ระบุเลขที่ยูนิต/ชั้น"),

        Label("ข้อมูลที่อยู่เพิ่มเติม (ถ้ามี)"),
        Textarea(id="extra_info", name="extra_info", placeholder="รายละเอียดเพิ่มเติม"),

        Div(
            Button("บันทึก", type="submit", style="border: none; background-color: #ff5722; color: white;",
                hx_post="/submit-address", hx_target="#form-msg", hx_swap="outerHTML"),
            style="margin-top: 20px;"
        ),

        Div(id="form-msg")  # สำหรับแสดงผลลัพธ์
    )

    return Titled(
        "เพิ่มที่อยู่ใหม่",
        Div(
            AX("⬅ กลับ", "/", "body", style="text-decoration: none; font-size: 18px; color: black; display: inline-block;"),
            style="position: absolute; top: 10px; left: 10px;"
        ),
        form
    )

@app.get("/submit-address", methods=["POST"])
def submit_address(full_name: str, phone: str, location: str, street: str, unit: str = "", extra_info: str = ""):
    print(f"ข้อมูลที่ได้รับ: {full_name}, {phone}, {location}, {street}, {unit}, {extra_info}")  

    if not full_name or not phone or not location or not street:
        return Span("กรุณากรอกข้อมูลให้ครบถ้วน", cls="error")

    return Span("บันทึกที่อยู่สำเร็จ!", cls="success")
