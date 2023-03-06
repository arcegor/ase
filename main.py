import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from ui import Ui_Upload
from process import FileManager
import pandas as pd


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Upload()
        self.ui.setupUi(self)
        self.ui.buttonUpload.clicked.connect(self.buttonUpload_clicked)
        self.ui.buttonProcess.clicked.connect(self.buttonProcess_clicked)
        self.ui.buttonGet.clicked.connect(self.buttonGet_clicked)
        self.ui.buttonProcess.setDisabled(True)
        self.ui.buttonGet.setDisabled(True)

        self.fm = FileManager()

    def buttonUpload_clicked(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './~')[0]
        df = pd.read_excel(fname)
        self.fm.data[fname] = df
        self.ui.files.setText('\n'.join(str(x) for x in self.fm.data.keys()))
        self.ui.buttonProcess.setEnabled(True)
        self.ui.buttonUpload.setDisabled(True)

    def buttonProcess_clicked(self):
        self.fm.process_all(self.ui.progressBar)
        self.ui.progressBar.setValue(100)
        self.ui.progressBar.setFormat('{0:.2f}%'.format(100))
        self.ui.buttonGet.setEnabled(True)
        self.ui.buttonProcess.setDisabled(True)

    def buttonGet_clicked(self):
        self.fm.get_item()
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setFormat('{0:.2f}%'.format(0))
        self.fm = FileManager()
        self.ui.files.setText('')
        self.ui.buttonUpload.setEnabled(True)
        self.ui.buttonGet.setDisabled(True)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())
