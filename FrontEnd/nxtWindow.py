# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nxt.ui'
#
# Created: Mon Feb 17 19:46:33 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

import sys
import NXTprotocol.nxt as nxt

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(329, 88)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 330, 89))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_6 = QtGui.QGridLayout(self.widget)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.homeY = QtGui.QPushButton(self.widget)
        self.homeY.setObjectName(_fromUtf8("homeY"))
        self.gridLayout_2.addWidget(self.homeY, 1, 0, 1, 1)
        self.homeX = QtGui.QPushButton(self.widget)
        self.homeX.setObjectName(_fromUtf8("homeX"))
        self.gridLayout_2.addWidget(self.homeX, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.valY = QtGui.QSpinBox(self.widget)
        self.valY.setObjectName(_fromUtf8("valY"))
        self.gridLayout.addWidget(self.valY, 1, 1, 1, 1)
        self.valX = QtGui.QSpinBox(self.widget)
        self.valX.setObjectName(_fromUtf8("valX"))
        self.gridLayout.addWidget(self.valX, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.go = QtGui.QPushButton(self.widget)
        self.go.setObjectName(_fromUtf8("go"))
        self.gridLayout_3.addWidget(self.go, 0, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.catchPawn = QtGui.QPushButton(self.widget)
        self.catchPawn.setObjectName(_fromUtf8("catchPawn"))
        self.gridLayout_5.addWidget(self.catchPawn, 0, 0, 1, 1)
        self.releasePawn = QtGui.QPushButton(self.widget)
        self.releasePawn.setObjectName(_fromUtf8("releasePawn"))
        self.gridLayout_5.addWidget(self.releasePawn, 0, 1, 1, 1)
        self.close = QtGui.QPushButton(self.widget)
        self.close.setObjectName(_fromUtf8("close"))
        self.gridLayout_5.addWidget(self.close, 0, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.close, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)

# ~~~~~~~~~~~~~   MY CODE STARTS HERE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        QtCore.QObject.connect(self.homeX, QtCore.SIGNAL("clicked()"), nxt.setHomeX)
        QtCore.QObject.connect(self.homeY, QtCore.SIGNAL("clicked()"), nxt.setHomeY)
        QtCore.QObject.connect(self.catchPawn, QtCore.SIGNAL("clicked()"), nxt.catchPawn)
        QtCore.QObject.connect(self.releasePawn, QtCore.SIGNAL("clicked()"), nxt.releasePawn)
        QtCore.QObject.connect(self.go, QtCore.SIGNAL("clicked()"), self.nxtGoToPos)
# ~~~~~~~~~~~~~   MY CODE ENDS HERE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        QtCore.QMetaObject.connectSlotsByName(Dialog)


# ~~~~~~~~~~~~~   MY CODE STARTS HERE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def nxtGoToPos(self):
        print "going to (%i %i)" % (self.valX.value(), self.valY.value())
        nxt.goto(self.valX.value(), self.valY.value())
# ~~~~~~~~~~~~~   MY CODE ENDS HERE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.homeY.setText(_translate("Dialog", "Home Y", None))
        self.homeX.setText(_translate("Dialog", "Home X", None))
        self.label.setText(_translate("Dialog", "Go to:", None))
        self.label_3.setText(_translate("Dialog", "Y", None))
        self.label_2.setText(_translate("Dialog", "X", None))
        self.go.setText(_translate("Dialog", "Go!", None))
        self.catchPawn.setText(_translate("Dialog", "Catch!", None))
        self.releasePawn.setText(_translate("Dialog", "Release!", None))
        self.close.setText(_translate("Dialog", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

