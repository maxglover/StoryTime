from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

def add_speech_bubble(image_url, text):
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    # Example coordinates and bubble size
    bubble_coords = (50, 50, 400, 200)
    draw.rectangle(bubble_coords, outline="black", fill="white")
    draw.text((60, 60), text, fill="black", font=font)

    return image
