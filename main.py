import sys
from pathlib import Path

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from ProcessManager import ProcessManager
from ui import Ui_Upload
from FileManager import FileManager
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
        filenames, _ = QFileDialog.getOpenFileNames(
            self,
            'Open file',
            './~',
            "(*.xls *.xlsx)"
        )
        if filenames:
            filenames = [str(Path(filename)) for filename in filenames]
        else:
            return
        for filename in filenames:
            self.fm.data[filename] = pd.read_excel(filename)
        if not self.fm.validate():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Документы не соответствуют шаблону!")
            msg.setWindowTitle("Ошибка валидации!")
            msg.exec_()
            return
        self.ui.files.setText('\n'.join(str(x) for x in self.fm.data.keys()))
        self.ui.buttonProcess.setEnabled(True)
        self.ui.buttonUpload.setDisabled(True)

    def buttonProcess_clicked(self):
        self.fm.pm.find_collisions(self.fm.data)
        self.ui.buttonGet.setEnabled(True)
        self.ui.buttonProcess.setDisabled(True)

    def buttonGet_clicked(self):
        self.fm.get_result(self.fm.result)
        self.fm.clear()
        self.ui.files.setText('')
        self.ui.buttonUpload.setEnabled(True)
        self.ui.buttonGet.setDisabled(True)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())
