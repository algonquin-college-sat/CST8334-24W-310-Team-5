from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from menu_ui import Ui_MainWindow
from datasets import Impl_DatasetsWindow
from models import Impl_ModelsWindow
from predictions import Impl_PredictionsWindow
from help import Impl_HelpWindow
from visualize import Impl_VisualizationWindow
from dataanalysis import Impl_DataAnalysisWindow


class Impl_MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    """Creates menu window"""

    def __init__(self):
        """Initializes menu window object"""
        super(Impl_MainWindow, self).__init__()
        self.setupUi(self)

        self.customEvents()
        self.customInit()

    def customInit(self):
        """Custom init method"""
        pass

    def customEvents(self):
        """Custom events method; here you connect functions with the UI."""
        self.btn_Datasets.clicked.connect(self.btn_Datasets_clicked)
        self.btn_Models.clicked.connect(self.btn_Models_clicked)
        self.btn_Predictions.clicked.connect(self.btn_Predictions_clicked)
        self.btn_Analysis.clicked.connect(self.btn_Analysis_clicked)
        self.btn_Visualize.clicked.connect(self.btn_Visualizations_clicked)
        self.btn_Help.clicked.connect(self.btn_Help_clicked)

    def btn_Datasets_clicked(self):
        """Clicked event on btn_Datasets component.
        Loads and shows Datasets Window.
        """

        self.clearRightLayout()  # Clear the right layout before adding a new window
        self.ds_ui = Impl_DatasetsWindow()
        self.rightLayout.addWidget(self.ds_ui)
        self.ds_ui.show()

    def btn_Models_clicked(self):
        """Clicked event on btn_Models component.
        Loads and shows Models Window.
        """

        self.clearRightLayout()  # Clear the right layout before adding a new window
        self.md_ui = Impl_ModelsWindow()
        self.rightLayout.addWidget(self.md_ui)
        self.md_ui.show()

    def btn_Predictions_clicked(self):
        """Clicked event on btn_Preditions component.
        Loads and shows Predictions Window.
        """

        self.clearRightLayout()  # Clear the right layout before adding a new window
        self.pd_ui = Impl_PredictionsWindow()
        self.rightLayout.addWidget(self.pd_ui)
        self.pd_ui.show()

    def btn_Analysis_clicked(self):
        """Clicked event on btn_DataAnalysis component.
        Loads and show DataAnalysis Window.
        """
        self.clearRightLayout()  # Clear the right layout before adding a new window
        self.da_ui = Impl_DataAnalysisWindow()
        self.rightLayout.addWidget(self.da_ui)
        self.da_ui.show()

    def btn_Visualizations_clicked(self):
        """Clicked event on btn_Visualize component.
        Loads and shows Visualization Window.
        """

        self.clearRightLayout()  # Clear the right layout before adding a new window
        self.vs_ui = Impl_VisualizationWindow()
        self.rightLayout.addWidget(self.vs_ui)
        self.vs_ui.show()

    def btn_Help_clicked(self):
        """Clicked event on btn_Help component.
        Loads and show Help Window.
        """
        self.clearRightLayout()  # Clear the right layout before adding a new window
        self.hs_ui = Impl_HelpWindow("Main")
        self.rightLayout.addWidget(self.hs_ui)
        self.hs_ui.show()

    def clearRightLayout(self):
        """Clears the content of the right layout."""
        while self.rightLayout.count():
            item = self.rightLayout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()