# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fourth.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FourthWindow(object):
    def setupUi(self, FourthWindow):
        FourthWindow.setObjectName("FourthWindow")
        FourthWindow.resize(240, 320)
        self.centralwidget = QtWidgets.QWidget(FourthWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(11, 20, 221, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton_3.setFont(font)
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_3.setIcon(icon)
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.verticalLayout.addWidget(self.commandLinkButton_3)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.verticalLayout.addWidget(self.commandLinkButton)
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton_2.setFont(font)
        self.commandLinkButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_2.setIcon(icon)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.verticalLayout.addWidget(self.commandLinkButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 270, 221, 23))
        self.pushButton.setObjectName("pushButton")
        FourthWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FourthWindow)
        self.statusbar.setObjectName("statusbar")
        FourthWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FourthWindow)
        QtCore.QMetaObject.connectSlotsByName(FourthWindow)

    def retranslateUi(self, FourthWindow):
        _translate = QtCore.QCoreApplication.translate
        FourthWindow.setWindowTitle(_translate("FourthWindow", "MainWindow"))
        self.commandLinkButton_3.setText(_translate("FourthWindow", "SearchNBookAFlight!"))
        self.commandLinkButton.setText(_translate("FourthWindow", "Customers!"))
        self.commandLinkButton_2.setText(_translate("FourthWindow", "View Booked Tickets!"))
        self.pushButton.setText(_translate("FourthWindow", "Cancel"))

