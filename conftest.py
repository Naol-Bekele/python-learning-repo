import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))


# Global fixtures
@pytest.fixture
def sample_numbers():
    """Provide sample numbers for tests."""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def sample_strings():
    """Provide sample strings for tests."""
    return ["hello", "world", "python", "test"]


@pytest.fixture
def sample_data_dict():
    """Provide sample dictionary data for tests."""
    return {"name": "Test User", "age": 30, "email": "test@example.com"}


# Add custom command-line options
def pytest_addoption(parser):
    """Add custom command-line options to pytest."""
    parser.addoption(
        "--run-integration",
        action="store_true",
        default=False,
        help="run integration tests that require external services",
    )


# Configure which tests to run based on command-line options
def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line("markers", "integration: mark test as integration test")


def pytest_collection_modifyitems(config, items):
    """Skip integration tests unless explicitly requested."""
    if not config.getoption("--run-integration"):
        skip_integration = pytest.mark.skip(
            reason="need --run-integration option to run"
        )
        for item in items:
            if "integration" in item.keywords:
                item.add_marker(skip_integration)
