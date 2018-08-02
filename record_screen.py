import cv2
import numpy as np
from PIL import ImageGrab
import time
import math
from direct_key_inputs import PressKey, ReleaseKey, W, A, S, D

tl_width = 0  # top left width, i.e top left x coordinate
tl_height = 40  # top left height, i.e top left y coordinate
br_width = 640  # bottom right width, i.e bottom right x coordinate
br_height = 510  # bottom right height, i.e bottom right y coordinate


def process_img(image):
    # convert to gray
    processed_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    processed_img = cv2.blur(processed_img,(3,3))
    cv2.imshow('Window_1',processed_img)
    # edge detection
    processed_img =  cv2.Canny(processed_img,30,90)
    # vertices which define the ROI
    vertices = np.array([[tl_width,0.66*(br_height - tl_height)],[tl_width,br_height],
                         [br_width,br_height],[br_width, 0.66*(br_height-tl_height)],
                         [0.75*(br_width-tl_width), 0.5*(br_height-tl_height)],
                         [0.25*(br_width-tl_width), 0.5*(br_height-tl_height)]], np.int32)
    processed_img = roi(processed_img, [vertices])
    # Find and draw lines on the edge detected image
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 100, np.array([]),
                            20, 10)
    draw_lines(processed_img,lines)
    
    return processed_img


def roi(img, vertices):
    #blank mask:
    mask = np.zeros_like(img)
    # fill the mask
    cv2.fillPoly(mask, vertices, 255)
    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    return masked
    

def draw_lines(img,lines):
    # To handle situations when no lines are detected
    if lines is not None:
        left_line_x = []
        left_line_y = []
        right_line_x = []
        right_line_y = []
        for line in lines:
            for x1, y1, x2, y2 in line:
                slope = (y2 - y1) / (x2 - x1 + 0.001)  # Calculating the slope.
                if math.fabs(slope) < 0.5:  # Only consider extreme slope
                    continue
                if slope <= 0:  # If the slope is negative, left group.
                    left_line_x.extend([x1, x2])
                    left_line_y.extend([y1, y2])
                else:  # Otherwise, right group.
                    right_line_x.extend([x1, x2])
                    right_line_y.extend([y1, y2])

        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]),
                     [255,255,255], 3)

def main():
    # This gives us time to set things up
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
    
    last_time = time.time()
    while(True):
        # Grab image from screen
        screen = np.array(ImageGrab.grab(bbox=(tl_width, tl_height,
                                               br_width, br_height)))
        print("Loop time : {}".format(time.time() - last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        cv2.imshow('Window',new_screen)
        # Exit if pressed 'q'
        break
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ =='__main__':
    main()
