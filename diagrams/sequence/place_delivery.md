
sequenceDiagram
    actor Member
    participant UI
    participant Controller
    participant User
    participant Order

    Member->>+UI: Place Delivery
    UI->>+Controller: POST Request to /order
    loop for order in Order
        Controller->>+Order: get_order_by(id)
        Order-->>-Controller: return order
    end
    Order->>Order: confirm_order_status()
    Controller->>+Order: get_cart()
    Order-->>-Controller: cart
    Controller->>+User: remove_cart(cart)
    User-->>-Controller: return None
    Controller-->>-UI: Redirect to review page
    UI-->>-Member: Show review page