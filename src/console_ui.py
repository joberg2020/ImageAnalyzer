from src.image_analyzer import ImageAnalyzer
from src.image_loader import ImageLoader


class ConsoleUI:

  def __init__(self, image_loader: ImageLoader, image_analyzer: ImageAnalyzer) -> None:
    """
    Creates a new console instance.
    """
    self.image_loader = image_loader
    self.image_analyzer = image_analyzer

  def start(self) -> None:
    """
    Start the console UI.
    """
    exit_message = 'Program exits. Bye!'
    while True:
      url = self.ask_for_url()
      if url == 'q':
        break
      try: 
        image = self.image_loader.load_from_url(url)
        image_properties = self.image_analyzer.analyze_image(image)
        print(f'Image properties: {image_properties}')

      except Exception as e:
        print(f'Error: {e}')
    print(exit_message)

  def ask_for_url(self) -> str:
    """
    Ask the user for the URL of the image they want to analyze.
    """
    return input('Enter the URL of the image you want to analyze: ')