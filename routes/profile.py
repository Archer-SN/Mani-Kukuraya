from app import app
from models import *
from fasthtml.common import *

@app.get("/profile")
def profile():
    return Container( 
                  
        Button("Back", type="button", 
            style="position: absolute; top: 20px; left: 20px; border: auto; background-color: #ff5722; color: white; padding: 10px 20px; font-size: 16px; border-radius: 5px;",
            onclick="window.history.back();")
        ,Card(
            Img(
                src="https://img.freepik.com/free-vector/blue-circle-with-white-user_78370-4707.jpg?t=st=1741278728~exp=1741282328~hmac=78f1490083116355da3df50ecd7af5eb868df1b4b5164b8bdd7b3e7c1ad0c6ca&w=740",
                alt="Profile Picture",
                style="width: 150px; height: auto; border-radius: 50%; display: block; margin: 0 auto;"
            ),
            H4(f"สวัสดีคุณ {user.name}",style="margin-top: 20px;"),
            style="box-shadow: 0 5px 8px 0 rgba(0,0,0,0.2); padding: 20px; text-align: center; margin-top:60px;"
        ),
        H2("ทั่วไป",style="margin-top: 20px;"),
        Button("รายการโปรด", type="submit",onclick="window.location.href='/favorite';", style="border: none; background-color: #ff5722; color: white; padding: 10px 20px; font-size: 16px; border-radius: 5px;"),
        Button("วิธีการชำระเงิน", type="submit",onclick="window.location.href='/favorites';", style="border: none; background-color: #ff5722; color: white; padding: 10px 20px; font-size: 16px; border-radius: 5px;"),
        Button("จัดการบัญชี", type="submit",onclick="window.location.href='/account';", style="border: none; background-color: #ff5722; color: white; padding: 10px 20px; font-size: 16px; border-radius: 5px;"),
        Button("สถานที่ที่บันทึกไว้", type="submit",onclick="window.location.href='/locations';", style="border: none; background-color: #ff5722; color: white; padding: 10px 20px; font-size: 16px; border-radius: 5px;"),
    )