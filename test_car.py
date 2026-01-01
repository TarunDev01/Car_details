
def test_full_name():
    car = Car("Toyota", "Fortuner", 2022, 4500000)
    assert car.full_name() == "Toyota Fortuner"

def test_is_luxury_true():
    car = Car("BMW", "X5", 2023, 8000000)
    assert car.is_luxury() is True

def test_is_luxury_false():
    car = Car("Maruti", "Swift", 2021, 800000)
    assert car.is_luxury() is False

def test_car_age():
    car = Car("Honda", "City", 2020, 1500000)
    assert car.car_age(2025) == 5
