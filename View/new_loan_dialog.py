# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\View\new_loan_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import math

import pandas as pd

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QButtonGroup


# View controller for the new loan prediction screen
class New_Loan_Dlg(QDialog):
    def __init__(self, data, lr):
        self.data = data
        self.lr = lr
        super().__init__()


        self.setObjectName("Dialog")
        self.resize(320, 540)
        self.setStyleSheet("background:#f7f7f7;")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_2.setObjectName("label_2")
        self.rural_btn = QtWidgets.QRadioButton(self)
        self.rural_btn.setGeometry(QtCore.QRect(150, 55, 51, 17))
        self.rural_btn.setObjectName("rural_btn")
        self.urban_btn = QtWidgets.QRadioButton(self)
        self.urban_btn.setGeometry(QtCore.QRect(240, 55, 51, 17))
        self.urban_btn.setObjectName("urban_btn")
        self.rural_btn.setText('Rural')
        self.urban_btn.setText('Urban')
        self.area_radio_grp = QButtonGroup()
        self.area_radio_grp.addButton(self.rural_btn)
        self.area_radio_grp.addButton(self.urban_btn)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_3.setObjectName("label_3")
        self.age_new_radio_btn = QtWidgets.QRadioButton(self)
        self.age_new_radio_btn.setGeometry(QtCore.QRect(150, 94, 82, 17))
        self.age_new_radio_btn.setObjectName("new_button")
        self.age_exist_radio_btn = QtWidgets.QRadioButton(self)
        self.age_exist_radio_btn.setGeometry(QtCore.QRect(240, 94, 82, 17))
        self.age_exist_radio_btn.setObjectName("exist_buttonn")
        self.age_exist_radio_btn.setText('Exist')
        self.age_new_radio_btn.setText('New')
        self.age_radio_grp = QButtonGroup()
        self.age_radio_grp.addButton(self.age_new_radio_btn)
        self.age_radio_grp.addButton(self.age_exist_radio_btn)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_4.setToolTip("")
        self.label_4.setObjectName("label_4")
        self.term_box = QtWidgets.QSpinBox(self)
        self.term_box.setGeometry(QtCore.QRect(211, 130, 81, 22))
        self.term_box.setObjectName("term_box")
        self.term_box.setMaximum(300)
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(10, 210, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(10, 250, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(10, 290, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(10, 170, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_8.setObjectName("label_8")
        self.approvalfy_box = QtWidgets.QSpinBox(self)
        self.approvalfy_box.setGeometry(QtCore.QRect(211, 170, 81, 22))
        self.approvalfy_box.setObjectName("approvalfy_box")
        self.approvalfy_box.setMaximum(2022)
        self.no_emp_box = QtWidgets.QSpinBox(self)
        self.no_emp_box.setGeometry(QtCore.QRect(211, 210, 81, 22))
        self.no_emp_box.setObjectName("no_emp_box")
        self.no_emp_box.setMaximum(10000)
        self.job_create_box = QtWidgets.QSpinBox(self)
        self.job_create_box.setGeometry(QtCore.QRect(211, 250, 81, 22))
        self.job_create_box.setObjectName("job_create_box")
        self.job_create_box.setMaximum(10000)
        self.job_retain_box = QtWidgets.QSpinBox(self)
        self.job_retain_box.setGeometry(QtCore.QRect(211, 290, 81, 22))
        self.job_retain_box.setObjectName("job_retain_box")
        self.job_retain_box.setMaximum(10000)
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(10, 330, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(10, 370, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(10, 410, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_11.setObjectName("label_11")
        self.gr_disburse_box = QtWidgets.QSpinBox(self)
        self.gr_disburse_box.setGeometry(QtCore.QRect(211, 330, 81, 22))
        self.gr_disburse_box.setObjectName("gr_disburse_box")
        self.gr_disburse_box.setMinimum(1000)
        self.gr_disburse_box.setMaximum(1000000)
        self.sba_appv_box = QtWidgets.QSpinBox(self)
        self.sba_appv_box.setGeometry(QtCore.QRect(211, 370, 81, 22))
        self.sba_appv_box.setObjectName("sba_appv_box")
        self.sba_appv_box.setMinimum(0)
        self.sba_appv_box.setMaximum(1000000)
        self.gr_appv_box = QtWidgets.QSpinBox(self)
        self.gr_appv_box.setGeometry(QtCore.QRect(211, 410, 81, 22))
        self.gr_appv_box.setObjectName("gr_appv_box")
        self.gr_appv_box.setMinimum(1000)
        self.gr_appv_box.setMaximum(1000000)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(80, 500, 160, 23))
        self.buttonBox.setStyleSheet("background:#0275d8;color:white;")
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(self.make_pred)
        self.buttonBox.rejected.connect(self.close)
        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(10, 460, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_12.setStyleSheet("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(230, 460, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setAutoFillBackground(False)
        self.label_13.setObjectName("label_13")
        self.label.setText("New Loan Default Prediction")
        self.label_2.setText("Geo. Area:")
        self.rural_btn.setText("Rural")
        self.urban_btn.setText("Urban")
        self.label_3.setText("Business Age:")
        self.age_new_radio_btn.setText("New")
        self.age_exist_radio_btn.setText("Existing")
        self.label_4.setText("Loan Term(months):")
        self.label_5.setText("No. of Employees:")
        self.label_6.setText("No. of Jobs Created:")
        self.label_7.setText("No. of Jobs Retained:")
        self.label_8.setText("Approval Fiscal Year:")
        self.label_9.setText("Disbursement Amount:")
        self.label_10.setText("Amount Backed By SBA:")
        self.label_11.setText("Total Amount of Loan:")
        self.label_12.setText("Chance of Payback:")
        self.set_tooltips()
        self.fill_mean_vals()

    def set_tooltips(self):
        self.label_2.setToolTip("Whether The Business Is Located In A Rural Or Urban District.")
        self.label_3.setToolTip("Whether The Business Is Brand New Or Already Existing.")
        self.label_4.setToolTip("The Term(length) of The Loan In Months")
        self.label_5.setToolTip("The Total Number of Employees Working For The Business.")
        self.label_6.setToolTip("The Number of Jobs The Business Will Create If The Loan Is Approved.")
        self.label_7.setToolTip("The Number of Jobs The Business Will Retain If The Loan Is Approved.")
        self.label_8.setToolTip("The fiscal year in which the loan will be approved.")
        self.label_9.setToolTip("Total Amount of Money Received by the Business.")
        self.label_10.setToolTip("The Amount of The Loan Guaranteed by The SBA.")
        self.label_11.setToolTip("The Total Amount of The Loan Approved By The Bank")
        self.label_12.setToolTip("The Percentage Chance That The Business Will Pay The Loan Back In Full.")

    # Prefill inputs with mean data for each feature
    def get_input(self):
        self.pred_data = {'Area_Urban': [], 'Area_Rural': [], 'Business_New': [], 'Business_Existing': [], 'Term': [],
                     'NoEmp': [], 'CreateJob': [], 'RetainedJob': [], 'DisbursementGross': [], 'GrAppv': [],
                     'SBA_Appv': [], 'ApprovalFY': []}
        self.pred_data['Area_Urban'].append(int(self.urban_btn.isChecked()))
        self.pred_data['Area_Rural'].append(int(self.rural_btn.isChecked()))
        self.pred_data['Business_New'].append(int(self.age_new_radio_btn.isChecked()))
        self.pred_data['Business_Existing'].append(int(self.age_exist_radio_btn.isChecked()))
        self.pred_data['Term'].append(self.term_box.value())
        self.pred_data['NoEmp'].append(self.no_emp_box.value())
        self.pred_data['CreateJob'].append(self.job_create_box.value())
        self.pred_data['RetainedJob'].append(self.job_retain_box.value())
        self.pred_data['DisbursementGross'].append(self.gr_disburse_box.value())
        self.pred_data['GrAppv'].append(self.gr_appv_box.value())
        self.pred_data['SBA_Appv'].append(self.sba_appv_box.value())
        self.pred_data['ApprovalFY'].append(self.approvalfy_box.value())

    # Return a percentage chance of the loan being paid in full based on user input
    def make_pred(self):
        self.get_input()
        df = pd.DataFrame(data=self.pred_data)
        default_perc = self.lr.make_pred(df)
        self.handle_label_color(default_perc)
        default_perc = "%.2f" % default_perc + '%'
        self.label_13.setText(default_perc)

    # Alter color of prediction based on percentage(red=low, high=green)
    def handle_label_color(self, percent):
        if percent < 50:
            self.label_13.setStyleSheet('background:#d9534f;')
        elif percent < 75:
            self.label_13.setStyleSheet('background:#f0ad4e;')
        else:
            self.label_13.setStyleSheet('background:#5cb85c')
    
    # find the mean values of each feature in the data
    def get_mean_vals(self):
        return self.data.get_data().groupby('MIS_Status_P I F').mean()

    # Prefill the input fields with the mean values of each feature
    def fill_mean_vals(self):
        mean_vals = self.get_mean_vals()
        self.age_exist_radio_btn.setChecked(True)
        self.urban_btn.setChecked(True)
        self.term_box.setValue(int(mean_vals['Term'][1]))
        self.no_emp_box.setValue(int(mean_vals['NoEmp'][1]))
        self.job_create_box.setValue(int(mean_vals['CreateJob'][1]))
        self.job_retain_box.setValue(int(mean_vals['RetainedJob'][1]))
        self.gr_disburse_box.setValue(int(mean_vals['DisbursementGross'][1]))
        self.gr_appv_box.setValue(int(mean_vals['GrAppv'][1]))
        self.sba_appv_box.setValue(int(mean_vals['SBA_Appv'][1]))
        self.approvalfy_box.setValue(int(mean_vals['ApprovalFY'][1]))
