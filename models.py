from datetime import datetime 
from fasthtml.common import *
import uuid
import random
import difflib

class Controller:
    def __init__(self, users, restaurants, foods):
        self.__users = users
        self.__restaurants = restaurants
        self.__foods = foods
        self.__recommended_food = []

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
            if restaurant.get_restaurant_id() == restaurant_id:
                return restaurant
<<<<<<< HEAD

    @classmethod
    def get_user(cls, auth):
        for user in cls._users:
            if user.get_user_id() == auth:
                return user
        return None

=======
    
>>>>>>> refs/remotes/origin/master
    def find_food(self):
        pass

    def get_categories(self):
        categories = []
        for food in self.__foods:
            print("nigga")
            if food.get_category() not in categories:
                categories.append(food.get_category())
        return categories
    def get_restaurant_home(self):
        restaurant_range = []
        recommended = []
        for i in range(10):
            randomed = random.choice(range(len(self.__restaurants)))
            if randomed in restaurant_range:
                continue
            else:
                restaurant_range.append(randomed)

        for k in restaurant_range:
            recommended.append(self.__restaurants[k])
        return recommended

    def get_restaurants(self):
        return self.__restaurants

    def dataforhomepage(self):
        cat = self.get_categories()
        rec = self.get_recommended_food()
        res = self.get_restaurant_home()
        pro = self.get_user_by_id("1").get_promotions()
        datalist = [cat,rec,res,pro]
        return datalist
    
    def get_restaurant_home(self):
        restaurant_range = []
        recommended = []
        for i in range(10):
            randomed = random.choice(range(len(self.__restaurants)))
            if randomed in restaurant_range:
                continue
            else:
                restaurant_range.append(randomed)

        for k in restaurant_range:
            recommended.append(self.__restaurants[k])
        return recommended

    def get_recommended_food(self):
        food_range = []
        recommended = []
        for i in range(4):
            randomed = random.choice(range(len(self.__foods)))
            if randomed in food_range:
                continue
            else:
                food_range.append(randomed)

        for k in food_range:
            recommended.append(self.__foods[k])
        return recommended
    
    def search_result(self, word):
        show_result =[]

        all_elements = [food for food in self.__foods] + \
                    [restaurant for restaurant in self.__restaurants]

        similar_names = difflib.get_close_matches(word, [name.get_name() for name in all_elements], n=3, cutoff=0.3)


        for result in range(len(similar_names)):
            for elements_object in all_elements:
                if similar_names[result] == elements_object.get_name():
                    show_result.append(elements_object)
                else:
                    continue
        return show_result

        
        
def search_result(self, word):
        show_result =[]

        all_elements = [food for food in self.foods] + \
                    [restaurant for restaurant in self.restaurants]

        similar_names = difflib.get_close_matches(word, [name.get_name() for name in all_elements], n=3, cutoff=0.3)


        for result in range(len(similar_names)):
            for elements_object in all_elements:
                if similar_names[result] == elements_object.get_name():
                    show_result.append(elements_object)
                else:
                    continue
        return show_result 


    def get_choice_by_id(self, choice_id):
        for food in self.__foods:
            for option in food.get_food_options():
                for choice in option.get_choices():
                    if choice.get_id() == choice_id:
                        return choice
        return None


class User:
<<<<<<< HEAD
    def __init__(self, user_id: str, name: str, username, password, carts=[], locations=[], user_order_history=[], promotions=[], reviews=[], favorites=[]):
=======
    def __init__(self, user_id: str, name, username, password):
>>>>>>> refs/remotes/origin/master
        self.__user_id = user_id
        self.__name = name
        self.__username = username
        self.__password = password
<<<<<<< HEAD
        self.__carts = carts
        self.__locations = locations
        self.__user_order_history = user_order_history
        self.__promotions = promotions
        self.__reviews = reviews
        self.__favorites = favorites
=======
        self.__carts = []
        self.__locations = []
        self.__user_order_history = []
        self.__promotions = []
        self.__reviews = []
        self.__favorites = []
