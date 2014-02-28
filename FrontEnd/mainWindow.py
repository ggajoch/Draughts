from PyQt4.QtCore import *
from PyQt4.QtGui import *

import MainApp.conf as config

import nxtWindow
import configWindow
import mainWindowUI as ui
import gui


class mainWindow(QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)

        self.connect(self.calibrateCornersButton, SIGNAL("clicked()"), gui.calibrate_image)
        self.connect(self.configButton,SIGNAL("clicked()"),self.configButton_click)
        self.connect(self.nxtControlButton, SIGNAL("clicked()"), self.nxtControlButton_click)
        self.connect(self, SIGNAL("text"),self.add_textHandler)

    def add_textHandler(self):
        self.movesList.append(self.textToAdd)

    def add_text(self,string):
        self.textToAdd = string
        self.emit(SIGNAL("text"),self.add_textHandler)

    def nxtControlButton_click(self):
        ui = nxtWindow.nxtWindow(self)
        ui.exec_()

    def configButton_click(self):
        ui = configWindow.configWindow(self)
        ui.lineEdit.setText(config.IP)
        ui.spinBox.setValue(config.threshold)
        if ui.exec_():
            config.IP = ui.lineEdit.text()
            config.threshold = ui.spinBox.value()

    def updateImageHadler(self):
        myPixmap = QPixmap(QString.fromUtf8('tmp.jpg'))
        scene = QGraphicsScene()
        scene.addPixmap(myPixmap)
        self.image.setScene(scene)
        self.movesList.append("updated")