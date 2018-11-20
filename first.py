# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FirstWindow(object):
    def setupUi(self, FirstWindow):
        FirstWindow.setObjectName("FirstWindow")
        FirstWindow.resize(361, 215)
        FirstWindow.setStyleSheet("")
        FirstWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(FirstWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.newadminButton = QtWidgets.QPushButton(self.centralwidget)
        self.newadminButton.setGeometry(QtCore.QRect(0, 0, 181, 211))
        self.newadminButton.setObjectName("newadminButton")
        self.currentadminButton = QtWidgets.QPushButton(self.centralwidget)
        self.currentadminButton.setGeometry(QtCore.QRect(180, 0, 181, 211))
        self.currentadminButton.setObjectName("currentadminButton")
        FirstWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FirstWindow)
        QtCore.QMetaObject.connectSlotsByName(FirstWindow)

    def retranslateUi(self, FirstWindow):
        _translate = QtCore.QCoreApplication.translate
        FirstWindow.setWindowTitle(_translate("FirstWindow", "Select To Use!"))
        self.newadminButton.setToolTip(_translate("FirstWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Please click to Register as a new User!</span></p></body></html>"))
        self.newadminButton.setText(_translate("FirstWindow", "New Admin?"))
        self.currentadminButton.setToolTip(_translate("FirstWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Please click to enter the application!</span></p></body></html>"))
        self.currentadminButton.setText(_translate("FirstWindow", "Current Admin?"))

