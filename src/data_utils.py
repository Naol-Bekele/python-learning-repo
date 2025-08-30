"""
Data utility functions for basic Python operations.
"""


def validate_variable_name(name: str) -> bool:
    """
    Validate if a variable name follows Python naming conventions.

    Args:
        name (str): The variable name to validate

    Returns:
        bool: True if valid, False otherwise
    """
    if not name:
        return False

    # Check if starts with digit
    if name[0].isdigit():
        return False

    # Check if contains only valid characters
    valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
    return all(char in valid_chars for char in name)


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Convert Fahrenheit temperature to Celsius.

    Args:
        fahrenheit (float): Temperature in Fahrenheit

    Returns:
        float: Temperature in Celsius
    """
    return (fahrenheit - 32) * 5 / 9


def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Args:
        radius (float): Radius of the circle

    Returns:
        float: Area of the circle
    """
    return 3.14159 * radius**2
