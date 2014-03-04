# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowUI.ui'
#
# Created: Tue Mar 04 21:38:58 2014
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
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(630, 80, 120, 146))
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
        self.saveSettingsButton = QtGui.QPushButton(self.layoutWidget)
        self.saveSettingsButton.setObjectName(_fromUtf8("saveSettingsButton"))
        self.gridLayout.addWidget(self.saveSettingsButton, 4, 0, 1, 1)
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
        self.connectionStatusLabel = QtGui.QLabel(self.centralwidget)
        self.connectionStatusLabel.setGeometry(QtCore.QRect(630, 610, 131, 16))
        self.connectionStatusLabel.setObjectName(_fromUtf8("connectionStatusLabel"))
        self.tabWidget_2 = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(820, 20, 261, 441))
        self.tabWidget_2.setAutoFillBackground(True)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.movesListTextBrowser = QtGui.QTextBrowser(self.tab)
        self.movesListTextBrowser.setGeometry(QtCore.QRect(0, 0, 256, 421))
        self.movesListTextBrowser.setObjectName(_fromUtf8("movesListTextBrowser"))
        self.tabWidget_2.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.logsTextBrowser = QtGui.QTextBrowser(self.tab_3)
        self.logsTextBrowser.setGeometry(QtCore.QRect(0, 0, 256, 421))
        self.logsTextBrowser.setObjectName(_fromUtf8("logsTextBrowser"))
        self.tabWidget_2.addTab(self.tab_3, _fromUtf8(""))
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
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Draughts player", None))
        self.configButton.setText(_translate("MainWindow", "Config", None))
        self.calibrateCornersButton.setText(_translate("MainWindow", "Calibrate corners", None))
        self.nxtControlButton.setText(_translate("MainWindow", "NXT control", None))
        self.makeMoveButton.setText(_translate("MainWindow", "Make move", None))
        self.saveSettingsButton.setText(_translate("MainWindow", "Save settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Image), _translate("MainWindow", "Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Edges", None))
        self.connectionStatusLabel.setText(_translate("MainWindow", "Connection Status:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Moves list", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Logs", None))

