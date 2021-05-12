import datetime
import decimal

class VendingMachine:
    def __init__(self, id) -> None:
        self.__id = id
        self.__service_mode = False
        self.__levels = []
        self.__purchases = []
        self.__product_description = []

        for level in range(7):
            self.__levels.append(Level(level, self))

    def buy(self, number):
        return True

    def new_sale(self, purchase):
        self.__purchases.append(purchase)

    @property
    def id(self):
        return self.__id

    @property
    def service_mode(self):
        return self.__service_mode

    @service_mode.setter
    def set_service_mode(self, service_mode):
        self.__service_mode = service_mode

    @property
    def levels(self):
        return self.__levels

    @property
    def purchases(self):
        return self.__purchases

    @property
    def product_description(self):
        return self.__product_description

#############################################################

class Level:
    def __init__(self, level, vending_machine) -> None:
        self.__vending_machine = vending_machine
        self.__level_number = level
        self.__spirales = []

        for _ in range(6):
            self.__spirales.append(Spirale(self))

    def buy(self, spiral_number):
        return True

    @property
    def vending_machine(self):
        return self.__vending_machine

    @property
    def level_number(self):
        return self.__level_number

#############################################################

class Spirale:
    def __init__(self, level) -> None:
        self.__level = level
        self.__products = []

    @property
    def level(self):
        return self.__level

    def buy(self):
        return True

    def add_product(self, product):
        if len(self.__products) < 7:
            self.__products.append(product)

    def remove_product(self, product):
        if len(self.__products) > 0:
            self.__products.remove(product)

    def turn_spirale(self):
        return True

#############################################################

class Purchase:
    def __init__(self, product) -> None:
        self.__name = product.get_name()
        self.__price = product.get_price()
        self.__product = product
        self.__date_of_sale = datetime.datetime.now()

    @property
    def name(self):
        return self.__name
    @property
    def price(self):
        return self.__price
    @property
    def product(self):
        return self.__product
    @property
    def date_of_sale(self):
        return self.__date_of_sale

#############################################################

class Product:
    def __init__(self, expiration_date, product_description) -> None:
        self.__expiration_date = expiration_date
        self.__product_description = product_description

    @property
    def product_description(self):
        return self.__product_description

    @property
    def expiration_date(self):
        return self.__expiration_date
    
    @property
    def name(self):
        return self.__product_description.name()
    
    @property
    def price(self):
        return self.__product_description.price()

#############################################################

class ProductDescription:
    def __init__(self, name, price, vending_machine) -> None:
        self.__name = name
        self.__price = price
        self.__vending_machine = vending_machine

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def vending_machine(self):
        return self.__vending_machine