import cv2
import copy
import sys

sys.path.append("Game")
sys.path.append("Image")
from basicStructs import *
from AIlogic import *
import splitBoard as Image


proc = Image.ImageProcess()

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

prev = Image.take_photo()

while a.gameWon() == 0:
    turns += 1
    ok = 0

    while ok == 0:
        img = Image.take_photo()
        b = proc.frame_table(img, False)
        After = a.boardFromCamera(b)
        #print "From Camera:\n",b
        #print After

        cv2.imshow('image', proc.trimmed)
        xxx = cv2.waitKey(0)
        if xxx == 27:
            sys.exit(0)
        cv2.destroyAllWindows()

        if After is not None:
            print "OK"
            a = After
            ok = 1
        else:
            print "Bad Move! Try again! Previous board:"
            print a
            """img = Image.take_photo()
            proc.frame_table(img, False)
            cv2.imshow('image', proc.trimmed)
            xxx = cv2.waitKey(0)
            if xxx == 27:
                sys.exit(0)
            if xxx > 0:
                break"""
            cv2.destroyAllWindows()
            #Template = a.copy()
            #Template.swapSides()
            #for move in Template.possibleMoves():
            #print move

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


