# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_timer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DesignTimer(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(758, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.minute_label = QtWidgets.QLabel(self.centralwidget)
        self.minute_label.setGeometry(QtCore.QRect(270, 200, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.minute_label.setFont(font)
        self.minute_label.setObjectName("minute_label")
        self.second_label = QtWidgets.QLabel(self.centralwidget)
        self.second_label.setGeometry(QtCore.QRect(390, 200, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.second_label.setFont(font)
        self.second_label.setObjectName("second_label")
        self.unLabel = QtWidgets.QLabel(self.centralwidget)
        self.unLabel.setGeometry(QtCore.QRect(360, 190, 31, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.unLabel.setFont(font)
        self.unLabel.setObjectName("unLabel")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(320, 420, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 758, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.minute_label.setText(_translate("MainWindow", "00"))
        self.second_label.setText(_translate("MainWindow", "00"))
        self.unLabel.setText(_translate("MainWindow", ":"))
        self.startButton.setText(_translate("MainWindow", "START"))