>>>>>>> refs/remotes/origin/master
        self.__current_order = None
        self.favorite_restaurants = []

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
    
    def add_review(self,review):
        return self.__reviews.append(review)

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
    
    def get_cart_by_restaurant_id(self, restaurant_id):
        for cart in self.__carts:
            if cart.get_restaurant().get_restaurant_id() == restaurant_id:
                return cart
        return None

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

    def add_favorite(self, restaurant_id):
        if restaurant_id not in self.favorite_restaurants:
            self.favorite_restaurants.append(restaurant_id)

    def remove_favorite(self, restaurant_id):
        if restaurant_id in self.favorite_restaurants:
            self.favorite_restaurants.remove(restaurant_id)

    def show_review(self):
        for review in self.__reviews:
            comment = review._Review__comment
            rating = review._Review__stars
            print(f"Comment: {comment}, Rating: {rating}")

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
    
    def edit_location(self, full_name, phone_number, address, street, unit, extra_information):
        self.__full_name = full_name
        self.__phone_number = phone_number
        self.__address = address
        self.__street = street
        self.__unit = unit
        self.__extra_information = extra_information

class UserOrder:
    def __init__(self, status, restaurant, foods):
        self.__id = uuid.uuid4()
        self.__status = status
        self.__restaurant = restaurant
        self.__foods = foods

class Review:
    def __init__(self, user, comment, stars):
        self.__user = user
        self.__comment = comment
        self.__stars = stars

class Restaurant:
<<<<<<< HEAD
    def __init__(self, name, menu, score, reviews, restaurant_image, description="", restaurant_id=uuid.uuid4().hex):
        self.__restaurant_id = restaurant_id
=======
    def __init__(self, name, menu,description, score, reviews, restaurant_image):
        self.__restaurant_id = uuid.uuid4().hex
>>>>>>> refs/remotes/origin/master
        self.__name = name
        self.__menu = menu
        self.__description = description
        self.__score = score
        self.__reviews = reviews
        self.__restaurant_image = restaurant_image

    def get_restaurant_id(self):
        return self.__restaurant_id

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
    def add_food(self, food):
        self.__menu.append(food)

    def get_image(self):
        return self.__restaurant_image

    def add_review(self,user,review,stars):
        comment = Review(user,review,stars)
        self.reviews.append(comment)
        return "Success"

    def get_description(self):
        return self.__description

class FoodOption:
    def __init__(self, option_name, choices, max_selection):
        self.__option_id = uuid.uuid4().hex
        self.__option_name = option_name
        self.__choices = choices
        self.__max_selection = max_selection

    def get_id(self):
        return self.__option_id

    def add_choice(self, choice):
        self.__choices.append(choice)

    def get_choices(self):
        return self.__choices

    def get_name(self):
        return self.__option_name


class OptionChoice:
    def __init__(self, option, choice, choices_value, price):
        self.__choice_id = uuid.uuid4().hex
        self.__option = option
        self.__choice = choice
        self.__choices_value = choices_value

    def get_id(self):
        return self.__choice_id

    def get_name(self):
        return self.__choice

    def get_option(self):
        return self.__option 

class Food:
    def __init__(self, restaurant, name, description, price, category, food_image, food_id=uuid.uuid4().hex):
        self.__restaurant = restaurant
        self.__food_id = food_id
        self.__name = name    
        self.__description = description 
        self.__price = price     
        self.__category = category
        self.__food_image = food_image
        self.__food_options = []
    
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_description(self):
        return self.__description

    def get_image(self):
        return self.__food_image
    
    def get_category(self):
        return self.__category

    def get_food_id(self):
        return self.__food_id
    
    def get_food_options(self):
        return self.__food_options

    def add_option(self, option):
        self.__food_options.append(option)

    def get_restaurant(self):
        return self.__restaurant

class SelectedFoodOption():
    def __init__(self, option):
        self.__option = option
        self.__selected_choices = []

    def select_choice(self, choice):
        self.__selected_choices.append(choice)

    def get_option(self):
        return self.__option

    def get_selected_choices(self):
        return self.__selected_choices

class SelectedFood:
    def __init__(self, food, quantity, selected_food_id=uuid.uuid4().hex,):
        self.__selected_food_id = selected_food_id
        self.__food = food
        self.__selected_options = [SelectedFoodOption(option) for option in food.get_food_options()]
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity
    
    def get_name(self):
        return self.__food.get_name()

    def calculate_price(self):
        total_price = self.__food.get_price()
        return total_price * self.__quantity

    def add_choice(self, choice):
        for selected_option in self.__selected_options:
            option = selected_option.get_option()
            if choice in option.get_choices():
                selected_option.select_choice(choice)
    
    def get_selected_options(self):
        return self.__selected_options


