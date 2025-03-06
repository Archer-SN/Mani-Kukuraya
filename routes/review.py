from app import app
from models import *
from fasthtml.common import *


@app.get("/review")
def CollectReview():
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
        Div(
            Label(
                "Comment:",
                Input(
                    type="text", 
                    id="comment",
                    name="comment", 
                    placeholder="Type your comment here...",
                    style="width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px; margin-top: 5px;"
                )
            ),
            Button(
                "Submit", 
                type="submit",
                hx_post="/submitreview", hx_target="#comment",
                style="margin-top: 10px; padding: 10px 20px; border: none; background-color: orange; color: white; cursor: pointer;"
            ),
            style="margin-top: 20px;"
        )
    )
@app.post("/submitreview", methods=["POST"])
def SubmitReview(comment: str):
    print(f"ข้อมูลที่ได้รับ: {comment}")  
    return Response(headers={"HX-Redirect": "/review"})
