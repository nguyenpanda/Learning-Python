import sys
import csv
from colorama import Back, Style, Fore


class Item:
    pay_rate = 0.8
    all_ins = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"{price} must greater than zero"
        assert quantity >= 0, f"{quantity} must greater than zero"

        # Assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Action to execute
        Item.all_ins.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        return self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file):  # cls stand for class
        with open(file, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            items = list(reader)

        for item in items:
            Item(
                name=str(item.get('name')),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", {self.price}, {self.quantity})'

    def __str__(self):
        return f'{self.name}: {self.price}*{self.quantity}'


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phone=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(name, price, quantity)

        # Run validations to the received arguments
        assert broken_phone >= 0, f"{broken_phone} must great than zero"

        # Assign to self object
        self.broken_phone = broken_phone

class Laptop(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_laptop=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(name, price, quantity)

        # Run validations to the received arguments
        assert broken_laptop >= 0, f"{broken_laptop} must great than zero"

        # Assign to self object
        self.broken_laptop = broken_laptop

phone1 = Phone("Iphone", 1000, 3, 1)
print(phone1.all_ins)

print(Back.BLACK, Style.BRIGHT, Fore.GREEN)
print(f"All class level: {[i for i in Item.__dict__]}")  # All class level
print(f"All instance level: {[i for i in phone1.__dict__]} \n")  # All instance level
print(Style.RESET_ALL)

print(sys)

