import base64
import random
import string
import io
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def generate_captcha():
    height = 150
    width = 70
    font_size = 32
    number_of_line = 5
    number_of_points = 200

    image = Image.new("RGBA", size=[height, width], color="white")
    draw = ImageDraw.Draw(image)
    words: str = generate_random_words()

    try:
        font = ImageFont.truetype(font="arial.ttf", size=font_size)
    except:
        font = ImageFont.load_default(size=font_size)

    spacing = height // (len(words))
    _ = 0.75
    for letter in words:
        x = spacing * _
        y = random.randint(0, 23)
        _ = round(_, 2) + 0.75
        draw.text(xy=(x, y), text=letter, font=font, fill=(0, 0, 0), spacing=50.0)

    #  lines
    for _ in range(number_of_line):
        point_1 = (random.randint(10, 40), random.randint(10, 50))  # [x, y]
        point_2 = (random.randint(80, 160), random.randint(30, 50))  # [x, y]
        draw.line(xy=[point_1, point_2], fill=(20, 20, 20), width=2, joint="curve")

    #  noise
    for point in range(number_of_points):
        x = random.randint(10, 140)
        y = random.randint(10, 60)
        draw.point((x, y), fill="gray")

    image = image.filter(ImageFilter.GaussianBlur(0.5))

    return pillow_to_base64(pillow_image=image)


def generate_random_words():
    letters = [letter for letter in string.ascii_uppercase]
    return "".join([random.choice(letters) for char in range(5)])


def pillow_to_base64(pillow_image):
    image_buffer = io.BytesIO()
    pillow_image.save(image_buffer, format="PNG")
    img_base64 = base64.b64encode(image_buffer.getvalue()).decode("utf-8")

    return img_base64


generate_captcha()
