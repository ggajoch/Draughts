import cv2

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from mainWindow import *


sys.path.append("../MainApp")
sys.path.append("../Game")
sys.path.append(r"..\Image")
from mainApp import *
from basicStructs import *
from AIlogic import *
import Image


class image_updater(QThread):
    def run(self):
        print sys.path
        proc = Image.ImageProcess()
        while True:
            print "aaa"
            img = Image.take_photo()
            proc.frame_table(img, False)
            cv2.imwrite("tmp.jpg", proc.trimmed)
            global ui
            ui.updateImage.emit()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    global ui
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    th = image_updater()
    th.start()
    sys.exit(app.exec_())