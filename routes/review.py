from app import app
from models import *
from fasthtml.common import *

# ✅ เก็บรีวิวที่ผู้ใช้ส่งมา
reviews = []

@app.post("/review")

def collect_review(restaurant_id: str):
    """ หน้าสำหรับเขียนรีวิวและแสดงความคิดเห็นที่มีอยู่แล้ว """
    restaurant = controller.get_restaurant_by_id(restaurant_id)
    return Container(
        H1("Review Page"),
        Card(
            Img(
                src=f"{restaurant.get_image()}",
                alt="Food Image",
                style="width: 200px; height: auto; border-radius: 8px; display: block; margin: 0 auto;"
            ),
            style="box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); padding: 20px; text-align: center;"
        ),
        # ✅ แสดงรายการรีวิว
        Div(
            *[P(f"💬 {review['comment']} - ⭐ {'★' * review['rating']}") for review in reviews],
            id="review-list",
            style="margin-top: 20px; padding: 10px; border-top: 1px solid #ddd;"
        ),
        # ✅ ฟอร์มสำหรับเพิ่มความคิดเห็นใหม่
        Form(
            Input(type="hidden", id="", name="restaurant_id", value=restaurant.get_restaurant_id()),  # ซ่อนค่า rating
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
            # ⭐ สร้างการเลือกดาว 1-5 ด้วยตัวอักษร ★
            Label(
                "Rating:",
                Div(
                    *[Span(
                        "★", 
                        id=f"star-{i}",
                        style=f"font-size: 30px; cursor: pointer; margin: 0 5px;", 
                        onclick=f"document.getElementById('rating').value = {i}; highlightStars({i})"
                    ) for i in range(1, 6)],
                    style="margin-top: 5px; display: flex; justify-content: center;"
                )
            ),
            Input(type="hidden", id="rating", name="rating", required=True),  # ซ่อนค่า rating
            Button(
                "Submit", 
                type="submit",
                hx_post="/submitreview", 
                hx_target="#review-list",  # ✅ อัปเดตส่วนที่แสดงความคิดเห็น
                hx_swap="beforeend",  # ✅ เพิ่มความคิดเห็นใหม่ด้านล่าง
                onclick="setTimeout(() => window.location.href = '/home', 500);",  # ✅ เปลี่ยนหน้าไปที่ /home หลังส่งข้อมูล
                style="margin-top: 10px; padding: 10px 20px; border: none; background-color: orange; color: white; cursor: pointer;"
            ),
            style="margin-top: 20px;"
        ),
        Script(
            """
            function highlightStars(selected) {
                for (let i = 1; i <= 5; i++) {
                    let star = document.getElementById('star-' + i);
                    if (i <= selected) {
                        star.style.color = 'gold';  // Highlight selected stars with gold color
                    } else {
                        star.style.color = 'gray';  // Dim unselected stars
                    }
                }
            }
            """
        )
    )

@app.post("/submitreview")
def submit_review(restaurant_id: str, comment: str, rating: int):
    restaurant = controller.get_restaurant_by_id(restaurant_id)
    """ บันทึกรีวิวและส่งกลับไปแสดงในหน้าเว็บ """
    restaurant.add_review(user,comment,rating)  # ✅ บันทึกความคิดเห็นใหม่พร้อมคะแนน
    return P(f"💬 {comment} - ⭐ {'★' * rating}")  # ✅ ส่ง HTML กลับไปแสดงความคิดเห็นใหม่พร้อมคะแนน