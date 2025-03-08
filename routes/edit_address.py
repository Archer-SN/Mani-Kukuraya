from app import app
from models import *
from fasthtml.common import *

@app.get("/edit-address/{id}")
def address_view(id: str):
    location = user.get_location_by_id(id)
    if not location:
        return Div("ไม่พบข้อมูลที่อยู่", cls="error")

    return Main(
        Titled(
            "แก้ไขที่อยู่",
            Div(
                A("⬅ กลับ", href ="/locations", style="text-decoration: none; font-size: 18px; color: black; display: inline-block;"),
            style="position: absolute; top: 10px; left: 10px;"
            ),
            Section(
                Div(
                    Form(
                        Label("ชื่อ-นามสกุล", For="full_name"),
                        Input(name="full_name", required=True, value=location.full_name, placeholder="กรอกชื่อ-นามสกุล"),

                        Label("เบอร์โทรศัพท์มือถือ", For="phone"),
                        Input(name="phone", type="tel", required=True, value=location.phone_number, placeholder="กรอกเบอร์โทรศัพท์"),

                        Label("จังหวัด/เขต(อำเภอ)/รหัสไปรษณีย์/แขวง(ตำบล)", For="location"),
                        Input(name="location", required=True, value=location.address, placeholder="กรอกข้อมูลพื้นที่"),

                        Label("ถนน/ชื่ออาคาร", For="street"),
                        Input(name="street", required=True, value=location.street, placeholder="กรอกถนน/ชื่ออาคาร"),

                        Label("เลขที่ยูนิต/ชั้น", For="unit"),
                        Input(name="unit", value=location.unit or "-", placeholder="กรอกเลขที่ยูนิต/ชั้น"),

                        Label("ข้อมูลที่อยู่เพิ่มเติม (ถ้ามี)", For="extra_info"),
                        Input(name="extra_info", value=location.extra_information or "", placeholder="รายละเอียดเพิ่มเติม"),

                        Input(type="hidden", name="id", value=str(location.id)),

                        Div(
                            Button("บันทึกการเเก้ไข", type="submit", style="border: none; background-color: #ff5722; color: white;",
                                hx_post=f"/update-address/{location.id}", hx_target="#form-msg"),
                            cls="button-container"
                        ),

                        Div(id="form-msg", cls="text-center"),
                        cls="form-container"
                    ),cls="container"

                )
            )
        )
    )


@app.post("/update-address/{id}")
def submit_address(id:str, full_name: str, phone: str, address: str, street: str, unit: str = "", extra_info: str = ""):
    print(f"ข้อมูลที่ได้รับ: {full_name}, {phone}, {address}, {street}, {unit}, {extra_info}")  

    if not full_name or not phone or not address or not street:
        return Span("กรุณากรอกข้อมูลให้ครบถ้วน", cls="error")
    
    user.get_location_by_id(id).edit_location(full_name.strip(), phone.strip(), address.strip(), street.strip(), unit.strip(), extra_info.strip())
    if location is None:
        print(f"ไม่พบที่อยู่สำหรับ ID: {id}")  
        return Span("ไม่พบข้อมูลที่อยู่", cls="error")
    
    return Response(headers={"HX-Redirect": "/locations"})