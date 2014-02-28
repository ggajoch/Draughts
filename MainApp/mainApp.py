import copy
import sys
import cv2
from PyQt4.QtCore import *
from Game.basicStructs import *
from Game.AIlogic import *
import Image.Image as Image




class MainApp(QThread):
    proc = Image.ImageProcess()

    def run(self):
        a = Board()
        #img = Image.take_photo()
        #a = proc.frame_table(img, False)

        for i in range(0, 8, 2):
            a.set(i, 0, Field.AI)
            a.set(i, 6, Field.HU)

        for i in range(1, 8, 2):
            a.set(i, 1, Field.AI)
            a.set(i, 7, Field.HU)

        print a
        sys.stdout.flush()
        turns = 0

        while a.gameWon() == 0:
            turns += 1
            ok = 0
            bads = 0
            while ok == 0:
                img = Image.take_photo()
                b = self.proc.frame_table(img, False)
                After = a.boardFromCamera(b)

                if After is not None:
                    print "OK"
                    bads = 0
                    a = After
                    ok = 1
                else:
                    bads += 1
                if bads >= 1:
                    cv2.imshow('image', self.proc.trimmed)
                    xxx = cv2.waitKey(0)
                    if xxx == 27:
                        sys.exit(0)
                    cv2.destroyAllWindows()
                    print "Bad Move! Try again! Previous board:"
                    print a

            sys.stdout.write("Turn " + str(turns))
            res = minimaks(copy.deepcopy(a), 6)
            print "White:", res[1]
            a.executeMove(res[1])
            print "After Move:\n", a
            if a.gameWon() != 0:
                break

        print a
        if a.gameWon() == 1:
            print "AI won!"
        else:
            print "Human won!"
        print "In", turns, "turns."


