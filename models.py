

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
        self.__orders = []

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
            
    def get_user_by_username(self, username):
        for user in self.__users:
            if user.username == username:
                return user

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
        
    def get_food_by_id(self, food_id):
        for food in self.__foods:
            print(food.get_food_id())
            if food.get_food_id() == food_id:
                return food
    
    def get_restaurant_by_id(self, restaurant_id):
        for restaurant in self.__restaurants:
            if restaurant.get_restaurant_id() == restaurant_id:
                return restaurant

    def get_categories(self):
        categories = []
        for food in self.__foods:
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
        datalist = [cat,rec,res]
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

    def get_choice_by_id(self, choice_id):
        for food in self.__foods:
            for option in food.get_food_options():
                for choice in option.get_choices():
                    if choice.get_id() == choice_id:
                        return choice
        return None

    def get_order_by_id(self, order_id):
        for order in self.__orders:
            if order.get_order_id() == order_id:
                return order
        return None
    def get_orders(self):
        return self.__orders

    def create_order(self, user, cart, location):
        order = Order(user, cart, location)
        self.__orders.append(order)
        return order


class User:
    def __init__(self, user_id: str, name, username, password):
        self.__user_id = user_id
        self.__name = name
        self.__username = username
        self.__password = password
        self.__carts = []
        self.__locations = []
        self.__user_order_history = []
        self.__promotions = []
        self.__reviews = []
        self.__favorites = set()

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
            
    def get_foods_incart(self):
        return len(self.__carts)
    
    def get_cart_by_restaurant_id(self, restaurant_id):
        for cart in self.__carts:
            if cart.get_restaurant().get_restaurant_id() == restaurant_id:
                return cart
        return None

    def get_cart_by_cart_id(self, cart_id):
        for cart in self.__carts:
            if cart.get_cart_id() == cart_id:
                return cart
        return None

    @property
    def name(self):
        return self.__name
    
    @property
    def username(self):
        return self.__username
    
    @property
    def password (self) :
        return self.__password

    def get_locations(self):
        return self.__locations


    def send_recentorder(self):
        return self.__user_order_history

    def add_cart(self, new_cart):
        self.__carts.append(new_cart)

    def get_carts(self):
        return self.__carts
        
    def add_favorite(self, restaurant):
        self.__favorites.add(restaurant)

    def remove_favorite(self, restaurant):
        self.__favorites.discard(restaurant)
    
    def get_favorites(self):
        return list(self.__favorites)

    def get_promotions_by_restaurant(self, restaurant):
        available_promotions = []
        for promotion in self.__promotions:
            if promotion.get_restaurant() == restaurant:
                available_promotions.append(promotion)
        return available_promotions
    
    def remove_cart(self, cart):
        self.__carts.remove(cart)


class Promotion:
    def __init__(self, name, restaurant, promotion_code, discount):
        self.__name = name
        self.__restaurant = restaurant
        self.__promotion_code = promotion_code
        self.__discount = discount

    def get_name(self):
        return self.__name

    def get_image(self):
        return self.__restaurant.get_image()

    def get_promotion_code(self):
        return self.__promotion_code
    
    def get_restaurant(self):
        return self.__restaurant

    def get_discount(self):
        return self.__discount

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

class Review:
    def __init__(self, user, comment, stars):
        self.__user = user
        self.__comment = comment
        self.__stars = stars

class Restaurant:
    def __init__(self, name, menu,description, score, reviews, restaurant_image):
        self.__restaurant_id = uuid.uuid4().hex
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
        self.__reviews.append(comment)
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
    def __init__(self, option, choice, price):
        self.__choice_id = uuid.uuid4().hex
        self.__option = option
        self.__choice = choice
        self.__price = price

    def get_id(self):
        return self.__choice_id

    def get_name(self):
        return self.__choice

    def get_option(self):
        return self.__option 
    
    def get_price(self):
        return self.__price

class Food:
    def __init__(self, restaurant, name, description, price, category, food_image, food_id=None):
        self.__restaurant = restaurant
        self.__food_id = food_id or uuid.uuid4().hex
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
    def __init__(self, food, quantity, selected_food_id=None):
        self.__selected_food_id = selected_food_id or uuid.uuid4().hex
        self.__food = food
        self.__selected_options = [SelectedFoodOption(option) for option in food.get_food_options()]
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity
    
    def get_name(self):
        return self.__food.get_name()

    def calculate_price(self):
        total_price = self.__food.get_price()
        return round(total_price * self.__quantity, 2)

    def add_choice(self, choice):
        for selected_option in self.__selected_options:
            option = selected_option.get_option()
            if choice in option.get_choices():
                selected_option.select_choice(choice)
    
    def get_selected_options(self):
        return self.__selected_options


