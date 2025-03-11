from app import *
from models import *
from fasthtml.common import *

from fasthtml.common import *
from app import app

@app.post("/update-payment")
def update_payment(order_id: str, payment: str):
    order = controller.get_order_by_id(order_id)
    if payment == "qr":
        payment_method = QRPayment(order.calculate_price(), qr_code_data="/static/qrcode.png")
        order.select_payment(payment_method)
    elif payment == "cash":
        payment_method = CashPayment(order.calculate_price(), "THB")
        order.select_payment(payment_method)
        


@app.post("/payment")
def payment_page(order_id: str):
    order = controller.get_order_by_id(order_id)
    payment = order.get_payment_method()
    if isinstance(payment, QRPayment):
        return Titled(
            "การชำระเงินสำหรับสั่งอาหาร",
            Div(
                AX("⬅ กลับ",href="/selectedFood", style="text-decoration: none; font-size: 18px; color: black; display: inline-block;"),
                style="position: absolute; top: 10px; left: 10px;"
            ),
            Div(
                H3(f"{order.calculate_price()} บาท", style="color: black;"),
                Img(src=payment.get_qr_code_data(), style="width: 200px; height: 200px;"),
                P("หมดอายุภายใน 10:00 นาที", style="color: gray; font-size: 14px;"),
                Button("ยืนยันการชำระเงิน", type="submit",
                    style="border: none; background-color: #ff5722; color: white; padding: 10px 20px; font-size: 16px; border-radius: 5px;",
                    hx_post="/order", hx_target="#main", hx_swap="outerHTML", hx_vals={'order_id': order.get_order_id()}),
            ),
            style="text-align: center; margin-top: 50px;",
            id="main"
        )
    else:
        return Titled(
            "การชำระเงินสำหรับสั่งอาหาร",
            Div(
                AX("⬅ กลับ",href="/selectedFood", style="text-decoration: none; font-size: 18px; color: black; display: inline-block;"),
                style="position: absolute; top: 10px; left: 10px;"
            ),
            Div(
                H3(f"{order.calculate_price()} บาท", style="color: black;"),        
                Button("ยืนยันการชำระเงิน", type="submit",
                    style="border: none; background-color: #ff5722; color: white; padding: 10px 20px; font-size: 16px; border-radius: 5px;",
                    hx_post="/order", hx_target="#main", hx_swap="outerHTML", hx_vals={"order_id": order.get_order_id()}),
            ),
            style="text-align: center; margin-top: 50px;",
            id="main"
        )

@app.post("/confirm-payment")
def confirm_payment():
    return Span("ชำระเงินสำเร็จ!", style="color: green; font-size: 18px;", id="payment-msg")
