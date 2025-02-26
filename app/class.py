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
    pass

class FoodOption:
    pass

class OptionChoice:
    pass

class FoodComment:
    pass

class SelectedFood:
    pass

class Cart:
    pass

# TODO: foshforce
class Payment :
    def __init__(self, amount : float, currency : str) :
        self.__amount = amount        
        self.__currency =  currency        
        self.__        
        self.__        


class QRPayment(Payment):
    pass

class CashPayment(Payment):
    pass

class DeliveryOption:
    pass

class Order:
    pass

# TODO: Create classes to simulate the app
def create_instance():
    pass