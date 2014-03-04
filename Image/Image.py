import cv2
import copy
import sys
from threading import Timer
import time

import numpy as np

import Game.basicStructs as BS



# ~~~~~~~~~~~~~~~~~~~~~~~~~IMAGE TAKING LIB ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
request = False
timerStop = False
def get_img():
    #print "Request!"
    global request
    request = True
    while request == True:
        time.sleep(0.1)
    img = cv2.imread("shot.jpg")
    return img

def take_photo():
    #print conf.IP
    import MainApp.conf as conf
    import urllib

    try:
        urllib.urlretrieve("http://" + str(conf.get('IP')) + ":8080/shot.jpg", "shot.jpg")
    except:
        print "Cannot connect!"
        #os.system(r"wget --tries 1 --timeout 3 http://" + str(conf.get('IP')) + ":8080/shot.jpg -O shot.jpg --quiet")


timer = Timer(0,0)

def check_for_request(): #periodically checking for new request from other threads
    global request
    if request:
        take_photo()
        request = False
    global timer
    if not timerStop:
        timer = Timer(0.1, check_for_request)
        timer.start()
check_for_request()

def timer_stop():
    global timerStop, timer
    timerStop = True
    timer.cancel()
# ~~~~~~~~~~~~~~~~~~~~~~~~~END IMAGE TAKING LIB ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Field:
    def __init__(self, Image, xx, yy):
        self.x = xx
        self.y = yy
        self.img = Image

MousePoints = []


def show_image(img):
    cv2.namedWindow('image')
    cv2.imshow('image', img)
    a = cv2.waitKey(0)
    cv2.destroyAllWindows()
    return a


