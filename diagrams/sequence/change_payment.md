
sequenceDiagram
    actor Member
    participant UI
    participant Controller
    participant User
    participant Order

    Member->>+UI: change payment method
    UI->>+Controller: Post request to /update-payment
    loop order in Order
        Controller->>+Order: get_order_by_id(order_id)
    end
    alt payment == "qr"
        Controller->>+QRPayment: create instance QRPayment
        QRPayment-->>-Controller: return instance QRPayment
    else
        Controller->>+CashPayment: create instance CashPayment
        CashPayment-->>-Controller: return instance CashPayment
    end
    Controller-->>-UI: return None
    UI-->>-Member: Change selected box