class Cart:
    def __init__(self, restaurant : Restaurant, user: User):
        self.__cart_id = uuid.uuid4().hex
        self.__restaurant = restaurant
        self.__user = user
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
        return round(total_price, 2)

    def get_restaurant(self):
        return self.__restaurant

    def get_cart_id(self):
        return self.__cart_id
    
    def get_user(self):
        return self.__user

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
        return True

    def get_qr_code_data(self):
        return self.__qr_code_data

class CashPayment(Payment):
    def __init__(self, amount, currency, received_amount=0):
        super().__init__(amount, currency)
        self.__received_amount = received_amount
        self.__change = 0

    def pay(self):
        return True

class DeliveryOption:
    def __init__(self, name, estimate_time, price):
        self.__name = name
        self.__estimate_time = estimate_time
        self.__price = price
    
    def __str__(self):
        return self.__name + " < " + str(self.__estimate_time) + " " + str(self.__price) + " บาท"

    def get_price(self):
        return self.__price

    def get_name(self):
        return self.__name

class Order:
    # Create delivery options
    priority_delivery = DeliveryOption(
        name="Priority",
        estimate_time="25 นาที",
        price=50
    )

    standard_delivery = DeliveryOption(
        name="Standard",
        estimate_time="25 นาที",
        price=32
    )

    saver_delivery = DeliveryOption(
        name="Saver",
        estimate_time="35 นาที",
        price=0
    )

    delivery_options = [
        priority_delivery,
        standard_delivery,
        saver_delivery
    ]

    def __init__(self, user: User, cart: Cart, location: Location):
        self.__order_id = cart.get_cart_id()
        self.__user = user
        self.__cart = cart
        self.__location = location
        self.__delivery_option = self.standard_delivery
        self.__payment_method = None
        self.__selected_promotion = None
        # Not delivered
        self.__status = "Not Delivered"

    def select_location(self, new_location):
        self.__location = new_location

    def select_payment(self, new_payment):
        self.__payment_method = new_payment

    def select_delivery_option(self, delivery_name):
        self.__delivery_option = self.get_delivery_option_by_name(delivery_name)

    def get_delivery_option_by_name(self, delivery_name):
        for delivery_option in self.delivery_options:
            if delivery_option.get_name() == delivery_name:   
                return delivery_option

    def get_delivery_option(self):
        return self.__delivery_option

    def calculate_price(self):
        total_price = self.__cart.calculate_price() + self.__delivery_option.get_price()
        if (self.__selected_promotion):
            total_price -= self.__selected_promotion.get_discount() 
        return round(max(0, total_price), 2)

    def get_order_id(self):
        return self.__order_id

    def select_promotion(self, promotion):
        self.__selected_promotion = promotion

    def get_cart(self):
        return self.__cart
    
    def get_selected_promotion(self):
        return self.__selected_promotion
    
    def get_location(self):
        return self.__location
    
    def get_payment_method(self):
        return self.__payment_method
    
    def confirm_order_status(self):
        self.__status = "Delivered"
    
    def get_user(self):
        return self.__user



# Simulated Data
user = User(
    user_id="1",
    name="Yokphon ",
    username="foshforce",
    password="password123",
)

kfc_restaurant = Restaurant(
    name="KFC",
    menu=[],
    description="Fast-food chain known for its buckets of fried chicken, plus wings & sides.",
    score=4.5,
    reviews=[],
    restaurant_image="https://www.centralworld.co.th/storage/stores/K/kfc.jpg"
)

kfc_promotion = Promotion(
    name="KFC Discount",
    restaurant=kfc_restaurant,
    promotion_code="KFC2023",
    discount=10
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
    discount=10
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
    discount=10
)


tokyo_sushi_bar = Restaurant(
    name="Tokyo Sushi Bar",
    menu=[],
    description="Authentic Japanese sushi and sashimi with fresh ingredients.",
    score=4.8,
    reviews=[],
    restaurant_image="https://tse3.mm.bing.net/th?id=OIP.7gVZmLcz9XkjKvUpBagcYgHaE7&pid=Api"
)

