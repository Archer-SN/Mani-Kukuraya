
sequenceDiagram
    actor Member
    participant UI
    participant Controller
    participant User
    participant Order
    participant Cart
    participant Restaurant

    Member->>+UI: View order page
    UI->>+Controller: Request order page from /order
    loop user in User
        Controller->>+User: get_user_by_username(username)
        User-->>-Controller: return user
    end
    loop for order in Order
        Controller->>+Order: get_order_by(id)
        Order-->>-Controller: return order
    end
    loop for cart in Cart:
        Controller->>+Cart: get_cart_by_cart_id(id)
        Cart-->>-Controller: return cart
    end
    Controller->>+Cart: get_foods()
    Cart-->>-Controller: return list of food instances
    Controller->>+Restaurant: get_restaurant()
    Restaurant->>+Controller: restaurant instance

    Controller->>+Cart: get_user()
    Cart-->>-Controller: user
    Controller->>+User: get_promotions_by_restaurant(restaurant)

    loop for promotion in Promotion:
        User->>+Promotion: get promotion
        Promotion-->>-User: return promotion
    end

    User-->>-Controller: return list of promotions
    Controller-->>-UI: return Order page html
    UI-->>-Member: Display Order page





    