"""
Loop utility functions for common iteration patterns.
"""


def safe_while_loop(condition_func, action_func, max_iterations=1000):
    """
    Execute a while loop with safety limits to prevent infinite loops.

    Args:
        condition_func: Function that returns boolean for loop condition
        action_func: Function to execute each iteration
        max_iterations: Maximum number of iterations allowed

    Returns:
        Number of iterations performed
    """
    count = 0
    while condition_func() and count < max_iterations:
        action_func()
        count += 1
    return count


def nested_loop_matrix(rows, cols, action_func):
    """
    Execute a nested loop pattern for matrix operations.

    Args:
        rows: Number of rows
        cols: Number of columns
        action_func: Function called with (row, col) arguments

    Returns:
        List of results from action_func calls
    """
    results = []
    for row in range(rows):
        for col in range(cols):
            results.append(action_func(row, col))
    return results


def compound_interest_calculator(principal, rate, years):
    """
    Calculate compound interest over time.

    Args:
        principal: Initial investment amount
        rate: Annual interest rate as percentage
        years: Number of years to calculate

    Returns:
        List of tuples with (year, amount)
    """
    results = []
    current_amount = principal
    for year in range(1, years + 1):
        current_amount = current_amount * (1 + rate / 100)
        results.append((year, round(current_amount, 2)))
    return results
