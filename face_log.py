import sys
import mysql.connector
import cv2
import numpy as np
import face_recognition
from PIL import Image
import os
from PyQt5 import QtCore, QtGui , QtWidgets
from PyQt5.QtCore import QTimer ,QCoreApplication
from PyQt5.QtGui  import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from foodshow_finalpi import Ui_Dialog
face_locations = []
face_encodings = []
face_names = []
ID_list = []
know_face_names = []
known_face_encodings = []
process_this_frame = True
len_ID = 0
name = ''


class MyConverter(mysql.connector.conversion.MySQLConverter):

    def row_to_python(self, row, fields):
        row = super(MyConverter, self).row_to_python(row, fields)

        def to_unicode(col):
            if type(col) == bytearray:
                return col.decode('utf-8')
            return col

        return[to_unicode(col) for col in row]

mem_cache = ''
mem_count = 0




class webcam_dialog(QDialog):
    def loadData(self):
        global know_face_names
        global known_face_encodings
        mydb = mysql.connector.connect(
            converter_class=MyConverter,
            host="34.80.120.194",
            user="root",
            passwd="@Stang1996",
            database="project4c",
            port = 3306
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT username FROM users ORDER BY id ASC")
        myresult = mycursor.fetchall()
        for USER in myresult:
            for IDdetail in USER:
                know_face_names.append(IDdetail)
        mydb.close()
        len_ID = int((len(know_face_names)))
        for IDLoadPic in range(len_ID):
            if (IDLoadPic < len_ID):
                person_image = face_recognition.load_image_file("pic/"+str(IDLoadPic+1)+".jpg")
                known_face_encodings.append(face_recognition.face_encodings(person_image)[0]) 
    def __init__(self):
        super(webcam_dialog,self).__init__()
        loadUi('webcam_dialog.ui',self)
        self.image=None
        self.StartButton.clicked.connect(self.start_webcam)
        self.StopButton.clicked.connect(self.stop_webcam)
    def selectFood(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.UsertoData(name)
        self.ui.setupUi(self.window)
        self.ui.user_name.setText(str(name))
        self.window.show()
    def start_webcam(self):
        self.loadData()
        self.capture=cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        #self.minW = 0.1*self.capture.get(3)
        #self.minH = 0.1*self.capture.get(4)
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(100)

    def update_frame(self):
        global mem_count
        ret,self.image = self.capture.read()
        self.image=cv2.flip(self.image,1)
        self.displayImage(self.image,1)
        if mem_count > 20:
                if mem_cache != 0:
                    self.selectFood()
                    self.stop_webcam()
                    mem_count = 0

    def stop_webcam(self):
        self.timer.stop()
        self.capture.release()
        cv2.destroyAllWindows()
        pass
 
    def displayImage(self,img,window=1):
        
        global name
        global mem_cache
        global mem_count
        global face_locations,face_encoding
        global know_face_names,known_face_encodings
         
        small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        process_this_frame = True
        # ประมวลผลเฟรมเว้นเฟรมเพื่อประหยัดเวลา
        if process_this_frame:
        # ค้นหาใบหน้าที่มีทั้งหมดในภาพ จากนั้นทำการ encodings ใบหน้าเพื่อจะนำไปใช้เปรียบเทียบต่อ
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings,face_encoding)
                name = "Unknown"
                if True in matches:
                    first_match_index = matches.index(True)
                    name = know_face_names[first_match_index]
                    if (name == mem_cache):
                        mem_count += 1
                    elif (mem_cache == ''):
                        mem_cache == name
                        mem_count += 1
                    else:
                        mem_count = 0	
                else:
                    mem_count = 0
                    mem_cache = ''
                face_names.append(name)
        process_this_frame = not process_this_frame
        # แสดงผลลัพธ์
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            # วาดกล่องรอบใบหน้า
            cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)

            # เขียนตัวหนังสือที่แสดงชื่อลงที่กรอบ
            cv2.rectangle(img, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(img,"User="+name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        qformat=QImage.Format_Indexed8
        if len(img.shape)==3 : # [0]=rows, [1]=cols, [2]=channels
            if img.shape[2]==4 :    
                qformat=QImage.Format_RGBA8888
            else :
                qformat=QImage.Format_RGB888
        outImage=QImage(img,img.shape[1],img.shape[0],img.strides[0],qformat)
        #BGR>>RGB
        outImage=outImage.rgbSwapped()
        if window==1:
           self.ImageLabel.setPixmap(QPixmap.fromImage(outImage))
           self.ImageLabel.setScaledContents(True)
       
if __name__=='__main__':
    app=QApplication(sys.argv)
    window=webcam_dialog()
    window.setWindowTitle('Face Detection')
    window.show()
    sys.exit(app.exec_())
    

