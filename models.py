from datetime import datetime 
from fasthtml.common import *
import uuid

class Controller:
    def __init__(self, users, restaurants, foods):
        self.__users = users
        self.__restaurants = restaurants
        self.__catagories = [["This is test","https://example.com/image2.jpg"],["This is test2","https://example.com/image2.jpg"],["This is test3","https://example.com/image2.jpg"],["This is test4","https://example.com/image2.jpg"],["This is test5","https://example.com/image2.jpg"],["This is test6","https://example.com/image2.jpg"],["This is test7","https://example.com/image2.jpg"],["This is test8","https://example.com/image2.jpg"],["This is test9","https://example.com/image2.jpg"],["This is test10","https://example.com/image"]]
        self.__foods = foods

    def get_user_by_id(self, user_id):
        for user in self.__users:
            if user.get_user_id() == user_id:
                return user
        
    def get_food_by_id(self, food_id):
        for food in self.__foods:
            if food.get_food_id() == food_id:
                return food
    
    def get_restaurant_by_id(self):
        for restaurant in self.__restaurants:
            if restaurant.get_restaurant_id() == restaurant_id:
                return restaurants


    def find_food(self):
        pass
    def get_numbers_catagories(self):
        return self.__catagories
        

    
class User:
    def __init__(self, user_id, name, username, password, carts=[], locations=[], user_order_history=[], promotions=[], reviews=[]):
        self.__user_id = user_id
        self.__name = name
        self.__username = username
        self.__password = password
        self.__carts = carts
        self.__locations = []
        self.__user_order_history = user_order_history
        self.__promotions = promotions
        self.__reviews = reviews
        self.__current_order = None

    def set_username(self, new_username):
        self.__username = new_username

    def set_password(self, new_password: int):
        self.__password = new_password

    def get_user_id(self):
        return self.__user_id

    def get_promotions(self):
        return self.__promotions

    def add_location(self, new_location):
        self.__locations.append(new_location)

    def add_payment(self, new_payment_method):
        self.__payment = new_payment_method

    def add_promotion(self, promotion):
        self.__promotions.append(promotion)

    def get_promotion(self, promotion_code):
        for promotion in self.__promotions:
            if promotion.get_promotion_code() == promotion_code:
                return promotion

    def use_promotion(self, promotion):
        self.__promotions.remove(promotion)

    def add_location(self, location) :
        if isinstance(location, Location) :
            self.__locations.append(location)
        else :
            return "Error Object only"

    def get_current_order(self):
        return self.__current_order

    def set_current_order(self, new_order):
        self.__current_order = new_order

class Promotion:
    def __init__(self, name, restaurant, promotion_code):
        self.__name = name
        self.__restaurant = restaurant
        self.__promotion_code = promotion_code

    def get_name(self):
        return self.__name

    def get_image(self):
        return self.__restaurant.get_image()

    def get_promotion_code(self):
        return self.__promotion_code

class Location:
    def __init__(self, phone_number, address,unit, extra_information) :
        self.__phone_number = phone_number
        self.__address = address
        self.__unit = unit
        self.__extra_information = extra_information

    @property
    def phone_number(self) :
        return self.__phone_number
    
    @property
    def address(self) :
        return self.__address
    
    @property
    def unit(self) :
        return self.__unit
    
    @property 
    def note(self) :
        return self.__note
    
    def __str__(self):
        return f"{self.__phone_number} {self.__address} {self.__unit} {self.__extra_information}"
    
    def to_list (self) :
        return [self.__phone_number, self.__address, self.__unit , self.__extra_information]
    



class UserOrder:
    def __init__(self, status, restaurant, foods):
        self.__id = uuid.uuid4()
        self.__status = status
        self.__restaurant = restaurant
        self.__foods = foods

class Review:
    def __init__(self, score, user, comment, stars):
        self.__score = score
        self.__user = user
        self.__comment = comment
        self.__stars = stars

import uuid

