class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


if __name__ == "__main__":
    car = Car("Toyota", "Innova")
    print("Car Name:", car.full_name())
