import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStackedWidget
from registration import *
from PyQt5.QtGui import QIcon
import sqlite3
from homep import *
import pos_form
import analiz_form
import preparat
import shutil
import os



#Регистрация
class Registration(QtWidgets.QMainWindow):
    def __init__(self):
        super(Registration, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init__Ui()

        self.ui.pushButton_3.clicked.connect(self.auth)
        self.ui.pushButton_2.clicked.connect(self.reg)
        self.base_line_edit = [self.ui.login, self.ui.pushButton_3]


    def init__Ui(self):
        self.setWindowTitle("Immuno - авторизация")
        self.setWindowIcon(QIcon("probirka.png"))

#Проверка заполненности полей регистрации
    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text())== 0:
                    return
            funct(self)
        return wrapper

    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)
    
    @check_input
    def auth(self):
        name = self.ui.login.text()
        passw = self.ui.password.text()
        id = 1
        self.check_db(id, name, passw)

    @check_input
    def reg(self):
        name = self.ui.login.text()
        passw = self.ui.password.text()
        i = 2
        self.check_db(i, name, passw)

#Проверка наличия логина/пароля в БД
    def check_db(self, i, name, passw):
        try:
            if i == 1:
                con = sqlite3.connect('users.db')
                cur = con.cursor()

                cur.execute(f"""SELECT * FROM users WHERE name ='{name}';""")
                value = cur.fetchall()

                if value != [] and value[0][2] == passw:
                    self.second_form = HomePage(value[0][0])
                    self.second_form.show()
                    self.close()
                else:
                    self.signal_handler("Неправильно введен логин и/или пароль")
                cur.close()
                con.close()

            elif i == 2:
                con = sqlite3.connect('users.db')
                cur = con.cursor()

                cur.execute(f"""SELECT * FROM users WHERE name ='{name}';""")
                value = cur.fetchall()

                if value != []:
                    self.signal_handler("Такой логин уже занят")
                elif value == []:
                    cur.execute(f"""INSERT INTO users (name, password) VALUES ('{name}', '{passw}')""")
                    self.signal_handler("Вы успешно зарегистрированы")
                    con.commit()
                cur.close()
                con.close()
        except sqlite3.Error as error:
            QtWidgets.QMessageBox.about(self, 'Ошибка!', "Проблема с базой данных")



