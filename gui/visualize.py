from visualize_ui import Ui_VisualizationWindow
from help import Impl_HelpWindow
import pandas as pd
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget, QMainWindow, QApplication, QPushButton
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, precision_recall_curve, average_precision_score, roc_curve, auc
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import os
from PyQt5.QtGui import QPixmap, QImage
from PIL import ImageQt



class Impl_VisualizationWindow(Ui_VisualizationWindow, QtWidgets.QMainWindow):
    """Creates Visualization window"""

    def __init__(self):
        """Initializes Visualization window object"""
        super(Impl_VisualizationWindow, self).__init__()
        self.setupUi(self)

        self.customInit()
        self.customEvents()

    def customInit(self):
        """Custom init method"""
        self.btn_Vis_ConfMatrix.setEnabled(False)
        self.btn_Vis_ROC.setEnabled(False)
        self.btn_Vis_PRC.setEnabled(False)
        self.btn_SavePlot.setEnabled(False)
        self.df_dataset = None
        self.true_labels = None
        self.predicted_labels = None
        self.predicted_probabilities = None
        self.true_labels_mapped = None
        self.status_mapping = {'Escalated': True, 'FALSE': False, 'False Positive': False, 'escalated': True,'True Positive': True, 'false-positive': False}


    def customEvents(self):
        """Custom events method; here you connect functions with the UI."""

        self.btn_LoadPredResults.clicked.connect(self.btn_LoadPredResults_clicked)
        self.btn_Vis_ConfMatrix.clicked.connect(self.btn_Vis_ConfMatrix_clicked)
        self.btn_Vis_ROC.clicked.connect(self.btn_Vis_ROC_clicked)
        self.btn_Vis_PRC.clicked.connect(self.btn_Vis_PRC_clicked)
        self.btn_SavePlot.clicked.connect(self.btn_SavePlot_clicked)
        self.btn_Help.clicked.connect(self.btn_Help_clicked)

    def loadDataframe(self, filename):
        """Loads a dataframe from filepath

        Args:
            filename (str): File path to dataframe.
        """
        self.df_dataset = pd.read_csv(filename)
        self.btn_Vis_ConfMatrix.setEnabled(True)
        self.btn_Vis_ROC.setEnabled(True)
        self.btn_Vis_PRC.setEnabled(True)

        # Assuming your CSV file has columns for 'true_labels' and 'predicted_labels'
        self.true_labels = self.df_dataset['@status']
        self.predicted_labels = self.df_dataset['escalated_predicted']
        # Predicted probabilities for positive class
        self.predicted_probabilities = self.df_dataset['escalated_values_predicted']
        # Encode categorical labels to numeric format
        self.true_labels_mapped = self.df_dataset['@status'].map(self.status_mapping)

    def checkFilesHealth(self):
        """Checks that dataset, schema and model files are healthy.
        Returns:
            bool: Whether all files are valid or not.
        """
        dataset_check = self.txtB_DatasetPath.text() != ""
        return dataset_check

    def btn_LoadPredResults_clicked(self):
        """clicked event on btn_LoadPredResults
                Opens a file dialog to load a dataset.
                """
        widget = QtWidgets.QWidget()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            widget,
            "Open Prediction Result File",
            "",
            "CSV Files (*.csv)",
            options=options,
        )
        if fileName:
            self.txtB_DatasetPath.setText(fileName)
        if self.checkFilesHealth():
            self.loadDataframe(self.txtB_DatasetPath.text())

    def btn_Vis_ConfMatrix_clicked(self):

        # Create confusion matrix
        conf_matrix = confusion_matrix(self.true_labels, self.predicted_labels)

        # Clear the canvas before displaying the new plot
        self.plotCanvas.figure.clf()

        # Display the Matplotlib plot within the canvas
        ax = self.plotCanvas.figure.subplots()
        sns.heatmap(conf_matrix, annot=True, cmap='Blues', fmt='d', ax=ax)
        ax.set_xlabel('Predicted labels')
        ax.set_ylabel('True labels')
        ax.set_title('Confusion Matrix')
        self.plotCanvas.draw()

        # Enable save button
        self.btn_SavePlot.setEnabled(True)


    def btn_Vis_ROC_clicked(self):
        # ROC Curve
        fpr, tpr, thresholds = roc_curve(self.true_labels_mapped, self.predicted_probabilities)
        roc_auc = auc(fpr, tpr)

        # Clear the canvas before displaying the new plot
        self.plotCanvas.figure.clf()

        # Display the Matplotlib plot within the canvas
        ax = self.plotCanvas.figure.subplots()
        ax.plot(fpr, tpr, color='blue', lw=2, label='ROC curve (AUC = %0.2f)' % roc_auc)
        ax.plot([0, 1], [0, 1], color='gray', linestyle='--')
        ax.set_xlabel('False Positive Rate')
        ax.set_ylabel('True Positive Rate')
        ax.set_title('Receiver Operating Characteristic (ROC) Curve')
        ax.legend(loc='lower right')
        self.plotCanvas.draw()

        # Enable save button
        self.btn_SavePlot.setEnabled(True)

    def btn_Vis_PRC_clicked(self):
        # Calculate precision and recall
        precision, recall, _ = precision_recall_curve(self.true_labels_mapped, self.predicted_probabilities)

        # Calculate average precision score
        average_precision = average_precision_score(self.true_labels_mapped, self.predicted_probabilities)

        # Clear the canvas before displaying the new plot
        self.plotCanvas.figure.clf()

        # Display the Matplotlib plot within the canvas
        ax = self.plotCanvas.figure.subplots()
        ax.step(recall, precision, color='b', alpha=0.7, where='post')
        ax.fill_between(recall, precision, step='post', alpha=0.3, color='b')
        ax.set_xlabel('Recall')
        ax.set_ylabel('Precision')
        ax.set_ylim([0.0, 1.05])
        ax.set_xlim([0.0, 1.0])
        ax.set_title('Precision-Recall Curve (AP={0:0.2f})'.format(average_precision))
        self.plotCanvas.draw()

        # Enable save button
        self.btn_SavePlot.setEnabled(True)

    def btn_SavePlot_clicked(self):
        """Clicked event on btn_SavePlot component."""
        # Check if there is a current figure being displayed
        if self.plotCanvas.figure:
            file_name, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save Image", "",
                                                                 "PNG Files (*.png);;JPEG Files (*.jpeg *.jpg)")
            if file_name:
                # Get the extension of the file
                file_extension = os.path.splitext(file_name)[1].lower()
                # Check the file extension and save the image accordingly
                if file_extension in ['.png', '.jpeg', '.jpg']:
                    self.plotCanvas.figure.savefig(file_name, format=file_extension[1:], dpi=300)
                    QtWidgets.QMessageBox.information(None, "Success", "Image saved successfully.")
                else:
                    QtWidgets.QMessageBox.warning(None, "Warning", "Please save the image as PNG or JPEG.")
            else:
                QtWidgets.QMessageBox.warning(None, "Warning", "Please provide a file name.")
        else:
            QtWidgets.QMessageBox.warning(None, "Warning", "No image to save.")

    def btn_Help_clicked(self):
        """Clicked event on btn_Help component.
        Loads and show Help Window.
        """
        self.hs_ui = Impl_HelpWindow("Visualization")
        self.hs_ui.show()