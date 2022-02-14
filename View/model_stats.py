# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\View\model_stats.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


# View controller for the model statistics screen
class Ui_Dialog(QDialog):
    def __init__(self, data, lr):
        self.data = data.get_data()
        self.lr = lr
        super().__init__()

        self.setObjectName("Dialog")
        self.resize(707, 382)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(270, 335, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 241, 21))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.summary_table = QtWidgets.QTextBrowser(self)
        self.summary_table.setGeometry(QtCore.QRect(300, 20, 380, 152))
        self.summary_table.setObjectName("summary_table")
        self.summary_table.horizontalScrollBar()
        self.mean_label = QtWidgets.QLabel(self)
        self.mean_label.setGeometry(QtCore.QRect(300, 200, 380, 20))
        self.mean_label.setObjectName("mean_label")
        self.cnf_label = QtWidgets.QLabel(self)
        self.cnf_label.setGeometry(QtCore.QRect(10, 170, 271, 20))
        self.cnf_label.setObjectName("cnf_label")
        self.accuracyLabel = QtWidgets.QLabel(self)
        self.accuracyLabel.setGeometry(QtCore.QRect(10, 40, 100, 16))
        self.accuracyLabel.setObjectName("accuracyLabel")
        self.precisionsLabel = QtWidgets.QLabel(self)
        self.precisionsLabel.setGeometry(QtCore.QRect(10, 60, 100, 16))
        self.precisionsLabel.setObjectName("precisionsLabel")
        self.recallLabel = QtWidgets.QLabel(self)
        self.recallLabel.setGeometry(QtCore.QRect(10, 80, 100, 16))
        self.recallLabel.setObjectName("recallLabel")

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Regression Model Statistics"))
        self.accuracyLabel.setText(_translate("Dialog", "Accuracy:"))
        self.precisionsLabel.setText(_translate("Dialog", "Precision:"))
        self.recallLabel.setText(_translate("Dialog", "Recall"))
        self.cnf_label.setText(_translate("Dialog", "Confusion Matrix"))
        self.mean_label.setText(_translate("Dialog", "Mean values"))

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.print_metrics()
        self.print_summary()
        self.print_cnf()
        self.print_mean()

    # Find and print the mean data for each chargeoff status
    def print_mean(self):
        self.mean_table = QtWidgets.QTableWidget(self)
        self.mean_table.setGeometry(QtCore.QRect(300, 220, 380, 106))
        self.mean_table.setObjectName("mean_table")
        mean_data = self.lr.get_mean()
        features = ['ApprovalFY', 'Term', 'NoEmp', 'CreateJob', 'RetainedJob', 'DisbursementGross', 'GrAppv',
                    'SBA_Appv', 'Area_Rural', 'Area_Urban', 'Business_Existing', 'Business_New']

        self.mean_table.setRowCount(2)
        self.mean_table.setColumnCount(12)

        for row in range(2):
            self.mean_table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(int(mean_data[features[0]][row]))))
            self.mean_table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(int(mean_data[features[1]][row]))))
            self.mean_table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(int(mean_data[features[2]][row]))))
            self.mean_table.setItem(row, 3, QtWidgets.QTableWidgetItem(str(int(mean_data[features[3]][row]))))
            self.mean_table.setItem(row, 4, QtWidgets.QTableWidgetItem(str(int(mean_data[features[4]][row]))))
            self.mean_table.setItem(row, 5, QtWidgets.QTableWidgetItem(str(int(mean_data[features[5]][row]))))
            self.mean_table.setItem(row, 6, QtWidgets.QTableWidgetItem(str(int(mean_data[features[6]][row]))))
            self.mean_table.setItem(row, 7, QtWidgets.QTableWidgetItem(str(int(mean_data[features[7]][row]))))
            self.mean_table.setItem(row, 8, QtWidgets.QTableWidgetItem(str(round(mean_data[features[8]][row]))))
            self.mean_table.setItem(row, 9, QtWidgets.QTableWidgetItem(str(round(mean_data[features[9]][row]))))
            self.mean_table.setItem(row, 10, QtWidgets.QTableWidgetItem(str(round(mean_data[features[10]][row]))))
            self.mean_table.setItem(row, 11, QtWidgets.QTableWidgetItem(str(round(mean_data[features[11]][row]))))
        for i in range(12):
            self.mean_table.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        self.mean_table.setHorizontalHeaderLabels(features)
        self.mean_table.setVerticalHeaderLabels(['chgoff', 'p i f'])

    # Find and display the accuracy metrics of the model
    def print_metrics(self):
        metrics = self.lr.get_metrics()
        acc = "%.2f" % (metrics['Accuracy'] * 100) + '%'
        prec = "%.2f" % (metrics['Precision'] * 100) + '%'
        rec = "%.2f" % (metrics['Recall'] * 100) + '%'

        self.accuracyLabel.setText('Accuracy: ' + acc)
        self.precisionsLabel.setText('Precision: ' + prec)
        self.recallLabel.setText('Recall: ' + rec)

    # Print the summary of the regression model
    def print_summary(self):
        summary = self.lr.get_sm_results()
        self.summary_table.setText(summary.as_text())

    # Display the CNF chart
    def print_cnf(self):
        self.cnf_table = QtWidgets.QTableWidget(self)

        data = self.lr.create_conf_matrix().tolist()
        self.cnf_table.setRowCount(2)
        self.cnf_table.setColumnCount(2)
        self.cnf_table.setItem(0, 0, QtWidgets.QTableWidgetItem(str(data[0][0])))
        self.cnf_table.setItem(0, 1, QtWidgets.QTableWidgetItem(str(data[0][1])))
        self.cnf_table.setItem(1, 0, QtWidgets.QTableWidgetItem(str(data[1][0])))
        self.cnf_table.setItem(1, 1, QtWidgets.QTableWidgetItem(str(data[1][1])))

        self.cnf_table.setGeometry(QtCore.QRect(10, 190, 271, 85))
        self.cnf_table.setObjectName("cnf_table")
        # Table will fit the screen horizontally
        self.cnf_table.setHorizontalHeaderLabels(['chgoff', 'p i f'])
        self.cnf_table.setVerticalHeaderLabels(['chgoff', 'p i f'])
        self.cnf_table.horizontalHeader().setStretchLastSection(True)
        self.cnf_table.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)

