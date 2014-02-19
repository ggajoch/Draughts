# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Wed Feb 19 02:31:36 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import nxtWindow
import configWindow


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

    updateImage = QtCore.pyqtSignal()
    add_text = QtCore.pyqtSignal()

    def register_interface(self, GUIInterface):
        self.interface = GUIInterface

    def register_worker(self, w):
        self.worker = w

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1143, 657)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.image = QtGui.QGraphicsView(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(20, 10, 600, 600))
        self.image.setObjectName(_fromUtf8("image"))
        self.movesList = QtGui.QTextBrowser(self.centralwidget)
        self.movesList.setGeometry(QtCore.QRect(840, 20, 256, 471))
        self.movesList.setObjectName(_fromUtf8("movesList"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(674, 80, 92, 83))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.nxtControlButton = QtGui.QPushButton(self.widget)
        self.nxtControlButton.setObjectName(_fromUtf8("nxtControlButton"))
        self.gridLayout.addWidget(self.nxtControlButton, 0, 0, 1, 1)
        self.configButton = QtGui.QPushButton(self.widget)
        self.configButton.setObjectName(_fromUtf8("configButton"))
        self.gridLayout.addWidget(self.configButton, 1, 0, 1, 1)
        self.calibrateCornersButton = QtGui.QPushButton(self.widget)
        self.calibrateCornersButton.setObjectName(_fromUtf8("calibrateCornersButton"))
        self.gridLayout.addWidget(self.calibrateCornersButton, 2, 0, 1, 1)
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

        self.updateImage.connect(self.updateImageHadler) #custom slot for updating image {!}
        self.add_text.connect(self.add_textHandler)

        MainWindow.connect(self.calibrateCornersButton, QtCore.SIGNAL("clicked()"), self.calibrateHandler)
        MainWindow.connect(self.nxtControlButton, QtCore.SIGNAL("clicked()"), self.nxtWindowHandler)
        MainWindow.connect(self.configButton,QtCore.SIGNAL("clicked()"),self.configHandler)

    def add_textHandler(self):
        self.movesList.append(self.textToAdd)

    def add_textFunction(self,string):
        #self.movesList.append(string)
        self.textToAdd = string
        self.add_text.emit()

    def calibrateHandler(self):
        self.interface.calibrate_image(self.worker)

    def nxtWindowHandler(self):
        Dialog = QtGui.QDialog()
        ui = nxtWindow.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.exec_()

    def configWindowHandler(self):
        Dialog = QtGui.QDialog()
        ui = configWindow.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.exec_()

    def updateImageHadler(self):
        myPixmap = QtGui.QPixmap(QtCore.QString.fromUtf8('tmp.jpg'))
        scene = QtGui.QGraphicsScene()
        scene.addPixmap(myPixmap)
        self.image.setScene(scene)
        self.movesList.append("updated")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Draughts player", None))
        self.nxtControlButton.setText(_translate("MainWindow", "NXT control", None))
        self.configButton.setText(_translate("MainWindow", "Config", None))
        self.calibrateCornersButton.setText(_translate("MainWindow", "Calibrate corners", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

