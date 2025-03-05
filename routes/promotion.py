from app import app
from models import *
from fasthtml.common import *
from lucide_fasthtml import Lucide

@app.get("/")
def view_promotion():
    offers = [
        {
            "title": "[ร้านก๋วยเตี๋ยวโกจิน] ส่วนลดราคา 150 บาท เมื่อซื้อครบ 100 บาท",
            "code": "07510943",
            "image": "/static/noodle.jpg",
        }
    ] * 5  # Repeat the offer 5 times

    return Container(
        Section(
            H1("Available Offers", cls="text-center"),
            Div(
                Input(placeholder="ใส่รหัสโปรโมชั่นที่นี่", cls="search", type="text"),
                cls="grid"
            )
        ),
        Section(
            *[
                Article(
                    Div(
                        Img(src=offer["image"], cls="avatar"),
                        Div(
                            Span("Just for you", cls="badge"),
                            Hgroup(
                                H3(offer["title"]),
                                P(f"#Code {offer['code']}"),
                            )
                        ),
                        A("Use Now", href="#", cls="contrast button"),
                        cls="grid"
                    ),
                    cls="card"
                )
                for offer in offers
            ]
        )
    )