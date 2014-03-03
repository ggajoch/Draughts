# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowUI.ui'
#
# Created: Sun Mar 02 21:55:18 2014
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
        MainWindow.resize(1103, 674)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
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
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 612, 631))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Image = QtGui.QWidget()
        self.Image.setObjectName(_fromUtf8("Image"))
        self.imageNormal = QtGui.QGraphicsView(self.Image)
        self.imageNormal.setGeometry(QtCore.QRect(0, 0, 605, 605))
        self.imageNormal.setObjectName(_fromUtf8("imageNormal"))
        self.tabWidget.addTab(self.Image, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.imageEdges = QtGui.QGraphicsView(self.tab_2)
        self.imageEdges.setGeometry(QtCore.QRect(0, 0, 605, 605))
        self.imageEdges.setObjectName(_fromUtf8("imageEdges"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.text = QtGui.QLabel(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(660, 530, 381, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(36)
        self.text.setFont(font)
        self.text.setText(_fromUtf8(""))
        self.text.setObjectName(_fromUtf8("text"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1103, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Draughts player", None))
        self.configButton.setText(_translate("MainWindow", "Config", None))
        self.calibrateCornersButton.setText(_translate("MainWindow", "Calibrate corners", None))
        self.nxtControlButton.setText(_translate("MainWindow", "NXT control", None))
        self.makeMoveButton.setText(_translate("MainWindow", "Make move", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Image), _translate("MainWindow", "Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Edges", None))

