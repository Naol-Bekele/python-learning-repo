import pytest
from src.data_structures import (
    create_named_tuple,
    safe_list_operations,
    list_comprehension_examples,
    sort_with_custom_key,
    nested_data_examples,
    dictionary_operations,
    nested_dictionary_example,
    calculate_mean,
    calculate_median,
    cats_with_hats,
)


def test_create_named_tuple():
    """Test named tuple creation."""
    Point = create_named_tuple("Point", ["x", "y"])
    p = Point(10, 20)

    assert p.x == 10
    assert p.y == 20
    assert p == (10, 20)





def test_list_comprehension_examples():
    """Test list comprehension examples."""
    results = list_comprehension_examples()

    assert results["squares"] == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    assert results["even_squares"] == [0, 4, 16, 36, 64]
    assert results["flattened_matrix"] == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert results["float_numbers"] == [1.5, 2.3, 5.25]


def test_sort_with_custom_key():
    """Test sorting with custom key."""
    students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
    sorted_students = sort_with_custom_key(students, lambda x: x[1], reverse=True)

    assert sorted_students == [("Bob", 92), ("Alice", 85), ("Charlie", 78)]


def test_nested_data_examples():
    """Test nested data examples."""
    results = nested_data_examples()

    assert results["matrix"][1][2] == 6
    assert results["student_grades"][1][1] == 92


def test_dictionary_operations():
    """Test dictionary operations."""
    results = dictionary_operations()

    assert "Colorado" in results["capitals"]
    assert "Texas" not in results["capitals"]
    assert results["removed_value"] == "Albany"
    assert "California" in results["keys"]
    assert "Denver" in results["values"]


def test_nested_dictionary_example():
    """Test nested dictionary example."""
    states = nested_dictionary_example()

    assert states["Texas"]["capital"] == "Austin"
    assert states["Texas"]["population"] == 30000000
    assert states["New York"]["flower"] == "Rose"


def test_calculate_mean():
    """Test mean calculation."""
    values = [1, 2, 3, 4, 5]
    assert calculate_mean(values) == 3.0


def test_calculate_median():
    """Test median calculation."""
    # Odd number of elements
    assert calculate_median([1, 3, 2]) == 2

    # Even number of elements
    assert calculate_median([1, 3, 2, 4]) == 2.5


def test_cats_with_hats():
    """Test cats with hats solution."""
    hatted_cats = cats_with_hats()

    # Should be 10 cats with hats (perfect squares)
    assert len(hatted_cats) == 10
    assert hatted_cats == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
