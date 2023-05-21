from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QWidget, QProgressBar, QVBoxLayout


class ProgressBar(QWidget):

    def __init__(self):
        super().__init__()
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 500, 75)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.pbar)
        self.setLayout(self.layout)
        self.setGeometry(300, 300, 550, 100)

    def show(self):
        self.pbar.show()

    def set_value(self, value):
        self.pbar.setValue(value)
