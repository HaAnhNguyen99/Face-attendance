from tkinter import *
from datetime import datetime
import face_recognition
import cv2
import os
import sqlite3
from threading import Thread
import pandas as pd
from datetime import datetime
from tkinter import messagebox as mbx
from tkinter import *
from datetime import datetime
import face_recognition
import numpy as np
import time
import sqlite3
from threading import Thread
import pandas as pd
from datetime import datetime
from tkinter import messagebox as mbx
from Database import Database_Subjects
from Database import Database_DiemDanh

window = Toplevel()
window.geometry("1168x753")
window.title("Điểm danh")
window.configure(bg = "#ffffff")

dbMH = Database_Subjects('Database/db.db')
dbDD = Database_DiemDanh('Database/db.db')
now = datetime.now()
ngay = now.strftime('%d/%m/%y')
t = time.localtime()
Gio = time.strftime("%H:%M", t)
monhoctrongngay = []
nhomHP = []
path = 'ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)
i = 0
count = 0
dssvDD = []
dsSv_DD = []
Null = 'NULL'

for i in dbMH.Mon_TrongNgay(ngay, Gio):
    monhoctrongngay.extend(i)
for i in dbMH.Lay_NhomHP(ngay, Gio):
    nhomHP.extend(i)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
encodeListKnown = findEncodings(images)

# encodeListKnown = Thread(findEncodings(images))
# encodeListKnown.start()
print('Encodeing Complete')

def markAttendance(name,status):
    Mamh = clicked.get()
    NHP = NhomHP.get()
    subjects = clicked.get()
    a = name.split("-")
    ten = a[0]
    mssv = a[1]
    for i in dbDD.fetch_sv(mssv, Mamh, NHP, ngay):
        dssvDD.extend(i)
    for i in dbDD.Check_ckOut_Not(Mamh, NHP, mssv, ngay):
        dsSv_DD.extend(i)
    print("status = ",status)
    print("dssvDD = ", dssvDD)
    print("mssv   = ", mssv)
    if (name != "Unknown"):
        if (status == 0):
            if  mssv not in dssvDD:
                status = 'Check In'
                dbDD.insert(mssv, ten, Gio, ngay, subjects, NHP, status, Null)
                for i in dbDD.fetch():
                    print(i)
        else:
            status = 'Check Out'
            if mssv not in dsSv_DD:
                dbDD.insert(mssv, ten, Gio, ngay, subjects, NHP, Null, status)
            dbDD.insert_checkOut(mssv, Mamh, NHP, ngay)

def Camera(status):
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

        for encodeFace,faceLoc in zip (encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames [matchIndex].upper()
                print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (255, 255, 0), cv2.FILLED)
                a = name.split("-")
                hello = "Hello"
                Name = a[0]
                mssV = a[1]
                cv2.putText(img, hello + Name, (x1 + 4, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                cv2.putText(img, mssV, (x1 + 4, y2 + 40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                markAttendance(name, status)

            else:
                Name =  'Hello người lạ'
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (255, 255, 0), cv2.FILLED)
                cv2.putText(img, Name, (x1 + 4, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow('webcam',img)
        key = cv2.waitKey(1)
        if  key%256 == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

def btn_CheckOut():
    Camera(1)
    return
def btn_CheckIn():
    Camera(0)
    return

canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 753,
    width = 1168,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"Background/DiemDanh_bg/background.png")
background = canvas.create_image(
    639.5, 408.5,
    image=background_img)

img0 = PhotoImage(file = f"Background/DiemDanh_bg/img0.png")
b0 = Button(window,
    border = 0,
    background = "white",
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_CheckIn,
    relief = "flat")

b0.place(
    x = 433, y = 450,
    width = 275,
    height = 67)

img1 = PhotoImage(file = f"Background/DiemDanh_bg/img1.png")
b1 = Button(window,
    border = 0,
    background = "white",
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_CheckOut,
    relief = "flat")

b1.place(
    x = 776, y = 450,
    width = 275,
    height = 67)

if(monhoctrongngay != []):
    #dropdown
    clicked = StringVar()
    clicked.set(monhoctrongngay[0])
    drop = OptionMenu(window, clicked, *monhoctrongngay)
    drop.config(width = 15, background = "#F5CBBD", border = 0 ,highlightthickness = 0, activebackground = "#F5CBBD" )
    drop.place(x=574, y=365)

    NhomHP = StringVar()
    NhomHP.set(nhomHP[0])
    drop = OptionMenu(window, NhomHP, *nhomHP)
    drop.config(width=15, background = "#F5CBBD", border = 0,  highlightthickness = 0,  activebackground = "#F5CBBD")
    drop.place(x=780, y=365)

else:
    mbx.showerror("Error", "Không có môn học nào trong ngày")
    b0["state"] = DISABLED
    b1["state"] = DISABLED

window.resizable(False, False)
window.mainloop()