class HomePage(QtWidgets.QWidget):
    def __init__(self, arg):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initUI()
        self.id = arg

    def initUI(self):
        self.setWindowTitle("Immuno - Home Page")
        self.setWindowIcon(QIcon("probirka.png"))

        self.ui.stackedWidget.setCurrentIndex(0) #Пустая страница, перед тем как пользователь ни разу не выбрал категорию
        self.ui.poseshenia.clicked.connect(self.list_po) #Страница посещений
        self.ui.analizi.clicked.connect(self.list_analiz) #Страница анализов
        self.ui.preparati.clicked.connect(self.list_prep) #Страница принимаемых препаратов

        self.ui.add_pos.clicked.connect(self.show_pos_form) #Добавление посещений
        self.ui.add_analiz.clicked.connect(self.show_analiz_form) #Добавление анализов
        self.ui.add_prep.clicked.connect(self.show_prep_form) #Добавление принимаемых препаратов

        self.ui.obnov_analiz.clicked.connect(self.list_po)#Обновление результатов
        self.ui.del_pos.clicked.connect(self.delit_pos)
    

    def list_po(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        try:
            con = sqlite3.connect('users.db')
            cur = con.cursor()

            list_pose = cur.execute(f"""SELECT * FROM pos_users WHERE id = {self.id}""")

        except sqlite3.Error as error:
            QtWidgets.QMessageBox.about(self, 'Ошибка!', "Проблема с базой данных посещений")
        
        
        self.ui.listWidget.clear()
        for element in list_pose:
            self.text = f"                                                       Дата: {element[0]}\n     Врач: {element[1]}\n     Рекомендации: {element[2]}\n"
            self.ui.listWidget.addItem(self.text)

        con.commit()
        cur.close()
        con.close()
    


    def list_prep(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        try:
            con = sqlite3.connect('users.db')
            cur = con.cursor()

            list_pr = cur.execute(f"""SELECT * FROM prepar_users WHERE id = {self.id}""")

        except sqlite3.Error as error:
            QtWidgets.QMessageBox.about(self, 'Ошибка!', "Проблема с базой данных принимаемых прераратов")
        
        
        self.ui.listWidget_2.clear()
        for element in list_pr:
            self.text = f"                                                     Название: {element[2]}\n   С {element[0]} по {element[1]}\n   Дополнительно: {element[2]}\n"
            self.ui.listWidget_2.addItem(self.text)

        con.commit()
        cur.close()
        con.close()



    def list_analiz(self):
        self.ui.stackedWidget.setCurrentIndex(3) 
        try:
            con = sqlite3.connect('users.db')
            cur = con.cursor()
            
            list_pr = cur.execute(f"""SELECT * FROM analiz_users WHERE id = {self.id}""")

        except sqlite3.Error as error:
            QtWidgets.QMessageBox.about(self, 'Ошибка!', "Проблема с базой данных анализов")
        
        
        self.ui.listWidget_3.clear()
        self.lst_names = []
        for element in list_pr:
            self.text = f"  Название: {element[0]}   Дата: {element[1]}\n"
            self.lst_names.append(element[1][:2] + element[1][3:5] + element[1][6:]+ element[0])
            self.ui.listWidget_3.addItem(self.text)

        self.ui.listWidget_3.itemDoubleClicked.connect(self.showpic)

        con.commit()
        cur.close()
        con.close() 

    def showpic(self):

        self.image = "image/" + self.lst_names[self.ui.listWidget_3.currentRow()]
        print(self.image)

        self.window = QtWidgets.QLabel()
        self.window.setPixmap(QtGui.QPixmap(self.image))
        self.window.resize(800, 800)
        self.window.show()
        self.window.activateWindow()
     


    def show_pos_form(self):
        self.pos_form = AddPos(self.id)
        self.pos_form.show()

    def show_analiz_form(self):
        self.an_form = AddAnaliz(self.id)
        self.an_form.show()
    
    def show_prep_form(self):
        self.prep_form = AddPrep(self.id)
        self.prep_form.show()
    
    def delit_pos(self):
        self.msgBox = QtWidgets.QMessageBox()
        self.msgBox.setText("Вы действительно хотите безвозвратно удалить эту запись?")
        self.msgBox.addButton("Отмена",  QtWidgets.QMessageBox.NoRole)
        self.msgBox.addButton("да",  QtWidgets.QMessageBox.YesRole)

        self.listItems=self.ui.listWidget.selectedItems()
        if not self.listItems: return        
        for item in self.listItems:
            if self.msgBox.exec_() == 1:
                listItems=self.ui.listWidget.selectedItems()
                if not listItems: return        
                for item in listItems:
                    self.ui.listWidget.takeItem(self.ui.listWidget.row(item))
        try:
            con = sqlite3.connect('users.db')
            cur = con.cursor()
            
            #for item in self.listItems:
                #cur.execute(f"""UPDATE pos_users SET idTable = '{self.ui.listWidget.row(item)}' WHERE id = {item[3]} AND date = {item[0]} AND name_doc = {item[1]} and text = {item[2]}""")

        except sqlite3.Error as error:
            QtWidgets.QMessageBox.about(self, 'Ошибка!', "Проблема с базой данных посещений")

        con.commit()
        cur.close()
        con.close()
    
        


class AddPos(QtWidgets.QWidget):
    def __init__(self, arg):
        super().__init__()
        self.ui = pos_form.Ui_Form()
        self.ui.setupUi(self)
        self.initUI()
        self.id = arg
    
    def initUI(self):
        self.setWindowTitle("Immuno")
        self.setWindowIcon(QIcon("probirka.png"))

        self.ui.add_pos.clicked.connect(self.list_pos)
    
    def list_pos(self):
        date = "{}".format(self.ui.dateEdit.dateTime().toString('dd-MM-yyyy'))
        spec = self.ui.comboBox.currentText()
        txt = self.ui.textEdit.toPlainText()

        try:
            con = sqlite3.connect('users.db')
            cur = con.cursor()

            cur.execute(f"""INSERT INTO pos_users (date, name_doc, text, id) VALUES ('{date}', '{spec}', '{txt}', '{self.id}')""")
            
            con.commit()
            cur.close()
            con.close()
            self.close()
        except sqlite3.Error as error:
            QtWidgets.QMessageBox.about(self, 'Ошибка!', "Проблема с базой данных посещений")


class AddAnaliz(QtWidgets.QWidget):
    def __init__(self, arg):
        super().__init__()
        self.ui = analiz_form.Ui_Form()
        self.ui.setupUi(self)
        self.initUI()
        self.id = arg
    
    def initUI(self):
        self.setWindowTitle("Immuno")
        self.setWindowIcon(QIcon("probirka.png"))

        self.ui.add_zapis.clicked.connect(self.list_analiz)
        self.ui.add_file.clicked.connect(self.photo)

    def list_analiz(self):
        date_sd = "{}".format(self.ui.dateEdit.dateTime().toString('dd-MM-yyyy'))
        name_photo = self.ui.lineEdit.text() + ".png"
        try:
            con = sqlite3.connect('users.db')
            cur = con.cursor()

            cur.execute(f"""INSERT INTO analiz_users (name_an, date, id) VALUES ('{name_photo}', '{date_sd}', '{self.id}')""")

            con.commit()
            cur.close()
            con.close()
            self.close()
        except sqlite3.Error as error:
            QtWidgets.QMessageBox.about(self, 'Ошибка!', "Проблема с базой данных принимаемых прераратов")

#Сохранение фото в отдельную папку
    def photo(self):
        if self.ui.lineEdit.text() == '':
            QtWidgets.QMessageBox.about(self, 'Ошибка!', "Введите название анализа")
        else:
            self.imagePath = ''

            self.imagePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Выбрать фото", "", 
                                   "Image Files (*.png )")

            if self.imagePath:
                destination_path = "image/" + "{}".format(self.ui.dateEdit.dateTime().toString('ddMMyyyy')) + self.ui.lineEdit.text() + ".png"
                shutil.move(self.imagePath, destination_path)
                QtWidgets.QMessageBox.about(self, 'Успешно', "Файл добавлен")

        

class AddPrep(QtWidgets.QWidget):
    def __init__(self, arg):
        super().__init__()
        self.ui = preparat.Ui_Form()
        self.ui.setupUi(self)
        self.initUI()
        self.id = arg
    
    def initUI(self):
        self.setWindowTitle("Immuno")
        self.setWindowIcon(QIcon("probirka.png"))

        self.ui.add_prep.clicked.connect(self.list_prep)
    
    def list_prep(self):
        name_prep = self.ui.lineEdit.text()
        date1 = "{}".format(self.ui.dateEdit.dateTime().toString('dd-MM-yyyy'))
        date2 = "{}".format(self.ui.dateEdit.dateTime().toString('dd-MM-yyyy'))
        txt = self.ui.textEdit.toPlainText()
    
        try:
            con = sqlite3.connect('users.db')
            cur = con.cursor()

            cur.execute(f"""INSERT INTO prepar_users (date_start, date_end, name, text, id) VALUES ('{date1}', '{date2}', '{name_prep}', '{txt}', '{self.id}')""")

            con.commit()
            cur.close()
            con.close()
            self.close()
        except sqlite3.Error as error:
            QtWidgets.QMessageBox.about(self, 'Ошибка!', "Проблема с базой данных принимаемых прераратов")


if __name__ == '__main__':      
  app = QtWidgets.QApplication(sys.argv)
  application = Registration()
  application.show()

  sys.exit(app.exec())
