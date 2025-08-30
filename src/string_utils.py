"""
String utility functions for common string operations.
"""


def string_info(text: str) -> dict:
    """
    Get information about a string.

    Args:
        text (str): The string to analyze

    Returns:
        dict: Dictionary with string information
    """
    return {
        "length": len(text),
        "uppercase": text.upper(),
        "lowercase": text.lower(),
        "stripped": text.strip(),
        "words": text.split(),
        "starts_with_space": text.startswith(" "),
        "ends_with_space": text.endswith(" "),
    }


def find_and_replace(text: str, find_str: str, replace_str: str) -> str:
    """
    Find and replace text in a string.

    Args:
        text (str): The original text
        find_str (str): The text to find
        replace_str (str): The text to replace with

    Returns:
        str: The modified text
    """
    return text.replace(find_str, replace_str)


def format_squares(start: int, end: int) -> list:
    """
    Format numbers and their squares using f-strings.

    Args:
        start (int): Starting number
        end (int): Ending number (inclusive)

    Returns:
        list: List of formatted strings
    """
    return [f"{n} squared is {n * n}" for n in range(start, end + 1)]
