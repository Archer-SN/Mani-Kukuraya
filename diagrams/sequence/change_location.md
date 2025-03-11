
sequenceDiagram
    actor Member
    participant UI
    participant Controller
    participant User
    participant Order

    Member->>+UI: select delivery option
    UI->>+Controller: Post request to /update-delivery
    loop order in Order
        Controller->>+Order: get_order_by_id(order_id)
        Order-->>-Controller: return order
    end
    Controller->>+Order: select_delivery_option(delivery_type)
    Order-->>-Controller: return None
    Controller-->>-UI: return HTML element
    UI-->>-Member: update page with the new element
