import sys
import time
from threading import Timer

from PyQt4.QtGui import *
from PyQt4.QtCore import *

import Image.Image as Image
import Image.takeImage as Shooter
from MainApp import logger
import mainWindow
import MainApp.mainApp as main

ImageProcess = Image.ImageProcess()

image_update_flag = True


class Worker(QThread):
    run = 1
    def __init__(self, Main=None):
        super(Worker, self).__init__(Main)
        #self.ui = mainWindow.mainWindow()
        self.ui = Main
        self.new = False
        self.set_pos_flag = False
        self.dots = 0
        self.gameplay = True

    def calc_image(self):
        try:
            self.ui.imgNormal = self.img
            self.ui.imgEdges = self.img
            self.table = ImageProcess.frame_table(self.img, False)
            self.ui.imgNormal = ImageProcess.trimmed
            self.ui.imgEdges = ImageProcess.edgesImage
            self.ui.updateImage()
        #print "New image"
        except Exception as ex:
            logger.log("cannot calculate image" + str(ex), error=True)

    def run(self):
        while True:
            if image_update_flag:
                self.img = Shooter.get_img()
                if self.img is None:
                    self.ok = False
                    self.ui.setConnectionStatus(False)
                else:
                    self.ok = True
                    self.ui.setConnectionStatus(True)
                    self.calc_image()
            time.sleep(0.1)
            if self.ok and self.gameplay:  #self.new:
                self.ui.Log("making move...")
                self.t = Timer(0.5, self.update_thinking_status)
                self.t.start()
                if main.move(self.table, self.ui):
                    #self.gameplay = False
                    pass
                self.t.cancel()
                ui.update_thinking_bar()
                ui.update_thinking_label("")
                self.new = False
                if self.set_pos_flag:
                    main.set_position(self.table)
                    self.set_pos_flag = False

    def update_thinking_status(self):
        ui.update_thinking_bar()
        str = "Thinking"
        for i in xrange(self.dots):
            str += "."
        ui.update_thinking_label(str)
        self.dots += 1
        self.dots = self.dots % 4
        self.t = Timer(0.5, self.update_thinking_status)
        self.t.start()

    def set_position(self):
        self.set_pos_flag = True

    def new_move(self):
        self.new = True

    def calibrate_image(self):
        logger.log("calibrating image")
        global image_update_flag
        image_update_flag = False
        try:
            img = Shooter.get_img()
            ImageProcess.calibrate_board(img)
        except Exception as ex:
            logger.log("cannot calibrate image" + str(ex),error=True)
        image_update_flag = True


if __name__ == "__main__":
    app = QApplication(sys.argv)

    global ui
    ui = mainWindow.mainWindow()
    ui.show()

    logger.register_ui(ui)

    th = Worker(ui)

    ui.use_thread(th)

    th.start()

    logger.log("Starting app")
    x = app.exec_()
    #th.terminate()
    Shooter.timer_stop()
    logger.log("app end")
    sys.exit(x)