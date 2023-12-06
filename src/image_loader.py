from PIL import Image
import io
import requests

class ImageLoader:
  
  def load_from_url(self, url: str) -> Image.Image:
    """
    Load an image from a URL.
    """
    response = requests.get(url)
    response.raise_for_status()

    image_stream = io.BytesIO(response.content)
    image = Image.open(image_stream)
    image.load()

    return image