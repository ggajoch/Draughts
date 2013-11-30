import cv2
import copy
import sys

import numpy as np

sys.path.append("../Game")
import basicStructs as BS


class Field:
    def __init__(self, Image, xx, yy):
        self.x = xx
        self.y = yy
        self.img = Image


class ImageProcess:
    def __init__(self):
        self.param1 = [[33 for i in xrange(8)] for j in xrange(8)]
        self.param2 = [[20 for i in xrange(8)] for j in xrange(8)]
        self.fields1 = self.fields2 = []
        self.FieldTable = [[1 for j in xrange(8)] for i in xrange(8)]

    def calibratation(self, fieldList):
        for field in fieldList:
            for p1, p2 in [(a, b) for a in xrange(10, 50) for b in xrange(10, 50)]:
                self.param1[field.x][field.y] = p1
                self.param2[field.x][field.y] = p1
                if self.searchForPawn(field.img, [field.x, field.y]) == 1 and self.searchForPawn(field.img, [field.x,
                                                                                                             field.y]) == -1:
                    print "Calibrated field", field.x, field.y, "values", p1, p2
                    break

    def loadImage(self, image):
        self.img = image

    def mouseEvent(self, event, x, y, flags, param):
        global MouseImgCopy, MousePoints
        if event == cv2.EVENT_LBUTTONDOWN:
            MousePoints.append([x, y])
            cv2.circle(MouseImgCopy, (x, y), 4, (0, 255, 0), -1)


    def imageSplit(self, points=[]):
        #points = [[80, 138], [427, 122], [81, 494], [439, 489]]
        global MouseImgCopy, MousePoints
        MousePoints = points
        MouseImgCopy = copy.deepcopy(self.img)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.mouseEvent)
        while True:
            cv2.imshow('image', MouseImgCopy)
            if len(points) == 4 or cv2.waitKey(1) & 0xFF == 27:
                break
        print points
        cv2.destroyAllWindows()

        rows, cols, ch = self.img.shape
        pts1 = np.float32(points)
        pts2 = np.float32([[0, 0], [600, 0], [0, 600], [600, 600]])
        M = cv2.getPerspectiveTransform(pts1, pts2)
        dst = cv2.warpPerspective(self.img, M, (600, 600))
        points = []
        for i in range(1, 602, 75):
            for j in range(1, 602, 75):
                points.append([j, i])
        dic = {}
        for i in range(0, 9):
            for j in range(0, 9):
                dic[i, j] = points[9 * i + j]
        print dic[0, 0], dic[1, 1]

        for i in xrange(8):
            for j in xrange(8):
                if (i + j) % 2 == 1:
                    x1 = dic[i, j][0]
                    y1 = dic[i, j][1]
                    x2 = dic[i + 1, j + 1][0]
                    y2 = dic[i + 1, j + 1][1]
                    self.FieldTable[i][j] = dst[y1:y2, x1:x2]

        cv2.namedWindow('image')
        #cv2.circle(dst, tuple(i), 3, (0, 0, 255), -1)
        cv2.imshow('image', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    def frame_table(self, image, AIIsWhite):
        self.img = copy.deepcopy(image)
        self.imageSplit([[70, 150], [388, 158], [65, 462], [383, 469]])
        cv2.namedWindow('image')

        result = [[0 for i in xrange(8)] for j in xrange(8)]
        for i in xrange(8):
            for j in xrange(8):
                if (i + j) % 2 == 1:
                    print [i, j]
                    result[i][j] = self.searchForPawn(self.FieldTable[i][j], [i, j])

        board = BS.Board()
        if AIIsWhite:
            WhiteConst = BS.Field.AI
            BlackConst = BS.Field.HU
        else:
            WhiteConst = BS.Field.HU
            BlackConst = BS.Field.AI

        self.imgWithDots = copy.deepcopy(image)
        for i in xrange(8):
            for j in xrange(8):
                if result[i][j] == 1:
                    board[i, j] = WhiteConst
                elif result[i][j] == -1:
                    board[i, j] = BlackConst
                else:
                    board[i, j] = BS.Field.EMPTY

        while True:
            cv2.imshow('image', self.img)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        cv2.destroyAllWindows()

        print board

    def searchForPawn(self, img, pos):
        """function returns:
        0 - no figure
        1 - white
        -1 - black"""
        #global img
        #img2 = cv2.imread(r"C:\Users\rexina\Dropbox\AGH\MiTP\cz.jpg")
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img2 = cv2.medianBlur(img2, 5)
        #cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

        circles = cv2.HoughCircles(img2, cv2.cv.CV_HOUGH_GRADIENT, 1, 20,
                                   param1=self.param1[pos[0]][pos[1]],
                                   param2=self.param2[pos[0]][pos[1]],
                                   minRadius=15,
                                   maxRadius=0)

        print circles
        if circles is None or len(circles[0]) > 1:
            print "NO_PAWN"
            return 0

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
            print circles

        #print "|!!!| ", sums, divi

        suma = sums[0] + sums[1] + sums[2]
        #print "KOLOR: ",suma

        if suma > 300:
            print "WHITE PAWN"
            cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

        else:
            print "BLACK PAWN"
            cv2.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 2)
            cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

        #cv2.imshow('detected circles', img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        if suma > 300:
            return 1
        else:
            return -1


drawing = False
ix = iy = 0




if __name__ == "__main__":
    #os.system("wget http://192.168.137.156:8080/photoaf.jpg -O shot.jpg")
    img = cv2.imread(r"asm.jpg")
    imgCopy = copy.deepcopy(img)
    proc = ImageProcess()
    proc.frame_table(imgCopy, True)
