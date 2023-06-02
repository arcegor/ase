import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QProgressBar, QVBoxLayout

from FileManager import FileManager
from ui import Ui_Upload


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Upload()
        self.ui.setupUi(self)

        # Здесь можно настроить html разметку для приветствия
        self.html = '<h3>Добро пожаловать!</h3>'

        # Progress bar
        self.ui.progressBar.setValue(0)
        # Кнопки
        self.ui.buttonChooseSource.clicked.connect(self.buttonChooseSource_clicked)
        self.ui.buttonFindCollisions.clicked.connect(self.buttonFindCollisions_clicked)
        self.ui.buttonDownloadFixed.clicked.connect(self.buttonDownloadFixed_clicked)
        self.ui.buttonDownloadReport.clicked.connect(self.buttonDownloadReport_clicked)
        self.ui.buttonChooseTarget.clicked.connect(self.buttonChooseTarget_clicked)
        self.ui.buttonReset.clicked.connect(self.buttonReset_clicked)
        self.ui.buttonFindCollisions.setDisabled(True)
        self.ui.buttonDownloadFixed.setDisabled(True)
        self.ui.buttonDownloadReport.setDisabled(True)
        self.ui.buttonChooseTarget.setDisabled(True)
        self.fm = FileManager()
        self.ui.SomeInfo.setHtml(self.html)

    def buttonChooseSource_clicked(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open file', './~', '(*.xls *.xlsx *.xlsm)')
        if not filename:
            return
        self.fm.source_filenames['source'] = filename
        if self.is_valid():
            self.ui.buttonChooseTarget.setEnabled(True)
            self.ui.buttonChooseSource.setDisabled(True)
            self.ui.SomeInfo.append(f'Эталонный файл {filename} успешно загружен!\nВыберите проверяемый файл\n')

    def buttonChooseTarget_clicked(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open file', './~', '(*.xls *.xlsx *.xlsm)')
        if not filename:
            return
        self.fm.source_filenames['target'] = filename
        if self.is_valid():
            self.ui.buttonChooseTarget.setDisabled(True)
            self.ui.SomeInfo.append(f'Проверяемый файл {filename} успешно загружен!\nТеперь можно провести проверку!\n')
            self.ui.buttonFindCollisions.setEnabled(True)

    def buttonFindCollisions_clicked(self):
        if not self.fm.process(self.ui.progressBar):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка обработки!")
            msg.setWindowTitle("Ошибка!")
            msg.exec_()
            return
        self.ui.progressBar.setValue(100)
        self.ui.progressBar.setFormat('Готово! {0:.2f}%'.format(100))
        self.ui.SomeInfo.append(f'Проверка успешно завершена!\nТеперь можно скачать исправленный файл!\n')
        self.ui.buttonDownloadReport.setEnabled(True)
        self.ui.buttonDownloadFixed.setEnabled(True)
        self.ui.buttonFindCollisions.setDisabled(True)

    def buttonDownloadFixed_clicked(self):
        filename, _ = QFileDialog.getSaveFileName(None, "Save Fixed File", './~', '(*.xlsx)')
        if not filename:
            return
        if self.fm.get_result(flag='target', filename=filename):
            self.ui.SomeInfo.append('Исправленный файл:\n' + filename)
            self.ui.buttonDownloadFixed.setDisabled(True)

    def buttonDownloadReport_clicked(self):
        filename, _ = QFileDialog.getSaveFileName(None, "Save Report File", './отчет.xlsx', '(*.xlsx)')
        if not filename:
            return
        if self.fm.get_result(flag='report', filename=filename):
            self.ui.SomeInfo.append(f'Отчет:\n {filename} \n')
            self.ui.SomeInfo.append(f'Количество найденных коллизий: {self.fm.pm.collisions_count} \n'
                                    f'В процентах от общего числа: {int(self.fm.percent)}%')
            self.ui.buttonDownloadReport.setDisabled(True)

    def is_valid(self):
        if not self.fm.validate():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Документы не соответствуют шаблону!")
            msg.setWindowTitle("Ошибка валидации!")
            msg.exec_()
            return False
        return True

    def buttonReset_clicked(self):
        self.fm.clear()
        self.ui.buttonDownloadFixed.setDisabled(True)
        self.ui.buttonDownloadFixed.setDisabled(True)
        self.ui.buttonFindCollisions.setDisabled(True)
        self.ui.buttonChooseSource.setEnabled(True)
        self.ui.buttonChooseTarget.setDisabled(True)
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setFormat('{0:.2f}%'.format(0))
        self.ui.SomeInfo.setHtml(self.html)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    app.setWindowIcon(QIcon('atom.ico'))
    app.setStyle('Fusion')
    application = MainWindow()
    application.show()
    sys.exit(app.exec())
