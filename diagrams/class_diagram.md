```mermaid
classDiagram

class Controller {
    - users: List[User]
    - restaurants: List[Restaurant]
    - foods: List[Food]
    - recommended_food: List[Food]
    - orders: List[Order]
    + add_restaurant(restaurant: Restaurant)
    + add_user(user: User)
    + add_food(food: Food)
    + get_user_by_id(user_id: str): User
    + search_result(word: str): List[Union[Food, Restaurant]]
    + get_food_by_id(food_id: str): Food
    + get_restaurant_by_id(restaurant_id: str): Restaurant
    + get_categories(): List[str]
    + get_restaurant_home(): List[Restaurant]
    + get_restaurants(): List[Restaurant]
    + dataforhomepage(): List[Any]
    + get_recommended_food(): List[Food]
    + get_choice_by_id(choice_id: str): OptionChoice
    + get_order_by_id(order_id: str): Order
    + get_orders(): List[Order]
    + create_order(user: User, cart: Cart, location: Location): Order
}

class User {
    - user_id: str
    - name: str
    - username: str
    - password: str
    - carts: List[Cart]
    - locations: List[Location]
    - user_order_history: List[Order]
    - promotions: List[Promotion]
    - reviews: List[Review]
    - favorites: Set[Restaurant]
    + set_username(new_username: str)
    + set_name(new_name: str)
    + set_password(new_password: str)
    + get_user_id(): str
    + get_promotions(): List[Promotion]
    + add_location(new_location: Location)
    + add_payment(new_payment_method: Payment)
    + add_promotion(promotion: Promotion)
    + get_promotion(promotion_code: str): Promotion
    + use_promotion(promotion: Promotion)
    + get_locations(): List[Location]
    + get_location_by_id(location_id: str): Location
    + get_foods_incart(): int
    + get_cart_by_restaurant_id(restaurant_id: str): Cart
    + get_cart_by_cart_id(cart_id: str): Cart
    + get_current_user(): User
    + send_recentorder(): List[Order]
    + add_cart(new_cart: Cart)
    + get_carts(): List[Cart]
    + add_favorite(restaurant: Restaurant)
    + remove_favorite(restaurant: Restaurant)
    + get_favorites(): List[Restaurant]
    + get_promotions_by_restaurant(restaurant: Restaurant): List[Promotion]
    + remove_cart(cart: Cart)
}

class Promotion {
    - name: str
    - restaurant: Restaurant
    - promotion_code: str
    - discount: float
    + get_name(): str
    + get_image(): str
    + get_promotion_code(): str
    + get_restaurant(): Restaurant
    + get_discount(): float
}

class Location {
    - id: str
    - full_name: str
    - phone_number: str
    - address: str
    - street: str
    - unit: str
    - extra_information: str
    + edit_location(full_name: str, phone_number: str, address: str, street: str, unit: str, extra_information: str)
}

class Review {
    - user: User
    - comment: str
    - stars: int
}

class Restaurant {
    - restaurant_id: str
    - name: str
    - menu: List[Food]
    - description: str
    - score: float
    - reviews: List[Review]
    - restaurant_image: str
    + get_restaurant_id(): str
    + get_name(): str
    + get_menu(): List[Food]
    + get_score(): float
    + get_reviews(): List[Review]
    + get_restaurant_image(): str
    + add_food(food: Food)
    + get_image(): str
    + add_review(user: User, review: str, stars: int): str
    + get_description(): str
}

class FoodOption {
    - option_id: str
    - option_name: str
    - choices: List[OptionChoice]
    - max_selection: int
    + get_id(): str
    + add_choice(choice: OptionChoice)
    + get_choices(): List[OptionChoice]
    + get_name(): str
}

class OptionChoice {
    - choice_id: str
    - option: FoodOption
    - choice: str
    - price: float
    + get_id(): str
    + get_name(): str
    + get_option(): FoodOption
    + get_price(): float
}

class Food {
    - restaurant: Restaurant
    - food_id: str
    - name: str
    - description: str
    - price: float
    - category: str
    - food_image: str
    - food_options: List[FoodOption]
    + get_name(): str
    + get_price(): float
    + get_description(): str
    + get_image(): str
    + get_category(): str
    + get_food_id(): str
    + get_food_options(): List[FoodOption]
    + add_option(option: FoodOption)
    + get_restaurant(): Restaurant
}

class SelectedFoodOption {
    - option: FoodOption
    - selected_choices: List[OptionChoice]
    + select_choice(choice: OptionChoice)
    + get_option(): FoodOption
    + get_selected_choices(): List[OptionChoice]
}

class SelectedFood {
    - selected_food_id: str
    - food: Food
    - selected_options: List[SelectedFoodOption]
    - quantity: int
    + get_quantity(): int
    + get_name(): str
    + calculate_price(): float
    + add_choice(choice: OptionChoice)
    + get_selected_options(): List[SelectedFoodOption]
}

class Cart {
    - cart_id: str
    - restaurant: Restaurant
    - user: User
    - selected_foods: List[SelectedFood]
    - status: str
    + get_foods(): List[SelectedFood]
    + add_to_cart(food: SelectedFood)
    + delete_from_cart(food: SelectedFood)
    + calculate_price(): float
    + get_restaurant(): Restaurant
    + get_cart_id(): str
    + get_user(): User
}

class Payment {
    - amount: float
    - currency: str
    - status: bool
    - timestamp: datetime
}

class QRPayment {
    - qr_code_data: str
    - reference_number: str
    + pay(): bool
    + get_qr_code_data(): str
}

class CashPayment {
    - received_amount: float
    - change: float
    + pay(): bool
}

class DeliveryOption {
    - name: str
    - estimate_time: str
    - price: float
    + get_price(): float
    + get_name(): str
}

class Order {
    - order_id: str
    - user: User
    - cart: Cart
    - location: Location
    - delivery_option: DeliveryOption
    - payment_method: Payment
    - selected_promotion: Promotion
    - status: str
    + select_location(new_location: Location)
    + select_payment(new_payment: Payment)
    + select_delivery_option(delivery_name: str)
    + get_delivery_option_by_name(delivery_name: str): DeliveryOption
    + get_delivery_option(): DeliveryOption
    + calculate_price(): float
    + get_order_id(): str
    + select_promotion(promotion: Promotion)
    + get_cart(): Cart
    + get_selected_promotion(): Promotion
    + get_location(): Location
    + get_payment_method(): Payment
    + confirm_order_status()
    + get_user(): User
}

Controller o-- User
Controller o-- Restaurant

User o-- Order

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