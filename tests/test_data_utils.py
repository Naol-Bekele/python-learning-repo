import pytest
from src.data_utils import (
    validate_variable_name,
    fahrenheit_to_celsius,
    calculate_circle_area,
)


def test_validate_variable_name():
    """Test variable name validation."""
    assert validate_variable_name("user_name") is True
    assert validate_variable_name("score1") is True
    assert validate_variable_name("_hidden_value") is True
    assert validate_variable_name("9lives") is False
    assert validate_variable_name("") is False


def test_fahrenheit_to_celsius():
    """Test Fahrenheit to Celsius conversion."""
    assert round(fahrenheit_to_celsius(212), 2) == 100.00
    assert round(fahrenheit_to_celsius(32), 2) == 0.00


def test_calculate_circle_area():
    """Test circle area calculation."""
    assert round(calculate_circle_area(5), 2) == 78.54