class ImageProcess:
    def __init__(self):
        self.param1 = 70
        self.param2 = 15
        self.fields1 = self.fields2 = []
        self.FieldTable = [[1 for j in xrange(8)] for i in xrange(8)]
        #self.splitPoints = [[458, 333], [458, 692], [817, 327], [826, 692]]


    def calibratation(self, fieldList): # check A1, next via white edge, across board and left corner
        for field in fieldList:
            for p1, p2 in [(a, b) for a in xrange(10, 50) for b in xrange(10, 50)]:
                self.param1[field.x][field.y] = p1
                self.param2[field.x][field.y] = p1
                if self.searchForPawn(field.img, [field.x, field.y]) == 1 and self.searchForPawn(field.img, [field.x,
                                                                                                             field.y]) == -1:
                    print "Calibrated field", field.x, field.y, "values", p1, p2
                    break

    def addToCalibrate(self, img):
        self.loadImage(img)
        self.imageSplit()
        result = [[0 for i in xrange(8)] for j in xrange(8)]
        for i in xrange(8):
            for j in xrange(8):
                if (i + j) % 2 == 1:
                    #print [i, j]
                    self.Threshold[i][j] += (self.searchForPawn(self.FieldTable[i][j], [i, j], True) / 2.0)
        print self.Threshold


    def loadImage(self, image):
        self.img = image

    def mouseEvent(self, event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE:
            self.ImgCopy2 = copy.deepcopy(self.ImgCopy)
            cv2.circle(self.ImgCopy2, (x, y), 3, (0, 255, 0), -1)

        if event == cv2.EVENT_LBUTTONUP:
            self.splitPointsTemp.append([x, y])
            cv2.circle(self.ImgCopy, (x, y), 3, (255, 255, 255), -1)
            self.ImgCopy2 = copy.deepcopy(self.ImgCopy)

    def calibrate_board(self,img):
        import MainApp.conf as conf

        self.img = img
        self.ImgCopy = copy.deepcopy(self.img)
        self.ImgCopy2 = copy.deepcopy(self.img)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.mouseEvent)
        self.splitPointsTemp = []
        while True:
            cv2.imshow('image', self.ImgCopy2)
            if len(self.splitPointsTemp) == 4 or cv2.waitKey(1) & 0xFF == 27:
                break
        if len(self.splitPointsTemp) == 4:
            self.splitPoints = self.splitPointsTemp
            #print self.splitPoints
        conf.set('splitPoints', self.splitPoints)
        cv2.destroyAllWindows()

    def imageSplit(self):
        import MainApp.conf as conf

        self.splitPoints = eval(conf.get('splitPoints'))
        if len(self.splitPoints) != 4:
            print "Board not detected!"
        rows, cols, ch = self.img.shape
        pts1 = np.float32(self.splitPoints)
        pts2 = np.float32([[0, 0], [600, 0], [0, 600], [600, 600]])
        M = cv2.getPerspectiveTransform(pts1, pts2)
        self.trimmed = cv2.warpPerspective(self.img, M, (600, 600))
        self.edgesImage = cv2.warpPerspective(self.edgesImage, M, (600, 600))

        #~~~~~~~~~~~~~~IMAGE ROTATION~~~~~~~~~~~~

        #rows, cols, depth = self.trimmed.shape

        #M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
        #self.trimmed = cv2.warpAffine(self.trimmed, M, (cols, rows))


        #~~~~~~~~~~~~~~IMAGE ROTATION~~~~~~~~~~~~

        points = []
        for i in range(1, 602, 75):
            for j in range(1, 602, 75):
                points.append([j, i])
        dic = {}
        for i in range(0, 9):
            for j in range(0, 9):
                dic[i, j] = points[9 * i + j]

        for i in xrange(8):
            for j in xrange(8):
                if (i + j) % 2 == 1:
                    x1 = dic[i, j][0]
                    y1 = dic[i, j][1]
                    x2 = dic[i + 1, j + 1][0]
                    y2 = dic[i + 1, j + 1][1]
                    self.FieldTable[i][j] = self.trimmed[y1:y2, x1:x2]
        for i in xrange(8):
            for j in xrange(8):
                x1 = dic[i, j][0]
                y1 = dic[i, j][1]
                x2 = dic[i + 1, j + 1][0]
                y2 = dic[i + 1, j + 1][1]
                cv2.circle(self.trimmed, (x1, y1), 2, (0, 0, 255))
                cv2.circle(self.trimmed, (x2, y2), 2, (0, 0, 255))

    def frame_table(self, image, AIIsWhite):
        import MainApp.conf as conf

        img2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #img2 = cv2.medianBlur(img2, 5)
        #self.edgesImage = cv2.GaussianBlur(img2, (3, 3), 0)
        self.edgesImage = copy.deepcopy(image)
        self.edgesImage = cv2.Canny(self.edgesImage, float(conf.get('param1')), float(conf.get('param2'))) #90, 200

        self.img = copy.deepcopy(image)
        self.imageSplit()

        result = [[0 for i in xrange(8)] for j in xrange(8)]
        for i in xrange(8):
            for j in xrange(8):
                if (i + j) % 2 == 1:
                    #print [i, j]
                    result[i][j] = self.searchForPawn(self.FieldTable[i][j], [i, j])

        board = BS.Board()
        rotatedBoard = BS.Board()
        if AIIsWhite:
            WhiteConst = BS.Field.AI
            BlackConst = BS.Field.HU
        else:
            WhiteConst = BS.Field.HU
            BlackConst = BS.Field.AI

        for i in xrange(8):
            for j in xrange(8):
                if result[i][j] == 1:
                    board[i, j] = WhiteConst
                elif result[i][j] == -1:
                    board[i, j] = BlackConst
                else:
                    board[i, j] = BS.Field.EMPTY

        for i in xrange(8):
            for j in xrange(8):
                rotatedBoard[j, 7 - i] = board[i, j]

        return rotatedBoard


    def searchForPawn(self, img, pos, returnColorValue=False):
        import MainApp.conf as conf

        """function returns:
        0 - no figure
        1 - white
        -1 - black"""

        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img2 = cv2.medianBlur(img2, 5)
        edges = cv2.GaussianBlur(img2, (3, 3), 0)
        edges = cv2.Canny(edges, 90, 200)
        #show_image(edges)
        x, dst = cv2.threshold(img2, 50, 255, cv2.THRESH_BINARY)
        #show_image(dst)


        circles = cv2.HoughCircles(edges, cv2.cv.CV_HOUGH_GRADIENT, 1, 20,
                                   param1=70,
                                   param2=20,
                                   minRadius=10,
                                   maxRadius=0)

        #print circles
        if circles is None: #or len(circles[0]) > 1:
            #print "NO_PAWN"
            return 0

        circles = np.uint16(np.around(circles))
        i = circles[0][0]

        d = int(i[2] / 1.6)
        x = i[0]
        y = i[1]
        #cv2.rectangle(img, (x - d, y - d), (x + d, y + d), (0, 255, 0))
        sums = [0.0, 0.0, 0.0]
        divi = 0
        for row in dst[x - d:x + d, y - d:y + d]:
            for px in row:
                sums += px
                divi += 1

                #if divi != 0: sum = [i/divi for i in sum]
        try:
            sums /= divi
        except TypeError:
            print circles

        #print "|!!!| ", sums, divi

        suma = sums[0] + sums[1] + sums[2]
        #print "KOLOR: ",suma

        if returnColorValue:
            return suma
        thr = int(conf.get('threshold'))
        #print thr, suma
        if suma > thr:
            #print "WHITE PAWN"
            cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv2.circle(self.edgesImage, (i[0], i[1]), i[2], (0, 255, 0), 2)

        else:
            #print "BLACK PAWN"
            cv2.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 2)
            cv2.circle(self.edgesImage, (i[0], i[1]), i[2], (0, 0, 255), 2)

        #cv2.imshow('detected circles', img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        if suma > thr:##self.Threshold[pos[0]][pos[1]]:
            return 1
        else:
            return -1


drawing = False
ix = iy = 0


if __name__ == "__main__":

    proc = ImageProcess()
    #proc.calibrate_board()




    cv2.destroyAllWindows()
    while True:
        img = take_photo()
        board = proc.frame_table(img, False)

        cv2.imshow('image', proc.trimmed)
        xxx = cv2.waitKey(0)
        if xxx == 27:
            sys.exit(0)
        cv2.destroyAllWindows()

        print board
