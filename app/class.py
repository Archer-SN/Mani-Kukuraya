import datetime
# TODO: kaka
class App:
    def __init__(self, users, restaurants):
        self.users = users
        self.restaurants = restaurants

class User:
    def __init__(self, user_id, name, username, password, carts, locations, user_order_history, promotions, reviews):
        self.user_id = user_id
        self.name = name
        self.username = username
        self.password = password
        self.carts = carts
        self.locations = locations
        self.user_order_history = user_order_history
        self.promotions = promotions
        self.reviews = reviews

class Promotion:
    def __init__(self, name, restaurant, promotion_code):
        self.name = name
        self.restaurant = restaurant
        self.promotion_code = promotion_code

class Location:
    def __init__(self, phone_number, location_name, address, note):
        self.phone_number = phone_number
        self.location_name = location_name
        self.address = address
        self.note = note

class User:
    def __init(self, user_id, name, username, password, carts, locations, user_order_history, promotions, reviews):
        pass

class Promotion:
    def __init__(self, name, restaurant, promotion_code):
        pass

class Location:
    def __init__(self, phone_number, location_name, address, note):
        pass

# TODO: guer
class UserOrder:
    pass

class Review:
    pass

class Restaurant:
    pass

class RestaurantCollection:
    pass

# TODO: palm
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
        self.__cart_id = card_id
        self.__restaurant_id = restaurant_id
        self.__selected_food_id = selected_food_id
        self.__price = 0.00
        self.status = 'open'

# TODO: foshforce
class Payment :
    def __init__(self, amount : float, currency = "THB") :
        self.__amount = amount # จำนวนเงินที่ต้องชำระ      
        self.__currency =  currency # สกุลเงิน       
        self.__status = False        
        self.__timestamp = datetime.now() #เวลาการทำรายการ  


class QRPayment(Payment):
    def __init__(self, amount, currency = "THB", qr_code_data = "", reference_number = "" ):
        super().__init__(amount, currency)
        self.__qr_code_data = qr_code_data # ข้อมูล QRCODE สำหรับชำระเงิน
        self.__reference_number = reference_number # หมายเลขอ้างอิงการทำรายการ

    def pay() :
        pass

class CashPayment(Payment):
    def __init__(self, amount, currency, received_amount = 0):
        super().__init__(amount, currency)
        self.__received_amount = received_amount
        self.__change = 0

    def pay() :
        pass

class DeliveryOption:
    def __init__(self,name , estimate_time, price):
        self.__name = name
        self.__estimate_time = estimate_time
        self.__price = price

class Order:
    def __init__(self, user : User, cart : Cart, location : Location, deliveryoption : DeliveryOption, payment_method : Payment, selected_promotion : Promotion) :
        self.__user = user
        self.__cart = cart
        self.__location = location
        self.__deliveryoption = deliveryoption
        self.__payment_method = payment_method
        self.__selected_promotion = selected_promotion

    def select_location() :
        pass

    def select_payment() :
        pass

    def select_delivery_option() :
        pass

    def calculate_price() :
        pass


# TODO: Create classes to simulate the app
def create_instance():
    pass