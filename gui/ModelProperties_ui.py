import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class Ui_ModelPropertiesWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("ModelProperties")
        self.resize(400, 500)
        self.setWindowTitle("Model Properties")
        self.setWindowIcon(QtGui.QIcon("../res/ML4CYBER_Logo.png"))
        
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = BasicEmptyWindow()
    window.show()
    sys.exit(app.exec_())
