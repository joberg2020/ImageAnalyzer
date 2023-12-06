from unittest.mock import patch, MagicMock
from src.image_loader import ImageLoader
from PIL import Image
import pytest
import io

with open('tests/test_data/test_jpg_200x300.jpg', 'rb') as buffer:
    test_jpg_data: bytes = buffer.read()

def test_load_from_url_should_return_image_object():
    with patch('requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = test_jpg_data
        mock_get.return_value = mock_response

        sut = ImageLoader()
        actual = sut.load_from_url('http://somethingsomething.com/image.jpg')
        assert isinstance(actual, Image.Image)

def test_load_from_url_should_raise_exception_when_status_code_is_not_200():
    with patch('requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        sut = ImageLoader()
        with pytest.raises(Exception):
            sut.load_from_url('http://somethingsomething.com/image.jpg')
