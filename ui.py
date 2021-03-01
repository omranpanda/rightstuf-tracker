# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(922, 654)
        MainWindow.setStyleSheet("color: rgb(244, 244, 244);\n"
"background-color: rgb(50, 50, 50);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(310, 280, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.verticalLayoutWidget_4.setFont(font)
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_URL = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_URL.setFont(font)
        self.label_URL.setObjectName("label_URL")
        self.verticalLayout_4.addWidget(self.label_URL)
        self.line_URL = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.line_URL.setFont(font)
        self.line_URL.setObjectName("line_URL")
        self.verticalLayout_4.addWidget(self.line_URL)
        self.push_URL = QtWidgets.QPushButton(self.centralwidget)
        self.push_URL.setGeometry(QtCore.QRect(320, 490, 281, 91))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.push_URL.setFont(font)
        self.push_URL.setObjectName("push_URL")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 50, 611, 81))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Sequence to Video"))
        self.label_URL.setText(_translate("MainWindow", "Input URL"))
        self.line_URL.setText(_translate("MainWindow", "https://www.rightstufanime.com"))
        self.push_URL.setText(_translate("MainWindow", "Save URL"))
        self.label.setText(_translate("MainWindow", "RightStufAnime Price Tracker"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())