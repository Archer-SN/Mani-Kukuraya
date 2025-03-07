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
                        Input(id="full_name", name="full_name", required=True, value=location.full_name, placeholder="กรอกชื่อ-นามสกุล"),

                        Label("เบอร์โทรศัพท์มือถือ", For="phone"),
                        Input(id="phone", name="phone", type="tel", required=True, value=location.phone_number, placeholder="กรอกเบอร์โทรศัพท์"),

                        Label("จังหวัด/เขต(อำเภอ)/รหัสไปรษณีย์/แขวง(ตำบล)", For="location"),
                        Input(id="location", name="location", required=True, value=location.address, placeholder="กรอกข้อมูลพื้นที่"),

                        Label("ถนน/ชื่ออาคาร", For="street"),
                        Input(id="street", name="street", required=True, value=location.street, placeholder="กรอกถนน/ชื่ออาคาร"),

                        Label("เลขที่ยูนิต/ชั้น", For="unit"),
                        Input(id="unit", name="unit", value=location.unit or "-", placeholder="กรอกเลขที่ยูนิต/ชั้น"),

                        Label("ข้อมูลที่อยู่เพิ่มเติม (ถ้ามี)", For="extra_info"),
                        Input(id="extra_info", name="extra_info", value=location.extra_information or "", placeholder="รายละเอียดเพิ่มเติม"),

                        Input(type="hidden", name="id", value=str(location.id)),

                        Div(
                            Button("บันทึกการแก้ไข", type="submit", cls="primary-button full-width",
                                hx_post="/update-address", hx_target="#form-msg"),
                            cls="button-container"
                        ),

                        Div(id="form-msg", cls="text-center"),
                        cls="form-container"
                    ),cls="container"

                )
            )
        )
    )


@app.post("/update-address")
def update_address(request):
    form_data = request.form() 
    location_id = form_data.get("id", "").strip()  

    full_name = form_data.get("full_name", "").strip()
    phone = form_data.get("phone", "").strip()
    location = form_data.get("location", "").strip()
    street = form_data.get("street", "").strip()
    unit = form_data.get("unit", "").strip()
    extra_info = form_data.get("extra_info", "").strip()

    if not location_id or not full_name or not phone:
        return Span("กรุณากรอกข้อมูลให้ครบถ้วน", cls="error")

    for loc in user.get_locations():
        if str(loc.id) == location_id:
            loc.full_name = full_name
            loc.phone_number = phone
            loc.address = location
            loc.street = street
            loc.unit = unit
            loc.extra_information = extra_info
            return Response(headers={"HX-Redirect": "/locations"}) 

    return Span("ไม่พบข้อมูลที่อยู่", cls="error")
