from PyQt4.QtGui import *
import configWindowUI as ui
import MainApp.conf as conf


class configWindow(QDialog, ui.Ui_Config):
    def __init__(self, parent=None):
        super(configWindow, self).__init__(parent)
        self.setupUi(self)

    def on_p1_valueChanged(self, x):
        import MainApp.conf as conf

        conf.set('param1', x)
        self.WorkingThread.calc_image()

    def on_p2_valueChanged(self, x):
        import MainApp.conf as conf

        conf.set('param2', x)
        self.WorkingThread.calc_image()

    def on_leftButton_clicked(self):
        x = int(conf.get('rotate'))
        conf.set('rotate', x + 1)

    def on_rightButton_clicked(self):
        x = int(conf.get('rotate'))
        conf.set('rotate', x - 1)