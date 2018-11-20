# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'third.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SigninWindow(object):
    def setupUi(self, SigninWindow):
        SigninWindow.setObjectName("SigninWindow")
        SigninWindow.resize(331, 280)
        self.centralwidget = QtWidgets.QWidget(SigninWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 181, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 50, 121, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 80, 181, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.signinButton = QtWidgets.QPushButton(self.centralwidget)
        self.signinButton.setGeometry(QtCore.QRect(120, 210, 75, 41))
        self.signinButton.setObjectName("signinButton")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(0, 0, 71, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setObjectName("commandLinkButton")
        SigninWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SigninWindow)
        self.statusbar.setObjectName("statusbar")
        SigninWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SigninWindow)
        QtCore.QMetaObject.connectSlotsByName(SigninWindow)

    def retranslateUi(self, SigninWindow):
        _translate = QtCore.QCoreApplication.translate
        SigninWindow.setWindowTitle(_translate("SigninWindow", "Sign-In Admin!"))
        self.label.setText(_translate("SigninWindow", "Welcome, Admin!"))
        self.label_2.setText(_translate("SigninWindow", "Please Sign-In:"))
        self.label_3.setText(_translate("SigninWindow", "Username:"))
        self.label_4.setText(_translate("SigninWindow", "Password:"))
        self.label_5.setText(_translate("SigninWindow", "E-Mail: "))
        self.signinButton.setText(_translate("SigninWindow", "Sign-In!"))
        self.commandLinkButton.setText(_translate("SigninWindow", "Back"))

