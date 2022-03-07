import sqlite3
import tkinter
from tkinter import *
from tkinter import messagebox
from datetime import datetime
import face_recognition
import cv2
import numpy as np
from threading import Thread
from tkinter import ttk

window = Tk()

def Diemdanhsv():
    import DiemDanh

def btn_clicked_DN():
    if (user_input.get() == "" or pass_input.get() == ""):
        messagebox.showinfo('info', 'Vui lòng nhập tài khoản và mật khẩu')
    else:
        db = sqlite3.connect('Database/db.db')
        c = db.cursor()
        c.execute("SELECT * FROM Accounts WHERE account = ? AND password = ?",(user_input.get(), pass_input.get()))
        row = c.fetchone()
        if row:
            messagebox.showinfo('info','Đăng nhập thành công')
            window.withdraw()
            import Main_frm
        else:
            messagebox.showinfo('info', 'Đăng nhập thất bại')
        c.connection.commit()

def btn_clicked_Dky():
    print("Đăng ký")

def btn_clicked_forgotPassword():
    print("Quên mật khẩu")

window.geometry("1720x1100")
window.configure(bg="#ffffff")
user_input = tkinter.StringVar()
pass_input = tkinter.StringVar()
canvas = Canvas(
    window,
    bg="#000000",
    height=1720,
    width=1200,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"Background/background.png")
background = canvas.create_image(
    680, 350,
    image=background_img)

img0 = PhotoImage(file=f"Background/btn_login.png")
b0 = Button(window,
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked_DN,
    pady = 20)

b0.place(
    x=105, y=555,
    width=106,
    height=30)

img2 = PhotoImage(file=f"Background/ForgotPassword.png")
b2 = Button(window,
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked_forgotPassword,
    relief="flat")

b2.place(
    x=100, y=280,
    width=148,
    height=28)

img3 = PhotoImage(file=f"Background/DiemDanh.png")
b3 = Button(window,
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command= Diemdanhsv,
    relief="flat")

b3.place(
    x=105, y=200,
    width=310,
    height=51)

txt_DN = tkinter.Entry(window, textvariable = user_input)
txt_DN.place(
    x = 105,
    y = 385,
    width=300,
    height=25
)

txt_Password = tkinter.Entry(window, textvariable = pass_input, show = "*")

txt_Password.place(
    x = 105,
    y = 510,
    width=300,
    height=25
)
# img1 = PhotoImage(file=f"Background/SignUp.png")
b1 = Button(window,
    # image=img1,z`
    borderwidth=0,
    highlightthickness=0,
    command= btn_clicked_Dky,
    relief="flat")

b1.place(
    x=380, y=58,
    width=52,
    height=20)
window.mainloop()