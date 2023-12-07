from src.console_ui import ConsoleUI
from src.image_loader import ImageLoader
from src.image_analyzer import ImageAnalyzer

def main() -> None:
  """
  Main entry point of the application.
  """
  image_loader = ImageLoader()
  image_analyzer = ImageAnalyzer()
  console_ui = ConsoleUI(image_loader, image_analyzer)
  console_ui.start()

if __name__ == '__main__':
  main()