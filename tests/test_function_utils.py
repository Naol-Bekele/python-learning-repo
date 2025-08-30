import pytest
from src.function_utils import (
    apply_lambda_operations,
    filter_with_lambda,
    sort_with_key,
)


def test_apply_lambda_operations():
    """Test applying lambda operations to data."""
    data = [1, 2, 3, 4, 5]
    squared = apply_lambda_operations(data, lambda x: x**2)
    assert squared == [1, 4, 9, 16, 25]


def test_filter_with_lambda():
    """Test filtering data with lambda condition."""
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = filter_with_lambda(data, lambda x: x % 2 == 0)
    assert evens == [2, 4, 6, 8, 10]


def test_sort_with_key():
    """Test sorting with key function."""
    data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    sorted_data = sort_with_key(data, lambda x: x[1])
    assert sorted_data == [("Bob", 25), ("Alice", 30), ("Charlie", 35)]
