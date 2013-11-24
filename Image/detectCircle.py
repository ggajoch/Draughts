import cv2
#import cv2.cv
import numpy as np

def searchForPawn(img):
    #img2 = cv2.imread(r"C:\Users\rexina\Dropbox\AGH\MiTP\cz.jpg")
    img2 = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
    img2 = cv2.medianBlur(img2,5)
    #cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(img2,cv2.cv.CV_HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)

    if len(circles) == 0:
        print "NO_PAWN"
        return 0
    print circles
    circles = np.uint16(np.around(circles))
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

    sums /= divi
    suma = sums[0] + sums[1] + sums[2]
    print "KOLOR: ",suma

    if suma > 300:
        print "WHITE PAWN"
    else:
        print "BLACK PAWN"
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)


    cv2.imshow('detected circles',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

drawing = False
def mouseEvent(event, x, y, flags, param):
    global ix, iy, drawing,img
    if event == cv2.EVENT_LBUTTONDOWN:
        ix,iy = x,y
        drawing = True
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        imgX = img[iy:y,ix:x]
        cv2.imshow('detected circles',imgX)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        searchForPawn (imgX)
        
img = cv2.imread(r"C:\Users\rexina\Dropbox\AGH\MiTP\b.jpg")

cv2.namedWindow('image')
cv2.setMouseCallback('image',mouseEvent)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

