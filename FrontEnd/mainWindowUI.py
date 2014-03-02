# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowUI.ui'
#
# Created: Sat Mar 01 03:06:56 2014
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1143, 657)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.image = QtGui.QGraphicsView(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(20, 10, 605, 605))
        self.image.setObjectName(_fromUtf8("image"))
        self.movesList = QtGui.QTextBrowser(self.centralwidget)
        self.movesList.setGeometry(QtCore.QRect(840, 20, 256, 471))
        self.movesList.setObjectName(_fromUtf8("movesList"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(674, 80, 92, 112))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.configButton = QtGui.QPushButton(self.layoutWidget)
        self.configButton.setObjectName(_fromUtf8("configButton"))
        self.gridLayout.addWidget(self.configButton, 1, 0, 1, 1)
        self.calibrateCornersButton = QtGui.QPushButton(self.layoutWidget)
        self.calibrateCornersButton.setObjectName(_fromUtf8("calibrateCornersButton"))
        self.gridLayout.addWidget(self.calibrateCornersButton, 2, 0, 1, 1)
        self.nxtControlButton = QtGui.QPushButton(self.layoutWidget)
        self.nxtControlButton.setObjectName(_fromUtf8("nxtControlButton"))
        self.gridLayout.addWidget(self.nxtControlButton, 0, 0, 1, 1)
        self.makeMoveButton = QtGui.QPushButton(self.layoutWidget)
        self.makeMoveButton.setObjectName(_fromUtf8("makeMoveButton"))
        self.gridLayout.addWidget(self.makeMoveButton, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1143, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Draughts player", None))
        self.configButton.setText(_translate("MainWindow", "Config", None))
        self.calibrateCornersButton.setText(_translate("MainWindow", "Calibrate corners", None))
        self.nxtControlButton.setText(_translate("MainWindow", "NXT control", None))
        self.makeMoveButton.setText(_translate("MainWindow", "Make move", None))

