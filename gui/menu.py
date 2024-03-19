from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from menu_ui import Ui_MainWindow
from datasets import Impl_DatasetsWindow
from datasets_labeler import Impl_DatasetsLabelerWindow
from labeler import Impl_LabelerWindow
from risk_from_menu import Impl_LabelerToRisk
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
        # self.btn_Label_clicked()
        # self.handleButtonClick(self.btn_Label)
        # pass

    def customEvents(self):
        """Custom events method; here you connect functions with the UI."""
        # Connect the buttons to their respective action handlers
        self.btn_Label.clicked.connect(self.btn_Label_clicked)
        self.btn_Datasets.clicked.connect(self.btn_Datasets_clicked)
        self.btn_Labeler.clicked.connect(self.btn_Labeler_clicked)
        self.btn_Risk.clicked.connect(self.btn_Risk_clicked)
        self.btn_Models.clicked.connect(self.btn_Models_clicked)
        self.btn_Predictions.clicked.connect(self.btn_Predictions_clicked)
        self.btn_Analysis.clicked.connect(self.btn_Analysis_clicked)
        self.btn_Visualize.clicked.connect(self.btn_Visualizations_clicked)
        self.btn_Help.clicked.connect(self.btn_Help_clicked)

        # Connect the buttons to the handleButtonClick method for highlighting
        # self.btn_Label.clicked.connect(lambda: self.handleButtonClick(self.btn_Label))
        self.btn_Datasets.clicked.connect(lambda: self.handleButtonClick(self.btn_Datasets))
        self.btn_Labeler.clicked.connect(lambda: self.handleButtonClick(self.btn_Labeler))
        self.btn_Risk.clicked.connect(lambda: self.handleButtonClick(self.btn_Risk))
        self.btn_Models.clicked.connect(lambda: self.handleButtonClick(self.btn_Models))
        self.btn_Predictions.clicked.connect(lambda: self.handleButtonClick(self.btn_Predictions))
        self.btn_Analysis.clicked.connect(lambda: self.handleButtonClick(self.btn_Analysis))
        self.btn_Visualize.clicked.connect(lambda: self.handleButtonClick(self.btn_Visualize))
        self.btn_Help.clicked.connect(lambda: self.handleButtonClick(self.btn_Help))

    def btn_Label_clicked(self):
        """Clicked event on btn_Datasets component.
        Loads and shows Datasets Window.
        """

        self.clearRightLayout()  # Clear the right layout

    def btn_Datasets_clicked(self):
        """Clicked event on btn_Datasets component.
        Loads and shows Datasets Window.
        """

        self.clearRightLayout()  # Clear the right layout before adding a new window
        self.ds_ui = Impl_DatasetsWindow()
        self.rightLayout.addWidget(self.ds_ui)
        self.ds_ui.show()

    def btn_Labeler_clicked(self):
        """Clicked event on btn_Datasets component.
        Loads and shows Datasets Window.
        """

        self.clearRightLayout()  # Clear the right layout before adding a new window
        self.ds_ui = Impl_LabelerWindow()
        self.rightLayout.addWidget(self.ds_ui)
        self.ds_ui.show()

    def btn_Risk_clicked(self):
        """Clicked event on btn_Datasets component.
        Loads and shows Datasets Window.
        """
        self.clearRightLayout()  # Clear the right layout before adding a new window
        self.ds_ui = Impl_LabelerToRisk()
        
        # self.rightLayout.addWidget(self.ds_ui)
        # self.ds_ui.show()

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

    def handleButtonClick(self, clicked_button):
        # Define CSS styles for default and highlighted buttons within the method
        default_style = """
            QPushButton {
                background-color: #ffffff;
                border-radius: 3px;
                border: 6px solid #5d64b0;
                color: #355398;
                font: 12pt "Times";
                font-weight: bold;
                padding: 5px 3px;
                text-decoration: none;
            }
            QPushButton:hover {
                background-color: #def2ff;
            }
            QPushButton:pressed {
                position: relative;
                top: 1px;
            }
        """

        highlighted_style = """
            QPushButton {
                background-color: #def2ff;  /* Highlighted state background */
                border-radius: 3px;
                border: 6px solid #5d64b0;  /* Consider a different border color to indicate active state */
                color: #355398;
                font: 12pt "Times";
                font-weight: bold;
                padding: 5px 3px;
                text-decoration: none;
                position: relative;  /* Optional: to mimic the pressed effect */
            }
        """

        # Reset the style of the previously highlighted button
        if hasattr(self, 'currently_highlighted_button') and self.currently_highlighted_button is not None:
            self.currently_highlighted_button.setStyleSheet(default_style)

        # Check if the clicked button is the btn_Label
        if clicked_button == self.btn_Label:
            # No stylesheet applied for btn_Label when clicked
            self.currently_highlighted_button = None
        else:
            # Apply the highlighted style to the clicked button
            clicked_button.setStyleSheet(highlighted_style)
            # Update the reference to the currently highlighted button
            self.currently_highlighted_button = clicked_button