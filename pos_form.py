# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pos_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(458, 440)
        Form.setStyleSheet("background-color:#a9cad9")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#35525e;")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(140, 30, 110, 22))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("color:#35525e;\n"
"background-color: white;")
        self.dateEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2050, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2005, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#35525e;")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(170, 80, 151, 22))
        self.comboBox.setStyleSheet("color:#35525e;\n"
"background-color: white;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#35525e;")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(23, 170, 411, 201))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: white;")
        self.textEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit.setObjectName("textEdit")
        self.add_pos = QtWidgets.QPushButton(Form)
        self.add_pos.setGeometry(QtCore.QRect(170, 400, 131, 23))
        self.add_pos.setStyleSheet("QPushButton{\n"
"    -webkit-transition-duration: 0.4s; \n"
"    transition-duration: 0.4s;\n"
"    border-radius: 5px;\n"
"    background-color: white;\n"
"    border: 1px solid #35525e;\n"
"    color: #35525e;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #35525e;\n"
"    color: white;\n"
"}")
        self.add_pos.setObjectName("add_pos")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "???????? ??????????????????"))
        self.label_2.setText(_translate("Form", "?????????????????????????? ??????????"))
        self.comboBox.setItemText(0, _translate("Form", "????????????????"))
        self.comboBox.setItemText(1, _translate("Form", "??????"))
        self.comboBox.setItemText(2, _translate("Form", "??????????????"))
        self.comboBox.setItemText(3, _translate("Form", "??????????????????"))
        self.comboBox.setItemText(4, _translate("Form", "????????????????????"))
        self.comboBox.setItemText(5, _translate("Form", "????????????"))
        self.comboBox.setItemText(6, _translate("Form", "??????????????????"))
        self.label_3.setText(_translate("Form", "??????????????????:"))
        self.textEdit.setPlaceholderText(_translate("Form", "?????????????????????? ??????????????????, ???????????????????????? ?? ??.??."))
        self.add_pos.setText(_translate("Form", "???????????????? ??????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
