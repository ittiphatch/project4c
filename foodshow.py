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
type_user = 0
nes_user = []
table_count = 0
cal_limit = 0.0
cal_sum = 0.0
Na_sum = 0.0
fat_sum = 0.0
sw_sum = 0.0
chol_sum = 0.0
Na_total=[]
fat_total= [] 
sw_total= [] 
chol_total = []
type_total = []
list_send = ["","","","","","","","","",""]
id_number = 0

class MyConverter(mysql.connector.conversion.MySQLConverter):

    def row_to_python(self, row, fields):
        row = super(MyConverter, self).row_to_python(row, fields)

        def to_unicode(col):
            if type(col) == bytearray:
                return col.decode('utf-8')
            return col

        return[to_unicode(col) for col in row]

class Ui_Dialog(QMessageBox):
    def TypecompOther(self,type_id): 
        global type_user,type_total
        if (type_user == 0)|(type_total[type_id]==0):
            return False
        else:
            if (type_total[type_id] > type_user):
                if (type_total[type_id] % type_user == 0):
                    return True
                else:
                    return False
            else: 
                if (type_user % type_total[type_id] == 0):
                    return True
                else:
                    return False     
    def picShow(self,number):
        self.pic = QGraphicsScene()
        self.pic.addPixmap(QPixmap('food_pic/'+str(number)+'.jpg'))
        return self.pic
    def UsertoData(self,name):
        global cal_limit,type_user,nes_user,id_number
        mydb = mysql.connector.connect(
            converter_class=MyConverter,
            host="34.80.120.194",
            user="root",
            passwd="@Stang1996",
            database="project4c",
            port = 3306
        )                               
        mycursor = mydb.cursor()

        sql = "SELECT ID FROM users WHERE username = %s"
        adr = (name ,)

        mycursor.execute(sql, adr)

        myresult = mycursor.fetchall()
        for USER in myresult:
            for IDdetail in USER:
                id = IDdetail
        print(id)
        id_number = id
        mycursor.close()
        mycursor = mydb.cursor()
        sql2 = "SELECT type FROM user_data WHERE id = %s"
        adr2 = (id ,)
        mycursor.execute(sql2,adr2)
        myresult = mycursor.fetchall()
        for tyot in myresult:
            for type_detail in tyot:
                if type_detail == None:
                    type_detail = 0
                type_user = type_detail
        mycursor.close()
        mycursor = mydb.cursor()
        sql3 = "SELECT cal,sodium,fat,sugar,cloresterol FROM user_data WHERE id = %s"
        adr3 = (id ,)
        mycursor.execute(sql3,adr3)
        myresult = mycursor.fetchall()
        mydb.close
        for nes in myresult:
            for nesdetail in nes:
                nes_user.append(nesdetail)
        cal_limit = nes_user[0]
    def checkMark(self,type_id):
        if(self.TypecompOther(type_id)==True):
            return "x"
        else:
            return ""           
    def messengerSelect1(self):
        _translate = QtCore.QCoreApplication.translate
        global a,table_count,cal_sum,Na_sum,fat_sum,sw_sum,chol_sum,list_send
        type_Logic = self.TypecompOther(0+((bar_buttom-1)*4))
        selectBut = QtWidgets.QMessageBox.question(self ,"Select Food","Do you choose this food?",QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        if selectBut == QtWidgets.QMessageBox.Yes:
            if (table_count == 10):
                QtWidgets.QMessageBox.warning(self,"Food list Alert","Too many food",QtWidgets.QMessageBox.Cancel)
            elif (type_Logic==True):
                QtWidgets.QMessageBox.warning(self,"Food Alert","Shoudn't choose this food",QtWidgets.QMessageBox.Cancel)
            elif ((cal_sum + cal_total[0+((bar_buttom-1)*4)])>cal_limit):
                QtWidgets.QMessageBox.warning(self,"Calories Alert","Too much calories",QtWidgets.QMessageBox.Cancel)
            elif ((Na_sum + Na_total[0+((bar_buttom-1)*4)])>nes_user[1]):
                QtWidgets.QMessageBox.warning(self,"Nutrition Alert","Too much Sodium",QtWidgets.QMessageBox.Cancel)
            elif ((fat_sum + fat_total[0+((bar_buttom-1)*4)])>nes_user[2]):
                QtWidgets.QMessageBox.warning(self,"Nutrition Alert","Too much fat",QtWidgets.QMessageBox.Cancel)
            elif ((sw_sum + sw_total[0+((bar_buttom-1)*4)])>nes_user[3]):
                QtWidgets.QMessageBox.warning(self,"Nutrition Alert","Too much sugar",QtWidgets.QMessageBox.Cancel)
            elif ((chol_sum + chol_total[0+((bar_buttom-1)*4)])>nes_user[4]):
                QtWidgets.QMessageBox.warning(self,"Nutrition Alert","Too much Cholesterol",QtWidgets.QMessageBox.Cancel)
            else:
                list_send[table_count]=(a[0+((bar_buttom-1)*4)])
                self.tableWidget.setItem(table_count,0,QtWidgets.QTableWidgetItem(a[0+((bar_buttom-1)*4)]))
                self.tableWidget.setItem(table_count,1,QtWidgets.QTableWidgetItem(str(cal_total[0+((bar_buttom-1)*4)])))
                cal_sum = cal_sum + cal_total[0+((bar_buttom-1)*4)]
                Na_sum = Na_sum + Na_total[0+((bar_buttom-1)*4)]
                fat_sum = fat_sum + fat_total[0+((bar_buttom-1)*4)]
                chol_sum = chol_sum + chol_total[0+((bar_buttom-1)*4)]
                sw_sum = sw_sum + sw_total[0+((bar_buttom-1)*4)]
                self.CalTotal.setText(_translate("Dialog", str(cal_sum)))
                table_count += 1
        else:
            pass
    def messengerSelect2(self):
        _translate = QtCore.QCoreApplication.translate
        global a,table_count,cal_sum,Na_sum,fat_sum,sw_sum,chol_sum,list_send
        type_Logic = self.TypecompOther(1+((bar_buttom-1)*4))
        selectBut = QtWidgets.QMessageBox.question(self ,"Select Food","Do you choose this food?",QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)        
        if selectBut == QtWidgets.QMessageBox.Yes:
            if (table_count == 10):
                QtWidgets.QMessageBox.warning(self,"Food list Alert","Too many food",QtWidgets.QMessageBox.Cancel)
            elif (type_Logic==True):
                QtWidgets.QMessageBox.warning(self,"Food Alert","Shoudn't choose this food",QtWidgets.QMessageBox.Cancel)
            elif ((cal_sum + cal_total[1+((bar_buttom-1)*4)])>cal_limit):
                QtWidgets.QMessageBox.warning(self,"Calories Alert","Too much calories",QtWidgets.QMessageBox.Cancel)
            elif ((Na_sum + Na_total[1+((bar_buttom-1)*4)])>nes_user[1]):
                QtWidgets.QMessageBox.warning(self,"Nutrition Alert","Too much Sodium",QtWidgets.QMessageBox.Cancel)
            elif ((fat_sum + fat_total[1+((bar_buttom-1)*4)])>nes_user[2]):
                QtWidgets.QMessageBox.warning(self,"Nutrition Alert","Too much fat",QtWidgets.QMessageBox.Cancel)
            elif ((sw_sum + sw_total[1+((bar_buttom-1)*4)])>nes_user[3]):
                QtWidgets.QMessageBox.warning(self,"Nutrition Alert","Too much sugar",QtWidgets.QMessageBox.Cancel)
            elif ((chol_sum + chol_total[1+((bar_buttom-1)*4)])>nes_user[4]):
                QtWidgets.QMessageBox.warning(self,"Nutrition Alert","Too much Cholesterol",QtWidgets.QMessageBox.Cancel)
            else:
                list_send[table_count]=(a[1+((bar_buttom-1)*4)])
                self.tableWidget.setItem(table_count,0,QtWidgets.QTableWidgetItem(a[1+((bar_buttom-1)*4)]))
                self.tableWidget.setItem(table_count,1,QtWidgets.QTableWidgetItem(str(cal_total[1+((bar_buttom-1)*4)])))
                cal_sum = cal_sum + cal_total[1+((bar_buttom-1)*4)]
                Na_sum = Na_sum + Na_total[1+((bar_buttom-1)*4)]
                fat_sum = fat_sum + fat_total[1+((bar_buttom-1)*4)]
                chol_sum = chol_sum + chol_total[1+((bar_buttom-1)*4)]
                sw_sum = sw_sum + sw_total[1+((bar_buttom-1)*4)]
                self.CalTotal.setText(_translate("Dialog", str(cal_sum)))
                table_count += 1
        else:
            pass
    def messengerSelect3(self):
        _translate = QtCore.QCoreApplication.translate
        global a,table_count,cal_sum,Na_sum,fat_sum,sw_sum,chol_sum,list_send
        type_Logic = self.TypecompOther(2+((bar_buttom-1)*4))
        selectBut = QtWidgets.QMessageBox.question(self ,"Select Food","Do you choose this food?",QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        if selectBut == QtWidgets.QMessageBox.Yes:
            if (table_count == 10):
                QtWidgets.QMessageBox.warning(self,"Food list Alert","Too many food",QtWidgets.QMessageBox.Cancel)
                pass
            elif (type_Logic==True):
                QtWidgets.QMessageBox.warning(self,"Food Alert","Shoudn't choose this food",QtWidgets.QMessageBox.Cancel)
                pass
            elif ((cal_sum + cal_total[2+((bar_buttom-1)*4)])>cal_limit):
                QtWidgets.QMessageBox.warning(self,"Nutrition Alert","Too much calories",QtWidgets.QMessageBox.Cancel)
            elif ((Na_sum + Na_total[2+((bar_buttom-1)*4)])>nes_user[1]):
                QtWidgets.QMessageWarming(self,"Nutrition Alert","Too much Sodium",QtWidgets.QMessageBox.Cancel)
            elif ((fat_sum + fat_total[2+((bar_buttom-1)*4)])>nes_user[2]):
                QtWidgets.QMessageBox.warning(self,"Nutrition Alert","Too much fat",QtWidgets.QMessageBox.Cancel)
            elif ((sw_sum + sw_total[2+((bar_buttom-1)*4)])>nes_user[3]):
                QtWidgets.QMessageBox.warning(self,"Nutrition Alert","Too much sugar",QtWidgets.QMessageBox.Cancel)
            elif ((chol_sum + chol_total[2+((bar_buttom-1)*4)])>nes_user[4]):
                QtWidgets.QMessageBox.warning(self,"Nutrition Alert","Too much Cholesterol",QtWidgets.QMessageBox.Cancel)
            else:
                list_send[table_count]=(a[2+((bar_buttom-1)*4)])
                self.tableWidget.setItem(table_count,0,QtWidgets.QTableWidgetItem(a[2+((bar_buttom-1)*4)]))
                self.tableWidget.setItem(table_count,1,QtWidgets.QTableWidgetItem(str(cal_total[2+((bar_buttom-1)*4)])))
                cal_sum = cal_sum + cal_total[2+((bar_buttom-1)*4)]
                Na_sum = Na_sum + Na_total[2+((bar_buttom-1)*4)]
                fat_sum = fat_sum + fat_total[2+((bar_buttom-1)*4)]
                chol_sum = chol_sum + chol_total[2+((bar_buttom-1)*4)]
                sw_sum = sw_sum + sw_total[2+((bar_buttom-1)*4)]
                self.CalTotal.setText(_translate("Dialog", str(cal_sum)))
                table_count += 1
        else:
            pass        
    def messengerSelect4(self):
        _translate = QtCore.QCoreApplication.translate
        global a,table_count,cal_sum,Na_sum,fat_sum,sw_sum,chol_sum,list_send
        type_Logic = self.TypecompOther(3+((bar_buttom-1)*4))
        selectBut = QtWidgets.QMessageBox.question(self ,"Select Food","Do you choose this food?",QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        if selectBut == QtWidgets.QMessageBox.Yes:
            if (table_count == 10):
                QtWidgets.QMessageBox.warning(self,"Food list Alert","Too many food",QtWidgets.QMessageBox.Cancel)
            elif ((cal_sum + cal_total[3+((bar_buttom-1)*4)])>cal_limit):
                QtWidgets.QMessageBox.warning(self,"Calories Alert","ํToo much calories",QtWidgets.QMessageBox.Cancel)
            elif (type_Logic==True):
                QtWidgets.QMessageBox.warning(self,"Food Alert","Shoudn't choose this food",QtWidgets.QMessageBox.Cancel)
            elif ((Na_sum + Na_total[3+((bar_buttom-1)*4)])>nes_user[1]):
                QtWidgets.QMessageBox.warning(self,"Nutrition Alert","Too much Sodium",QtWidgets.QMessageBox.Cancel)
            elif ((fat_sum + fat_total[3+((bar_buttom-1)*4)])>nes_user[2]):
                QtWidgets.QMessageBox.warning(self,"Nutrition Alert","Too much fat",QtWidgets.QMessageBox.Cancel)
            elif ((sw_sum + sw_total[3+((bar_buttom-1)*4)])>nes_user[3]):
                QtWidgets.QMessageBox.warning(self,"Nutrition Alert","Too much sugar",QtWidgets.QMessageBox.Cancel)
            elif ((chol_sum + chol_total[3+((bar_buttom-1)*4)])>nes_user[4]):
                QtWidgets.QMessageBox.warning(self,"Nutrition Alert","Too much Cholesterol",QtWidgets.QMessageBox.Cancel)
            else:
                list_send[table_count]=(a[3+((bar_buttom-1)*4)])
                self.tableWidget.setItem(table_count,0,QtWidgets.QTableWidgetItem(a[3+((bar_buttom-1)*4)]))
                self.tableWidget.setItem(table_count,1,QtWidgets.QTableWidgetItem(str(cal_total[3+((bar_buttom-1)*4)])))
                cal_sum = cal_sum + cal_total[3+((bar_buttom-1)*4)]
                Na_sum = Na_sum + Na_total[0+((bar_buttom-1)*4)]
                fat_sum = fat_sum + fat_total[0+((bar_buttom-1)*4)]
                chol_sum = chol_sum + chol_total[0+((bar_buttom-1)*4)]
                sw_sum = sw_sum + sw_total[0+((bar_buttom-1)*4)]
                
                self.CalTotal.setText(_translate("Dialog", str(cal_sum)))
                table_count += 1
        else:
            pass
    def checkLen(self):
        global len_food
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
        a = []
        for food in myresult:
            for fooddetail in food:
                a.append(fooddetail)
        mydb.close()
        len_food = int((len(a)) / 4)
        if ((int(len(a)) % 4) != 0):
            len_food += 1                       
    def confirmBut(self):
        global id_number,list_send,cal_sum
        yonBut = QtWidgets.QMessageBox.warning(self ,"Confirm","Are you sure to choose these menus?",QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        if yonBut  == QtWidgets.QMessageBox.Yes :
            mydb = mysql.connector.connect(
                converter_class=MyConverter,
                host="34.80.120.194",
                user="root",
                passwd="@Stang1996",
                database="project4c",
                port = 3306
            )
            mycursor = mydb.cursor()
            sql = ("UPDATE user_history SET cal = "+str(cal_sum)+",food1 = %s,food2 = %s ,food3 = %s ,food4 = %s ,food5 = %s ,food6 = %s ,food7 = %s ,food8 = %s ,food9 = %s ,food10 = %s WHERE id = "+str(id_number)+";")
            mycursor.execute(sql,list_send)
            mydb.commit()
            QtWidgets.QMessageBox.information(self,"Pass","We send your menu",QtWidgets.QMessageBox.Ok)
            mydb.close
        else:
            pass
    def nesTolist(self):
        global cal_total,Na_total,fat_total,sw_total,chol_total,type_total
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
        mycursor.close
        mycursor = mydb.cursor()
        mycursor.execute("SELECT sodium FROM food ORDER BY food_id ASC")
        myresult = mycursor.fetchall()
        for Na in myresult:
            for Nadetail in Na:
                Na_total.append(Nadetail) 
        mycursor.close
        mycursor = mydb.cursor()
        mycursor.execute("SELECT fat FROM food ORDER BY food_id ASC")
        myresult = mycursor.fetchall()
        for fat in myresult:
            for fatdetail in fat:
                fat_total.append(fatdetail) 
        mycursor.close
        mycursor = mydb.cursor()
        mycursor.execute("SELECT sugar FROM food ORDER BY food_id ASC")
        myresult = mycursor.fetchall()
        for sw in myresult:
            for swdetail in sw:
                sw_total.append(swdetail) 
        mycursor.close
        mycursor = mydb.cursor()
        mycursor.execute("SELECT cloresterol FROM food ORDER BY food_id ASC")
        myresult = mycursor.fetchall()
        for chol in myresult:
            for choldetail in chol:
                chol_total.append(choldetail) 
        mycursor.close
        mycursor = mydb.cursor()
        mycursor.execute("SELECT other FROM food ORDER BY food_id ASC")
        myresult = mycursor.fetchall()
        for type_l in myresult:
            for typedetail in type_l:
                if  (typedetail == None) : 
                    typedetail = 0
                type_total.append(typedetail)
        #print(type_total)
        mycursor.close  
        mydb.close
             
    def BackBut(self):
        _translate = QtCore.QCoreApplication.translate
        global bar_buttom,a
        if (bar_buttom > 1):
            bar_buttom -= 1
            self.food_1.setText(_translate("Dialog", self.checkMark(0+((bar_buttom-1)*4))+a[0+((bar_buttom-1)*4)]))
            self.food_2.setText(_translate("Dialog", self.checkMark(1+((bar_buttom-1)*4))+a[1+((bar_buttom-1)*4)]))
            self.food_3.setText(_translate("Dialog", self.checkMark(2+((bar_buttom-1)*4))+a[2+((bar_buttom-1)*4)]))
            self.food_4.setText(_translate("Dialog", self.checkMark(3+((bar_buttom-1)*4))+a[3+((bar_buttom-1)*4)]))
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
            self.food_1.setText(_translate("Dialog", self.checkMark(0+((bar_buttom-1)*4))+a[0+((bar_buttom-1)*4)]))
            self.food_2.setText(_translate("Dialog", self.checkMark(1+((bar_buttom-1)*4))+a[1+((bar_buttom-1)*4)]))
            self.food_3.setText(_translate("Dialog", self.checkMark(2+((bar_buttom-1)*4))+a[2+((bar_buttom-1)*4)]))
            self.food_4.setText(_translate("Dialog", self.checkMark(3+((bar_buttom-1)*4))+a[3+((bar_buttom-1)*4)]))
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
        self.nesTolist()
        self.food_1.setText(_translate("Dialog", self.checkMark(0+((bar_buttom-1)*4))+a[0+((bar_buttom-1)*4)]))
        self.food_2.setText(_translate("Dialog", self.checkMark(1+((bar_buttom-1)*4))+a[1+((bar_buttom-1)*4)]))
        self.food_3.setText(_translate("Dialog", self.checkMark(2+((bar_buttom-1)*4))+a[2+((bar_buttom-1)*4)]))
        self.food_4.setText(_translate("Dialog", self.checkMark(3+((bar_buttom-1)*4))+a[3+((bar_buttom-1)*4)]))
        self.CalTotal.setText(_translate("Dialog", str(cal_sum)))
        self.graphicsView.setScene(self.picShow(1))
        self.graphicsView_2.setScene(self.picShow(2))
        self.graphicsView_3.setScene(self.picShow(3))
        self.graphicsView_4.setScene(self.picShow(4))
    def clearBut(self):
        _translate = QtCore.QCoreApplication.translate
        global cal_sum,table_count,list_send
        yonBut = QtWidgets.QMessageBox.warning(self ,"Select Food","Do want to clear this list?",QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        if yonBut  == QtWidgets.QMessageBox.Yes :
            cal_sum = 0.0
            Na_sum = 0.0
            fat_sum = 0.0
            chol_sum = 0.0
            sw_sum = 0.0
            list_send = ["","","","","","","","","",""]
            i = 0
            for i in range(int(table_count)):  
                self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem())
            table_count = 0 
            self.CalTotal.setText(_translate("Dialog", str(cal_sum)))       
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(793, 447)
        self.label_welcome = QtWidgets.QLabel(Dialog)
        self.label_welcome.setGeometry(QtCore.QRect(56, 0, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_welcome.setFont(font)
        self.label_welcome.setObjectName("label_welcome")
        self.user_name = QtWidgets.QLabel(Dialog)
        self.user_name.setGeometry(QtCore.QRect(180, 0, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.user_name.setFont(font)
        self.user_name.setObjectName("user_name")
        #self.label_select = QtWidgets.QLabel(Dialog)
        #self.label_select.setGeometry(QtCore.QRect(60, 80, 371, 31))
        #font = QtGui.QFont()
        #font.setPointSize(14)
        #self.label_select.setFont(font)
        #self.label_select.setObjectName("label_select")
        self.backButton = QtWidgets.QPushButton(Dialog)
        self.backButton.setGeometry(QtCore.QRect(10, 410, 89, 25))
        self.backButton.setObjectName("backButton")
        self.backButton.clicked.connect(self.BackBut)
        self.nextButton = QtWidgets.QPushButton(Dialog)
        self.nextButton.setGeometry(QtCore.QRect(420, 410, 89, 25))
        self.nextButton.setObjectName("nextButton")
        self.nextButton.clicked.connect(self.NextBut)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(50, 50, 201, 131))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(300, 50, 201, 131))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.select_1 = QtWidgets.QPushButton(Dialog)
        self.select_1.setGeometry(QtCore.QRect(100, 200, 89, 25))
        self.select_1.setObjectName("select_1")
        self.graphicsView_3 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_3.setGeometry(QtCore.QRect(50, 230, 201, 131))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView_4 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_4.setGeometry(QtCore.QRect(300, 230, 201, 131))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.select_2 = QtWidgets.QPushButton(Dialog)
        self.select_2.setGeometry(QtCore.QRect(360, 200, 89, 25))
        self.select_2.setObjectName("select_2")
        self.select_3 = QtWidgets.QPushButton(Dialog)
        self.select_3.setGeometry(QtCore.QRect(100, 380, 89, 25))
        self.select_3.setObjectName("select_3")
        self.select_4 = QtWidgets.QPushButton(Dialog)
        self.select_4.setGeometry(QtCore.QRect(360, 380, 89, 25))
        self.select_4.setObjectName("select_4")
        self.select_1.clicked.connect(self.messengerSelect1)
        self.select_2.clicked.connect(self.messengerSelect2)
        self.select_3.clicked.connect(self.messengerSelect3)
        self.select_4.clicked.connect(self.messengerSelect4)
        self.food_1 = QtWidgets.QLabel(Dialog)
        self.food_1.setGeometry(QtCore.QRect(30, 180, 221, 20))
        self.food_1.setObjectName("food_1")
        self.food_3 = QtWidgets.QLabel(Dialog)
        self.food_3.setGeometry(QtCore.QRect(30, 360, 221, 20))
        self.food_3.setObjectName("food_3")
        self.food_2 = QtWidgets.QLabel(Dialog)
        self.food_2.setGeometry(QtCore.QRect(290, 180, 221, 20))
        self.food_2.setObjectName("food_2")
        self.food_4 = QtWidgets.QLabel(Dialog)
        self.food_4.setGeometry(QtCore.QRect(290, 360, 221, 20))
        self.food_4.setObjectName("food_4")
        self.confirmButton = QtWidgets.QPushButton(Dialog)
        self.confirmButton.setGeometry(QtCore.QRect(540, 410, 89, 21))
        self.confirmButton.setObjectName("confirmButton")
        self.confirmButton.clicked.connect(self.confirmBut)
        self.clearButtom = QtWidgets.QPushButton(Dialog)
        self.clearButtom.setGeometry(QtCore.QRect(680, 410, 89, 21))
        self.clearButtom.setObjectName("clearButtom")
        self.clearButtom.clicked.connect(self.clearBut)
        self.label_welcome_2 = QtWidgets.QLabel(Dialog)
        self.label_welcome_2.setGeometry(QtCore.QRect(540, 360, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_welcome_2.setFont(font)
        self.label_welcome_2.setObjectName("label_welcome_2")
        self.label_welcome_3 = QtWidgets.QLabel(Dialog)
        self.label_welcome_3.setGeometry(QtCore.QRect(710, 360, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_welcome_3.setFont(font)
        self.label_welcome_3.setObjectName("label_welcome_3")
        self.CalTotal = QtWidgets.QLabel(Dialog)
        self.CalTotal.setGeometry(QtCore.QRect(620, 360, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.CalTotal.setFont(font)
        self.CalTotal.setObjectName("CalTotal")
        self.label_welcome_5 = QtWidgets.QLabel(Dialog)
        self.label_welcome_5.setGeometry(QtCore.QRect(530, -10, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_welcome_5.setFont(font)
        self.label_welcome_5.setObjectName("label_welcome_5")
        self.Cal_Limit = QtWidgets.QLabel(Dialog)
        self.Cal_Limit.setGeometry(QtCore.QRect(640, -10, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Cal_Limit.setFont(font)
        self.Cal_Limit.setObjectName("Cal_Limit")
        self.label_welcome_7 = QtWidgets.QLabel(Dialog)
        self.label_welcome_7.setGeometry(QtCore.QRect(730, -10, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_welcome_7.setFont(font)
        self.label_welcome_7.setObjectName("label_welcome_7")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(540, 30, 231, 331))
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
        #self.label_select.setText(_translate("Dialog", "What would you like to order please? "))
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

  

        
    