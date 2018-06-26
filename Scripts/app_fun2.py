# -*- coding: utf-8 -*-
#%%
import random
import string
from PIL import Image
from claptcha import Claptcha

def randomString():
    rndLetters = (random.choice(string.ascii_uppercase) for _ in range(6))
    rd = "".join(rndLetters)
    c = Claptcha(rd, "newfont.ttf", (300,150),resample=Image.BICUBIC)
    c.write('canvas.jpg')
