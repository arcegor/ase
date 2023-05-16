import sys
from pathlib import Path

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from ui import Ui_Upload
from FileManager import FileManager
import pandas as pd
import qt_material


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
            "(*.xls *.xlsx *.xlsm)"
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
        if not self.fm.process():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка обработки!")
            msg.setWindowTitle("Ошибка!")
            msg.exec_()
            return
        self.ui.buttonGet.setEnabled(True)
        self.ui.buttonProcess.setDisabled(True)

    def buttonGet_clicked(self):
        self.fm.get_result()
        self.fm.clear()
        self.ui.files.setText('\n'.join(str(x) for x in self.fm.result.keys()))
        self.ui.buttonUpload.setEnabled(True)
        self.ui.buttonGet.setDisabled(True)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    qt_material.apply_stylesheet(app, theme='light_cyan.xml', invert_secondary=True)
    app.setWindowIcon(QIcon('atom.ico'))
    app.setStyle('Fusion')
    application = MainWindow()
    application.show()
    sys.exit(app.exec())
