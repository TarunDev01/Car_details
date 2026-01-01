from car import Car

def test_full_name():
    car = Car("Honda", "City")
    assert car.full_name() == "Honda City"
