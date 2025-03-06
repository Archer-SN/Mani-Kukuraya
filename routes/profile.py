from app import app
from models import *
from fasthtml.common import *

@app.get("/profile")
def Profile():
    return Container(
        Card(
            H3("Profile"),
            Img(
                src="https://randomuser.me/api/portraits/men/54.jpg",
                alt="Profile Picture",
                style="width: 200px; height: auto; border-radius: 50%; display: block; margin: 0 auto;"
            ),
            H4("John Doe"),
            P("Web Developer"),
            style="box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); padding: 20px; text-align: center;"
        )
    )