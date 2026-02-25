# A simple function
def calculate_discounted_price(price, discount_rate):
    if discount_rate < 0 or discount_rate > 1:
        raise ValueError("Discount must be between 0 and 1")
    return price * (1 - discount_rate)

# TESTS
import pytest

def test_normal_discount():
    assert calculate_discounted_price(100, 0.2) == 80

def test_zero_discount():
    assert calculate_discounted_price(50, 0) == 50

def test_full_discount():
    assert calculate_discounted_price(200, 1) == 0

def test_invalid_discount_high():
    with pytest.raises(ValueError):
        calculate_discounted_price(100, 1.5)

def test_invalid_discount_negative():
    with pytest.raises(ValueError):
        calculate_discounted_price(100, -0.1)

  ''' output

  ============================= test session starts =============================
collecting ... collected 5 items

pytest-example.py::test_normal_discount PASSED                           [ 20%]
pytest-example.py::test_zero_discount PASSED                             [ 40%]
pytest-example.py::test_full_discount PASSED                             [ 60%]
pytest-example.py::test_invalid_discount_high PASSED                     [ 80%]
pytest-example.py::test_invalid_discount_negative PASSED                 [100%]

============================== 5 passed in 0.01s ==============================

Process finished with exit code 0
'''
