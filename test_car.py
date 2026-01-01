from car import Car

def test_full_name():
    car = Car("Tata", "Nexon", 1400000, 17)
    assert car.full_name() == "Tata Nexon"

def test_car_details():
    car = Car("Tata", "Punch", 700000, 20)
    assert "Price" in car.car_details()
    assert "Mileage" in car.car_details()
