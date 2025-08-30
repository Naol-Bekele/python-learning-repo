import pytest
import requests
from unittest.mock import patch, MagicMock
from src.api_utils import (
    make_api_request,
    get_joke,
    get_dog_images,
)


@patch("src.api_utils.requests.get")
def test_make_api_request_success(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    response = make_api_request("http://test.com")
    assert response.status_code == 200


@patch("src.api_utils.requests.get")
def test_make_api_request_timeout(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout
    response = make_api_request("http://test.com")
    assert response is None


@patch("src.api_utils.make_api_request")
def test_get_joke(mock_request):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "setup": "Test joke",
        "punchline": "Test punchline",
    }
    mock_request.return_value = mock_response

    setup, punchline = get_joke()
    assert setup == "Test joke"
    assert punchline == "Test punchline"


@patch("src.api_utils.make_api_request")
def test_get_dog_images(mock_request):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": ["image1.jpg", "image2.jpg"]}
    mock_request.return_value = mock_response

    images = get_dog_images(2)
    assert len(images) == 2
    assert "image1.jpg" in images
