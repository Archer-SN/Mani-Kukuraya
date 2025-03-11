sequenceDiagram

    actor Member

    participant UI
    participant Controller
    participant Order
    participant User
    participant Promotion

    Member->>+UI: Use Promotion
    UI->>+Controller: Post request to /promotion
    Controller->>+User: get_promotion(promotion_code)
    loop promotion in Promotion
        User->>+Promotion: get promotion from code
        Promotion-->>-User: return promotion
    end
    User-->>-Controller: promotion
    loop order in Order:
        Controller->>+Order: get_order_by_id(order_id)
        Order-->>-Controller: return order
    end
    opt order == None
        Controller->>+User: get_cart_by_cart_id(order_id)
        loop cart in Cart
            User->>+Cart: get cart
            Cart-->>-User: return cart
        end
        User->>-Controller: return cart
    end
    opt cart == None
        Controller->>+Cart: create Cart instance
        Cart-->>-Controller: return Cart instance
    end
    Controller->>+User: get_locations()
    User->>+User: get_locations
    User-->>-Controller: return locations
    Controller->>+Order: select_promotion(promotion)
    Order-->>-Controller: return None
    Controller-->>-UI: return order
    UI-->>-Member: Show that promotion is used