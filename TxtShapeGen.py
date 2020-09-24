from PIL import Image, ImageDraw, ImageFont
import random
import string

# generate a bunch of random text
# write text out to some font
# print text onto image

canvas_x = 1000
canvas_y = 1000

font_list = [
    "/Library/Fonts/Arial.ttf",
    "/Users/aarenstade/Library/Fonts/aaaiight-fat.ttf",
    "/Users/aarenstade/Library/Fonts/AARDC___.TTF",
    "/Users/aarenstade/Library/Fonts/Ackbar.ttf",
    "/Users/aarenstade/Library/Fonts/Yiggivoo UC 3D.ttf",
    "/Users/aarenstade/Library/Fonts/Amatic-Bold.ttf",
    "/Users/aarenstade/Library/Fonts/America Faster Regular.ttf",
    "/Users/aarenstade/Library/Fonts/AMERSN__.ttf",
    "/Users/aarenstade/Library/Fonts/BELACU.ttf",
    "/Users/aarenstade/Library/Fonts/carbon phyber.ttf",
    "/Users/aarenstade/Library/Fonts/deftone stylus.ttf",
    "/Users/aarenstade/Library/Fonts/JUDAS___.TTF",
    "/Users/aarenstade/Library/Fonts/Kingthings Petrock.ttf",
]


# alien_fonts = [
#     "/Users/aarenstade/Desktop/AlienFonts/ALIENATO.TTF",
#     "/Users/aarenstade/Desktop/AlienFonts/Aliencons TFB.ttf",
#     "/Users/aarenstade/Desktop/AlienFonts/Aliencons two.ttf",
#     "/Users/aarenstade/Desktop/AlienFonts/alm_____.ttf",
#     "/Users/aarenstade/Desktop/AlienFonts/ArtMonsters.ttf",
#     "/Users/aarenstade/Desktop/AlienFonts/Glipervelz-Origy FULL.ttf",
#     "/Users/aarenstade/Desktop/AlienFonts/Happy Monsters.ttf",
#     "/Users/aarenstade/Desktop/AlienFonts/Other Space.ttf",
#     "/Users/aarenstade/Desktop/AlienFonts/Ovnis.ttf",
#     "/Users/aarenstade/Desktop/AlienFonts/Rangers_.ttf",
#     "/Users/aarenstade/Desktop/AlienFonts/StayOnTarget-Regular.ttf"
# ]

shape_options = [
    'ellipse',
    'rectangle',
    'line'
]


def random_shape(img):
    max_size = 10
    min_size = 5
    x_cor = random.randint(0, canvas_x)
    y_cor = random.randint(0, canvas_y)
    min_col = 0
    max_col = 255
    index = random.randint(0, len(shape_options) - 1)
    option = shape_options[index]
    print('chose: {}'.format(option))
    draw = ImageDraw.Draw(img)
    if(option == 'ellipse'):
        col = random_color(min_col, max_col)
        x = x_cor
        y = y_cor
        x2 = random.randint(min_size, max_size)
        y2 = random.randint(min_size, max_size)
        draw.ellipse([(x, y), (x2, y2)], fill=col)
    elif (option == "rectangle"):
        col = random_color(min_col, max_col)
        x = x_cor
        y = y_cor
        x2 = random.randint(min_size, max_size)
        y2 = random.randint(min_size, max_size)
        draw.rectangle([(x, y), (x2, y2)], fill=col)
    elif (option == "line"):
        col = random_color(min_col, max_col)
        x = x_cor
        y = y_cor
        x2 = random.randint(min_size, max_size)
        y2 = random.randint(min_size, max_size)
        width = random.randint(5, 100)
        draw.line([(x, y), (x2, y2)], fill=col, width=width)


def random_font():
    index = random.randint(0, len(font_list) - 1)
    chosen_font = font_list[index]
    return chosen_font


def random_color(min_val, max_val):
    r = random.randint(min_val, max_val)
    g = random.randint(min_val, max_val)
    b = random.randint(min_val, max_val)
    return (r, g, b)


ascii_types = [
    string.ascii_lowercase,
    string.ascii_uppercase,
    string.punctuation,
    string.octdigits,
]


def random_string():
    letters = random.choice(ascii_types)
    length = random.randint(1, 2)
    text = ''.join(random.choice(letters) for i in range(length))
    return text


def generate_image(img, text_amount):
    for i in range(text_amount):
        if(i % 100 == 0):
            print(i)
        x = random.randint(0, canvas_x)
        y = random.randint(0, canvas_y)
        # create random string
        new_string = random_string()
        draw = ImageDraw.Draw(img)
        # create random font
        font_name = random_font()
        font_size = random.randint(5, 250)
        new_font = ImageFont.truetype(font_name, font_size)
        font_color = random_color(0, 255)
        # random_shape(img)
        draw.text((x, y), new_string, font=new_font, fill=font_color)


def handler(object_number, filename):
    img = Image.new('RGB', (canvas_x, canvas_y))
    generate_image(img, object_number)
    img.save(filename)
