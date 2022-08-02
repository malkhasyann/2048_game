# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 560)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # edit
        logo_pixmap = QPixmap(':/logos/logo300')
        self.picture_label = QtWidgets.QLabel(self.centralwidget)
        self.picture_label.setGeometry(QtCore.QRect(46, 50, 300, 300))
        self.picture_label.setPixmap(logo_pixmap)
        self.picture_label.resize(logo_pixmap.width(),
                                  logo_pixmap.height())

        self.button_play = QtWidgets.QPushButton(self.centralwidget)
        self.button_play.setGeometry(QtCore.QRect(40, 410, 263, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.button_play.setFont(font)
        self.button_play.setStyleSheet("border-radius: 10;\n"
"background-color: rgb(180, 180, 180)")
        self.button_play.setObjectName("button_play")
        self.grid_size = QtWidgets.QSpinBox(self.centralwidget)
        self.grid_size.setGeometry(QtCore.QRect(310, 410, 51, 31))
        self.grid_size.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_size.setMinimum(3)
        self.grid_size.setMaximum(8)
        self.grid_size.setObjectName("grid_size")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_play.setText(_translate("MainWindow", "PLAY"))