class Cart:
<<<<<<< HEAD
    def __init__(self, cart_id, restaurant : Restaurant, selected_foods):
        self.__cart_id = cart_id
=======
    def __init__(self, restaurant : Restaurant):
        self.__cart_id = uuid.uuid4().hex
>>>>>>> refs/remotes/origin/master
        self.__restaurant = restaurant
        self.__selected_foods = []
        self.__status = 'open'

    def get_foods(self):
        return self.__selected_foods

    def add_to_cart(self, food):
        self.__selected_foods.append(food)

    def delete_from_cart(self, food):
        self.__selected_foods.remove(food)

    def calculate_price(self):
        total_price = 0
        for selected_food in self.__selected_foods:
            total_price += selected_food.calculate_price()
        return total_price

    def get_restaurant(self):
        return self.__restaurant

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

# Simulated Data

user = User(
    user_id="1",
    name="Yokphon ",
    username="foshforce",
    password="password123",
<<<<<<< HEAD
    carts=[],
    locations=[],
    user_order_history=[],
    promotions=[],
    reviews=[]
=======
>>>>>>> refs/remotes/origin/master
)

kfc_restaurant = Restaurant(
    name="KFC",
    menu=[],
    description="Fast-food chain known for its buckets of fried chicken, plus wings & sides.",
    score=4.5,
    reviews=[],
    restaurant_image="www.images.unsplash.com/photo-1612170153139-6f881ff067e0?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8Y2hpY2tlbnxlbnwwfHwwfHx8MA%3D%3D"
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

kfc_food1 = Food(
    restaurant=kfc_restaurant,
    food_id="1",
    name="Fried Chicken",
    description="Crispy fried chicken",
    price=5.99,
    category="Main Course",
    food_image="https://www.allrecipes.com/thmb/4GEksBrJ9OsiB2ZcoQQv5xW1n_0=/0x512/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/AR-89268-triple-dipped-fried-chicken-beauty-4x3-3961ac838ddd41958e7cb9f49376cd68.jpg"
)

kfc_food2 = Food(
    restaurant=kfc_restaurant,
    food_id="2",
    name="Chicken Burger",
    description="Delicious chicken burger",
    price=4.99,
    category="Main Course",
    food_image="https://www.chicken.ca/wp-content/uploads/2022/11/Chicken-Burgers-1180x580.jpg"
)

kfc_food3 = Food(
    food_id="20",
    name="Pork Burgur",
    description="Delicious chicken burger",
    price=4.99,
    category="Main Course",
    food_image="https://example.com/chicken_burger.jpg"
)

dq_food1 = Food(
    restaurant=dairy_queen_restaurant,
    food_id="3",
    name="Blizzard",
    description="Ice cream with mix-ins",
    price=3.99,
    category="Dessert",
    food_image="https://upload.wikimedia.org/wikipedia/commons/a/ae/StrawberrySundae.jpg"
)

dq_food2 = Food(
    restaurant=dairy_queen_restaurant,
    food_id="4",
    name="Sundae",
    description="Ice cream sundae",
    price=2.99,
    category="Dessert",
    food_image="https://s3-ap-southeast-1.amazonaws.com/cdn.dairyqueenthailand.com/images/1670569171.png"
)

mcd_food1 = Food(
    restaurant=mc_donald_restaurant,
    food_id="5",
    name="Big Mac",
    description="Classic Big Mac burger",
    price=5.49,
    category="Main Course",
    food_image="https://theeburgerdude.com/wp-content/uploads/2021/01/Big-Mac-2048x2048.jpg"
)

mcd_food2 = Food(
    restaurant=mc_donald_restaurant,
    food_id="6",
    name="French Fries",
    description="Crispy french fries",
    price=2.49,
    category="Side",
    food_image="https://cdn.britannica.com/34/206334-050-7637EB66/French-fries.jpg"
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
dq_option_toppings.add_choice(dq_food_choice1)
dq_option_toppings.add_choice(dq_food_choice2)
dq_option_toppings.add_choice(dq_food_choice3)

dq_option_size.add_choice(dq_food_choice4)
dq_option_size.add_choice(dq_food_choice5)
dq_option_size.add_choice(dq_food_choice6)

# Add options to Dairy Queen foods
dq_food1.add_option(dq_option_toppings)
dq_food1.add_option(dq_option_size)

dq_food2.add_option(dq_option_toppings)
dq_food2.add_option(dq_option_size)

# Create food options for KFC foods
kfc_option_sides = FoodOption(
    option_name="Sides",
    choices=[],
    max_selection=2
)

kfc_option_drinks = FoodOption(
    option_name="Drinks",
    choices=[],
    max_selection=1
)

# Create food choices for KFC foods
kfc_food_choice1 = OptionChoice(
    option=kfc_option_sides,
    choice="Fries",
    choices_value="Fries",
    price=1.5
)

kfc_food_choice2 = OptionChoice(
    option=kfc_option_sides,
    choice="Coleslaw",
    choices_value="Coleslaw",
    price=1.0
)

kfc_food_choice3 = OptionChoice(
    option=kfc_option_drinks,
    choice="Coke",
    choices_value="Coke",
    price=1.0
)

kfc_food_choice4 = OptionChoice(
    option=kfc_option_drinks,
    choice="Pepsi",
    choices_value="Pepsi",
    price=1.0
)

# Add choices to options
kfc_option_sides.add_choice(kfc_food_choice1)
kfc_option_sides.add_choice(kfc_food_choice2)

kfc_option_drinks.add_choice(kfc_food_choice3)
kfc_option_drinks.add_choice(kfc_food_choice4)

# Add options to KFC foods
kfc_food1.add_option(kfc_option_sides)
kfc_food1.add_option(kfc_option_drinks)

kfc_food2.add_option(kfc_option_sides)
kfc_food2.add_option(kfc_option_drinks)

# Create food options for McDonald's foods
mcd_option_sides = FoodOption(
    option_name="Sides",
    choices=[],
    max_selection=2
)

mcd_option_drinks = FoodOption(
    option_name="Drinks",
    choices=[],
    max_selection=1
)

# Create food choices for McDonald's foods
mcd_food_choice1 = OptionChoice(
    option=mcd_option_sides,
    choice="Fries",
    choices_value="Fries",
    price=1.5
)

mcd_food_choice2 = OptionChoice(
    option=mcd_option_sides,
    choice="Salad",
    choices_value="Salad",
    price=2.0
)

mcd_food_choice3 = OptionChoice(
    option=mcd_option_drinks,
    choice="Coke",
    choices_value="Coke",
    price=1.0
)

mcd_food_choice4 = OptionChoice(
    option=mcd_option_drinks,
    choice="Sprite",
    choices_value="Sprite",
    price=1.0
)

# Add choices to options
mcd_option_sides.add_choice(mcd_food_choice1)
mcd_option_sides.add_choice(mcd_food_choice2)

mcd_option_drinks.add_choice(mcd_food_choice3)
mcd_option_drinks.add_choice(mcd_food_choice4)

# Add options to McDonald's foods
mcd_food1.add_option(mcd_option_sides)
mcd_food1.add_option(mcd_option_drinks)

mcd_food2.add_option(mcd_option_sides)
mcd_food2.add_option(mcd_option_drinks)

# Get KFC restaurant from the controller
kfc_restaurant_from_controller = controller.get_restaurant_by_id(1)

# Create a cart for the user
cart = Cart(
    restaurant=kfc_restaurant,
)

# Add food to the cart
selected_food = SelectedFood(
    selected_food_id=uuid.uuid4(),
    food=kfc_food1,
    quantity=2
)

cart.add_to_cart(selected_food)

# Add the cart to the user's carts
user._User__carts.append(cart)

# Print the cart details
print(f"User {user.get_user_id()} has the following items in their cart:")
for food in cart.get_foods():
    print(f"- {food._SelectedFood__food._Food__name} (Quantity: {food._SelectedFood__quantity})")

# Add all foods to the controller
controller.add_food(kfc_food1)
controller.add_food(kfc_food2)
controller.add_food(dq_food1)
controller.add_food(dq_food2)
controller.add_food(mcd_food1)
controller.add_food(mcd_food2)

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
<<<<<<< HEAD
user.add_location(location)

# Print the user's locations
print(f"User {user.get_user_id()} has the following locations:")
for loc in user.get_locations():
    print(f"- {loc.full_name}, {loc.address}, {loc.street}, {loc.unit}, {loc.extra_information}")
=======
user.add_location(location)
>>>>>>> refs/remotes/origin/master
