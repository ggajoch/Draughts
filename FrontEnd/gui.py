import sys
import time

from PyQt4.QtGui import *
from PyQt4.QtCore import *

import Image.Image as Image
import mainWindow
import MainApp.mainApp as main


ImageProcess = Image.ImageProcess()

image_update_flag = True


class Worker(QThread):
    run = 1
    def __init__(self, Main=None):
        super(Worker, self).__init__(Main)
        self.ui = Main
        self.new = False

    def run(self):
        while True:
            if image_update_flag:
                self.img = Image.get_img()
                try:
                    self.table = ImageProcess.frame_table(self.img, False)
                    self.ui.imgNormal = ImageProcess.trimmed
                    self.ui.imgEdges = ImageProcess.edgesImage
                    self.ui.updateImage()
                    print "New image"
                except Exception as ex:
                    print "Error!", ex
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
    Image.timer_stop()
    print "finished"
    sys.exit(x)