from app import *
from models import *
from fasthtml.common import *

@app.get("/address")
def address_view():
    form = Form(
        Label("ชื่อ-นามสกุล"),
        Input(name="full_name", required=True, placeholder="กรอกชื่อ-นามสกุล",hx_target="#full_name", hx_trigger="blur"),

        Label("เบอร์โทรศัพท์มือถือ"),
        Input(name="phone", type="tel", required=True, placeholder="กรอกเบอร์โทรศัพท์",hx_target="#phone", hx_trigger="blur"),

        Label("จังหวัด/เขต(อำเภอ)/รหัสไปรษณีย์/แขวง(ตำบล)"),
        Input(name="location", required=True, placeholder="กรอกข้อมูลพื้นที่", hx_target="#location", hx_trigger="blur"),

        Label("ถนน/ชื่ออาคาร"),
        Input(name="street", required=True, placeholder="กรอกถนน/ชื่ออาคาร", hx_target="#street", hx_trigger="blur"),

        Label("บ้านเลขที่/ชั้น"),
        Input(name="unit", required=False, placeholder="กรอกบ้านเลขที่/ชั้น", hx_target="#unit", hx_trigger="blur"),

        Label("ข้อมูลเพิ่มเติม (ถ้ามี)"),
        Input(name="extra_info", required=False, placeholder="รายละเอียดเพิ่มเติม",hx_target="#extra_info", hx_trigger="blur"),
        
        Button("บันทึก", type="submit", style="border: none; background-color: #ff5722; color: white;",
               hx_post="/submit-address", hx_target="#form-msg"),

        Div(id="form-msg")
    )


    return Titled(
        "เพิ่มที่อยู่ใหม่",
        Div(
            A("⬅ กลับ", href ="/locations", style="text-decoration: none; font-size: 18px; color: black; display: inline-block;"),
            style="position: absolute; top: 10px; left: 10px;"
    
        ),
        form
    )

@app.post("/submit-address")
def submit_address(full_name: str, phone: str, address: str, street: str, unit: str = "", extra_info: str = ""):

    if not full_name or not phone or not address or not street:
        return Span("กรุณากรอกข้อมูลให้ครบถ้วน", cls="error")
    
    user.add_location(Location(full_name, phone, address, street, unit, extra_info))
    return Response(headers={"HX-Redirect": "/locations"})

