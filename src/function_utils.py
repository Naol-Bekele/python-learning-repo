"""
Function utility module with helper functions for functional programming patterns.
"""


def apply_lambda_operations(data, operation):
    """
    Apply a lambda operation to each element in data.

    Args:
        data: Iterable to process
        operation: Lambda function to apply

    Returns:
        Result of applying the operation
    """
    return [operation(x) for x in data]


def filter_with_lambda(data, condition):
    """
    Filter data based on a lambda condition.

    Args:
        data: Iterable to filter
        condition: Lambda function that returns boolean

    Returns:
        Filtered list
    """
    return [x for x in data if condition(x)]


def sort_with_key(data, key_func):
    """
    Sort data using a key function.

    Args:
        data: Iterable to sort
        key_func: Function to extract comparison key

    Returns:
        Sorted list
    """
    return sorted(data, key=key_func)


# Example lambda functions for common operations
square = lambda x: x**2
is_even = lambda x: x % 2 == 0
get_second_element = lambda x: x[1]
to_lower = lambda s: s.lower()
