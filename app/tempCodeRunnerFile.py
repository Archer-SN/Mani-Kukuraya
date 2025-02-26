            Button("-", type="button", id="decrease",
                hx_post="/update-quantity",
                hx_target="#quantity",
                hx_swap="outerHTML",
                hx_vals='js:{"quantity": Number(document.getElementById("quantity").innerText), "action": "decrease"}',
                style="font-size: 20px; width: 40px; height: 40px;"),

            Span("1", id="quantity", style="font-size: 28px; font-weight: bold; position: relative; top: -5px; margin: 0 20px;"),

            Button("+", type="button", id="increase",
                hx_post="/update-quantity",
                hx_target="#quantity",
                hx_swap="outerHTML",
                hx_vals='js:{"quantity": Number(document.getElementById("quantity").innerText), "action": "increase"}',
                style="font-size: 20px; width: 40px; height: 40px;"),
            
            style="display: flex; justify-content: center; align-items: center; margin: 15px 0;"
        ),