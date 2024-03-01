from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import MySQLdb

from PyQt5.uic import loadUiType

ui,_ = loadUiType('library.ui')
 
class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI_Changes()

    
    def Handle_UI_Changes(self):
        self.Handle_Buttons()

    
    def Handle_Buttons(self):
        self.Hide_Themes()
        self.tabWidget.tabBar().setVisible(False) #thanks to this line we can hide the tabbar of bigger tab widget
        self.pushButton_21.clicked.connect(self.Hide_Themes)
        self.pushButton_4.clicked.connect(self.Show_Themes)
        
        self.pushButton.clicked.connect(self.Calender_Tab)
        self.pushButton_3.clicked.connect(self.Books_Tab)
        self.pushButton_2.clicked.connect(self.Users_Tab)
        self.pushButton_5.clicked.connect(self.Settings_Tab)

        self.pushButton_7.clicked.connect(self.Add_New_Book)

        self.pushButton_14.clicked.connect(self.Add_Category)

    def Show_Themes(self):
        self.groupBox_3.show()
    def Hide_Themes(self):
        self.groupBox_3.hide()


    def Calender_Tab(self):
        self.tabWidget.setCurrentIndex(0)
    def Books_Tab(self):
        self.tabWidget.setCurrentIndex(1)
    def Users_Tab(self):
        self.tabWidget.setCurrentIndex(2)
    def Settings_Tab(self):
        self.tabWidget.setCurrentIndex(3)



    def Add_New_Book(self):
        self.database = MySQLdb.connect(host='localhost', user='root' , password='123456528' , database='library') #connect the database
        self.cur = self.database.cursor()

        book_title = self.lineEdit_2.text()
        book_code = self.lineEdit_4.text()
        book_category = self.comboBox_3.CurrentText()
        book_author = self.comboBox_4.CurrentText()
        book_publisher = self.comboBox_5.CurrentText()
        book_price = self.lineEdit_5.text()
        

    def Search_Books(self):
        pass
    def Edit_Books(self):
        pass
    def Delete_Books(self):
        pass



    def Add_New_User(self):
        pass
    def Login(self):
        pass
    def Edit_User(self):
        pass


    def Add_Category(self):
        self.database = MySQLdb.connect(host='localhost', user='root' , password='123456528' , database='library') #connect the database
        self.cur = self.database.cursor()

        category_name = self.lineEdit_21.text()

        self.cur.execute('''
            INSERT INTO category (category_name) VALUES (%s)
        ''' , (category_name, )) #we should put a comma after category_name

        #I have taken an error right here, which is about idcategory's auto increment
        #I solved the problem thanks to this line:
        #ALTER TABLE users ADD id int NOT NULL AUTO_INCREMENT primary key

        self.database.commit()
        print('new category has added')


    def Add_Author(self):
        pass

    def Add_Publisher(self):
        pass
 
def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()        