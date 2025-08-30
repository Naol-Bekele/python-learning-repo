import numpy as np
from src.nb_data_utils import (
    create_sample_data,
    array_operations_demo,
    statistical_operations,
)


def test_create_sample_data():
    data = create_sample_data()
    assert data.shape == (4, 4)
    assert data[0, 0] == 1


def test_array_operations():
    operations = array_operations_demo()
    assert "scalar_multiplication" in operations
    assert operations["scalar_multiplication"].shape == (3, 3)


def test_statistical_operations():
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    stats = statistical_operations(matrix)
    assert stats["min"] == 1
    assert stats["max"] == 9
    assert stats["mean"] == 5.0
