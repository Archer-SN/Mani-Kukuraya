from app import app
from models import *
from fasthtml.common import *

@app.get("/profile")
def profile():
    return Titled("Profile",
        Card(
            Img(
                src="https://img.freepik.com/free-vector/blue-circle-with-white-user_78370-4707.jpg?t=st=1741278728~exp=1741282328~hmac=78f1490083116355da3df50ecd7af5eb868df1b4b5164b8bdd7b3e7c1ad0c6ca&w=740",
                alt="Profile Picture",
                style="width: 200px; height: auto; border-radius: 50%; display: block; margin: 0 auto;"
            ),
            H4("สวัสดีคุณ John Doe",style="margin-top: 20px;"),
            style="box-shadow: 0 5px 8px 0 rgba(0,0,0,0.2); padding: 20px; text-align: center;"
        ),
        H2("ทั่วไป",style="margin-top: 20px;"),
        Card(
            P("รายการโปรด"),
            
            style="box-shadow: 0 5px 8px 0 rgba(0,0,0,0.2); padding: 10px; text-align: center;"

        ),
        Card(
            P("ประวัติการสั่งอาหาร"),
            
            style="box-shadow: 0 5px 8px 0 rgba(0,0,0,0.2); padding: 10px; text-align: center;"

        ),
        Card(
            P("แก้ไขข้อมูลส่วนตัว"),
            
            style="box-shadow: 0 5px 8px 0 rgba(0,0,0,0.2); padding: 10px; text-align: center;"

        ),
        Card(
            P("สถานที่ที่บันทึกไว้"),
            style="box-shadow: 0 5px 8px 0 rgba(0,0,0,0.2); padding: 10px; text-align: center;"

        )
    )