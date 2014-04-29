import cv2

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import MainApp.conf as config
import nxtWindow
import configWindow
import mainWindowUI as ui
import gui
from MainApp.logger import log


class mainWindow(QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)
        self.thread = gui.Worker()
        self.connect(self.configButton, SIGNAL("clicked()"), self.configButton_click)
        self.connect(self.nxtControlButton, SIGNAL("clicked()"), self.nxtControlButton_click)
        self.connect(self.makeMoveButton, SIGNAL("clicked()"), self.new_move)
        self.connect(self.setBoard, SIGNAL("clicked()"), self.setBoardHandler)

        self.connect(self, SIGNAL("moveList"), self.add_MoveTextHandler)
        self.connect(self, SIGNAL("textLabel"), self.setTextHandler)
        self.connect(self, SIGNAL("image_update"), self.updateImageHadler)
        self.connect(self, SIGNAL("connectionStatusHandler"), self.connectionStatusHandler)
        self.connect(self, SIGNAL("logAppend"), self.LogHandler)
        self.connect(self, SIGNAL("update_thinking_labelHandler"), self.update_thinking_labelHandler)
        self.connect(self, SIGNAL("update_thinking_barHandler"), self.update_thinking_barHandler)

    def use_thread(self, thr):
        self.thread = thr
        self.connect(self.calibrateCornersButton, SIGNAL("clicked()"), self.thread.calibrate_image)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    def new_move(self):
        log("making move")
        self.thread.new_move()
    def on_saveSettingsButton_clicked(self):
        config.save_config()
    def nxtControlButton_click(self):
        log("opening NXT window")
        ui = nxtWindow.nxtWindow(self)
        ui.exec_()
    def configButton_click(self):
        import MainApp.conf as Conf
        log("opening configuration window")
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

    def add_move(self, string, rightAlign=False):
        if rightAlign:
            string = "      " + string
        self.textToAdd = str(string)
        self.emit(SIGNAL("moveList"), self.add_MoveTextHandler)
    def add_MoveTextHandler(self):
        self.movesListTextBrowser.append(self.textToAdd)
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
    def Log(self,str):
        self.logText = str
        self.emit(SIGNAL("logAppend"), self.LogHandler)
    def LogHandler(self):
        self.logsTextBrowser.setHtml(self.logText)
        x = self.logsTextBrowser.verticalScrollBar()
        x.setValue(x.maximum())
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def setConnectionStatus(self, val):
        self.connectionStatusVal = val
        self.emit(SIGNAL("connectionStatusHandler"), self.connectionStatusHandler)
    def connectionStatusHandler(self):
        if self.connectionStatusVal:
            self.connectionStatusLabel.setText("<font color=#000000>Connection status: OK</font>")
        else:
            self.connectionStatusLabel.setText("<font color=#FF0000>Connection status: FAIL!</font>")

    def setBoardHandler(self):
        print "SET BOARD"
        self.thread.set_pos_flag = True

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def update_thinking_bar(self):
        import Game.AIlogic as ai
        #print ai.nodes, ai.nodesMax
        p = (100.0 * ai.nodes) / ai.nodesMax;
        if p > 100: p = 100
        self.pVal = p
        self.emit(SIGNAL("update_thinking_barHandler"), self.update_thinking_barHandler)

    def update_thinking_barHandler(self):
        self.thinkingProgress.setValue(int(self.pVal))

    def update_thinking_label(self, str):
        self.thinkingLabelString = str
        self.emit(SIGNAL("update_thinking_labelHandler"), self.update_thinking_labelHandler)

    def update_thinking_labelHandler(self):
        self.thinkingLabel.setText(self.thinkingLabelString)
