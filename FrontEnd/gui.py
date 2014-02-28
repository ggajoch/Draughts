import sys, time, os
import cv2
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from MainApp.mainApp import *
from Game.basicStructs import *
from Game.AIlogic import *
import Image.Image as Image

import nxtWindow
import mainWindow



image_update_flag = True
class image_updater(QThread):
    run = 1
    def __init__(self, Main=None):
        super(image_updater, self).__init__(Main)
        self.ui = Main

    def run(self):
        while True:
            if image_update_flag:
                """img = Image.get_img()
                try:
                    MainApp.proc.frame_table(img, False)
                    cv2.imwrite("tmp.jpg", MainApp.proc.trimmed)
                    self.ui.updateImage.emit()
                    self.ui.add_textFunction("New image")
                except:"""
                self.ui.add_text("Cannot connect!")
            time.sleep(2)


def calibrate_image():
    global image_update_flag
    image_update_flag = False
    img = Image.get_img()
    MainApp.proc.calibrate_board(img)
    image_update_flag = True


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui = mainWindow.mainWindow()
    ui.show()

    th = image_updater(ui)

    #ui.register_worker(th)
    #ui.register_interface(g)


    th.start()

    x = app.exec_()
    #th.terminate()
    Image.timer_stop()
    print "finished"
    sys.exit(x)