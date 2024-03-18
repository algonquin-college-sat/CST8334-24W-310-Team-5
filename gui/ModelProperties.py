from PyQt5 import QtCore, QtWidgets
from ModelProperties_ui import Ui_ModelPropertiesWindow

class Impl_ModelPropertiesWindow(Ui_ModelPropertiesWindow, QtWidgets.QMainWindow):
    """Creates model properties window"""
    
    def __init__(self):
        """Initializes help window object"""
        super(Impl_ModelPropertiesWindow, self).__init__()
        # self.type = type
        self.setupUi()
        self.customInit()

    def customInit(self):
        """Custom init method"""
