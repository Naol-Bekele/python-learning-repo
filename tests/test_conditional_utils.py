import pytest
from src.conditional_utils import temperature_converter, find_factors, grade_calculator


def test_temperature_converter():
    """Test temperature conversion."""
    # Celsius to Fahrenheit
    assert temperature_converter(0, "C", "F") == 32
    assert temperature_converter(100, "C", "F") == 212

    # Fahrenheit to Celsius
    assert temperature_converter(32, "F", "C") == 0
    assert temperature_converter(212, "F", "C") == 100

    # Same unit
    assert temperature_converter(50, "C", "C") == 50


def test_find_factors():
    """Test factor finding."""
    assert find_factors(12) == [1, 2, 3, 4, 6, 12]
    assert find_factors(7) == [1, 7]
    assert find_factors(1) == [1]

    # Test error case
    with pytest.raises(ValueError):
        find_factors(0)


def test_grade_calculator():
    """Test grade calculation."""
    assert grade_calculator(95) == "A"
    assert grade_calculator(85) == "B"
    assert grade_calculator(75) == "C"
    assert grade_calculator(65) == "D"
    assert grade_calculator(55) == "F"
