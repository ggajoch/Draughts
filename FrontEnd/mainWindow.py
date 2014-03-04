from PyQt4.QtCore import *
from PyQt4.QtGui import *

import cv2
import MainApp.conf as config
import nxtWindow
import configWindow
import mainWindowUI as ui
import gui


class mainWindow(QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)
        self.thread = gui.Worker()
        self.connect(self.configButton,SIGNAL("clicked()"),self.configButton_click)
        self.connect(self.nxtControlButton, SIGNAL("clicked()"), self.nxtControlButton_click)
        self.connect(self.makeMoveButton, SIGNAL("clicked()"), self.new_move)

        self.connect(self, SIGNAL("moveList"), self.add_MoveTextHandler)
        self.connect(self, SIGNAL("textLabel"), self.setTextHandler)
        self.connect(self, SIGNAL("image_update"), self.updateImageHadler)
        self.connect(self, SIGNAL("connectionStatusHandler"), self.connectionStatusHandler)

    def use_thread(self, thr):
        self.thread = thr
        self.connect(self.calibrateCornersButton, SIGNAL("clicked()"), self.thread.calibrate_image)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    def new_move(self):
        self.thread.new_move()
    def on_saveSettingsButton_clicked(self):
        config.save_config()
    def nxtControlButton_click(self):
        ui = nxtWindow.nxtWindow(self)
        ui.exec_()
    def configButton_click(self):
        import MainApp.conf as Conf
        ui = configWindow.configWindow(self)
        ui.WorkingThread = self.thread
        ui.lineEdit.setText(config.get('IP'))
        ui.colorThresholdVal.setValue(int(config.get('threshold')))
        ui.p1.setValue(int(Conf.get('param1')))
        ui.p2.setValue(int(Conf.get('param2')))
        if ui.exec_():
            config.set('IP', ui.lineEdit.text())
            config.set('threshold', ui.colorThresholdVal.value())
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def add_text(self,string):
        self.textToAdd = string
        self.emit(SIGNAL("moveList"),self.add_MoveTextHandler)
    def add_MoveTextHandler(self):
        self.movesList.append(self.textToAdd)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def updateImage(self):
        self.emit(SIGNAL("image_update"), self.updateImageHadler)

    def updateImageHadler(self):
        cvRGBImg = cv2.cvtColor(self.imgEdges, cv2.COLOR_GRAY2RGB)
        qimg = QImage(cvRGBImg.data, cvRGBImg.shape[1], cvRGBImg.shape[0], QImage.Format_RGB888)
        qpm = QPixmap.fromImage(qimg)
        scene = QGraphicsScene()
        scene.addPixmap(qpm)
        self.imageEdges.setScene(scene)

        cvRGBImg = cv2.cvtColor(self.imgNormal, cv2.cv.CV_BGR2RGB)
        qimg = QImage(cvRGBImg.data, cvRGBImg.shape[1], cvRGBImg.shape[0], QImage.Format_RGB888)
        qpm = QPixmap.fromImage(qimg)
        scene = QGraphicsScene()
        scene.addPixmap(qpm)
        self.imageNormal.setScene(scene)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def setText(self, str):
        self.textForLabel = QString(str)
        self.emit(SIGNAL("textLabel"), self.setTextHandler)
    def setTextHandler(self):
        self.text.setText(self.textForLabel)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def Log(self, str):
        self.logText = str
        self.emit(SIGNAL("logAppend"), self.LogHandler)
    def LogHandler(self):
        self.logsTextBrowser.append(self.logText)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def setConnectionStatus(self, val):
        self.connectionStatusVal = val
        self.emit(SIGNAL("connectionStatusHandler"),self.connectionStatusHandler)
    def connectionStatusHandler(self):
        if self.connectionStatusVal:
            self.connectionStatusLabel.setText("<font color=#000000>Connection status: OK</font>")
        else:
            self.connectionStatusLabel.setText("<font color=#FF0000>Connection status: FAIL!</font>")