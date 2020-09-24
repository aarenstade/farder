import TxtShapeGen
import numpy as np
from PIL import Image
import random


# generate txt / shape image
# apply grunge filter over image


grunge_choices = [
    "./grunge1.png",
    "./grunge2.png",
    "./grunge3.png",
    "./grunge4.png",
    "./grunge5.png",
]

def random_grunge():
    index = random.randint(0, len(grunge_choices) - 1)
    return grunge_choices[index]


def handler():
    # create filename
    filename = "farder.jpg"
    # define object number
    objects = random.randint(0,200)
    # call TxtShapeGen handler
    TxtShapeGen.handler(objects, filename)
    # create image
    # get image into np array
    imgarray = np.array(Image.open(filename))
    # get grunge image into np array
    grunge_img = random_grunge()
    garray = np.array(Image.open(grunge_img))
    garray.resize((1000,1000,3))
    new_img = imgarray * garray
    im = Image.fromarray(new_img)
    im.save('farder_updated2.jpg')

handler()