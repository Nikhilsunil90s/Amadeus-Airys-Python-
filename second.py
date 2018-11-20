# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(361, 294)
        self.centralwidget = QtWidgets.QWidget(RegisterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(49, 50, 261, 201))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.FName = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.FName.setObjectName("FName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.FName)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.LName = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.LName.setObjectName("LName")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.LName)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.EMail = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.EMail.setObjectName("EMail")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.EMail)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.Username = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Username.setObjectName("Username")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Username)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.Password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Password.setObjectName("Password")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Password)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.Telno = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Telno.setObjectName("Telno")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.Telno)
        self.registerButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.registerButton.setObjectName("registerButton")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.registerButton)
        self.cancelButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.cancelButton.setObjectName("cancelButton")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.cancelButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(76, 10, 201, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        RegisterWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RegisterWindow)
        self.statusbar.setObjectName("statusbar")
        RegisterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def retranslateUi(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "Register As Admin!"))
        self.label_2.setText(_translate("RegisterWindow", "First Name: "))
        self.label_3.setText(_translate("RegisterWindow", "Last Name: "))
        self.label_4.setText(_translate("RegisterWindow", "E-MailID:"))
        self.label_5.setText(_translate("RegisterWindow", "Username:"))
        self.label_6.setText(_translate("RegisterWindow", "Password: "))
        self.label_7.setText(_translate("RegisterWindow", "Tel. No.: "))
        self.registerButton.setText(_translate("RegisterWindow", "Register!"))
        self.cancelButton.setText(_translate("RegisterWindow", "Cancel!"))
        self.label.setText(_translate("RegisterWindow", "Register As an Admin Here!"))

