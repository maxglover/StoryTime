from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

def add_speech_bubble(image_url, text):
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    # Determine the size of the text and create a bubble using textbbox
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    bubble_width = text_width + 20
    bubble_height = text_height + 20
    bubble_x = 10
    bubble_y = 10

    # Draw the bubble
    draw.rectangle([bubble_x, bubble_y, bubble_x + bubble_width, bubble_y + bubble_height], fill="white")
    draw.text((bubble_x + 10, bubble_y + 10), text, fill="black", font=font)

    return image
