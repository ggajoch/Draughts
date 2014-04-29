from PyQt4.QtGui import *

import nxtWindowUI as ui

import NXTprotocol.nxt as nxt


class nxtWindow(QDialog, ui.Ui_Dialog):
    def __init__(self, parent=None):
        super(nxtWindow, self).__init__(parent)
        self.setupUi(self)

    def on_homeX_clicked(self):
        nxt.setHome()

    def on_catchPawn_clicked(self):
        nxt.catchPawn()

    def on_releasePawn_clicked(self):
        nxt.releasePawn()

    def on_go_clicked(self):
        print "going to (%i %i)" % (self.valX.value(), self.valY.value())
        nxt.goto(self.valX.value(), self.valY.value())