
<!-- ```mermaid -->
classDiagram

class Controller {
    - users
    - restaurants
    - foods
    + get_food_by_id(food_id)
    + get_restaurant_by_id(restaurant_id)
    + get_user_by_id(user_id)
}


class Restaurant {
    - name
    - menu
    - score
    - reviews
    - restaurant_image
    + get_restaurant_id()
    + get_restaurant_share()
    + get_food(food_name)
    + get_image()
    + get_score()
    + get_reviews()
}

class User {
    - user_id
    - name
    - username
    - password
    - carts
    - saved_locations
    - UserOrder_history
    - promotions
    - reviews
    + set_username(new_username)
    + set_password(new_password)
    + get_user_id(user_id)
    + get_promotions()
    + add_location(location)
    + add_payment()
    + add_favorite_restaurant(restaurant_id)
    + delete_favorite_restaurant(restaurant_id)
    + add_promotion(promotion)
    + use_promotion(promotion)
    + get_promotion(promotion_code)
    + share_restaurant()
}


class Food {
    - food_id
    - name
    - options
    - category
    - description
    - price
    - food_image
    + get_name()
}

class FoodOption {
    - option_name
    - choices
    - max_selection
}

class OptionChoice {
    - option
    - choice_name
    - price
}

class SelectedFoodOption {
    - option
    - selected_choices
    + select_choice()
}

class SelectedFood {
    - food
    - requirement
    - selected_options
    - comment
    + select_option()
    + calculate_price()

}

class Cart {
    - restaurant
    - selected_foods
    + add_to_cart()
    + delete_from_cart()
    + edit_cart()
    + calculate_price()
    + get_foods()
}

class Promotion {
    - name
    - restaurant
    - promotion_code
    + get_image()
    + get_promotion_code()
    + get_name()
}

class Payment {
    + pay()
}

class QRPayment {
    + pay()
}

class CashPayment {
    + pay()
}

class Location {
    - phone_number
    - location_name
    - address
    - note
}

class DeliveryOption {
    - name
    - estimated_time
    - price
}

class Order {
    - user
    - cart
    - location
    - delivery_option
    - payment_method
    - selected_promotion
    + select_location()
    + select_payment()
    + select_delivery_option()
    + calculate_price()
}

class UserOrder {
    - id
    - status
    - restaurant
    - foods
}

class Review {
    - user
    - stars
    - comment
}

Controller o-- User
Controller o-- Restaurant

User o-- UserOrder

FoodOption --o Food
OptionChoice --o FoodOption
Food <-- SelectedFood
FoodOption <-- SelectedFoodOption
SelectedFoodOption --o OptionChoice 
SelectedFood --o SelectedFoodOption

Restaurant o-- Food


Review --o Restaurant
Review --o User


Promotion --o User
Location --o User
DeliveryOption <-- Order

Payment <|-- CashPayment
Payment <|-- QRPayment

Restaurant <-- Cart
Cart *-- SelectedFood
Cart --o User

Cart <-- Order
Location <-- Order
Payment <-- Order
User <-- Order
