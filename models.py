from datetime import datetime 
from fasthtml.common import *
import uuid

class Controller:
    def __init__(self, users, restaurants, foods):
        self.__users = users
        self.__restaurants = restaurants
        self.__catagories = [["This is test","https://example.com/image2.jpg"]]
        self.__foods = foods
        self.__recommended_food = [["อาหารไม่สะอาด","https://static.thairath.co.th/media/B6FtNKtgSqRqbnNsbKFRA9Hw1ddaiN8vczDH5awGUi4JQ7XTjwF2YTlnGfAZTGUAcQDXv.webp"],["อาหารสะอาด","https://hdmall.co.th/blog/wp-content/uploads/2024/03/11-%E0%B8%AD%E0%B8%B2%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%9E%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%AA%E0%B8%B8%E0%B8%82%E0%B8%A0%E0%B8%B2%E0%B8%9E-%E0%B8%AD%E0%B8%A2%E0%B8%B2%E0%B8%81%E0%B8%81%E0%B8%B4%E0%B8%99%E0%B9%80%E0%B8%9E%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%AA%E0%B8%B8%E0%B8%82%E0%B8%A0%E0%B8%B2%E0%B8%9E-%E0%B9%80%E0%B8%A3%E0%B8%B4%E0%B9%88%E0%B8%A1%E0%B8%95%E0%B9%89%E0%B8%99%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%AD%E0%B8%B0%E0%B9%84%E0%B8%A3%E0%B8%94%E0%B8%B5.jpg.webp"]]

    def add_restaurant(self, restaurant):
        self.__restaurants.append(restaurant)

    def add_user(self, user):
        self.__users.append(user)

    def add_food(self, food):
        self.__foods.append(food)

    def get_user_by_id(self, user_id):
        for user in self.__users:
            if user.get_user_id() == user_id:
                return user
        
    def get_food_by_id(self, food_id):
        for food in self.__foods:
            if food.get_food_id() == food_id:
                return food
    
    def get_restaurant_by_id(self, restaurant_id):
        for restaurant in self.__restaurants:
            if restaurant.get_restaurant_id() == str(restaurant_id):
                return restaurant

    def find_food(self):
        pass
    def get_catagories(self):
        return self.__catagories
    def get_recommended_food(self):
        return self.__recommended_food
        

    
class User:
    def __init__(self, user_id: str, name, username, password, carts=[], locations=[], user_order_history=[], promotions=[], reviews=[], favorites=[]):
        self.__user_id = user_id
        self.__name = name
        self.__username = username
        self.__password = password
        self.__carts = carts
<<<<<<< HEAD
        self.__locations = []
        self.__user_order_history = []
=======
        self.__locations = locations
        self.__user_order_history = user_order_history
>>>>>>> 393260a21d6a0e6945094c96816235aeccaa05d3
        self.__promotions = promotions
        self.__reviews = reviews
        self.__favorites = favorites
        self.__current_order = None

    def set_username(self, new_username):
        self.__username = new_username

    def set_name(self, new_name) :
        self.__name = new_name

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

    def add_location(self, location):
        if isinstance(location, Location): 
            self.__locations.append(location) 
            return "Add Location Success"
        return "Error: Object only"
        
    def get_locations(self):
        return  self.__locations
    
    def get_location_by_id(self, location_id):
        for location in self.__locations:
            print("1")
            print(location.id)
            print("2")
            print(location_id)
            if location.id == location_id:
                return location
    
    @classmethod
    def get_current_user(cls):
        return cls.onlyuser
    
    @property
    def name(self):
        return self.__name
    
    @property
    def password (self) :
        return self.__password

    def get_locations(self):
        return self.__locations

    def get_current_order(self):
        return self.__current_order

    def set_current_order(self, new_order):
        self.__current_order = new_order


    def send_recentorder(self):
        return self.__user_order_history

    def add_cart(self, new_cart):
        self.__carts.append(new_cart)

    def get_carts(self):
        return self.__carts
    def add_favorite(self, restaurant):
        self.__favorites.append(restaurant)

    def remove_favorite(self, restaurant):
        self.__favorites.remove(restaurant)

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
    def __init__(self, full_name="", phone_number="", address="",street="",unit="", extra_information="") :
        self.__id = uuid.uuid4().hex
        self.__full_name = full_name
        self.__phone_number = phone_number
        self.__address = address
        self.__street = street
        self.__unit = unit
        self.__extra_information = extra_information

    @property
    def id(self):
        return self.__id     

    @property
    def full_name(self):
        return self.__full_name

    @property
    def phone_number(self):
        return self.__phone_number

    @property
    def address(self):
        return self.__address
    
    @property
    def street(self):
        return self.__street

    @property
    def unit(self):
        return self.__unit

    @property
    def extra_information(self):  
        return self.__extra_information
    
    def edit_location(self,full_name, phone, address,street, unit, extra_info) :
        self.__full_name = full_name
        self.__phone_number = phone
        self.__address = address
        self.__street = street 
        self.__unit = unit
        self.__extra_information = extra_info



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

