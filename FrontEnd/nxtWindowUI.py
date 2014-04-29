# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nxtWindowUI.ui'
#
# Created: Sun Apr 27 17:47:48 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

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
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 330, 89))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_6 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.homeX = QtGui.QPushButton(self.layoutWidget)
        self.homeX.setObjectName(_fromUtf8("homeX"))
        self.gridLayout_2.addWidget(self.homeX, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.valY = QtGui.QSpinBox(self.layoutWidget)
        self.valY.setObjectName(_fromUtf8("valY"))
        self.gridLayout.addWidget(self.valY, 1, 1, 1, 1)
        self.valX = QtGui.QSpinBox(self.layoutWidget)
        self.valX.setObjectName(_fromUtf8("valX"))
        self.gridLayout.addWidget(self.valX, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.go = QtGui.QPushButton(self.layoutWidget)
        self.go.setObjectName(_fromUtf8("go"))
        self.gridLayout_3.addWidget(self.go, 0, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.catchPawn = QtGui.QPushButton(self.layoutWidget)
        self.catchPawn.setObjectName(_fromUtf8("catchPawn"))
        self.gridLayout_5.addWidget(self.catchPawn, 0, 0, 1, 1)
        self.releasePawn = QtGui.QPushButton(self.layoutWidget)
        self.releasePawn.setObjectName(_fromUtf8("releasePawn"))
        self.gridLayout_5.addWidget(self.releasePawn, 0, 1, 1, 1)
        self.close = QtGui.QPushButton(self.layoutWidget)
        self.close.setObjectName(_fromUtf8("close"))
        self.gridLayout_5.addWidget(self.close, 0, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.close, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.homeX.setText(_translate("Dialog", "Home axis", None))
        self.label.setText(_translate("Dialog", "Go to:", None))
        self.label_3.setText(_translate("Dialog", "Y", None))
        self.label_2.setText(_translate("Dialog", "X", None))
        self.go.setText(_translate("Dialog", "Go!", None))
        self.catchPawn.setText(_translate("Dialog", "Catch!", None))
        self.releasePawn.setText(_translate("Dialog", "Release!", None))
        self.close.setText(_translate("Dialog", "Close", None))

