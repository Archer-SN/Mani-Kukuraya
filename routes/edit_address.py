from app import app
from models import *
from fasthtml.common import *

@app.get("/edit-address/{id}")
def address_view(id: str):
    location = user.get_location_by_id(id)
    if not location:
        return Div("ไม่พบข้อมูลที่อยู่", cls="error")

    form = Form(
        Label("ชื่อ-นามสกุล"),
        Input(id="full_name", name="full_name", required=True, value=location.full_name, placeholder="กรอกชื่อ-นามสกุล",hx_target="#full_name", hx_trigger="blur"),

        Label("เบอร์โทรศัพท์มือถือ"),
        Input(id="phone", name="phone", type="tel", required=True,  value=location.phone_number,placeholder="กรอกเบอร์โทรศัพท์",hx_target="#phone", hx_trigger="blur"),

        Label("จังหวัด/เขต(อำเภอ)/รหัสไปรษณีย์/แขวง(ตำบล)"),
        Input(id="address", name="address", required=True, value=location.address, placeholder="กรอกข้อมูลพื้นที่", hx_target="#location", hx_trigger="blur"),

        Label("ถนน/ชื่ออาคาร"),
        Input(id="street", name="street", required=True, value=location.street, placeholder="กรอกถนน/ชื่ออาคาร", hx_target="#street", hx_trigger="blur"),

        Label("บ้านเลขที่/ชั้น"),
        Input(id="unit", name="unit", required=False, value=location.unit or "-",placeholder="กรอกบ้านเลขที่/ชั้น", hx_target="#unit", hx_trigger="blur"),

        Label("ข้อมูลเพิ่มเติม (ถ้ามี)"),
        Input(id="extra_info", name="extra_info", required=False, value=location.extra_information or "", placeholder="รายละเอียดเพิ่มเติม",hx_target="#extra_info", hx_trigger="blur"),
        
        Input(type="hidden", name="id", value=str(location.id)), 
        Button("บันทึก", type="submit", style="border: none; background-color: #ff5722; color: white;",
               hx_post=f"/update-address/{location.id}", hx_target="#form-msg"),

        Div(id="form-msg"),
    )


    return Titled(
        "เพิ่มที่อยู่ใหม่",
        Div(
            A("⬅ กลับ", href ="/locations", style="text-decoration: none; font-size: 18px; color: black; display: inline-block;"),
            style="position: absolute; top: 10px; left: 10px;"
    
        ),
        form
    )



@app.post("/update-address/{id}")
def submit_address(id:str, full_name: str, phone: str, address: str, street: str, unit: str = "", extra_info: str = ""):
    print(f"ข้อมูลที่ได้รับ: {full_name}, {phone}, {address}, {street}, {unit}, {extra_info}")  

    if not full_name or not phone or not address or not street:
        return Span("กรุณากรอกข้อมูลให้ครบถ้วน", cls="error")
    
    if user.get_location_by_id(id) is None:
        print(f"ไม่พบที่อยู่สำหรับ ID: {id}")  
        return Span("ไม่พบข้อมูลที่อยู่", cls="error")
    
    user.get_location_by_id(id).edit_location(full_name.strip(), phone.strip(), address.strip(), street.strip(), unit.strip(), extra_info.strip())

    
    return Response(headers={"HX-Redirect": "/locations"})