# TODO: kaka
class App:
    pass

class User:
    pass

class Promotion:
    pass

class Location:
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