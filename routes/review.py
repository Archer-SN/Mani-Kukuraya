from app import app
from models import *
from fasthtml.common import *



@app.get("/review")
def collect_review():
    """ หน้าสำหรับเขียนรีวิวและแสดงความคิดเห็นที่มีอยู่แล้ว """

    return Container(
        H1("รีวิวอาหารกันหน่อยยสิ"),
        Card(
            Img(
                src="https://static.thairath.co.th/media/dFQROr7oWzulq5Fa6rHIRiYHCRigP4Gyivh7rgX5F5HqUmbf9L4SQODbALPtARByTGY.webp",
                alt="Food Image",
                style="width: 200px; height: auto; border-radius: 8px; display: block; margin: 0 auto;"
            ),
            P("อาหารที่คุณซื้อ",style="color: #875; font-size: 16px; line-height: 1.5; margin-top: 10px;"),
            style="box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); padding: 20px; text-align: center;"
        ),
        # ✅ ฟอร์มสำหรับเพิ่มความคิดเห็นใหม่
        Form(
            Div(
                Label("Rating:"),
                Div(
                    *[
                        Input(
                            type="radio",
                            id=f"star-{i}",
                            name="rating",
                            value=str(i),
                            style="display: none;"
                        ) for i in range(5, 0, -1)
                    ],
                    *[
                        Label(
                            "★",
                            **{
                                "for": f"star-{i}"
                            },
                            style=(
                                "font-size: 24px; color: #ccc; cursor: pointer; margin: 0 5px;"
                            )
                        ) for i in range(5, 0, -1)
                    ],
                    style="display: flex; flex-direction: row-reverse; justify-content: flex-end; gap: 5px;"
                ),
                style="margin-bottom: 10px;"
            ),
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
                hx_include="closest form",
                style="margin-top: 10px; padding: 10px 20px; border: none; background-color: orange; color: white; cursor: pointer;"
            ),
            style="margin-top: 20px;"
        ),
        Script("""
            const stars = document.querySelectorAll('label[for^="star-"]');
            const radios = document.querySelectorAll('input[name="rating"]');
        
            function updateStars(selectedValue) {
                stars.forEach(label => {
                    const value = parseInt(label.getAttribute('for').split('-')[1]);
                    label.style.color = value <= selectedValue ? 'orange' : '#ccc';
                });
            }
        
            radios.forEach(radio => {
                radio.addEventListener('change', (event) => {
                    const selectedValue = parseInt(event.target.value);
                    updateStars(selectedValue);
                });
            });
        """)
    )

@app.post("/submitreview")
def submit_review(comment: str, rating: str):
    """ บันทึกรีวิวและส่งกลับไปแสดงในหน้าเว็บ """
    
    member = controller.get_user_by_id("1")
    reviewed = Review(member,comment,rating)
    member.add_review(reviewed)
    print(f"Success")
    member.show_review()
    
    return Redirect("/home")