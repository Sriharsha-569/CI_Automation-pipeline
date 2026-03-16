import sys
import os
sys.path.insert(0, os.path.abspath("."))

from src.calculator import add, subtract, multiply, divide, percentage
import pytest


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -1) == -2


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_percentage():
    assert percentage(50, 200) == 25.0


def test_percentage_zero_total():
    with pytest.raises(ValueError):
        percentage(50, 0)


def test_add_floats():
    assert add(1.5, 2.5) == 4.0


def test_multiply_by_zero():
    assert multiply(100, 0) == 0
