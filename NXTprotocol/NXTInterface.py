import NXTmail as NXTll #NXTSoft low level functions


class NXT:
    def __init__(self):
        self.nxt = NXTll.NXTconn()
        self.home_axis()
        self.x = 0
        self.y = 0

    def set_coords(self, x, y):
        self.nxt.sendNumberToMailbox(1)
        self.nxt.sendNumberToMailbox(x)
        self.nxt.sendNumberToMailbox(y)


    def pull_up(self):
        self.nxt.sendNumberToMailbox(2)

    def put_down(self):
        self.nxt.sendNumberToMailbox(3)

    def home_axis(self):
        self.nxt.sendNumberToMailbox(4)