from datetime import datetime 
from fasthtml.common import *


class Controller:
    def __init__(self, users, restaurants, foods):
        self.__users = users
        self.__restaurants = restaurants
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
                return restaurant

    
class User:
    def __init__(self, user_id, name, username, password, carts=[], locations=[], user_order_history=[], promotions=[], reviews=[]):
        self.__user_id = user_id
        self.__name = name
        self.__username = username
        self.__password = password
        self.__carts = carts
        self.__locations = locations
        self.__user_order_history = user_order_history
        self.__promotions = promotions
        self.__reviews = reviews

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

    def get_promotion(self, promotion_code):
        for promotion in self.__promotions:
            if promotion.get_promotion_code() == promotion_code:
                return promotion

    def use_promotion(self, promotion):
        self.__promotions.remove(promotion)

class Promotion:
    def __init__(self, name, restaurant, promotion_code, image):
        self.__name = name
        self.__restaurant = restaurant
        self.__promotion_code = promotion_code

    def get_promotion_code(self):
        return ""

class Location:
    def __init__(self, phone_number, location_name, address, note):
        self.__phone_number = phone_number
        self.__location_name = location_name
        self.__address = address
        self.__note = note

class UserOrder:
    def __init__(self, id, status, restaurant, foods):
        self.__id = id
        self.__status = status
        self.__restaurant = restaurant
        self.__foods = foods

class Review:
    def __init__(self, score, user, comment, stars):
        self.__score = score
        self.__user = user
        self.__comment = comment
        self.__stars = stars

class Restaurant:
    def __init__(self, name, menu, score, reviews, restaurant_image):
        self.__restaurant_id = UUID(hex=None, bytes=None, bytes_le=None, fields=None, int=None, version=None)
        self.__name = name
        self.__menu = menu
        self.__score = score
        self.__reviews = reviews
        self.__restaurant_image = restaurant_image

    def get_restaurant_id(self):
        return self.__restaurant_id

class Food:
    def __init__(self, food_id, name, description, price, category, food_image):
        self.__food_id = food_id
        self.__name = name    
        self.__description = description 
        self.__price = price     
        self.__category = category
        self.__food_image = food_image

class FoodOption:
    def __init__(self, option, choice, max_selection, food):
        self.__option = option
        self.__choice = choice
        self.__max_selection = max_selection
        self.__food = food

class OptionChoice:
    def __init__(self, option, choice, choices_value, price):
        self.__option = option
        self.__choice = choice
        self.__choices_value = choices_value
        self.__price = price

class FoodComment:
    def __init__(self, comment_id, food, user, rating, comment_text):
        self.__comment_id = comment_id
        self.__food = food
        self.__user = user
        self.__rating = rating
        self.__comment_text = comment_text

class SelectedFood:
    def __init__(self, selected_food_id, food, option, choice, quantity):
        self.__selected_food_id = selected_food_id
        self.__food = food
        self.__option = option
        self.__choice = choice
        self.__quantity = quantity

    def calculate_price():
        return 

class Cart:
    def __init__(self, cart_id, restaurants, selected_foods):
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