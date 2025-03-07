from app import app
from models import *
from fasthtml.common import *

# ✅ เก็บรีวิวที่ผู้ใช้ส่งมา
reviews = []

@app.get("/review")
def collect_review():
    """ หน้าสำหรับเขียนรีวิวและแสดงความคิดเห็นที่มีอยู่แล้ว """

    return Container(
        H1("Review Page"),
        Card(
            Img(
                src="https://static.thairath.co.th/media/dFQROr7oWzulq5Fa6rHIRiYHCRigP4Gyivh7rgX5F5HqUmbf9L4SQODbALPtARByTGY.webp",
                alt="Food Image",
                style="width: 200px; height: auto; border-radius: 8px; display: block; margin: 0 auto;"
            ),
            H3("Your Food"),
            style="box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); padding: 20px; text-align: center;"
        ),
        # ✅ แสดงรายการรีวิว
        Div(
            *[P(f"💬 {review}") for review in reviews],
            id="review-list",
            style="margin-top: 20px; padding: 10px; border-top: 1px solid #ddd;"
        ),
        # ✅ ฟอร์มสำหรับเพิ่มความคิดเห็นใหม่
        Form(
            Label(
                "Comment:",
                Input(
                    type="text", 
                    id="comment",
                    name="comment", 
                    required=True,
                    placeholder="Type your comment here...",
                    style="width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px; margin-top: 5px;"
                )
            ),
            Button(
                "Submit", 
                type="submit",
                hx_post="/submitreview", 
                hx_target="#review-list",  # ✅ อัปเดตส่วนที่แสดงความคิดเห็น
                hx_swap="beforeend",  # ✅ เพิ่มความคิดเห็นใหม่ด้านล่าง
                style="margin-top: 10px; padding: 10px 20px; border: none; background-color: orange; color: white; cursor: pointer;"
            ),
            style="margin-top: 20px;"
        )
    )

@app.post("/submitreview")
def submit_review(comment: str):
    """ บันทึกรีวิวและส่งกลับไปแสดงในหน้าเว็บ """
    reviews.append(comment)  # ✅ บันทึกความคิดเห็นใหม่
    print(f"📌 รีวิวใหม่: {comment}")

    return P(f"💬 {comment}")  # ✅ ส่ง HTML กลับไปแสดงความคิดเห็นใหม่