class Restaurant:
<<<<<<< HEAD
    def __init__(self, name="", menu=[], description="", score=0, reviews=[], restaurant_image="", restaurant_id=uuid.uuid4()):
=======
    def __init__(self, name, menu, score, reviews, restaurant_image, description="", restaurant_id=uuid.uuid4().hex):
>>>>>>> 393260a21d6a0e6945094c96816235aeccaa05d3
        self.__restaurant_id = restaurant_id
        self.__name = name
        self.__menu = menu
        self.__description = description
        self.__score = score
        self.__reviews = reviews
        self.__restaurant_image = restaurant_image
        self.__description = description

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


    def get_food(self, food_name):
        for food in self.__menu:
            if food.get_name() == food_name:
                return food

    def get_image(self):
        return self.__restaurant_image

    def get_description(self):
        return self.__description
    
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def get_menu(self):
        return self.__menu

    def add_food(self, food):
        self.__menu.append(food)

class Food:
    def __init__(self, food_id, name, description, price, category, food_image):
        self.__food_id = food_id
        self.__name = name    
        self.__description = description 
        self.__price = price     
        self.__category = category
        self.__food_image = food_image
    
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_description(self):
        return self.__description

    def get_image(self):
        return self.__food_image

class FoodOption:
    def __init__(self, option_name, choices, max_selection):
        self.__option_name = option_name
        self.__choices = choices
        self.__max_selection = max_selection

    def add_choice(self, choice):
        self.__choices.append(choice)


class OptionChoice:
    def __init__(self, option, choice, choices_value, price):
        self.__option = option
        self.__choice = choice
        self.__choices_value = choices_value
        self.__price = price


class SelectedFoodOption():
    def __init__(self, option, selected_choices=[]):
        self.__option = option
        self.__selected_choices = selected_choices

    def select_choice(self):
        pass


class SelectedFood:
    def __init__(self, selected_food_id, food, option, choice, quantity):
        self.__selected_food_id = selected_food_id
        self.__food = food
        self.__option = option
        self.__choice = choice
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity
    
    def get_name(self):
        return self.__food.get_name()

    def calculate_price(self):
        total_price = self.__food.get_price()


        return total_price * self.__quantity

class Cart:
<<<<<<< HEAD
    def __init__(self, cart_id, restaurants, selected_foods,restaurant):
=======
    def __init__(self, cart_id, restaurant : Restaurant, selected_foods):
>>>>>>> 393260a21d6a0e6945094c96816235aeccaa05d3
        self.__cart_id = cart_id
        self.__restaurant = restaurant
        self.__selected_foods = selected_foods
        self.__status = 'open'

    def get_foods(self):
        return self.__selected_foods

    def add_to_cart(self, food):
        self.__selected_foods.append(food)

    def delete_from_cart(self, food):
        self.__selected_foods.remove(food)

    def get_cart_items(self):
        return self.__selected_foods

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
<<<<<<< HEAD
    user_id= 67010751 ,
    name="Yokphon Ninbarun",
    username="ForceFord",
    password="911",
=======
    user_id="1",
    name="Yokphon ",
    username="foshforce",
    password="password123",
>>>>>>> 393260a21d6a0e6945094c96816235aeccaa05d3
    carts=[],
    locations=[],
    user_order_history=[],
    promotions=[],
    reviews=[]
)

