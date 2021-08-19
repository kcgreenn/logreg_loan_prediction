# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\View\prog_bar.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import time

from PyQt5.QtWidgets import QStyleFactory, QDialog, QVBoxLayout, QProgressBar
from PyQt5.QtCore import QThread, pyqtSignal



class Worker(QThread):
    update_progress = pyqtSignal(int)   # A custom signal to be emitted by the worker thread

    def setData(self, data, lr):
        self.data = data
        self.lr = lr

    def run(self):
        self.data.load_data()
        self.update_progress.emit(20)
        data = self.data.get_data()
        self.lr.make_pred_target(data)
        self.update_progress.emit(40)
        self.lr.train_test_split()
        self.update_progress.emit(60)
        self.lr.make_y_pred()
        self.update_progress.emit(80)
        self.lr.make_sm_model()
        self.update_progress.emit(99)


class ProgDialog(QDialog):
    def __init__(self, data, lr):
        super().__init__()
        self.data = data
        self.lr = lr

        self.setWindowTitle("Loading Data, This may take several minutes")
        self.setModal(True)
        self.resize(400, 70)
        self.progressBar = QProgressBar()
        self.progressBar.setValue(0)
        self.progressBar.setStyle(QStyleFactory.create('Fusion'))

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.progressBar)
        self.setLayout(self.layout)

    # Load data from csv file for regression model.
    def load_data(self):
        self.worker = Worker()
        self.worker.setData(self.data, self.lr)
        self.worker.start()  # Create the worker thread and call the "run" method.
        self.worker.update_progress.connect(
            self.update_prog_bar)  # Method to be called the worker thread emits the update progress signal.
        self.worker.finished.connect(
            self.evt_worker_finished)  # Method to be called when the worker thread emits the finished signal.

    def update_prog_bar(self, val):
        for i in range(val - 20, val, 1):
            self.progressBar.setValue(i)
            time.sleep(0.1)

    def evt_worker_update(self, prog):
        self.progressBar.setValue(prog)

    def evt_worker_finished(self):
        self.close()
