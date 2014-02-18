import cv2
import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from mainWindow import *

sys.path.append("../MainApp")
sys.path.append("../Game")
sys.path.append(r"..\Image")
from mainApp import *
from basicStructs import *
from AIlogic import *
import Image, time
import nxtWindow


class image_updater(QThread):
    run = 1
    def __init__(self, Main=None):
        super(image_updater, self).__init__(Main)
        self.ui = Main

    def update_ui(self, Main):
        super(image_updater, self).__init__(Main)
        self.ui = Main

    def run(self):
        while True:
            #img = Image.take_photo()
            #MainApp.proc.frame_table(img, False)
            #cv2.imwrite("tmp.jpg", MainApp.proc.trimmed)
            #self.ui.updateImage.emit()
            #GUI_info.text = "trolololo"
            #self.ui.add_text.emit("abc")
            self.ui.add_textFunction("abc")
            time.sleep(0.1)



class GuiHelpers:
    def __init__(self):
        pass

    def calibrate_image(self, w):
        w.quit()
        MainApp.proc.calibrate_board()
        w.start()


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
    sys.exit(app.exec_())