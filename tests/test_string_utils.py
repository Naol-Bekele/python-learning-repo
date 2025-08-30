import pytest
from src.string_utils import string_info, find_and_replace, format_squares


def test_string_info():
    """Test string information extraction."""
    info = string_info("   Hello World   ")

    assert info["length"] == 17
    assert info["uppercase"] == "   HELLO WORLD   "
    assert info["lowercase"] == "   hello world   "
    assert info["stripped"] == "Hello World"
    assert info["words"] == ["Hello", "World"]
    assert info["starts_with_space"] is True
    assert info["ends_with_space"] is True


def test_find_and_replace():
    """Test find and replace functionality."""
    original = "I'm telling you the truth; nothing but the truth!"
    expected = "I'm telling you lies; nothing but lies!"

    assert find_and_replace(original, "the truth", "lies") == expected


def test_format_squares():
    """Test square formatting."""
    squares = format_squares(1, 3)
    expected = ["1 squared is 1", "2 squared is 4", "3 squared is 9"]

    assert squares == expected
