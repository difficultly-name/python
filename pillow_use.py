from PIL import Image, ImageDraw, ImageFont
import numpy as np


def bg_color():

    return (np.random.randint(1, 255), np.random.randint(1, 255),
            np.random.randint(1, 255))


def random_txt():

    txt_list = []
    txt_list.extend([i for i in range(65, 91)])
    txt_list.extend([i for i in range(97, 123)])
    txt_list.extend([i for i in range(48, 58)])
    return chr(txt_list[np.random.randint(0, len(txt_list)-1)])


def txt_color():

    return (np.random.randint(32, 127), np.random.randint(32, 127),
            np.random.randint(32, 127))


def generate_code():
    width = 200
    height = 50
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    for w in range(width):
        for h in range(height):
            draw.point((w, h), fill=bg_color())
    my_font = ImageFont.truetype('arial.ttf', 36)
    for i in range(4):
        draw.text((50*i+10, 10), random_txt(), font=my_font, fill=txt_color())

    image.show()
    image.save('a.png', 'PNG')


generate_code()




