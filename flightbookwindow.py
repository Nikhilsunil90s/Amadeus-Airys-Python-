# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flightbookwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FlightBookWindow(object):
    def setupUi(self, FlightBookWindow):
        FlightBookWindow.setObjectName("FlightBookWindow")
        FlightBookWindow.resize(409, 217)
        self.centralwidget = QtWidgets.QWidget(FlightBookWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(90, 60, 241, 81))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 20, 241, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 150, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 150, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        FlightBookWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FlightBookWindow)
        self.statusbar.setObjectName("statusbar")
        FlightBookWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FlightBookWindow)
        QtCore.QMetaObject.connectSlotsByName(FlightBookWindow)

    def retranslateUi(self, FlightBookWindow):
        _translate = QtCore.QCoreApplication.translate
        FlightBookWindow.setWindowTitle(_translate("FlightBookWindow", "MainWindow"))
        self.label.setText(_translate("FlightBookWindow", "Departure Date: "))
        self.label_2.setText(_translate("FlightBookWindow", "Origin:"))
        self.comboBox.setItemText(0, _translate("FlightBookWindow", "AAP"))
        self.comboBox.setItemText(1, _translate("FlightBookWindow", "ABV"))
        self.comboBox.setItemText(2, _translate("FlightBookWindow", "ADS"))
        self.comboBox.setItemText(3, _translate("FlightBookWindow", "AEP"))
        self.comboBox.setItemText(4, _translate("FlightBookWindow", "AGC"))
        self.comboBox.setItemText(5, _translate("FlightBookWindow", "ALB"))
        self.comboBox.setItemText(6, _translate("FlightBookWindow", "ALX"))
        self.label_3.setText(_translate("FlightBookWindow", "Destination: "))
        self.comboBox_2.setItemText(0, _translate("FlightBookWindow", "IAD"))
        self.comboBox_2.setItemText(1, _translate("FlightBookWindow", "IAH"))
        self.comboBox_2.setItemText(2, _translate("FlightBookWindow", "IDI"))
        self.label_4.setText(_translate("FlightBookWindow", "Get The Best Prices Here!!!"))
        self.pushButton.setText(_translate("FlightBookWindow", "Get Flights!!!"))
        self.pushButton_2.setText(_translate("FlightBookWindow", "Cancel"))