class Restaurant:
    def __init__(self, name, menu, description, score, reviews, restaurant_image):
        self.__restaurant_id = uuid.uuid4()
        self.__name = name
        self.__menu = menu
        self.__description = description
        self.__score = score
        self.__reviews = reviews
        self.__restaurant_image = restaurant_image

    def get_restaurant_id(self):
        return str(self.__restaurant_id)

    def get_name(self):
        return self.__name

    def get_menu(self):
        return self.__menu

    def get_score(self):
        return self.__score

    def get_reviews(self):
        return self.__reviews

    def get_restaurant_image(self):
        return self.__restaurant_image

    @classmethod
    def from_data(cls, data):
        return cls(
            name=data["name"],
            menu=data.get("menu", []),
            description=data.get("description", ""),
            score=data.get("score", 0),
            reviews=data.get("reviews", []),
            restaurant_image=data.get("image", "")
        )

    @staticmethod
    def find_restaurant_id_by_name(restaurant_name):
        for restaurant in Restaurant._instances:
            if restaurant.get_name() == restaurant_name:
                return restaurant.get_restaurant_id()
        return None

    @classmethod
    def list_restaurants(cls):
        return cls._instances

    def get_food(self, food_name):
        for food in self.__menu:
            if food.get_name() == food_name:
                return food

    def get_image(self):
        return self.__restaurant_image


class Food:
    def __init__(self, name, description, price, category, food_image):
        self.__food_id = uuid.uuid4()
        self.__name = name    
        self.__description = description 
        self.__price = price     
        self.__category = category
        self.__food_image = food_image
    
    def get_food_id(self):
        return str(self.__food_id)

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_price(self):
        return self.__price

    def get_category(self):
        return self.__category

    def get_food_image(self):
        return self.__food_image


class FoodOption:
    def __init__(self, option_name, choices, max_selection):
        self.__option_name = option_name
        self.__choices = choices
        self.__max_selection = max_selection

    def get_option_name(self):
        return self.__option_name

    def get_choices(self):
        return self.__choices

    def get_max_selection(self):
        return self.__max_selection


class OptionChoice:
    def __init__(self, option, choice, choices_value, price):
        self.__option = option
        self.__choice = choice
        self.__choices_value = choices_value
        self.__price = price


    def get_choice(self):
        return self.__choice

    def get_option(self):
        return self.__option


class SelectedFoodOption:
    def __init__(self, option, selected_choices=None):
        if selected_choices is None:
            selected_choices = []
        self.__option = option
        self.__selected_choices = selected_choices

    def select_choice(self, choice):
        if len(self.__selected_choices) < self.__option.get_max_selection():
            self.__selected_choices.append(choice)
        else:
            raise ValueError(f"Cannot select more than {self.__option.get_max_selection()} choices for {self.__option.get_option_name()}")

    def get_selected_choices(self):
        return self.__selected_choices


class SelectedFood:
    def __init__(self, food, selected_options, quantity, comment_text=""):
        self.__selected_food_id = uuid.uuid4()
        self.__food = food
        self.__selected_options = selected_options
        self.__quantity = quantity
        self.__comment_text = comment_text

    def get_selected_food_id(self):
        return str(self.__selected_food_id)

    def get_food(self):
        return self.__food

    def get_selected_options(self):
        return self.__selected_options

    def get_quantity(self):
        return self.__quantity

    def get_comment_text(self):
        return self.__comment_text

    def calculate_price(self):
        total_price = self.__food.get_price() * self.__quantity

        for selected_option in self.__selected_options:
            for choice in selected_option.get_selected_choices():
                total_price += choice.get_price()

        return total_price

class Cart:
    def __init__(self, cart_id, restaurants, selected_foods,restaurant_id):
        self.__cart_id = cart_id
        self.__restaurant_id = restaurant_id
        self.__selected_foods = selected_foods
        self.__status = 'open'

    def get_foods(self):
        return self.__foods

    def add_to_cart(self, food):
        self.__foods.append(food)

    def delete_from_cart(self, food):
        self.__foods.remove(food)

    def calculate_price(self):
        total_price = 0
        for selected_food in self.__selected_foods:
            total_price += selected_food.calculate_price()
        return total_price
    