kfc_restaurant = Restaurant(
    restaurant_id="1",
    name="KFC",
    menu=[],
    description="Fast-food chain known for its buckets of fried chicken, plus wings & sides.",
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
    description="Chain of soft-serve ice cream & fast-food restaurants.",
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
    restaurant_id="5",
    name="McDonald's",
    menu=[],
    description="Fast food chain known for its burgers, fries & shakes.",
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

controller = Controller(
    users=[user],
    restaurants=[],
    foods=[]
)

# Create foods for each restaurant
kfc_food1 = Food(
    food_id="1",
    name="Fried Chicken",
    description="Crispy fried chicken",
    price=5.99,
    category="Main Course",
    food_image="https://example.com/fried_chicken.jpg"
)

kfc_food2 = Food(
    food_id="2",
    name="Chicken Burger",
    description="Delicious chicken burger",
    price=4.99,
    category="Main Course",
    food_image="https://example.com/chicken_burger.jpg"
)

dq_food1 = Food(
    food_id="3",
    name="Blizzard",
    description="Ice cream with mix-ins",
    price=3.99,
    category="Dessert",
    food_image="https://example.com/blizzard.jpg"
)

dq_food2 = Food(
    food_id="4",
    name="Sundae",
    description="Ice cream sundae",
    price=2.99,
    category="Dessert",
    food_image="https://example.com/sundae.jpg"
)

mcd_food1 = Food(
    food_id="5",
    name="Big Mac",
    description="Classic Big Mac burger",
    price=5.49,
    category="Main Course",
    food_image="https://example.com/big_mac.jpg"
)

mcd_food2 = Food(
    food_id="6",
    name="French Fries",
    description="Crispy french fries",
    price=2.49,
    category="Side",
    food_image="https://example.com/french_fries.jpg"
)

# Add foods to each restaurant
kfc_restaurant.add_food(kfc_food1)
kfc_restaurant.add_food(kfc_food2)

dairy_queen_restaurant.add_food(dq_food1)
dairy_queen_restaurant.add_food(dq_food2)

mc_donald_restaurant.add_food(mcd_food1)
mc_donald_restaurant.add_food(mcd_food2)

# Add restaurants to the controller
controller.add_restaurant(kfc_restaurant)
controller.add_restaurant(dairy_queen_restaurant)
controller.add_restaurant(mc_donald_restaurant)

# Create food options for Dairy Queen ice cream
dq_option_toppings = FoodOption(
    option_name="Toppings",
    choices=[],
    max_selection=3
)

dq_option_size = FoodOption(
    option_name="Size",
    choices=[],
    max_selection=1
)

# Create food choices for Dairy Queen ice cream
dq_food_choice1 = OptionChoice(
    option=dq_option_toppings,
    choice="Chocolate Chips",
    choices_value="Chocolate Chips",
    price=0.5
)

dq_food_choice2 = OptionChoice(
    option=dq_option_toppings,
    choice="Sprinkles",
    choices_value="Sprinkles",
    price=0.5
)

dq_food_choice3 = OptionChoice(
    option=dq_option_toppings,
    choice="Oreo Crumbs",
    choices_value="Oreo Crumbs",
    price=0.5
)

dq_food_choice4 = OptionChoice(
    option=dq_option_size,
    choice="Small",
    choices_value="Small",
    price=0.0
)

dq_food_choice5 = OptionChoice(
    option=dq_option_size,
    choice="Medium",
    choices_value="Medium",
    price=1.0
)

dq_food_choice6 = OptionChoice(
    option=dq_option_size,
    choice="Large",
    choices_value="Large",
    price=1.5
)

# Add choices to options
dq_option_toppings._FoodOption__choices.extend([dq_food_choice1, dq_food_choice2, dq_food_choice3])
dq_option_size._FoodOption__choices.extend([dq_food_choice4, dq_food_choice5, dq_food_choice6])

# Add options to Dairy Queen foods
dq_food1_options = [
    SelectedFoodOption(option=dq_option_toppings, selected_choices=[dq_food_choice1, dq_food_choice3]),
    SelectedFoodOption(option=dq_option_size, selected_choices=[dq_food_choice5])
]

dq_food2_options = [
    SelectedFoodOption(option=dq_option_toppings, selected_choices=[dq_food_choice2]),
    SelectedFoodOption(option=dq_option_size, selected_choices=[dq_food_choice4])
]

# Add selected food options to Dairy Queen foods
dq_food1.selected_options = dq_food1_options
dq_food2.selected_options = dq_food2_options

# Get KFC restaurant from the controller
kfc_restaurant_from_controller = controller.get_restaurant_by_id(1)
print(f"Retrieved restaurant: {kfc_restaurant_from_controller.get_name()}")

# Create a cart for the user
<<<<<<< HEAD
# cart = Cart(
#     cart_id=uuid.uuid4(),
#     restaurants=[kfc_restaurant],
#     selected_foods=[],
#     restaurants=kfc_restaurant
# )
=======
cart = Cart(
    cart_id=uuid.uuid4(),
    restaurant=kfc_restaurant,
    selected_foods=[],
)
>>>>>>> 393260a21d6a0e6945094c96816235aeccaa05d3

# Add food to the cart
# selected_food = SelectedFood(
#     selected_food_id=uuid.uuid4(),
#     food=kfc_food1,
#     option=None,
#     choice=None,
#     quantity=2
# )

# cart.add_to_cart(selected_food)

<<<<<<< HEAD
# # Add the cart to the user's carts
# user._User__carts.append(cart)

# # Print the cart details
# print(f"User {user.get_user_id()} has the following items in their cart:")
# for food in cart.get_foods():
#     print(f"- {food._SelectedFood__food._Food__name} (Quantity: {food._SelectedFood__quantity})")
=======
# Add the cart to the user's carts
user.add_cart(cart)
# Print the cart details
print(f"User {user.get_user_id()} has the following items in their cart:")
for food in cart.get_foods():
    print(f"- {food._SelectedFood__food._Food__name} (Quantity: {food._SelectedFood__quantity})")

# Create a location for the user
location = Location(
    full_name="John Doe",
    phone_number="1234567890",
    address="123 Main St",
    street="Main St",
    unit="Apt 1",
    extra_information="Near the park"
)

# Add the location to the user's locations
user.add_location(location)

# Print the user's locations
print(f"User {user.get_user_id()} has the following locations:")
for loc in user.get_locations():
    print(f"- {loc.full_name}, {loc.address}, {loc.street}, {loc.unit}, {loc.extra_information}")
>>>>>>> 393260a21d6a0e6945094c96816235aeccaa05d3
