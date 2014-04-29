#!/usr/bin/env python

import socket

import MainApp.conf as conf


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', int(conf.get('TCP_PORT'))))
except:
    print "TCP connection failed!"


def close():
    s.close()


def send_move(x1, y1, x2, y2):
    b = 7 - x1
    a = 7 - y1
    d = 7 - x2
    c = 7 - y2
    if c == -1:
        #beats
        c = 8
        d = 0
    if x2 == 8:
        #camera position
        a = 0
        b = 0
        c = 8
        d = y2

    if a == 9 and b == 9:
        #king
        a = 7 - y2
        b = 7 - x2
        c = 8
        d = 2

    try:
        s.send(str(a))
        s.send(str(b))
        s.send(str(c))
        s.send(str(d))
    except:
        print "TCP connection failed!"
    print "(", a, ",", b, ") -> (", c, ",", d, ")"


def setHome():
    send_move(0, 0, 8, 2)


def catchPawn():
    send_move(0, 0, 8, 3)


def releasePawn():
    send_move(0, 0, 8, 4)


def goto(x, y):
    send_move(9, 9, x, y)


if __name__ == "__main__":
    l = [[8, 8, 8, 8]]

    for x in l:
        send_move(x[0], x[1], x[2], x[3])