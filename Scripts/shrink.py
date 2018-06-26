import imutils
import cv2

def resize_image(image, w, h):
    (h, w) = image.shape[:2]
    if w > h:
        image = imutils.resize(image, width=w)
    else:
        image = imutils.resize(image, height=h)

    padW = int((width - image.shape[1]) / 2.0)
    padH = int((height - image.shape[0]) / 2.0)

    image = cv2.copyMakeBorder(image, padH, padH, padW, padW,
        cv2.BORDER_REPLICATE)
    image = cv2.resize(image, (w, h))
    return image