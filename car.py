class Car:
    def __init__(self, brand, model, price, mileage):
        self.brand = brand
        self.model = model
        self.price = price        # price in INR
        self.mileage = mileage    # km/l

    def full_name(self):
        return f"{self.brand} {self.model}"

    def car_details(self):
        return f"{self.full_name()} | Price: ₹{self.price} | Mileage: {self.mileage} km/l"


if __name__ == "__main__":
    cars = [
        Car("Toyota", "Innova", 2500000, 15),
        Car("Honda", "City", 1200000, 18),
        Car("Hyundai", "Creta", 1500000, 17),
        Car("Maruti", "Swift", 800000, 22)
    ]

    print("Car Models with Price and Mileage:")
    for car in cars:
        print(car.car_details())
