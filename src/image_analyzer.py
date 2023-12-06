from PIL import Image

class ImageAnalyzer:

  def analyze_image(self, image: Image) -> dict:
    """
    Analyze an image and return a dictionary of its properties.
    """
    return {'dimensions': image.size,
            'color_mode': image.mode}