# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'foodshow2.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from PyQt5.QtWidgets import QGraphicsScene ,QMessageBox
from PyQt5.QtGui import QPixmap
import string
import mysql.connector
bar_buttom = 1
len_food = 1
a = []
cal_total = []
table_count = 0.0
cal_limit = 2000.0
cal_sum = 0
class MyConverter(mysql.connector.conversion.MySQLConverter):

    def row_to_python(self, row, fields):
        row = super(MyConverter, self).row_to_python(row, fields)

        def to_unicode(col):
            if type(col) == bytearray:
                return col.decode('utf-8')
            return col

        return[to_unicode(col) for col in row]

class Ui_Dialog(QMessageBox):
    def picShow(self,number):
        self.pic = QGraphicsScene()
        self.pic.addPixmap(QPixmap('food_pic/'+str(number)+'.jpg'))
        return self.pic
    def messengerSelect1(self):
        _translate = QtCore.QCoreApplication.translate
        global a,table_count,cal_sum
        selectBut = QtWidgets.QMessageBox.question(self ,"Select Food","Do you choose this food?",QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        if selectBut == QtWidgets.QMessageBox.Yes:
            if ((cal_sum + cal_total[0+((bar_buttom-1)*4)])>cal_limit):
                QtWidgets.QMessageBox.warning(self,"Calories Alert","Overweight calories",QtWidgets.QMessageBox.Cancel)
            elif (table_count == 10):
                QtWidgets.QMessageBox.warning(self,"Food list Alert","Overflow Food",QtWidgets.QMessageBox.Cancel)
            else:
                self.tableWidget.setItem(table_count,0,QtWidgets.QTableWidgetItem(a[0+((bar_buttom-1)*4)]))
                self.tableWidget.setItem(table_count,1,QtWidgets.QTableWidgetItem(str(cal_total[0+((bar_buttom-1)*4)])))
                cal_sum = cal_sum + cal_total[0+((bar_buttom-1)*4)]
                self.CalTotal.setText(_translate("Dialog", str(cal_sum)))
                table_count += 1
        else:
            pass
    def messengerSelect2(self):
        _translate = QtCore.QCoreApplication.translate
        global a,table_count,cal_sum
        selectBut = QtWidgets.QMessageBox.question(self ,"Select Food","Do you choose this food?",QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        if selectBut == QtWidgets.QMessageBox.Yes:
            if ((cal_sum + cal_total[1+((bar_buttom-1)*4)])>cal_limit):
                QtWidgets.QMessageBox.warning(self,"Calories Alert","Over-nutrition",QtWidgets.QMessageBox.Cancel)
            elif (table_count == 10):
                QtWidgets.QMessageBox.warning(self,"Food list Alert","Shouldn't choose this food",QtWidgets.QMessageBox.Cancel)
            else:
                self.tableWidget.setItem(table_count,0,QtWidgets.QTableWidgetItem(a[1+((bar_buttom-1)*4)]))
                self.tableWidget.setItem(table_count,1,QtWidgets.QTableWidgetItem(str(cal_total[1+((bar_buttom-1)*4)])))
                cal_sum = cal_sum + cal_total[1+((bar_buttom-1)*4)]
                self.CalTotal.setText(_translate("Dialog", str(cal_sum)))
                table_count += 1
        else:
            pass
    def messengerSelect3(self):
        _translate = QtCore.QCoreApplication.translate
        global a,table_count,cal_sum
        selectBut = QtWidgets.QMessageBox.question(self ,"Select Food","Do you choose this food?",QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        if selectBut == QtWidgets.QMessageBox.Yes:
            if ((cal_sum + cal_total[2+((bar_buttom-1)*4)])>cal_limit):
                QtWidgets.QMessageBox.warning(self,"Calories Alert","Overweight calories",QtWidgets.QMessageBox.Cancel)
            elif (table_count == 10):
                QtWidgets.QMessageBox.warning(self,"Food list Alert","Overflow Food",QtWidgets.QMessageBox.Cancel)
            else:
                self.tableWidget.setItem(table_count,0,QtWidgets.QTableWidgetItem(a[2+((bar_buttom-1)*4)]))
                self.tableWidget.setItem(table_count,1,QtWidgets.QTableWidgetItem(str(cal_total[2+((bar_buttom-1)*4)])))
                cal_sum = cal_sum + cal_total[2+((bar_buttom-1)*4)]
                self.CalTotal.setText(_translate("Dialog", str(cal_sum)))
                table_count += 1
        else:
            pass
    def messengerSelect4(self):
        _translate = QtCore.QCoreApplication.translate
        global a,table_count,cal_sum
        selectBut = QtWidgets.QMessageBox.question(self ,"Select Food","Do you choose this food?",QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        if selectBut == QtWidgets.QMessageBox.Yes:
            if ((cal_sum + cal_total[3+((bar_buttom-1)*4)])>cal_limit):
                QtWidgets.QMessageBox.warning(self,"Calories Alert","Overweight calories",QtWidgets.QMessageBox.Cancel)
            elif (table_count == 10):
                QtWidgets.QMessageBox.warning(self,"Food list Alert","Overflow Food",QtWidgets.QMessageBox.Cancel)
            else:
                self.tableWidget.setItem(table_count,0,QtWidgets.QTableWidgetItem(a[3+((bar_buttom-1)*4)]))
                self.tableWidget.setItem(table_count,1,QtWidgets.QTableWidgetItem(str(cal_total[3+((bar_buttom-1)*4)])))
                cal_sum = cal_sum + cal_total[3+((bar_buttom-1)*4)]
                self.CalTotal.setText(_translate("Dialog", str(cal_sum)))
                table_count += 1
        else:
            pass
    def checkLen(self):
        global len_food
        mydb = mysql.connector.connect(
            converter_class=MyConverter,
            host="localhost",
            user="root",
            passwd="1234",
            database="project4c",
            port = 3306
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT food_name FROM food")
        myresult = mycursor.fetchall()
        a = []
        for food in myresult:
            for fooddetail in food:
                a.append(fooddetail)
        mydb.close()
        len_food = int((len(a)) / 4)
        if ((int(len(a)) % 4) != 0):
            len_food += 1
        
    def calTolist(self):
        global cal_total
        mydb = mysql.connector.connect(
            converter_class=MyConverter,
            host="34.80.120.194",
            user="root",
            passwd="@Stang1996",
            database="project4c",
            port = 3306
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT cal FROM food ORDER BY food_id ASC")
        myresult = mycursor.fetchall()
        for cal in myresult:
            for caldetail in cal:
                cal_total.append(caldetail)         
    def BackBut(self):
        _translate = QtCore.QCoreApplication.translate
        global bar_buttom,a
        if (bar_buttom > 1):
            bar_buttom -= 1
            self.food_1.setText(_translate("Dialog", a[0+((bar_buttom-1)*4)]))
            self.food_2.setText(_translate("Dialog", a[1+((bar_buttom-1)*4)]))
            self.food_3.setText(_translate("Dialog", a[2+((bar_buttom-1)*4)]))
            self.food_4.setText(_translate("Dialog", a[3+((bar_buttom-1)*4)]))
            self.graphicsView.setScene(self.picShow(1+(bar_buttom-1)*4))
            self.graphicsView_2.setScene(self.picShow(2+(bar_buttom-1)*4))
            self.graphicsView_3.setScene(self.picShow(3+(bar_buttom-1)*4))
            self.graphicsView_4.setScene(self.picShow(4+(bar_buttom-1)*4))
    def NextBut(self):
        _translate = QtCore.QCoreApplication.translate
        global bar_buttom,len_food,a
        self.checkLen()
        if (bar_buttom < len_food):
            bar_buttom += 1
            self.food_1.setText(_translate("Dialog", a[0+((bar_buttom-1)*4)]))
            self.food_2.setText(_translate("Dialog", "x "+a[1+((bar_buttom-1)*4)]))
            self.food_3.setText(_translate("Dialog", a[2+((bar_buttom-1)*4)]))
            self.food_4.setText(_translate("Dialog", a[3+((bar_buttom-1)*4)]))
            self.graphicsView.setScene(self.picShow(1+(bar_buttom-1)*4))
            self.graphicsView_2.setScene(self.picShow(2+(bar_buttom-1)*4))
            self.graphicsView_3.setScene(self.picShow(3+(bar_buttom-1)*4))
            self.graphicsView_4.setScene(self.picShow(4+(bar_buttom-1)*4))
    def databaseText(self):
        _translate = QtCore.QCoreApplication.translate
        global bar_buttom,cal_sum
        mydb = mysql.connector.connect(
            converter_class=MyConverter,
            host="34.80.120.194",
            user="root",
            passwd="@Stang1996",
            database="project4c",
            port = 3306
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT food_name FROM food")
        myresult = mycursor.fetchall()
        global a
        for food in myresult:
            for fooddetail in food:
                a.append(fooddetail)
        mydb.close()
        self.calTolist()
        self.food_1.setText(_translate("Dialog", a[0]))
        self.food_2.setText(_translate("Dialog", a[1]))
        self.food_3.setText(_translate("Dialog", a[2]))
        self.food_4.setText(_translate("Dialog", a[3]))
        self.CalTotal.setText(_translate("Dialog", str(cal_sum)))
        self.graphicsView.setScene(self.picShow(1))
        self.graphicsView_2.setScene(self.picShow(2))
        self.graphicsView_3.setScene(self.picShow(3))
        self.graphicsView_4.setScene(self.picShow(4))
    def clearBut(self):
        _translate = QtCore.QCoreApplication.translate
        global cal_sum,table_count
        yonBut = QtWidgets.QMessageBox.warning(self ,"Select Food","Do you choose this food?",QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        if yonBut  == QtWidgets.QMessageBox.Yes :
            cal_sum = 0.0
            i = 0
            for i in range(int(table_count)):  
                self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem())
            table_count = 0 
            self.CalTotal.setText(_translate("Dialog", str(cal_sum)))       
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(806, 675)
        self.label_welcome = QtWidgets.QLabel(Dialog)
        self.label_welcome.setGeometry(QtCore.QRect(56, 20, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_welcome.setFont(font)
        self.label_welcome.setObjectName("label_welcome")
        self.user_name = QtWidgets.QLabel(Dialog)
        self.user_name.setGeometry(QtCore.QRect(220, 20, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.user_name.setFont(font)
        self.user_name.setObjectName("user_name")
        self.label_select = QtWidgets.QLabel(Dialog)
        self.label_select.setGeometry(QtCore.QRect(60, 80, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_select.setFont(font)
        self.label_select.setObjectName("label_select")
        self.backButton = QtWidgets.QPushButton(Dialog)
        self.backButton.setGeometry(QtCore.QRect(30, 630, 89, 25))
        self.backButton.setObjectName("backButton")
        self.backButton.clicked.connect(self.BackBut)
        self.nextButton = QtWidgets.QPushButton(Dialog)
        self.nextButton.setGeometry(QtCore.QRect(430, 630, 89, 25))
        self.nextButton.setObjectName("nextButton")
        self.nextButton.clicked.connect(self.NextBut)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(20, 130, 241, 171))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(280, 130, 241, 171))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.select_1 = QtWidgets.QPushButton(Dialog)
        self.select_1.setGeometry(QtCore.QRect(100, 340, 89, 25))
        self.select_1.setObjectName("select_1")
        self.graphicsView_3 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_3.setGeometry(QtCore.QRect(20, 380, 241, 171))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView_4 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_4.setGeometry(QtCore.QRect(280, 380, 241, 171))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.select_2 = QtWidgets.QPushButton(Dialog)
        self.select_2.setGeometry(QtCore.QRect(360, 340, 89, 25))
        self.select_2.setObjectName("select_2")
        self.select_3 = QtWidgets.QPushButton(Dialog)
        self.select_3.setGeometry(QtCore.QRect(100, 590, 89, 25))
        self.select_3.setObjectName("select_3")
        self.select_4 = QtWidgets.QPushButton(Dialog)
        self.select_4.setGeometry(QtCore.QRect(360, 590, 89, 25))
        self.select_4.setObjectName("select_4")
        self.select_1.clicked.connect(self.messengerSelect1)
        self.select_2.clicked.connect(self.messengerSelect2)
        self.select_3.clicked.connect(self.messengerSelect3)
        self.select_4.clicked.connect(self.messengerSelect4)
        self.food_1 = QtWidgets.QLabel(Dialog)
        self.food_1.setGeometry(QtCore.QRect(30, 310, 221, 20))
        self.food_1.setObjectName("food_1")
        self.food_3 = QtWidgets.QLabel(Dialog)
        self.food_3.setGeometry(QtCore.QRect(40, 560, 221, 20))
        self.food_3.setObjectName("food_3")
        self.food_2 = QtWidgets.QLabel(Dialog)
        self.food_2.setGeometry(QtCore.QRect(300, 310, 221, 20))
        self.food_2.setObjectName("food_2")
        self.food_4 = QtWidgets.QLabel(Dialog)
        self.food_4.setGeometry(QtCore.QRect(300, 560, 221, 20))
        self.food_4.setObjectName("food_4")
        self.confirmButton = QtWidgets.QPushButton(Dialog)
        self.confirmButton.setGeometry(QtCore.QRect(540, 570, 89, 61))
        self.confirmButton.setObjectName("confirmButton")
        self.clearButtom = QtWidgets.QPushButton(Dialog)
        self.clearButtom.setGeometry(QtCore.QRect(700, 570, 89, 61))
        self.clearButtom.setObjectName("clearButtom")
        self.clearButtom.clicked.connect(self.clearBut)
        self.label_welcome_2 = QtWidgets.QLabel(Dialog)
        self.label_welcome_2.setGeometry(QtCore.QRect(540, 490, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_welcome_2.setFont(font)
        self.label_welcome_2.setObjectName("label_welcome_2")
        self.label_welcome_3 = QtWidgets.QLabel(Dialog)
        self.label_welcome_3.setGeometry(QtCore.QRect(710, 490, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_welcome_3.setFont(font)
        self.label_welcome_3.setObjectName("label_welcome_3")
        self.CalTotal = QtWidgets.QLabel(Dialog)
        self.CalTotal.setGeometry(QtCore.QRect(620, 490, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.CalTotal.setFont(font)
        self.CalTotal.setObjectName("CalTotal")
        self.label_welcome_5 = QtWidgets.QLabel(Dialog)
        self.label_welcome_5.setGeometry(QtCore.QRect(530, 40, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_welcome_5.setFont(font)
        self.label_welcome_5.setObjectName("label_welcome_5")
        self.Cal_Limit = QtWidgets.QLabel(Dialog)
        self.Cal_Limit.setGeometry(QtCore.QRect(640, 40, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Cal_Limit.setFont(font)
        self.Cal_Limit.setObjectName("Cal_Limit")
        self.label_welcome_7 = QtWidgets.QLabel(Dialog)
        self.label_welcome_7.setGeometry(QtCore.QRect(730, 40, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_welcome_7.setFont(font)
        self.label_welcome_7.setObjectName("label_welcome_7")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(540, 140, 241, 351))
        self.tableWidget.setMaximumSize(QtCore.QSize(241, 351))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.databaseText()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        global cal_limit
        _translate = QtCore.QCoreApplication.translate
        self.nextButton.setText(_translate("Dialog", "Next >"))
        self.label_welcome.setText(_translate("Dialog", "Welcome! "))
        self.label_select.setText(_translate("Dialog", "What would you like to order please? "))
        self.backButton.setText(_translate("Dialog", "< Back"))
        self.select_1.setText(_translate("Dialog", "Select"))
        self.select_2.setText(_translate("Dialog", "Select"))
        self.select_3.setText(_translate("Dialog", "Select"))
        self.select_4.setText(_translate("Dialog", "Select"))
        self.confirmButton.setText(_translate("Dialog", "Confirm(s)"))
        self.clearButtom.setText(_translate("Dialog", "Clear"))
        self.label_welcome_2.setText(_translate("Dialog", "Total :"))
        self.label_welcome_3.setText(_translate("Dialog", "kCal"))
        self.label_welcome_5.setText(_translate("Dialog", "Cal Limit :"))
        self.Cal_Limit.setText(_translate("Dialog", str(cal_limit)))
        self.label_welcome_7.setText(_translate("Dialog", "kCal"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Food"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Calorie(s)"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