texas_steakhouse = Restaurant(
    name="Texas Steakhouse",
    menu=[],
    description="Premium quality steaks and classic American barbecue.",
    score=4.7,
    reviews=[],
    restaurant_image="https://tse1.mm.bing.net/th?id=OIP.lx4-5D6QaCGN8upAqr8BUwHaDp&pid=Api"
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

dessert1 = Food(
    restaurant=dairy_queen_restaurant,
    food_id="7",
    name="Chocolate Cake",
    description="Rich and moist chocolate cake with a creamy frosting",
    price=4.99,
    category="Dessert",
    food_image="https://www.cookingclassy.com/wp-content/uploads/2019/10/chocolate-cake-3.jpg"
)

dessert2 = Food(
    restaurant=dairy_queen_restaurant,
    food_id="8",
    name="Strawberry Cheesecake",
    description="Smooth and creamy cheesecake with fresh strawberries",
    price=5.99,
    category="Dessert",
    food_image="https://images.unsplash.com/photo-1578985545062-69928b1d9587"
)

dessert3 = Food(
    restaurant=dairy_queen_restaurant,
    food_id="9",
    name="Mango Sticky Rice",
    description="Traditional Thai dessert with sticky rice, coconut milk, and ripe mango",
    price=3.99,
    category="Dessert",
    food_image="https://takestwoeggs.com/wp-content/uploads/2021/07/Thai-Mango-Sticky-Rice-Takestwoeggs-Process-Final-sq.jpg"
)

dessert4 = Food(
    restaurant=dairy_queen_restaurant,
    food_id="10",
    name="Matcha Ice Cream",
    description="Green tea flavored ice cream, smooth and refreshing",
    price=3.49,
    category="Dessert",
    food_image="https://sudachirecipes.com/wp-content/uploads/2022/08/matcha-ice-cream-thumbnail.jpg"
)

dessert5 = Food(
    restaurant=dairy_queen_restaurant,
    food_id="11",
    name="Tiramisu",
    description="Classic Italian dessert with layers of mascarpone and coffee-soaked ladyfingers",
    price=6.49,
    category="Dessert",
    food_image="https://natashaskitchen.com/wp-content/uploads/2019/11/Tiramisu-Cake-5.jpg"
)

dessert6 = Food(
    restaurant=mc_donald_restaurant,
    food_id="12",
    name="Caramel Pudding",
    description="Soft and silky caramel custard pudding",
    price=3.79,
    category="Dessert",
    food_image="https://cookmorphosis.com/wp-content/uploads/2020/12/ItalianTiramisu-2.jpg"
)

dessert7 = Food(
    restaurant=mc_donald_restaurant,
    food_id="13",
    name="Churros with Chocolate Dip",
    description="Crispy Spanish fried dough sticks with rich chocolate sauce",
    price=4.29,
    category="Dessert",
    food_image="https://easyweeknightrecipes.com/wp-content/uploads/2021/03/Churros16.jpg"
)

dessert8 = Food(
    restaurant=mc_donald_restaurant,
    food_id="14",
    name="Bubble Milk Tea",
    description="Refreshing milk tea with chewy tapioca pearls",
    price=4.99,
    category="Dessert",
    food_image="https://www.snixykitchen.com/wp-content/uploads/2014/01/CaramelPudding-4.jpg"
)

dessert9 = Food(
    restaurant=mc_donald_restaurant,
    food_id="15",
    name="Chocolate Lava Cake",
    description="Warm chocolate cake with a gooey molten center",
    price=5.49,
    category="Dessert",
    food_image="https://www.yourhomebasedmom.com/wp-content/uploads/2020/02/chocoalte-lava-cake-for-two.jpg"
)

dessert10 = Food(
    restaurant=mc_donald_restaurant,
    food_id="16",
    name="Macarons",
    description="French-style almond cookies with a creamy filling",
    price=6.99,
    category="Dessert",
    food_image="https://www.jordanwinery.com/wp-content/uploads/2020/04/French-Macaron-Cookie-Recipe-WebHero-6435.jpg"
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
    category="Main Course",
    food_image="https://cdn.britannica.com/34/206334-050-7637EB66/French-fries.jpg"
)

side_dish1 = Food(
    restaurant=kfc_restaurant,
    food_id="17",
    name="French Fries",
    description="Crispy golden fries with a sprinkle of salt",
    price=2.99,
    category="Side",
    food_image="https://images.pexels.com/photos/115740/pexels-photo-115740.jpeg?auto=compress&cs=tinysrgb&w=600"
)

side_dish2 = Food(
    restaurant=kfc_restaurant,
    food_id="18",
    name="Onion Rings",
    description="Crispy battered onion rings with a side of dipping sauce",
    price=3.49,
    category="Side",
    food_image="https://images.pexels.com/photos/31064139/pexels-photo-31064139/free-photo-of-gourmet-beef-dish-with-onion-rings-and-mushrooms.jpeg?auto=compress&cs=tinysrgb&w=600"
)

side_dish3 = Food(
    restaurant=mc_donald_restaurant,
    food_id="19",
    name="Mashed Potatoes",
    description="Smooth and buttery mashed potatoes with gravy",
    price=2.79,
    category="Side",
    food_image="https://images.unsplash.com/photo-1633356127583-ea05b7b1b5a6"
)

side_dish8 = Food(
    restaurant=mc_donald_restaurant,
    food_id="24",
    name="Baked Beans",
    description="Slow-cooked beans in a sweet and tangy sauce",
    price=2.99,
    category="Side",
    food_image="https://images.unsplash.com/photo-1586190848861-99aa4a171e90"
)


side_dish10 = Food(
    restaurant=kfc_restaurant,
    food_id="26",
    name="Mac & Cheese",
    description="Creamy and cheesy macaroni, a classic favorite",
    price=4.99,
    category="Side",
    food_image="https://images.unsplash.com/photo-1630628810905-5c0691e3fe72"
)

sushi_foods = [
    Food(tokyo_sushi_bar, "Salmon Nigiri", "Fresh salmon over sushi rice", 5.99, "Main Course", "https://media.istockphoto.com/id/492317534/th/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%96%E0%B9%88%E0%B8%B2%E0%B8%A2/%E0%B8%8B%E0%B8%B9%E0%B8%8A%E0%B8%B4%E0%B9%81%E0%B8%8B%E0%B8%A5%E0%B8%A1%E0%B8%AD%E0%B8%99.jpg?s=612x612&w=0&k=20&c=wij5X2QAKQlD1ND0xxid1vb_ExRDfBkwDkwrTM9ev1s="),
    Food(tokyo_sushi_bar, "Tuna Sashimi", "Sliced raw tuna with soy sauce", 6.99, "Main Course", "https://media.istockphoto.com/id/645670842/th/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%96%E0%B9%88%E0%B8%B2%E0%B8%A2/%E0%B8%9B%E0%B8%A5%E0%B8%B2%E0%B8%97%E0%B8%B9%E0%B8%99%E0%B9%88%E0%B8%B2%E0%B8%8B%E0%B8%B2%E0%B8%8A%E0%B8%B4%E0%B8%A1%E0%B8%B4%E0%B8%9B%E0%B8%A5%E0%B8%B2%E0%B8%94%E0%B8%B4%E0%B8%9A%E0%B9%83%E0%B8%99%E0%B8%AA%E0%B9%84%E0%B8%95%E0%B8%A5%E0%B9%8C%E0%B8%8D%E0%B8%B5%E0%B9%88%E0%B8%9B%E0%B8%B8%E0%B9%88%E0%B8%99%E0%B8%94%E0%B8%B1%E0%B9%89%E0%B8%87%E0%B9%80%E0%B8%94%E0%B8%B4%E0%B8%A1.jpg?s=612x612&w=0&k=20&c=JtVFc0_SAZ6KePXrB-WV_FO_zj0bilg7tb06jDCm2FQ="),
    Food(tokyo_sushi_bar, "Dragon Roll", "Shrimp tempura, avocado, and eel sauce", 7.99, "Main Course", "https://media.istockphoto.com/id/506104054/th/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%96%E0%B9%88%E0%B8%B2%E0%B8%A2/%E0%B8%A1%E0%B9%89%E0%B8%A7%E0%B8%99%E0%B8%8B%E0%B8%B9%E0%B8%8A%E0%B8%B4%E0%B8%A1%E0%B8%B1%E0%B8%87%E0%B8%81%E0%B8%A3%E0%B8%AA%E0%B8%B5%E0%B9%80%E0%B8%82%E0%B8%B5%E0%B8%A2%E0%B8%A7%E0%B8%81%E0%B8%B1%E0%B8%9A%E0%B8%9B%E0%B8%A5%E0%B8%B2%E0%B9%84%E0%B8%AB%E0%B8%A5-%E0%B8%AD%E0%B8%B0%E0%B9%82%E0%B8%A7%E0%B8%84%E0%B8%B2%E0%B9%82%E0%B8%94-%E0%B9%81%E0%B8%95%E0%B8%87%E0%B8%81%E0%B8%A7%E0%B8%B2-%E0%B8%A7%E0%B8%B2%E0%B8%8B%E0%B8%B2%E0%B8%9A%E0%B8%B4%E0%B9%81%E0%B8%A5%E0%B8%B0.jpg?s=612x612&w=0&k=20&c=iHESmE7TeybFRzhG6z0Wm0kQgHUhwA4fw8yRtHIYw6I="),
    Food(tokyo_sushi_bar, "Spicy Tuna Roll", "Tuna, spicy mayo, cucumber", 6.49, "Main Course", "https://media.istockphoto.com/id/495774976/th/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%96%E0%B9%88%E0%B8%B2%E0%B8%A2/%E0%B8%AA%E0%B9%84%E0%B8%9B%E0%B8%8B%E0%B8%B5%E0%B9%88%E0%B8%97%E0%B8%B9%E0%B8%99%E0%B9%88%E0%B8%B2%E0%B9%82%E0%B8%A3%E0%B8%A5.jpg?s=612x612&w=0&k=20&c=Ks09lxQka6H6eE-EikyDUabjT3e3NTMrMo_GL1Q-mUM="),
    Food(tokyo_sushi_bar, "California Roll", "Crab, avocado, cucumber", 5.99, "Main Course", "https://media.istockphoto.com/id/115547349/th/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%96%E0%B9%88%E0%B8%B2%E0%B8%A2/%E0%B9%81%E0%B8%84%E0%B8%A5%E0%B8%B4%E0%B8%9F%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B9%80%E0%B8%99%E0%B8%B5%E0%B8%A2%E0%B9%82%E0%B8%A3%E0%B8%A5.jpg?s=612x612&w=0&k=20&c=kwohQi26I6ZT_Y25albhWgXiRJ7nESPO9d24jyLCORA="),
    Food(tokyo_sushi_bar, "Miso Soup", "Traditional Japanese soup with tofu and seaweed", 2.99, "Side", "https://media.istockphoto.com/id/155341533/th/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%96%E0%B9%88%E0%B8%B2%E0%B8%A2/%E0%B8%8B%E0%B8%B8%E0%B8%9B%E0%B8%A1%E0%B8%B4%E0%B9%82%E0%B8%8B%E0%B8%B0.jpg?s=612x612&w=0&k=20&c=jQaumJaNXyvhhkaM3y9LRBymGkEgJjT11Ks2eFWYjd8="),
    Food(tokyo_sushi_bar, "Edamame", "Steamed soybeans with sea salt", 3.49, "Side", "https://media.istockphoto.com/id/175722505/th/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%96%E0%B9%88%E0%B8%B2%E0%B8%A2/%E0%B8%AA%E0%B8%B5%E0%B9%80%E0%B8%82%E0%B8%B5%E0%B8%A2%E0%B8%A7%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B8%97%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B9%8C-edamame-%E0%B8%81%E0%B8%B1%E0%B8%9A%E0%B9%80%E0%B8%81%E0%B8%A5%E0%B8%B7%E0%B8%AD%E0%B8%97%E0%B8%B0%E0%B9%80%E0%B8%A5.jpg?s=612x612&w=0&k=20&c=okihU8evE6J2mXfDjv8sv8LL6k1IaPqWENn4XALUqqs="),
    Food(tokyo_sushi_bar, "Gyoza", "Pan-fried Japanese dumplings", 4.99, "Side", "https://media.istockphoto.com/id/1301888183/th/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%96%E0%B9%88%E0%B8%B2%E0%B8%A2/%E0%B9%80%E0%B8%81%E0%B8%B5%E0%B9%8A%E0%B8%A2%E0%B8%A7%E0%B8%A2%E0%B9%88%E0%B8%B2%E0%B8%87.jpg?s=612x612&w=0&k=20&c=3gBmvVpxi_owbwff2IqnZbAojfH4z_W0xbCPLggj7_s="),
    Food(tokyo_sushi_bar, "Green Tea Ice Cream", "Matcha-flavored ice cream", 4.49, "Dessert", "https://media.istockphoto.com/id/1936927810/th/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%96%E0%B9%88%E0%B8%B2%E0%B8%A2/ice-cream-scoop-of-japanese-matcha-green-tea-on-wooden-table.jpg?s=612x612&w=0&k=20&c=V2_qqmz28sL-9APjIgq3JeSjDbXAs87NNqBj9FXdMxY="),
    Food(tokyo_sushi_bar, "Mochi", "Sweet rice cake with various fillings", 3.99, "Dessert", "https://media.istockphoto.com/id/1158085114/th/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%96%E0%B9%88%E0%B8%B2%E0%B8%A2/%E0%B9%84%E0%B8%AD%E0%B8%A8%E0%B8%81%E0%B8%A3%E0%B8%B5%E0%B8%A1%E0%B8%8D%E0%B8%B5%E0%B9%88%E0%B8%9B%E0%B8%B8%E0%B9%88%E0%B8%99%E0%B8%AB%E0%B8%A5%E0%B8%B2%E0%B8%A2%E0%B8%AA%E0%B8%B5%E0%B9%82%E0%B8%A1%E0%B8%88%E0%B8%B4%E0%B9%83%E0%B8%99%E0%B9%81%E0%B8%9B%E0%B9%89%E0%B8%87%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%A7%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%94%E0%B8%AD%E0%B8%81%E0%B8%A1%E0%B8%B0%E0%B8%A5%E0%B8%B4%E0%B8%9A%E0%B8%99%E0%B8%9E%E0%B8%B7%E0%B9%89%E0%B8%99%E0%B8%AB%E0%B8%A5%E0%B8%B1%E0%B8%87%E0%B8%AA%E0%B8%B5%E0%B8%9F%E0%B9%89%E0%B8%B2%E0%B8%84%E0%B8%AD%E0%B8%99%E0%B8%81%E0%B8%A3%E0%B8%B5%E0%B8%95-%E0%B8%82%E0%B8%99%E0%B8%A1%E0%B8%8D%E0%B8%B5%E0%B9%88%E0%B8%9B%E0%B8%B8%E0%B9%88%E0%B8%99%E0%B9%81%E0%B8%9A%E0%B8%9A%E0%B8%94%E0%B8%B1%E0%B9%89%E0%B8%87%E0%B9%80%E0%B8%94.jpg?s=612x612&w=0&k=20&c=F04jG2wXV5oDDntCxglE6Mn20OBvtdhWTudDVGxtBT8="),
    Food(tokyo_sushi_bar, "Tempura Shrimp", "Lightly battered deep-fried shrimp", 6.99, "Main Course", "https://media.istockphoto.com/id/1214520832/th/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%96%E0%B9%88%E0%B8%B2%E0%B8%A2/%E0%B9%80%E0%B8%97%E0%B8%A1%E0%B8%9B%E0%B8%B8%E0%B8%A3%E0%B8%B0.jpg?s=612x612&w=0&k=20&c=apk7loqRt3cn-siOmRLPdJKbaHnerZexTxIV-OLGkGc="),
    Food(tokyo_sushi_bar, "Tonkotsu Ramen", "Pork bone broth ramen with chashu", 9.99, "Main Course", "https://media.istockphoto.com/id/1144176036/th/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%96%E0%B9%88%E0%B8%B2%E0%B8%A2/%E0%B8%9A%E0%B8%B0%E0%B8%AB%E0%B8%A1%E0%B8%B5%E0%B9%88%E0%B8%A3%E0%B8%B2%E0%B9%80%E0%B8%A1%E0%B9%87%E0%B8%87%E0%B8%8D%E0%B8%B5%E0%B9%88%E0%B8%9B%E0%B8%B8%E0%B9%88%E0%B8%99.jpg?s=612x612&w=0&k=20&c=QvmnwaBOmcpqtVFi-KYil3e2CSF7vCVQ4X9sUbvdtP4="),
    Food(tokyo_sushi_bar, "Chicken Teriyaki", "Grilled chicken glazed with teriyaki sauce", 8.99, "Main Course", "https://media.istockphoto.com/id/1348103225/th/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%96%E0%B9%88%E0%B8%B2%E0%B8%A2/%E0%B9%84%E0%B8%81%E0%B9%88%E0%B9%80%E0%B8%97%E0%B8%AD%E0%B8%A3%E0%B8%B4%E0%B8%A2%E0%B8%B2%E0%B8%81%E0%B8%B4%E0%B9%80%E0%B8%AD%E0%B9%80%E0%B8%8A%E0%B8%B5%E0%B8%A2%E0%B9%80%E0%B8%9E%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%AA%E0%B8%B8%E0%B8%82%E0%B8%A0%E0%B8%B2%E0%B8%9E.jpg?s=612x612&w=0&k=20&c=f3NrNg_84R0_XJCK6PwKjomPMfBqayFuz6n4faDhGoI="),
    Food(tokyo_sushi_bar, "Sashimi Platter", "Assorted fresh sashimi", 12.99, "Main Course", "https://media.istockphoto.com/id/1225608498/th/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%96%E0%B9%88%E0%B8%B2%E0%B8%A2/%E0%B8%8A%E0%B8%B8%E0%B8%94%E0%B8%8B%E0%B8%B2%E0%B8%8A%E0%B8%B4%E0%B8%A1%E0%B8%B4%E0%B8%AB%E0%B8%A3%E0%B8%B9%E0%B8%AB%E0%B8%A3%E0%B8%B2.jpg?s=612x612&w=0&k=20&c=-m6hgSZ9ML6F3Y1urgmZwkr5YXGg5JgUzMlGizrdFlY="),
    Food(tokyo_sushi_bar, "Takoyaki", "Japanese octopus balls with sweet sauce", 5.49, "Side", "https://media.istockphoto.com/id/622003890/th/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%96%E0%B9%88%E0%B8%B2%E0%B8%A2/%E0%B8%97%E0%B8%B2%E0%B9%82%E0%B8%81%E0%B8%B0%E0%B8%A2%E0%B8%B2%E0%B8%81%E0%B8%B4.jpg?s=612x612&w=0&k=20&c=MbuCP2gtay-Drbkm8TwGlXGlifkTde4v2nBVRnuet_Y="),
    Food(tokyo_sushi_bar, "Yakitori", "Grilled chicken skewers", 6.49, "Main Course", "https://media.istockphoto.com/id/1171255420/th/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%96%E0%B9%88%E0%B8%B2%E0%B8%A2/%E0%B8%AD%E0%B8%B2%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%8D%E0%B8%B5%E0%B9%88%E0%B8%9B%E0%B8%B8%E0%B9%88%E0%B8%99.jpg?s=612x612&w=0&k=20&c=4MiKZcQxFPAzUhA9oo6KL9UxrD5jmjfdmRWqwNdqT7w="),
    Food(tokyo_sushi_bar, "Dorayaki", "Japanese pancake with red bean filling", 4.99, "Dessert", "https://media.istockphoto.com/id/1389397740/th/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%96%E0%B9%88%E0%B8%B2%E0%B8%A2/%E0%B9%82%E0%B8%94%E0%B8%A3%E0%B8%B2%E0%B8%A2%E0%B8%B2%E0%B8%81%E0%B8%B4.jpg?s=612x612&w=0&k=20&c=1td6qVo-ol-LKeFJnWkxZdir35Nc70rwTBgKcqKkmuQ="),
    Food(tokyo_sushi_bar, "Japanese Cheesecake", "Fluffy and light cheesecake", 5.99, "Dessert", "https://media.istockphoto.com/id/1224722546/th/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%96%E0%B9%88%E0%B8%B2%E0%B8%A2/%E0%B8%8A%E0%B8%B5%E0%B8%AA%E0%B9%80%E0%B8%84%E0%B9%89%E0%B8%81%E0%B8%9C%E0%B9%89%E0%B8%B2%E0%B8%9D%E0%B9%89%E0%B8%B2%E0%B8%A2%E0%B8%8D%E0%B8%B5%E0%B9%88%E0%B8%9B%E0%B8%B8%E0%B9%88%E0%B8%99-jiggly-%E0%B8%9A%E0%B8%99%E0%B8%88%E0%B8%B2%E0%B8%99.jpg?s=612x612&w=0&k=20&c=KMyWUFDYhNqLGKvVx3m9BIUUZR1dNRu8_p28DMjm7xw="),
]

steakhouse_foods = [
    Food(texas_steakhouse, "T-Bone Steak", "Perfectly grilled T-Bone steak", 15.99, "Main Course", "https://cdn.pixabay.com/photo/2019/10/23/13/58/food-4571699_1280.jpg"),
    Food(texas_steakhouse, "BBQ Ribs", "Slow-cooked ribs with smoky BBQ sauce", 14.99, "Main Course", "https://cdn.pixabay.com/photo/2017/06/05/18/46/pork-ribs-2374889_1280.jpg"),
    Food(texas_steakhouse, "Baked Potato", "Oven-baked potato with sour cream", 4.99, "Side", "https://cdn.pixabay.com/photo/2019/03/18/15/27/rotten-4063353_1280.jpg"),
    Food(texas_steakhouse, "Caesar Salad", "Fresh romaine lettuce with parmesan and croutons", 6.99, "Side", "https://cdn.pixabay.com/photo/2023/07/18/19/19/spring-rolls-8135469_1280.jpg"),
    Food(texas_steakhouse, "Brownie Sundae", "Warm brownie with vanilla ice cream", 6.49, "Dessert", "https://media.istockphoto.com/id/1199942388/th/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%96%E0%B9%88%E0%B8%B2%E0%B8%A2/%E0%B8%8A%E0%B8%B4%E0%B9%89%E0%B8%99%E0%B9%80%E0%B8%84%E0%B9%89%E0%B8%81%E0%B8%8A%E0%B9%87%E0%B8%AD%E0%B8%84%E0%B9%82%E0%B8%81%E0%B9%81%E0%B8%A5%E0%B8%95%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%81%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B8%9A%E0%B8%99%E0%B8%9E%E0%B8%B7%E0%B9%89%E0%B8%99%E0%B8%AB%E0%B8%A5%E0%B8%B1%E0%B8%87%E0%B8%AA%E0%B8%B5%E0%B8%82%E0%B8%B2%E0%B8%A7-%E0%B8%A1%E0%B8%B8%E0%B8%A1%E0%B8%A1%E0%B8%AD%E0%B8%87%E0%B8%94%E0%B9%89%E0%B8%B2%E0%B8%99%E0%B8%9A%E0%B8%99.jpg?s=612x612&w=is&k=20&c=8Td7qnfEwj6eqhvlfLXehTvlZ8PD3hF4HQI2NgfJbAQ="),
    Food(texas_steakhouse, "Apple Pie", "Classic American apple pie", 5.99, "Dessert", "https://media.istockphoto.com/id/450752471/th/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%96%E0%B9%88%E0%B8%B2%E0%B8%A2/%E0%B8%82%E0%B8%99%E0%B8%A1%E0%B8%9E%E0%B8%B2%E0%B8%A2%E0%B9%81%E0%B8%AD%E0%B8%9B%E0%B9%80%E0%B8%9B%E0%B8%B4%E0%B9%89%E0%B8%A5%E0%B8%AD%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B9%81%E0%B8%81%E0%B8%99%E0%B8%B4%E0%B8%84%E0%B9%82%E0%B8%AE%E0%B8%A1%E0%B9%80%E0%B8%A1%E0%B8%94.jpg?s=612x612&w=0&k=20&c=hMrEDZS4r67NwMrroX4rpF1Zftq6TC0i4gYD_BVgdj4="),
]


for food in sushi_foods:
    tokyo_sushi_bar.add_food(food)
    controller.add_food(food)

for food in steakhouse_foods:
    texas_steakhouse.add_food(food)
    controller.add_food(food)

# 📌 เพิ่มร้านค้าเข้าไปใน Controller
controller.add_restaurant(tokyo_sushi_bar)
controller.add_restaurant(texas_steakhouse)
# Add foods to each restaurant
kfc_restaurant.add_food(kfc_food1)
kfc_restaurant.add_food(kfc_food2)

dairy_queen_restaurant.add_food(dq_food1)
dairy_queen_restaurant.add_food(dq_food2)
dairy_queen_restaurant.add_food(dessert1)
dairy_queen_restaurant.add_food(dessert2)
dairy_queen_restaurant.add_food(dessert3)
dairy_queen_restaurant.add_food(dessert4)
dairy_queen_restaurant.add_food(dessert5)
dairy_queen_restaurant.add_food(dessert6)
dairy_queen_restaurant.add_food(dessert7)
dairy_queen_restaurant.add_food(dessert8)
dairy_queen_restaurant.add_food(dessert9)
dairy_queen_restaurant.add_food(dessert10)
controller.add_food(side_dish1)
controller.add_food(side_dish2)
controller.add_food(side_dish3)
controller.add_food(side_dish8)
controller.add_food(side_dish10)




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
    price=0.5
)

