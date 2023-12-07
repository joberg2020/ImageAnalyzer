import pytest
from src.console_ui import ConsoleUI
from unittest.mock import Mock, patch

@pytest.fixture
def mock_image_loader():
  return Mock()

@pytest.fixture
def mock_image_analyzer():
  return Mock()

@pytest.fixture
def sut(mock_image_loader, mock_image_analyzer):
  return ConsoleUI(mock_image_loader, mock_image_analyzer)

def test_console_ui_ask_for_url_should_ask_for_url(sut):
  # Arrange
  expected = 'Enter the URL of the image you want to analyze: '

  # Act
  with patch('builtins.input', return_value=expected) as mock_input:
    actual = sut.ask_for_url()
  
  # Assert
  mock_input.assert_called_once_with(expected)
  assert actual == expected

def test_console_ui_start_should_ask_for_url_and_return_exitmessage_when_user_enters_q(sut):
  # Arrange
  expected_exit_message = 'Program exits. Bye!'

  # Act
  with patch('builtins.input', return_value='q') as mock_input, patch('builtins.print') as mock_print:
    sut.start()
  
  # Assert
  mock_input.assert_called_once_with('Enter the URL of the image you want to analyze: ')
  mock_print.assert_called_once_with(expected_exit_message)

def test_console_ui_constructor_should_recive_image_loader_and_image_analyzer(sut):

  # Assert
  assert isinstance(sut.image_loader, Mock)
  assert isinstance(sut.image_analyzer, Mock)