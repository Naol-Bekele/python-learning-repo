"""
Conditional logic and control flow utilities.
"""


def validate_input(
    prompt, validation_func, error_message="Invalid input. Please try again."
):
    """
    Get validated input from user.

    Args:
        prompt: Input prompt to display
        validation_func: Function that returns True for valid input
        error_message: Message to display for invalid input

    Returns:
        Validated input
    """
    while True:
        try:
            user_input = input(prompt)
            if validation_func(user_input):
                return user_input
            else:
                print(error_message)
        except (ValueError, TypeError) as e:
            print(f"Error: {e}. Please try again.")


def temperature_converter(value, from_unit, to_unit):
    """
    Convert temperature between Celsius and Fahrenheit.

    Args:
        value: Temperature value to convert
        from_unit: Source unit ('C' or 'F')
        to_unit: Target unit ('C' or 'F')

    Returns:
        Converted temperature
    """
    if from_unit.upper() == "C" and to_unit.upper() == "F":
        return round(value * 9 / 5 + 32, 2)
    elif from_unit.upper() == "F" and to_unit.upper() == "C":
        return round((value - 32) * 5 / 9, 2)
    else:
        return value  # Same unit, no conversion needed


def find_factors(n):
    """
    Find all factors of a positive integer.

    Args:
        n: Positive integer to factor

    Returns:
        List of factors
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer")

    factors = []
    for num in range(1, n + 1):
        if n % num == 0:
            factors.append(num)
    return factors


def grade_calculator(score):
    """
    Convert a numerical score to a letter grade.

    Args:
        score: Numerical score (0-100)

    Returns:
        Letter grade
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
