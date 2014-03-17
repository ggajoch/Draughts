from Game.AIlogic import *
import Image.Image as Image
from MainApp.logger import log

a = Board()

for i in range(0, 8, 2):
    a.set(i, 0, Field.AI)
    a.set(i, 6, Field.HU)

for i in range(1, 8, 2):
    a.set(i, 1, Field.AI)
    a.set(i, 7, Field.HU)

print a
turns = 0

proc = Image.ImageProcess()


def move(table, ui):
    global a, turns
    #img = Image.take_photo()
    #b = proc.frame_table(img, False)
    After = a.boardFromCamera(table)

    if After is not None:
        print "OK"
        log("move OK")
        bads = 0
        a = After
        ok = 1

        sys.stdout.write("Turn " + str(turns))
        turns += 1
        log("calculating move... ", line=False,time=False)
        res = minimaks(copy.deepcopy(a), 6)
        log("done")
        print "White:", res[1]
        #ui.add_move(res[1])
        string = "%c%d -> %c%d" % (chr(ord('A') + 7 - res[1][0].src.x), 8-res[1][0].src.y, chr(ord('A') + 7 - res[1][0].dst.x), 8-res[1][0].dst.y)
        ui.add_move(string)
        a.executeMove(res[1])
        print "After Move:\n", a
    else:
        log("bad move",error=True)
        print "Bad Move! Try again!\nPrevious board:"
        print a
        print "Actual board:"
        print table

    res = a.gameWon()
    if res != 0:
        if res == 1:
            log("AI won!")
            print "AI won!"
        else:
            log("Human won!")
            print "Human won!"
        log("game ended in %d turns" % turns)
        print "In", turns, "turns."


"""class MainApp(QThread):
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


        print a
        if a.gameWon() == 1:
            print "AI won!"
        else:
            print "Human won!"
        print "In", turns, "turns."

"""
