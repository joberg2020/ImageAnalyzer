from src.image_analyzer import ImageAnalyzer
from unittest.mock import Mock
from PIL import Image
import io

def test_analyze_image_should_return_dictionary_with_dimensions_property():
  # Arrange
    with open('tests/test_data/test_png_323x323.png', 'rb') as buffer:
      test_png_data: bytes = buffer.read()

    image = Image.open(io.BytesIO(test_png_data))
    sut = ImageAnalyzer()
   
    # Act
    actual = sut.analyze_image(image)

    # Assert
    expected_dimensions = (323, 323)
    assert actual['dimensions'] == expected_dimensions