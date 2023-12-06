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

def test_console_ui_start_should_ask_for_url_and_return_exitmessage_when_user_enters_q():
  # Arrange
  sut = ConsoleUI()
  expected_exit_message = 'Program exits. Bye!'

  # Act
  with patch('builtins.input', return_value='q') as mock_input, patch('builtins.print') as mock_print:
    sut.start()
  
  # Assert
  mock_input.assert_called_once_with('Enter the URL of the image you want to analyze: ')
  mock_print.assert_called_once_with(expected_exit_message)