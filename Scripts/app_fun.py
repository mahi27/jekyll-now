# -*- coding: utf-8 -*-
from keras.models import load_model
import pickle
from PIL import Image
from PIL import ImageOps
import cv2
import imutils
from shrink import resize_image
import numpy as np


model_file = "captcha_model.hdf5"
model_labels = "model_labels.dat"

def predict_captcha(image_file):
    with open(model_labels, "rb") as f:
        lb = pickle.load(f)

    model = load_model(model_file)
    img = Image.open(image_file)
    img = ImageOps.invert(img)
    filename = "result.png"
    img.save(filename)
    image = cv2.imread(filename,0)
    contours = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    letter_image_regions = []

    for contour in contours:
        # Get the rectangle that contains the contour
        (x, y, w, h) = cv2.boundingRect(contour)
        #remove contours that are too small to be a letter
        if w > 5 and h > 5:
            if w < 65:
                letter_image_regions.append([x, y, w, h+5])
        #split the letters that are merged into one
            elif w >= 65:
                letter_image_regions.append([x, y, w//2, h+5])
                letter_image_regions.append([x+(w//2),y,w//2,h+5])
            

    if len(letter_image_regions) != 6:
        captcha_text = "Couldn't break the captcha"
    else:
        letter_image_regions = sorted(letter_image_regions, key=lambda x: x[0])
    
        predictions = []
    
        for letter_bounding_box in letter_image_regions:
            x, y, w, h = letter_bounding_box
            letter_image = image[y:y + h , x :x + w]
            letter_image = resize_image(letter_image, 20, 20)
            letter_image = np.expand_dims(letter_image, axis=2)
            letter_image = np.expand_dims(letter_image, axis=0)
            prediction = model.predict(letter_image)
            letter = lb.inverse_transform(prediction)[0]
            predictions.append(letter)
            
        captcha_text = "".join(predictions)
    return captcha_text
    
