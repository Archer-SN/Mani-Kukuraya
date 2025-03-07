from app import app
from models import *
from fasthtml.common import *
from lucide_fasthtml import Lucide

@app.get("/promotion")
def view_promotion():
    promotions = user.get_promotions()
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
                        Img(src=promotion["image"], cls="avatar"),
                        Div(
                            Span("Just for you", cls="badge"),
                            Hgroup(
                                H3(promotion["title"]),
                                P(f"#Code {promotion['code']}"),
                            )
                        ),
                        A("Use Now", hx_post="/promotion", cls="contrast button"),
                        cls="grid"
                    ),
                    cls="card"
                )
                for promotion in promotions
            ]
        )
    )

@app.post("/promotion")
def use_promotion():
    return Redirect("/order")

