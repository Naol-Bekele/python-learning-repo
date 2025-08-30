import numpy as np


def create_sample_data():
    """Create sample data for demonstration"""
    # Sample array operations
    arr = np.arange(1, 17).reshape(4, 4)
    return arr


def array_operations_demo():
    """Demonstrate common array operations"""
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    B = np.array([[5, 4, 3], [7, 6, 5], [9, 8, 7]])

    operations = {
        "scalar_multiplication": 2 * A,
        "element_wise_addition": A + B,
        "matrix_multiplication": A @ B,
        "comparison": A > 5,
    }
    return operations


def statistical_operations(matrix):
    """Perform statistical operations on array"""
    stats = {
        "min": matrix.min(),
        "max": matrix.max(),
        "mean": matrix.mean(),
        "sum": matrix.sum(),
        "std": matrix.std(),
        "column_sums": matrix.sum(axis=0),
        "row_sums": matrix.sum(axis=1),
    }
    return stats
