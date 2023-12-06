from src.console_ui import ConsoleUI
from unittest.mock import patch

def test_console_ui_ask_for_url_should_ask_for_url():
  # Arrange
  sut = ConsoleUI()
  expected = 'Enter the URL of the image you want to analyze: '

  # Act
  with patch('builtins.input', return_value=expected) as mock_input:
    actual = sut.ask_for_url()
  
  # Assert
  mock_input.assert_called_once_with(expected)
  assert actual == expected

