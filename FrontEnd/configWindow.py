from PyQt4.QtCore import *
from PyQt4.QtGui import *
import configWindowUI as ui

class configWindow(QDialog, ui.Ui_Config):
    def __init__(self, parent=None):
        super(configWindow, self).__init__(parent)
        self.setupUi(self)