from app import app
from models import *
from fasthtml.common import *


@app.get("/")
def CollectReview():
    return Titled(
        "Review Page",
        Style("body { background-color: white; }"),  # ตั้งค่า Background เป็นสีขาว

        Container(
            # Card ที่ 1 - แสดงการจัดการ Text และ Border
            Div(
                Form(
                    Label("Comment:"),
                    Input(type="text", style="margin: 10px; width: 50%;height:100px ; font-size: 20px;"""),
                    style="border: 3px solid #2196f3; border-radius: 10px; margin: 10px; width: 80%; height: 100%;"
                ),
                # style="""
                #     border: 3px solid #2196f3;
                #     border-radius: 10px;
                #     margin: 10px;
                #     width: 80%;
                #     height: 100%;
                # """
            ),
            Div(# สร้างปุ่มเพื่อเข้าไปยังหน้าเพิ่มรีวิว
                Button("Submit", style="margin: 10px 0px;"),
                style="margin: 10px 0px;",
            ),
        )
    )



