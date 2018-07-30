import cv2
import numpy as np
from PIL import ImageGrab
import time
from direct_key_inputs import PressKey, ReleaseKey, W, A, S, D

def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img =  cv2.Canny(processed_img, 60, 200)
    return processed_img

last_time = time.time()
while(True):
    screen = np.array(ImageGrab.grab(bbox=(0, 40, 640, 510)))
    print("Loop time : {}".format(time.time() - last_time))
    last_time = time.time()
    new_screen = process_img(screen)
    cv2.imshow('Window', new_screen)
    # cv2.imshow('Window', cv2.cvtColor(new_screen, cv2.COLOR_RGB2BGR))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
