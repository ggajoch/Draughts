import cv2
import numpy as np


def searchForPawn(img):
    #global img
    #img2 = cv2.imread(r"C:\Users\rexina\Dropbox\AGH\MiTP\cz.jpg")
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img2 = cv2.medianBlur(img2, 5)
    #cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(img2, cv2.cv.CV_HOUGH_GRADIENT, 1, 20, param1=43, param2=28, minRadius=0, maxRadius=0)

    if circles is None:
        print "NO_PAWN"
        return 0
    print circles
    circles = np.uint16(np.around(circles))
    i = circles[0][0]

    d = int(i[2] / 1.41)
    x = i[0]
    y = i[1]
    cv2.rectangle(img, (x - d, y - d), (x + d, y + d), (0, 255, 0))
    sums = [0.0, 0.0, 0.0]
    divi = 0
    for row in img2[x - d:x + d, y - d:y + d]:
        for px in row:
            sums += px
            divi += 1

    #if divi != 0: sum = [i/divi for i in sum]
    try:
        sums /= divi
    except TypeError:
        print "|!!!| ", sums, divi

    suma = sums[0] + sums[1] + sums[2]
    print "KOLOR: ", suma

    if suma > 300:
        print "WHITE PAWN"
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
    else:
        print "BLACK PAWN"
        cv2.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 2)
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)



        #cv2.imshow('detected circles',img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()


def flatImage(img, tab): #[[70,152],[392,159],[68,461],[381,469]]
    rows, cols, ch = img.shape
    pts1 = np.float32(tab)
    pts2 = np.float32([[0, 0], [600, 0], [0, 600], [600, 600]])

    M = cv2.getPerspectiveTransform(pts1, pts2)

    dst = cv2.warpPerspective(img, M, (600, 600))
    return dst


def searchPawns(img):
    points = []
    for i in range(1, 602, 75):
        for j in range(1, 602, 75):
            points.append([j, i])

    dic = {}
    for i in range(0, 9):
        for j in range(0, 9):
            dic[i, j] = points[9 * i + j]

    print dic[0, 0], dic[1, 1]

    for i in range(0, 8):
        for j in range(0, 8):
            x1 = dic[i, j][0]
            y1 = dic[i, j][1]
            x2 = dic[i + 1, j + 1][0]
            y2 = dic[i + 1, j + 1][1]
            #cv2.imshow('image',img[y1:y2,x1:x2])
            searchForPawn(dst[y1:y2, x1:x2])
            #cv2.waitKey(0)
