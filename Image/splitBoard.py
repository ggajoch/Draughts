import cv2
import copy
import sys
import os
import numpy as np

sys.path.append("../Game")
import basicStructs as BS


class Field:
    def __init__(self, Image, xx, yy):
        self.x = xx
        self.y = yy
        self.img = Image


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
        # [todo] - do sth with treshold
        self.Threshold = [[0, 168.6261111111111, 0, 172.33210059171597, 0, 217.72415844838923, 0, 200],
                          [187.78032544378698, 0, 187.92987179487179, 0, 200.40472647392289, 0, 172.39933658374594, 0],
                          [0, 209.38461538461539, 0, 204.87850817718606, 0, 189.74725714990137, 0, 171.61686390532543],
                          [200, 0, 208.26701183431953, 0, 198.93121301775147, 0, 298.09615384615387, 0],
                          [0, 189.03825021132715, 0, 211.66642011834318, 0, 210.86545138888889, 0, 204.1508875739645],
                          [160.65898593165076, 0, 199.6301775147929, 0, 282.01529113247864, 0, 336.66124260355031, 0],
                          [0, 174.03994082840237, 0, 188.14557797971258, 0, 339.61908284023667, 0, 302.1010600907029],
                          [165.08341551610783, 0, 216.80029585798817, 0, 177.81878698224853, 0, 177.77144970414201,
                           0]]#[[0 for i in xrange(8)] for j in xrange(8)]
        self.splitPoints = [[344, 175], [819, 183], [352, 661], [821, 658]]

    def calibratation(self, fieldList):
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
        global MouseImgCopy, MousePoints
        if event == cv2.EVENT_LBUTTONDOWN:
            MousePoints.append([x, y])
            cv2.circle(MouseImgCopy, (x, y), 4, (0, 255, 0), -1)


    def imageSplit(self):
        global MouseImgCopy, MousePoints
        MousePoints = self.splitPoints
        MouseImgCopy = copy.deepcopy(self.img)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.mouseEvent)
        while True:
            cv2.imshow('image', MouseImgCopy)
            if len(MousePoints) == 4 or cv2.waitKey(1) & 0xFF == 27:
                break
            #print MousePoints

        cv2.destroyAllWindows()

        rows, cols, ch = self.img.shape
        pts1 = np.float32(MousePoints)
        pts2 = np.float32([[0, 0], [600, 0], [0, 600], [600, 600]])
        M = cv2.getPerspectiveTransform(pts1, pts2)
        self.trimmed = cv2.warpPerspective(self.img, M, (600, 600))
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
        """function returns:
        0 - no figure
        1 - white
        -1 - black"""
        #global img
        #img2 = cv2.imread(r"C:\Users\rexina\Dropbox\AGH\MiTP\cz.jpg")
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img2 = cv2.medianBlur(img2, 7)
        #cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
        edges = cv2.GaussianBlur(img2, (3, 3), 0)
        edges = cv2.Canny(edges, 100, 100)

        x, dst = cv2.threshold(img2, 50, 255, cv2.THRESH_BINARY)
        #show_image(dst)
        #show_image(edges)

        circles = cv2.HoughCircles(edges, cv2.cv.CV_HOUGH_GRADIENT, 1, 20,
                                   param1=self.param1,
                                   param2=self.param2,
                                   minRadius=10,
                                   maxRadius=0)

        #print circles
        if circles is None or len(circles[0]) > 1:
            #print "NO_PAWN"
            return 0

        circles = np.uint16(np.around(circles))
        i = circles[0][0]

        d = int(i[2] / 1.6)
        x = i[0]
        y = i[1]
        cv2.rectangle(img, (x - d, y - d), (x + d, y + d), (0, 255, 0))
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
            #print pos," -> ",suma,"\t|\t",self.Threshold[pos[0]][pos[1]]
        #print "suma =",suma
        if suma > 700:#self.Threshold[pos[0]][pos[1]]:
            #print "WHITE PAWN"
            cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

        else:
            #print "BLACK PAWN"
            cv2.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 2)
            cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

        #cv2.imshow('detected circles', img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        if suma > 700:##self.Threshold[pos[0]][pos[1]]:
            return 1
        else:
            return -1


drawing = False
ix = iy = 0


def take_photo():
    os.system(r"C:\cygwin64\bin\wget.exe http://192.168.1.101:8080/photoaf.jpg -O shot.jpg --quiet")
    img = cv2.imread(r"shot.jpg")
    return img


if __name__ == "__main__":

    proc = ImageProcess()
    """while True:
        img = take_photo()
        proc.addToCalibrate(img)
        x = show_image(proc.trimmed)
        if x == 27:
            break"""

    print proc.Threshold

    cv2.destroyAllWindows()
    while True:
        img = take_photo()
        board = proc.frame_table(img, False)

        cv2.namedWindow('image')
        while True:
            cv2.imshow('image', proc.trimmed)
            a = cv2.waitKey(1)
            if a & 0xFF == 27:
                sys.exit(0)
            if a & 0xFF == ord('a'):
                break
        cv2.destroyAllWindows()

        print board
