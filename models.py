from datetime import datetime 

class Controller:
    def __init__(self, users, restaurants, foods):
        self.__users = users
        self.__restaurants = restaurants
        self.__foods = foods

    def find_user(self):
        pass
    
    def find_restaurant(self):
        pass

    def find_food(self):
        pass
    
class User:
    def __init__(self, user_id, name, username, password, carts, locations, user_order_history, promotions, reviews):
        self.__user_id = user_id
        self.__name = name
        self.__username = username
        self.__password = password
        self.__carts = carts
        self.__locations = []
        self.__user_order_history = user_order_history
        self.__promotions = promotions
        self.__reviews = reviews

    def login(self):
        pass
    
    def register(self):
        pass
    
    def logout(self):
        pass

    def edit_profile(self):
        pass

    def edit_password(self):
        pass

    def add_location(self, location) :
        if isinstance(location, Location) :
            self.__locations.append(location)
        else :
            return "Error Object only"

class Promotion:
    def __init__(self, name, restaurant, promotion_code):
        self.__name = name
        self.__restaurant = restaurant
        self.__promotion_code = promotion_code

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
    def __init__(self, name, menu, score, reviews):
        self.__name = name
        self.__menu = menu
        self.__score = score
        self.__reviews = reviews

class Food:
    def __init__(self, food_id, name, description, price, category):
        self.__food_id = food_id
        self.__name = name    
        self.__description = description 
        self.__price = price     
        self.__category = category

class FoodOption:
    def __init__(self, option, choice, max_selection, food_id):
        self.__option = option
        self.__choice = choice
        self.__max_selection = max_selection
        self.__food_id = food_id

class OptionChoice:
    def __init__(self, option, choice, choices_value, price):
        self.__option = option
        self.__choice = choice
        self.__choices_value = choices_value
        self.__price = price

class FoodComment:
    def __init__(self, comment_id, food_id, user_id, rating, comment_text):
        self.__comment_id = comment_id
        self.__food_id = food_id
        self.__user_id = user_id
        self.__rating = rating
        self.__comment_text = comment_text

class SelectedFood:
    def __init__(self, selected_food_id, food_id, option, choice, quantity):
        self.__selected_food_id = selected_food_id
        self.__food_id = food_id
        self.__option = option
        self.__choice = choice
        self.__quantity = quantity

class Cart:
    def __init__(self, cart_id, restaurant_id, selected_food_id):
        self.__cart_id = cart_id
        self.__restaurant_id = restaurant_id
        self.__selected_food_id = selected_food_id
        self.__price = 0.00
        self.__status = 'open'

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
        pass

    def create_user_order(self):
        pass
    

user1 = User("1", "Alice", "alice123", "password", [], [], [], [], [])
user2 = User("2", "Bob", "bob123", "password", [], [], [], [], [])

location1 = Location("1234567890", "Home", "123 Main St", "Near the park")
location2 = Location("0987654321", "Office", "456 Elm St", "Near the office")

promotion1 = Promotion("10% Off", "Pizza Place", "PIZZA10")
promotion2 = Promotion("Free Delivery", "Burger Joint", "BURGERFREE")

review1 = Review(5, user1, "Great food!", 5)
review2 = Review(4, user2, "Good service.", 4)

food1 = Food("1", "Pizza", "Cheese Pizza", 9.99, "Main Course")
food2 = Food("2", "Burger", "Beef Burger", 7.99, "Main Course")

food_option1 = FoodOption("1", "Size", 1, "1")
food_option2 = FoodOption("2", "Toppings", 3, "1")

option_choice1 = OptionChoice("1", "Small", "1", 0)
option_choice2 = OptionChoice("2", "Medium", "2", 1)
option_choice3 = OptionChoice("3", "Large", "3", 2)

food_comment1 = FoodComment("1", "1", "1", 5, "Delicious!")
food_comment2 = FoodComment("2", "2", "2", 4, "Tasty!")

selected_food1 = SelectedFood("1", "1", "1", "1", 2)
selected_food2 = SelectedFood("2", "2", "2", "2", 1)

cart1 = Cart("1", "1", "1")
cart2 = Cart("2", "2", "2")

restaurant1 = Restaurant("Pizza Place", [food1], 4.5, [review1])
restaurant2 = Restaurant("Burger Joint", [food2], 4.0, [review2])

delivery_option1 = DeliveryOption("Standard", 30, 5.00)
delivery_option2 = DeliveryOption("Express", 15, 10.00)

payment1 = CashPayment(20.00, "USD", 25.00)
payment2 = QRPayment(15.00, "USD", "QR12345", "REF12345")

order1 = Order(user1, cart1, location1, delivery_option1, payment1, promotion1)
order2 = Order(user2, cart2, location2, delivery_option2, payment2, promotion2)


user_kaka = User("1", "Kaka", "kaka", "1234", [], [], [], [], [])
user_guer = User("2", "Guer", "guer", "1234", [], [], [], [], [])

home = Location("02-222-2222", "Home", "123/456", "Near the park")
work = Location("02-333-3333", "Work", "789/101", "Near the school")
kfc_promotion = Promotion("Discount", "KFC", "KFC123")
# kfc = Restaurant("1", "KFC", "Fastfood", "02-111-1111", "123/456", "Near the park")
kfc_chicken = Food("1", "Chicken", "Fried chicken", 100, "Main course")
kfc_chicken_option = FoodOption("1", "Sauce", 1, "1")
kfc_chicken_option_choice = OptionChoice("1", "Ketchup", "1", 0)
kfc_chicken_comment = FoodComment("1", "1", "1", 5, "Delicious")
kfc_chicken_selected = SelectedFood("1", "1", "1", "1", 2)
kfc_cart = Cart("1", "1", "1")

# mcd = Restaurant("2", "McDonald", "Fastfood", "02-222-2222", "789/101", "Near the school")

saver_delivery = DeliveryOption("Saver", 30, 30)
cash_payment = CashPayment(100, "baht")