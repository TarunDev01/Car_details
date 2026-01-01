import sys

class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def full_name(self):
        return f"{self.brand} {self.model}"

    def is_luxury(self):
        return self.price > 2000000

    def car_age(self, current_year):
        return current_year - self.year


if __name__ == "__main__":
    if not sys.stdin.isatty():
        print("Running in CI mode – skipping user input")
        sys.exit(0)

    print("=== Car Details Input ===")
    brand = input("Enter car brand: ")
    model = input("Enter car model: ")
    year = int(input("Enter manufacturing year: "))
    price = int(input("Enter price (INR): "))

    car = Car(brand, model, year, price)

    print("\nCar Name:", car.full_name())
    print("Car Age:", car.car_age(2025))
    print("Luxury:", car.is_luxury())
