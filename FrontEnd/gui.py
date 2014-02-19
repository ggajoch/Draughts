import sys, time, os
import cv2
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from mainWindow import *
from MainApp.mainApp import *
from Game.basicStructs import *
from Game.AIlogic import *
import Image.Image as Image
import nxtWindow


class image_updater(QThread):
    run = 1
    def __init__(self, Main=None):
        super(image_updater, self).__init__(Main)
        self.ui = Main
        self.work = True

    def update_ui(self, Main):
        super(image_updater, self).__init__(Main)
        self.ui = Main

    def run(self):
        while True:
            if self.work:
                img = Image.get_img()
                try:
                    MainApp.proc.frame_table(img, False)
                    cv2.imwrite("tmp.jpg", MainApp.proc.trimmed)
                    self.ui.updateImage.emit()
                    self.ui.add_textFunction("New image")
                except:
                    self.ui.add_textFunction("Cannot connect!")


            time.sleep(2)


class GuiHelpers:
    def __init__(self):
        pass

    def calibrate_image(self, w):
        w.work = False
        img = Image.get_img()
        MainApp.proc.calibrate_board(img)
        w.work = True


if __name__ == "__main__":
    g = GuiHelpers()
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    th = image_updater(ui)

    ui.register_worker(th)
    ui.register_interface(g)


    th.start()

    x = app.exec_()
    th.terminate()
    Image.timer_stop()
    print "finished"
    sys.exit(x)