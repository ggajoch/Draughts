import NXTmail as NXTll #NXTSoft low level functions


nxt = NXTll.NXTconn()
x = 0
y = 0

def goto(x, y):
    nxt.sendNumberToMailbox(1)
    nxt.sendNumberToMailbox(x)
    nxt.sendNumberToMailbox(y)


def catchPawn():
    nxt.sendNumberToMailbox(2)

def releasePawn():
    nxt.sendNumberToMailbox(3)

def setHomeX():
    nxt.sendNumberToMailbox(4)
def setHomeY():
    nxt.sendNumberToMailbox(5)