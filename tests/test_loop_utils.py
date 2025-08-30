import pytest
from src.loop_utils import (
    safe_while_loop,
    nested_loop_matrix,
    compound_interest_calculator,
)


def test_safe_while_loop():
    """Test safe while loop execution."""
    counter = 0

    def condition():
        return counter < 5

    def action():
        nonlocal counter
        counter += 1

    iterations = safe_while_loop(condition, action)
    assert iterations == 5
    assert counter == 5


def test_nested_loop_matrix():
    """Test nested loop matrix generation."""
    results = nested_loop_matrix(2, 3, lambda r, c: f"{r},{c}")
    assert results == ["0,0", "0,1", "0,2", "1,0", "1,1", "1,2"]


def test_compound_interest_calculator():
    """Test compound interest calculation."""
    results = compound_interest_calculator(100, 5, 3)
    expected = [(1, 105.0), (2, 110.25), (3, 115.76)]

    for (yr, amt), (exp_yr, exp_amt) in zip(results, expected):
        assert yr == exp_yr
        assert abs(amt - exp_amt) < 0.1
