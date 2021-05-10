import datetime
import decimal

class VendingMachine:
    def __init__(self, id) -> None:
        self.__id = id
        self.__service_mode = False
        self.__levels = []
        self.__purchases = []
        self.__products = []

        for level in range(7):
            self.__levels.append(Level(level, self))

    def buy(self, number):
        return True

    def new_sale(self, purchase):
        self.__purchases.append(purchase)

class Level:
    def __init__(self, level, vending_machine) -> None:
        self.__vending_machine = vending_machine
        self.__level_number = level
        self.__spirales = []

        for _ in range(6):
            self.__spirales.append(Spirale(self))

    def buy(self, spiral_number):
        return True

class Spirale:
    def __init__(self, level) -> None:
        self.__level = level
        self.__products = []

    def buy(self):
        return True

    def add_product(self, product):
        self.__products.append(product)

    def remove_product(self, product):
        self.__products.remove(product)

    def turn_spirale(self):
        return True

    
class Purchase:
    def __init__(self, product) -> None:
        self.__product = product
        self.__date_of_sale = datetime.datetime.now()

class Product:
    def __init__(self, expiration_date, product_description) -> None:
        self.__expiration_date = expiration_date
        self.__product_description = product_description

class ProductDescription:
    def __init__(self, name, price, vending_machine) -> None:
        self.__name = name
        self.__price = price
        self.__vending_machine = vending_machine
    
    @property
    def get_name(self):
        return self.__name

    @property
    def get_price(self):
        return self.__price

