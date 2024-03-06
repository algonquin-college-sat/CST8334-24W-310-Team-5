import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFileDialog, QMessageBox
from dataanalysis_ui import Ui_DataAnalysisWindow

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import seaborn as sns
from sklearn.metrics import precision_recall_curve, roc_curve, auc, confusion_matrix

class Impl_DataAnalysisWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_DataAnalysisWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.currentChanged.connect(self.on_current_page_changed)
        self.setWindowTitle("Data Analysis")

        self.customInit()
        self.customEvents()

    def customEvents(self):
        self.ui.pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.pushButton_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButton_6.clicked.connect(self.load_csv_data)

    def customInit(self):
        self.csv_loaded = False
        self.page_frames = [
            self.ui.frame_Performance, 
            self.ui.frame_CWEs_accuracy, 
            self.ui.frame_ROC_curve, 
            self.ui.frame_T10_Issues, 
            self.ui.frame_whatever
        ]

    def display_page(self, page_index):
        # Get figures
        figure = self.figures[page_index]

        # Add figures into frames
        if figure is not None:
            frame = self.page_frames[page_index]
            if frame.layout() is None:
                layout = QVBoxLayout()
                frame.setLayout(layout)
            else:
                # Clean layout if existed
                layout = frame.layout()
                for i in reversed(range(layout.count())):
                    layout.itemAt(i).widget().setParent(None)

            layout.addWidget(FigureCanvas(figure))

    # When press the button, change figure
    def on_current_page_changed(self, index):
        if not self.csv_loaded:
            # If data hasn't loaded, show warning
            QMessageBox.warning(self, "No CSV File Selected", "Please select a CSV file first.")
            return
        self.display_page(index)
    
    def generate_all_charts(self):
        self.figures = [
            self.generate_performance_chart(),
            self.generate_cwes_accuracy_chart(),
            self.generate_roc_curve(),
            self.generate_t10_issues_table(),
            self.generate_whatever_data()
        ]
    
    def load_csv_data(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Choose a CSV file", "", "CSV Files (*.csv)", options=options)
        if fileName:
            try:
                self.data = pd.read_csv(fileName)
                self.ui.label_2.setText(os.path.basename(fileName))
                self.csv_loaded = True
                self.generate_all_charts()
                return self.data
            except Exception as e:
                print(f"Error loading CSV file: {e}")
                return None
        else:
            return None

    """Data Analysis"""

    def generate_performance_chart(self):
        self.data['@status'] = self.data['@status'].replace({'escalated': 1, 'false-positive': 0})
        self.data['escalated_predicted'] = self.data['escalated_predicted'].replace({'escalated': 1, 'False': 0})        

        y_true = self.data['@status']
        y_pred = self.data['escalated_predicted']

        # Generate report
        fig, ax = plt.subplots(figsize=(8, 6))

        cm = confusion_matrix(y_true, y_pred)
        sns.heatmap(cm, annot=True, cmap='Blues', fmt='g')
        ax.set_xlabel('Predicted labels')
        ax.set_ylabel('True labels')
        ax.set_title('Confusion Matrix')

        return fig
    
    def generate_roc_curve(self):
        self.data['@status'] = self.data['@status'].replace({'escalated': 1, 'false-positive': 0})

        y_true = self.data['@status']
        y_score = self.data['escalated_values_predicted']

        fpr, tpr, _ = roc_curve(y_true, y_score)
        roc_auc = auc(fpr, tpr)

        # Visualization
        fig, ax = plt.subplots()
        ax.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
        ax.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        ax.set_xlim([0.0, 1.0])
        ax.set_ylim([0.0, 1.05])
        ax.set_xlabel('False Positive Rate')
        ax.set_ylabel('True Positive Rate')
        ax.set_title('Receiver Operating Characteristic')
        ax.legend(loc="lower right")

        return fig

    def generate_t10_issues_table(self):
        fig, ax = plt.subplots(figsize=(15, 6))
        top_10_rules = self.data['rule->@name'].value_counts().head(10).index
        sns.countplot(data=self.data, y='rule->@name', palette='rocket', order=top_10_rules, ax=ax)
        ax.set_title('Top 10 Issues based on Rule Name')
        ax.set_ylabel('Rule Name')
        ax.set_xlabel('Count')
        ax.bar_label(ax.containers[0], fmt='%d')
        plt.tight_layout()
        return fig

    def generate_cwes_accuracy_chart(self):
        self.data['@status'] = self.data['@status'].replace({'escalated': 1, 'false-positive': 0})
        self.data['escalated_predicted'] = self.data['escalated_predicted'].replace({'escalated': 1, 'False': 0})        

        self.data.dropna(subset=['cwe->@id'], inplace=True)
        
        # Calculate accuracy
        grouped = self.data.groupby('cwe->@id').apply(
            lambda x: (x['@status'] == x['escalated_predicted']).sum() / len(x)
        ).dropna()
        grouped = grouped.sort_values(ascending=False)

        fig, ax = plt.subplots(figsize=(10, 6))

        cmap = sns.color_palette("coolwarm", as_cmap=True)
        norm = plt.Normalize(grouped.values.min(), grouped.values.max())
        colors = cmap(norm(grouped.values))

        sns.barplot(x=grouped.index, y=grouped.values, palette=colors, ax=ax, order=grouped.index)
        ax.set_xlabel('CWEs')
        ax.set_ylabel('Accuracy')
        ax.set_title('Accuracy by CWEs')
        plt.xticks(ticks=range(len(grouped.index)), labels=[f'{int(i)}' for i in grouped.index])
        ax.bar_label(ax.containers[0], fmt='%0.2f')
        plt.tight_layout()

        return fig

    def generate_whatever_data(self):
        self.data['@status'] = self.data['@status'].replace({'escalated': 1, 'false-positive': 0})

        y_true = self.data['@status']
        y_score = self.data['escalated_values_predicted']

        fig, ax = plt.subplots(figsize=(15, 6))
        precision, recall, _ = precision_recall_curve(y_true, y_score)
        pr_auc = auc(recall, precision)
        sns.lineplot(x=recall, y=precision, marker='.')
        ax.set_xlabel('Recall')
        ax.set_ylabel('Precision')
        ax.set_title(f'Precision-Recall Curve (AUC = {pr_auc:.2f})')
        return fig

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Impl_DataAnalysisWindow()
    window.show()
    sys.exit(app.exec_())