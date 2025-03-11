from app import app
from models import *
from fasthtml.common import *

# ✅ เก็บรีวิวที่ผู้ใช้ส่งมา
reviews = []
rating_state = 0

@app.get("/review")
def collect_review():
    picture_part = Div(
        Img(
            src="https://cdn.mos.cms.futurecdn.net/7NZogGkgY8PJiBEmBURazh-600-80.png.webp"
        )
    )

    review_form = Form(
        hx_post="/submit_review",
        hx_target="this",
        hx_swap="none",
        _children=[
            # ⭐ ส่วนดาวกดเลือก
            Div(
                *[
                    Button("★",
                        _style=(
                            "font-size: 40px; background: none; border: none; "
                            "cursor: pointer; color: #ccc; outline: none; box-shadow: none;"
                        ),
                        id=f"star-{i}"
                    )
                    for i in range(1, 6)
                ],
                id="star-container",
                _style="display: flex; gap: 10px; margin-bottom: 10px;"
            ),

            # ⭐ ช่องเก็บคะแนนที่เลือก
            Input(type="hidden", name="rating", id="rating_input"),

            # 💬 ฟอร์มความคิดเห็น
            Label("ความคิดเห็นของคุณ"),
            Textarea(
                name="comment",
                placeholder="พิมพ์ความคิดเห็นของคุณที่นี่...",
                _style="width: 300px; height: 100px; margin-bottom: 10px;"
            ),

            # ✅ ปุ่มส่งรีวิว
            Button("ส่งรีวิว", type="submit")
        ]
    )

    return Main(
        H1("Review", style="margin-left:40px;"),
        picture_part,
        review_form,

        # ⭐ Script ควบคุมดาว
        Script("""
            document.addEventListener('DOMContentLoaded', () => {
                const stars = document.querySelectorAll('#star-container button');
                stars.forEach((star, index) => {
                    star.addEventListener('click', () => {
                        document.getElementById('rating_input').value = index + 1;
                        stars.forEach((s, i) => {
                            s.style.color = i <= index ? '#FFD700' : '#ccc';
                        });
                    });
                });
            });
        """)
    )