
sequenceDiagram
    actor Member
    

    Member->>+UI: Add to cart
    UI->>+Controller: POST request /add-to-cart
    loop user in User
        Controller->>+User: get_user_by_username(username)
        User-->>-Controller: return user
    end
    loop food in Food
        Controller->>+Food: get_food_by_id(food_id)
        Food-->>-Controller: return food
    end
    loop restaurant in Restaurant
        Controller->>+Restaurant: get_restaurant_by_id(restaurant_id)
        Restaurant-->>-Controller: return restaurant
    end
    loop cart in Cart
        Controller->>+Cart: get_cart_by_restaurant_id(restaurant_id)
        Cart-->>-Controller: return cart
    end
    Controller->>+SelectedFood: create SelectedFood instance
    SelectedFood-->>-Controller: return SelectedFood instance

    alt cart == None
        loop choice_id in choices
            Controller->>+Choice: get_choice_by_id(choice_id)
            Choice-->>-Controller: return choice
            Choice->>+SelectedFood: add_choice(choice)
            SelectedFood-->>-Choice: return None
        end
        Controller->>+Cart: create Cart instance
        Cart-->>-Controller: return Cart instance
        Controller->>+User: add_cart(cart)
        User-->>-Controller: return None
        Controller->>+Cart: add_to_cart(selected_food)
        Cart-->>-Controller: return None
        Controller-->>-UI: Redirect to restaurant page
        UI-->>-Member: Renders restaurant page
    end
    