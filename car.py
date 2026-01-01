class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def full_name(self):
        return f"{self.brand} {self.model}"

    def is_luxury(self):
        return self.price > 2000000  # price in INR

    def car_age(self, current_year):
        return current_year - self.year
