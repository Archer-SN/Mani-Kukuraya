sequenceDiagram

    actor Member

    participant UI
    participant Controller
    participant Order
    participant User
    participant Promotion

    Member->>+UI: Use Promotion
    UI->>+Controller: Handle promotion usage
    loop for user in User
        Controller->>+User:  get_user_by_id(user_id)
        User->>-Controller: return user
    end
    Controller->>+User: get_current_order()
    loop for order in Order
        User->>+Order: get_order(user_id)
        Order->>-User: return order
    end
    User->>-Controller: return order
    Controller->>+Order: use_promotion(promotion_code)
    Order->>+User: use_promotion(promotion_code)
    loop for user in User
        User->>+Promotion: get_promotion(promotion_code)
        Promotion->>-User: return promotion
    end
    User->>-Order: return promotion
    Order->>-Controller: return promotion
    Controller->>-UI: Display current promotion





