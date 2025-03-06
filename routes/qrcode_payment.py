from app import *
from models import *
from fasthtml.common import *

from fasthtml.common import *
from app import app

@app.get("/payment")
def payment_page():
    amount = 113
    qr_code_url = "/static/qrcode.png"

    return Titled(
        "การชำระเงินสำหรับสั่งอาหาร",
        Div(
            AX("⬅ กลับ",href="/selectedFood", style="text-decoration: none; font-size: 18px; color: black; display: inline-block;"),
            style="position: absolute; top: 10px; left: 10px;"
        ),
        Div(
            H3(f"{amount} บาท", style="color: black;"),
            Img(src=qr_code_url, style="width: 200px; height: 200px;"),
            P("หมดอายุภายใน 10:00 นาที", style="color: gray; font-size: 14px;"),
            P(
                "ต้องการเปลี่ยนเป็นจ่ายด้วยเงินสด?",
                style="color: #ff5722; font-weight: bold;"
            ),
            Button("ยืนยันการชำระเงิน", type="submit",
                   style="border: none; background-color: #ff5722; color: white; padding: 10px 20px; font-size: 16px; border-radius: 5px;",
                   hx_post="/confirm-payment", hx_target="#payment-msg"),
            Div(id="payment-msg")
        ),
        style="text-align: center; margin-top: 50px;"
    )

@app.post("/confirm-payment")
def confirm_payment():
    return Span("ชำระเงินสำเร็จ!", style="color: green; font-size: 18px;", id="payment-msg")
