from PyQt5 import QtCore, QtGui, QtWidgets
from help import Impl_HelpWindow
from predictions import  Impl_PredictionsWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi()
        self.btn_Help.clicked.connect(self.btn_Help_clicked)

    def setupUi(self):
        # ... (Previous code for MainWindow setup)

        # Left division layout (for menu buttons)
        self.leftDivision = QtWidgets.QWidget(self)
        self.leftLayout = QtWidgets.QVBoxLayout(self.leftDivision)
        self.leftLayout.setObjectName("leftLayout")
        self.leftLayout.setContentsMargins(0, 0, 0, 0)
        self.leftLayout.setSpacing(0)

        # Right division layout (initially empty)
        self.rightDivision = QtWidgets.QWidget(self)
        self.rightLayout = QtWidgets.QVBoxLayout(self.rightDivision)
        self.rightLayout.setObjectName("rightLayout")
        self.rightLayout.setContentsMargins(0, 0, 0, 0)
        self.rightLayout.setSpacing(0)

        # Splitting the main window into left and right divisions
        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.splitter.addWidget(self.leftDivision)
        self.splitter.addWidget(self.rightDivision)
        self.splitter.setSizes([200, 760])  # Set initial sizes for left and right divisions
        self.splitter.setObjectName("splitter")

        # Set the splitter as the central widget
        self.setCentralWidget(self.splitter)

        # ... (Place your menu buttons in self.leftLayout)
        # HELP
        self.btn_Help = QtWidgets.QPushButton(self.leftDivision)
        self.btn_Help.setObjectName("btn_Help")
        self.btn_Help.setGeometry(QtCore.QRect(120, 680, 30, 100))
        self.leftLayout.addWidget(self.btn_Help)

    def btn_Help_clicked(self):
        """Clicked event on btn_Datasets component.
        Loads and shows Datasets Window on the right side.
        """
        self.clearRightLayout()  # Clear the right layout before adding a new window
        #self.ds_ui = Impl_HelpWindow("Prediction")
        self.ds_ui = Impl_PredictionsWindow()
        self.rightLayout.addWidget(self.ds_ui)
        self.ds_ui.show()

    def clearRightLayout(self):
        """Clears the content of the right layout."""
        while self.rightLayout.count():
            item = self.rightLayout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
