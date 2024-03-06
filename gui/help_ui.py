from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HelpWindow(object):
    def setupUi(self, HelpWindow):
        HelpWindow.setObjectName("HelpWindow")
        HelpWindow.resize(1280, 340)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        HelpWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        HelpWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../res/ML4CYBER_Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        HelpWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(HelpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QTextEdit(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 89, 1000, 205))
        self.label.setObjectName("label")
        self.label.setReadOnly(True)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 1000, 31))
        self.label_2.setObjectName("label_2")
        HelpWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HelpWindow)
        QtCore.QMetaObject.connectSlotsByName(HelpWindow)

    def retranslateUi(self, HelpWindow):
        _translate = QtCore.QCoreApplication.translate
        if(HelpWindow.type == "Main"):
            HelpWindow.setWindowTitle(_translate("HelpWindow", "Help | Vinci ML Tool"))
            self.label_2.setText(_translate("HelpWindow", "The application offers a streamlined workflow with three main buttons"))
            self.label.setText(_translate("HelpWindow", 'The "Datasets" button enables users to import and label datasets derived from the output report of a specific SAST tool.\n\nAfter dataset preparation, the "Model Training" button streamlines the process of training and storing a machine learning model. Users can accomplish this by loading the schema of the training dataset and configuring essential training parameters.\n\nUpon completion of model training, the "Predictions" button empowers users to apply the trained model for predicting outcomes on previously unseen test data.'))

        if(HelpWindow.type == "Labeler"):
            HelpWindow.setWindowTitle(_translate("HelpWindow", "Help | Vinci ML Tool"))
            self.label_2.setText(_translate("HelpWindow", "Here is all the information about the Labeler Window"))
            self.label.setText(_translate("HelpWindow", "Dataset Sampling:\n1. Load the previously saved dataset in CSV format.\n2. Choose the 'Stratified' type during the partitioning process.\n3. Save the resulting training set for future use.\n\nDataset Labeling:\n1. Load the recently created training dataset in the Dataset Labeling section.\n2. Review each finding presented individually.\n3. Utilize the checkboxes on the right to assign labels, differentiating between True and False.\n4. Save the labeled dataset.\n5. Close the window upon completing the labeling process."))    
            
        if(HelpWindow.type == "Risk"):
            HelpWindow.setWindowTitle(_translate("HelpWindow", "Help | Vinci ML Tool"))
            self.label_2.setText(_translate("HelpWindow", "Here is all the information about the Risk window."))
            self.label.setText(_translate("HelpWindow", "The Risk window facilitates the evaluation of software vulnerabilities, employing the Common Weakness Scoring System (CWSS) Score as a comprehensive metric. This ultimate score integrates the Base Finding Score, Attack Surface Score, and Environment Score to quantify the overall threat posed by software vulnerabilities. Detailed descriptions of each score component are accessible through various tabs within the window."))

        if(HelpWindow.type == "Prediction"):
            HelpWindow.setWindowTitle(_translate("HelpWindow", "Help | Vinci ML Tool"))
            self.label_2.setText(_translate("HelpWindow","Here is all the information about the Prediction window."))
            self.label.setText(_translate("HelpWindow",'''
1. Begin by loading the original dataset, including the associated schema and training model.
2. Initiate the prediction process by clicking on "Predict."
3. Once the prediction is complete, choose "Save Results" to export the predictions as a .csv file.
'''))

        if(HelpWindow.type == "Models"):
            HelpWindow.setWindowTitle(_translate("HelpWindow", "Help | Vinci ML Tool"))
            self.label_2.setText(_translate("HelpWindow", "Here is all the information about the 'Models' window."))
            self.label.setText(_translate("HelpWindow", "1. Load the training schema for your dataset in the Model Window.\n"
                                                "2. Specify training parameters such as epochs, learning rate, and chosen metrics.\n"
                                                "3. Start the training process by clicking 'Train Now' in the window.\n"
                                                "4. Save the trained model to your system using the 'Save Model' option.\n"
                                                "5. Additionally, set a threshold and review detailed metrics information in the lower section of the window."))

        if(HelpWindow.type == "Dataset"):
            HelpWindow.setWindowTitle(_translate("HelpWindow", "Help | Vinci ML Tool"))
            self.label_2.setText(_translate("HelpWindow", "Here is all the information about the DataSet Window."))
            self.label.setText(_translate("HelpWindow", "After selecting the 'Dataset' option in the main menu, follow these steps:\n"
                                                        "1. Click on 'Load Dataset' positioned at the top-left corner to start loading your dataset.\n"
                                                        "2. Choose the file format for your dataset (CSV, XML, or JSON).\n"
                                                        "3. Once the dataset is loaded, select the appropriate 'preset' corresponding to your SAST tool and file format. We recommend using CSV tools for CSV files, and similarly for XML and JSON formats. The tool will automatically detect the report type and load recommended features to enhance prediction accuracy.\n"
                                                        "4. Customize your dataset by adding or removing columns and applying specific data transformations to fulfill your analytical needs.\n"))

        if(HelpWindow.type == "Risk Model"):
            HelpWindow.setWindowTitle(_translate("HelpWindow", "Help | Vinci ML Tool"))
            self.label_2.setText(_translate("HelpWindow", "Here is all the information about the 'Risk Model' window."))
            self.label.setText(_translate("HelpWindow", "The risk model window can be used to train the dataset. Load the schema which you want to use for training. Set the epochs and learning rate. Also select the metrics you want to use. Click on Train Now to train the model and use Save Model to save the trained model to your system. The threshold can also be set and metrics information can be viewed on the bottom section of the window."))

        if (HelpWindow.type == "Visualization"):
            HelpWindow.setWindowTitle(_translate("HelpWindow", "Help | Vinci ML Tool"))
            self.label_2.setText(_translate("HelpWindow", "Here is all the information about the 'Visualization' window."))
            self.label.setText(_translate("HelpWindow",
                                          "This window facilitates the visualization of prediction results generated from the Prediction Window. Start by selecting and loading the prediction file, which should be in .csv format. After loading the file, click on one of the available visualization options to display the corresponding plot. You can save the generated plot using the 'Save Plot' button."))


import menu_res_rc
