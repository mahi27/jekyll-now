##import libraries
import random
import string
from PIL import Image
from claptcha import Claptcha
import os

#generate random string
def randomString():
    rndLetters = (random.choice(string.ascii_uppercase) for _ in range(6))
    return "".join(rndLetters)

# Initialize Claptcha object with random text, Newfont as font, of size
# 300x150px, using bicubic resampling filter
for i in range(2000):
    c = Claptcha(randomString, "newfont.ttf", (300,150),resample=Image.BICUBIC)
    text, _ = c.write('captcha1.png')
    os.rename('captcha1.png',text+".png")
