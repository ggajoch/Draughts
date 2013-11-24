from cv2 import *

def calc(x,y):
    global img
    col = [0,0,0]
    for i in range(-5,5):
        for j in range(-5,5):
            col += img[x+i][y+i]
    col /= 36
    sq = col[0] + col[1] + col[2]
    print sq
    if sq < 600:
        print "BLACK"
    elif sq > 1500:
        print "WHITE"
    else:
        print "NO ONE"


def sum_pixels(a, b):
    global img
    c = 0
    x = 0
    for i in range(0,2):
        if a[i] > b[i]:
            (a[i],b[i]) = (b[i],a[i])
    for j in range(a[0], b[0]):
        for i in range(a[1], b[1]):
            #print "A:", img[i][j
            for l in range(0,3):
                c += img[i][j][l]
            x += 1
            #print img[i][j] 
    #print "C = ",c," x = ", x
    return (c/float(x))
    
rectangles = []
constuctingRect = 0
def mouseEvent(e,x,y,a,b):
    global rectangles, img, constuctingRect


    if e == 4:
        if constuctingRect == 0:
            constuctingRect = 1
            rectangles.append([[x,y], [x,y]])
        else:
            constuctingRect = 0
            rectangles[-1][-1] = [x, y]
            print "-------------------"
            for i in rectangles:
                print i, sum_pixels(i[0], i[1])

    if constuctingRect == 1:
        rectangles[-1][-1] = [x, y]

    drawit(img.copy())
            


def drawit(img):
    global rectangles
#    print rectanglePoints, len(rectanglePoints)
    for i in rectangles:
        if len(i) >= 2:
            rectangle(img,tuple(i[0]), tuple(i[1]), cv.Scalar(0xff,0x00,0x00))
            
    imshow("a",img)

img = imread("D:\\b.jpg")
namedWindow("a")
setMouseCallback("a",mouseEvent,0)


while True:
    drawit(img)
    if waitKey(0) != -1:
        break

destroyWindow("a")
print t
for i in t:
    calc(i[0], i[1])
