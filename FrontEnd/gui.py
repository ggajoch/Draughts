import sys
import time

from PyQt4.QtGui import *
from PyQt4.QtCore import *

import Image.Image as Image
import Image.takeImage as Shooter
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

    def calc_image(self):
        #try:
        self.ui.imgNormal = self.img
        self.ui.imgEdges = self.img
        self.table = ImageProcess.frame_table(self.img, False)
        self.ui.imgNormal = ImageProcess.trimmed
        self.ui.imgEdges = ImageProcess.edgesImage
        self.ui.updateImage()
        #print "New image"
        #except Exception as ex:
        #    print "Error!", ex

    def run(self):
        while True:
            if image_update_flag:
                self.img = Shooter.get_img()
                if self.img is None:
                    print "Cannot connect!"
                    self.ui.setConnectionStatus(False)
                else:
                    self.ui.setConnectionStatus(True)
                    self.calc_image()
            time.sleep(0.1)
            if self.new:
                main.move(self.table)#self.img)
                self.new = False

    def new_move(self):
        self.new = True

    def calibrate_image(self):
        global image_update_flag
        image_update_flag = False
        try:
            img = Image.get_img()
            ImageProcess.calibrate_board(img)
        except:
            print "Cannot connect!"
        image_update_flag = True


if __name__ == "__main__":
    app = QApplication(sys.argv)

    global ui
    ui = mainWindow.mainWindow()
    ui.show()

    th = Worker(ui)

    ui.use_thread(th)

    th.start()

    x = app.exec_()
    #th.terminate()
    Shooter.timer_stop()
    print "finished"
    sys.exit(x)