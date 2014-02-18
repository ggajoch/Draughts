#from serial import Serial


class sender:
    def init(self,device):
        pass

    def sendByte(self,x):
        print x

    def readByte(self):
        return 0

    def sendAndReceive(self,comm):
        Mess = [0,0]
        length = len(comm)
        Mess[0] = (length & 0xFF)
        length = (length >> 8)
        Mess[1] = (length & 0xFF)
        for i in comm:
            Mess.append(i)
        for i in Mess:
            self.sendByte(i)

        length = self.readByte() + 256 * self.readByte()
        r = ""
        for i in xrange(length):
            r += self.readByte()
        return r
    
class NXTconn(sender):
    def __init__(self):
        self.connect(1, 2)

    def connect(self, sendMail, rcvMail):
        self.sendMailbox = sendMail
        self.rcvMailbox = rcvMail

    def readNumberFromMailbox(self):
        mess = [0, 0x13, (self.sendMailbox+10), 0, 1]
        r = self.sendAndReceive(mess)
        return int(r[9] + r[10])

    def sendNumberToMailbox(self, number):
        mess = [0, 9, self.rcvMailbox, 5, 0, 0, 0, 0, 0]
        for i in range(4, 8):
            mess[i] = (number & 0xFF)
            number = (number >> 8)
        self.sendAndReceive(mess)



if __name__ == "__main__":
    a = NXTconn(1,5)
    a.sendNumberToMailbox(511)
    a.readNumberFromMailbox()
#    mess = [i for i in xrange(13)]
#    a.sendAndReceive(mess)
