import datetime
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