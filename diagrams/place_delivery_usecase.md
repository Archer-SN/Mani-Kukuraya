
sequenceDiagram
    actor Member
    participant UI
    participant Controller
    participant User
    participant Order
    participant UserOrder

    Member->>+UI: Place Delivery
    UI->>+Controller: create new UserOrder
    loop for user in User
       Controller->>+User:  get_user_by_id(user_id)
       User->>-Controller: return user
    end
    Controller->>+User: get_current_order()
    loop for order in Order
        User->>+Order: get_order(user_id)
        Order->>-User: return order
    end

    User->>+Order: create_user_order()
    Order->>+UserOrder: Create UserOrder instance
    UserOrder->>-Order: return UserOrder
    Order->>-User: return UserOrder
    User->>-Controller: return UserOrder
    Controller->>-UI: redirect to confirmed delivery page
    UI->>-Member: Show confirmed delivery page