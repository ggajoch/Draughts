# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sat Feb 15 20:46:45 2014
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


class GUI_info__:
    def __init__(self):
        self.text = ""

GUI_info = GUI_info__()


class Ui_MainWindow(QtCore.QObject):
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
        self.image.setGeometry(QtCore.QRect(20, 10, 605, 605))
        self.image.setObjectName(_fromUtf8("image"))
        self.view = QtGui.QComboBox(self.centralwidget)
        self.view.setGeometry(QtCore.QRect(690, 30, 121, 22))
        self.view.setObjectName(_fromUtf8("view"))
        self.view.addItem(_fromUtf8(""))
        self.view.addItem(_fromUtf8(""))
        self.movesList = QtGui.QTextBrowser(self.centralwidget)
        self.movesList.setGeometry(QtCore.QRect(840, 20, 256, 471))
        self.movesList.setObjectName(_fromUtf8("movesList"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(710, 80, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 130, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(680, 180, 131, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(674, 220, 111, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
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

        MainWindow.connect(self.pushButton_4, QtCore.SIGNAL("clicked()"), self.calibrateHandler)#GUI.calibrate_image)
		
    def add_textHandler(self):
        self.movesList.append(GUI_info.text)

    def calibrateHandler(self):
        self.interface.calibrate_image(self.worker)

    def updateImageHadler(self):
        myPixmap = QtGui.QPixmap(QtCore.QString.fromUtf8('tmp.jpg'))
        scene = QtGui.QGraphicsScene()
        scene.addPixmap(myPixmap)
        self.image.setScene(scene)
        self.movesList.append("updated")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.view.setItemText(0, _translate("MainWindow", "Actual View", None))
        self.view.setItemText(1, _translate("MainWindow", "Board", None))
        self.pushButton.setText(_translate("MainWindow", "Reset Board", None))
        self.pushButton_2.setText(_translate("MainWindow", "Take back", None))
        self.pushButton_3.setText(_translate("MainWindow", "Force actual position", None))
        self.pushButton_4.setText(_translate("MainWindow", "Calibrate corners", None))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

