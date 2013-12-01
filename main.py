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

while a.gameWon() == 0:
    turns += 1
    ok = 0
    while ok == 0:
        img = Image.take_photo()
        After = proc.frame_table(img, False)
        print After

        cv2.imshow('image', proc.trimmed)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        if a.correctHumanMove(After):
            print "OK"
            a = After
            ok = 1
        else:
            print "Bad Move! Try again! Possible moves:"
            Template = a.copy()
            Template.swapSides()
            for move in Template.possibleMoves():
                print move

    sys.stdout.write("Turn " + str(turns))
    res = minimaks(copy.deepcopy(a), 6)
    print "White:", res[1]
    a.executeMove(res[1])

    if a.gameWon() != 0:
        break

print a
if a.gameWon() == 1:
    print "AI won!"
else:
    print "Human won!"
print "In", turns, "turns."