class Payment:
    def __init__(self, amount: float, currency="THB"):
        self.__amount = amount
        self.__currency = currency
        self.__status = False
        self.__timestamp = datetime.now()

class QRPayment(Payment):
    def __init__(self, amount, currency="THB", qr_code_data="", reference_number=""):
        super().__init__(amount, currency)
        self.__qr_code_data = qr_code_data
        self.__reference_number = reference_number

    def pay(self):
        pass

class CashPayment(Payment):
    def __init__(self, amount, currency, received_amount=0):
        super().__init__(amount, currency)
        self.__received_amount = received_amount
        self.__change = 0

    def pay(self):
        pass

class DeliveryOption:
    def __init__(self, name, estimate_time, price):
        self.__name = name
        self.__estimate_time = estimate_time
        self.__price = price

class Order:
    def __init__(self, user: User, cart: Cart, location: Location, deliveryoption: DeliveryOption, payment_method: Payment, selected_promotion: Promotion):
        self.__user = user
        self.__cart = cart
        self.__location = location
        self.__deliveryoption = deliveryoption
        self.__payment_method = payment_method
        self.__selected_promotion = selected_promotion

    def select_location(self, new_location):
        self.__location = new_location

    def select_payment(self, new_payment):
        self.__payment = new_payment

    def select_delivery_option(self, new_delivery_option):
        self.__delivery_option = new_delivery_option

    def calculate_price(self):
        self.__cart.calculate_price()

    def create_user_order(self):
        pass


user = User(
    user_id=1,
    name="Yokphon ",
    username="foshforce",
    password="password123",
    carts=[],
    locations=[],
    user_order_history=[],
    promotions=[],
    reviews=[]
)

kfc_restaurant = Restaurant(
    name="KFC",
    menu=[],
    score=4.5,
    reviews=[],
    restaurant_image="https://images.unsplash.com/photo-1612170153139-6f881ff067e0?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8Y2hpY2tlbnxlbnwwfHwwfHx8MA%3D%3D"
)

kfc_promotion = Promotion(
    name="KFC Discount",
    restaurant=kfc_restaurant,
    promotion_code="KFC2023",
)

dairy_queen_restaurant = Restaurant(
    name="Dairy Queen",
    menu=[],
    score=4.2,
    reviews=[],
    restaurant_image="https://s3-ap-southeast-1.amazonaws.com/cdn.dairyqueenthailand.com/images/1670569171.png"
)

dq_promotion = Promotion(
    name="Dairy Queen Discount",
    restaurant=dairy_queen_restaurant,
    promotion_code="DQ2023",
)

mc_donald_restaurant = Restaurant(
    name="McDonald's",
    menu=[],
    score=4.3,
    reviews=[],
    restaurant_image="https://www.shutterstock.com/image-photo/ayutthayathailand-march-7-2018-view-260nw-1181606473.jpg"
)

mcd_promotion = Promotion(
    name="McDonald's Discount",
    restaurant=mc_donald_restaurant,
    promotion_code="MCD2023",
)

user.add_promotion(dq_promotion)
user.add_promotion(mcd_promotion)

user.add_promotion(kfc_promotion)

Controller = Controller(
    users=[user],
    restaurants=[],
    foods=[]
)
restaurant_data = [
    {"name": "ไข่ขนป้า - ลาดกระบัง 46", "description": "อาหารตามสั่ง, ผัดไทย, ส้มตำ", "price": 299, "rating": 4.8, "distance": "5.7 km", "image": "egg.jpeg"},
]

for data in restaurant_data:
    Restaurant.from_data(data)

restaurant_list = Restaurant.list_restaurants()
print([restaurant.get_name() for restaurant in restaurant_list])