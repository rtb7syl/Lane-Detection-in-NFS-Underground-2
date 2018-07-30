import cv2
import numpy as np
from PIL import ImageGrab
import time
from direct_key_inputs import PressKey, ReleaseKey, W, A, S, D

tl_width = 0  # top left width, i.e top left x coordinate
tl_height = 40  # top left height, i.e top left y coordinate
br_width = 640  # bottom right width, i.e bottom right x coordinate
br_height = 510  # bottom right height, i.e bottom right y coordinate


def process_img(image):
    # convert to gray
    processed_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img =  cv2.Canny(processed_img,60,200)
    # vertices which define the ROI
    vertices = np.array([[tl_width,0.66*(br_height - tl_height)],[tl_width,br_height],
                         [br_width,br_height],[br_width, 0.66*(br_height-tl_height)],
                         [0.75*(br_width-tl_width), 0.5*(br_height-tl_height)],
                         [0.25*(br_width-tl_width), 0.5*(br_height-tl_height)]], np.int32)
    processed_img = roi(processed_img, [vertices])
    return processed_img


def roi(img, vertices):
    #blank mask:
    mask = np.zeros_like(img)
    # fill the mask
    cv2.fillPoly(mask, vertices, 255)
    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    return masked
    

def main():   
    last_time = time.time()
    while(True):
        # Grab image from screen
        screen = np.array(ImageGrab.grab(bbox=(tl_width, tl_height, br_width, br_height)))
        print("Loop time : {}".format(time.time() - last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        cv2.imshow('Window',new_screen)
        # Exit if pressed 'q'
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ =='__main__':
    main()
