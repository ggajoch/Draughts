import cv2
import copy

import numpy as np


#noinspection PyTrailingSemicolon
def searchForPawn(img):
    """function returns:
        0 - no figure
        1 - white
        -1 - black"""
    #global img
    #img2 = cv2.imread(r"C:\Users\rexina\Dropbox\AGH\MiTP\cz.jpg")
    img2 = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
    img2 = cv2.medianBlur(img2,5)
    #cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(img2, cv2.cv.CV_HOUGH_GRADIENT, 1, 20, param1=29, param2=26, minRadius=15, maxRadius=0)

    if circles is None:
        print "NO_PAWN"
        #noinspection PyTrailingSemicolon
        return 0
    print circles
    circles = np.uint16(np.around(circles))
    #if len(circles) > 1:
    #   return 0
    i = circles[0][0]


    d = int(i[2]/1.41)
    x = i[0]
    y = i[1]
    cv2.rectangle(img, (x-d,y-d),(x+d,y+d),(0,255,0))
    sums = [0.0, 0.0, 0.0]
    divi = 0
    for row in img2[x-d:x+d,y-d:y+d]:
        for px in row:
            sums += px
            divi += 1
        
    #if divi != 0: sum = [i/divi for i in sum]
    try:
        sums /= divi
    except TypeError:
        print "|!!!| ", sums, divi

    suma = sums[0] + sums[1] + sums[2]
    print "KOLOR: ",suma

    if suma > 300:
        print "WHITE PAWN"
        cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
        cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
        return 1
    else:
        print "BLACK PAWN"
        cv2.circle(img,(i[0],i[1]),i[2],(0,0,255),2)
        cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
        return -1



        #cv2.imshow('detected circles',img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

drawing = False
ix = iy = 0


def mouseEvent(event, x, y, flags, param):
    global ix, iy, drawing, imgCopy, points, left
    if event == cv2.EVENT_LBUTTONDOWN:
        print [x, y]
        points.append([x,y])
        cv2.circle(imgCopy, (x, y), 5, (0, 255, 0), -1)


if __name__ == "__main__":
    #os.system("wget http://192.168.137.124:8080/shot.jpg -O shot.jpg")
    img = cv2.imread(r"BW.jpg")
    imgCopy = copy.deepcopy(img)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', mouseEvent)

    points = []
    points = [[111, 148], [404, 140], [112, 443], [413, 443]]
    while True:
        cv2.imshow('image', imgCopy)
        if len(points) == 4 or cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyAllWindows()
    cv2.namedWindow('image')

    rows, cols, ch = img.shape
    #pts1 = np.float32([[70, 152],[392, 159],[68, 461],[381, 469]])
    pts1 = np.float32([points[i] for i in range(0, 4)])
    pts2 = np.float32([[0, 0], [600, 0], [0, 600], [600, 600]])

    M = cv2.getPerspectiveTransform(pts1, pts2)

    dst = cv2.warpPerspective(img, M, (600, 600))

    points = []
    for i in range(1, 602, 75):
        for j in range(1, 602, 75):
            points.append([j, i])
    print points

    print len(points)

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

    for i in points:
        cv2.circle(dst, tuple(i), 3, (0, 0, 255), -1)

    while True:
        cv2.imshow('image', dst)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    print points
    cv2.destroyAllWindows()

