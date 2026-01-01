class Car:
    def __init__(self, car_id, brand, model, price, quantity):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity
