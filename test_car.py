
from car import Car

def test_total_cost_basic():
    car = Car("C101", "Tata", "Nexon", 1200000, 2)
    assert car.total_cost() == 2400000

def test_total_cost_single_car():
    car = Car("C102", "Honda", "City", 1000000, 1)
    assert car.total_cost() == 1000000

def test_total_cost_zero_quantity():
    car = Car("C103", "Hyundai", "i20", 800000, 0)
    assert car.total_cost() == 0

def test_negative_price():
    car = Car("C104", "Test", "ModelX", -500000, 1)
    assert car.total_cost() == -500000
