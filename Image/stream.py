import cv2
import os
import sys


def shot():
    os.system(r"wget http://192.168.2.5:8080/shot.jpg -O shot.jpg --quiet")
    img = cv2.imread(r"shot.jpg")
    return img


if __name__ == "__main__":
    while True:
        img = shot()
        cv2.imshow('image', img)
        xxx = cv2.waitKey(10)
        if xxx == 27:
            sys.exit(0)