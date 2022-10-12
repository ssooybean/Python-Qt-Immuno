# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(393, 387)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #a9cad9;\n"
"color: #34454d;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setStyleSheet("background-color: #a9cad9")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(90, 120, 211, 171))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.login = QtWidgets.QLineEdit(self.widget)
        self.login.setStyleSheet("border: 2px solid white;\n"
"color: #3e5a66;\n"
"")
        self.login.setObjectName("login")
        self.verticalLayout.addWidget(self.login)
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setStyleSheet("border: 2px solid white;\n"
"color: #3e5a66;\n"
"")
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: #35525e;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #436878;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: #35525e;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #436878;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(110, 60, 161, 52))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pic_col = QtWidgets.QLabel(self.widget1)
        self.pic_col.setText("")
        self.pic_col.setPixmap(QtGui.QPixmap("probirka.png"))
        self.pic_col.setObjectName("pic_col")
        self.horizontalLayout.addWidget(self.pic_col)
        self.name_pril = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.name_pril.setFont(font)
        self.name_pril.setStyleSheet("color: white;")
        self.name_pril.setObjectName("name_pril")
        self.horizontalLayout.addWidget(self.name_pril)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 393, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login.setPlaceholderText(_translate("MainWindow", "Login..."))
        self.password.setPlaceholderText(_translate("MainWindow", "Password.."))
        self.pushButton_3.setText(_translate("MainWindow", "Sign in"))
        self.pushButton_2.setText(_translate("MainWindow", "Sign up"))
        self.name_pril.setText(_translate("MainWindow", "Immuno"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