dq_food_choice2 = OptionChoice(
    option=dq_option_toppings,
    choice="Sprinkles",
    price=0.5
)

dq_food_choice3 = OptionChoice(
    option=dq_option_toppings,
    choice="Oreo Crumbs",
    price=0.5
)

dq_food_choice4 = OptionChoice(
    option=dq_option_size,
    choice="Small",
    price=0.0
)

dq_food_choice5 = OptionChoice(
    option=dq_option_size,
    choice="Medium",
    price=1.0
)

dq_food_choice6 = OptionChoice(
    option=dq_option_size,
    choice="Large",
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
    price=1.5
)

kfc_food_choice2 = OptionChoice(
    option=kfc_option_sides,
    choice="Coleslaw",
    price=1.0
)

kfc_food_choice3 = OptionChoice(
    option=kfc_option_drinks,
    choice="Coke",
    price=1.0
)

kfc_food_choice4 = OptionChoice(
    option=kfc_option_drinks,
    choice="Pepsi",
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
    price=1.5
)

mcd_food_choice2 = OptionChoice(
    option=mcd_option_sides,
    choice="Salad",
    price=2.0
)

mcd_food_choice3 = OptionChoice(
    option=mcd_option_drinks,
    choice="Coke",
    price=1.0
)

mcd_food_choice4 = OptionChoice(
    option=mcd_option_drinks,
    choice="Sprite",
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
    user=user
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
user.add_location(location)

# Multiply all food prices by 35
for food in controller.get_restaurants():
    for item in food.get_menu():
        item._Food__price *= 10

# Multiply all choice prices by 10
for food in controller.get_restaurants():
    for item in food.get_menu():
        for option in item.get_food_options():
            for choice in option.get_choices():
                choice._OptionChoice__price *= 10