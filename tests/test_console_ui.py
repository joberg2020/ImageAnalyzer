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

def test_console_ui_start_should_call_image_loader_load_image_with_url_when_user_enters_url(sut):
  # Arrange
  expected_url = 'http://somethingsomething.com/image.jpg'
  expected_exit_message = 'Program exits. Bye!'

  # Act
  with patch('builtins.input', side_effect=[expected_url, 'q']) as mock_input, patch('builtins.print') as mock_print:
    sut.start()
  
  # Assert
  mock_input.assert_called_with('Enter the URL of the image you want to analyze: ')
  sut.image_loader.load_from_url.assert_called_once_with(expected_url)
  mock_print.assert_any_call(expected_exit_message)


def test_console_ui_prints_properties_of_image_when_user_enters_url(sut, mock_image_analyzer):
  # Arrange
  mock_image_analyzer.analyze_image.return_value = {
    'dimensions': (100, 100),
     'color_mode': 'RGB'
     }
  mocked_url = 'http://somethingsomething.com/image.jpg'

  with patch('builtins.input', side_effect=[mocked_url, 'q']), patch('builtins.print') as mock_print:
    sut.start()
  
  # Assert
  mock_image_analyzer.analyze_image.assert_called_once()

  mock_print.assert_any_call("Image properties: {'dimensions': (100, 100), 'color_mode': 'RGB'}")
  