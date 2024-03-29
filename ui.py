# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'upload.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Upload(object):
    def setupUi(self, Upload):
        Upload.setObjectName("Upload")
        Upload.resize(1056, 487)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Upload.sizePolicy().hasHeightForWidth())
        Upload.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        Upload.setFont(font)
        self.layoutWidget = QtWidgets.QWidget(Upload)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 1012, 467))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.buttonChooseSource = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.buttonChooseSource.setFont(font)
        self.buttonChooseSource.setObjectName("buttonChooseSource")
        self.gridLayout_4.addWidget(self.buttonChooseSource, 0, 1, 1, 1)
        self.buttonFindCollisions = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.buttonFindCollisions.setFont(font)
        self.buttonFindCollisions.setObjectName("buttonFindCollisions")
        self.gridLayout_4.addWidget(self.buttonFindCollisions, 1, 0, 1, 1)
        self.buttonDownloadReport = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.buttonDownloadReport.setFont(font)
        self.buttonDownloadReport.setObjectName("buttonDownloadReport")
        self.gridLayout_4.addWidget(self.buttonDownloadReport, 1, 2, 1, 1)
        self.buttonDownloadFixed = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.buttonDownloadFixed.setFont(font)
        self.buttonDownloadFixed.setObjectName("buttonDownloadFixed")
        self.gridLayout_4.addWidget(self.buttonDownloadFixed, 1, 1, 1, 1)
        self.buttonChooseTarget = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.buttonChooseTarget.setFont(font)
        self.buttonChooseTarget.setObjectName("buttonChooseTarget")
        self.gridLayout_4.addWidget(self.buttonChooseTarget, 0, 0, 1, 1)
        self.buttonReset = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.buttonReset.setFont(font)
        self.buttonReset.setObjectName("buttonReset")
        self.gridLayout_4.addWidget(self.buttonReset, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 3, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.SomeInfo = QtWidgets.QTextBrowser(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SomeInfo.sizePolicy().hasHeightForWidth())
        self.SomeInfo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.SomeInfo.setFont(font)
        self.SomeInfo.setObjectName("SomeInfo")
        self.gridLayout.addWidget(self.SomeInfo, 2, 0, 1, 1)
        self.Statistics = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Statistics.setFont(font)
        self.Statistics.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Statistics.setAlignment(QtCore.Qt.AlignCenter)
        self.Statistics.setWordWrap(False)
        self.Statistics.setObjectName("Statistics")
        self.gridLayout.addWidget(self.Statistics, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.retranslateUi(Upload)
        QtCore.QMetaObject.connectSlotsByName(Upload)

    def retranslateUi(self, Upload):
        _translate = QtCore.QCoreApplication.translate
        Upload.setWindowTitle(_translate("Upload", "Upload"))
        self.buttonChooseSource.setText(_translate("Upload", "Выбрать эталонный файл"))
        self.buttonFindCollisions.setText(_translate("Upload", "Найти коллизии"))
        self.buttonDownloadReport.setText(_translate("Upload", "Скачать отчет"))
        self.buttonDownloadFixed.setText(_translate("Upload", "Скачать исправленный файл"))
        self.buttonChooseTarget.setText(_translate("Upload", "Выбрать проверяемый файл"))
        self.buttonReset.setText(_translate("Upload", "Начать сначала"))
        self.Statistics.setText(_translate("Upload", "Статистика по коллизиям"))
