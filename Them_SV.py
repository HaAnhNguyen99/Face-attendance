from tkinter import *
import tkinter
import sqlite3
from unidecode import unidecode
import tkinter.messagebox as mbox
import time
import cv2
import shutil
from tkinter import filedialog
from PIL import ImageTk, Image
import os
conn = sqlite3.connect('Database/db.db')
c = conn.cursor()
def them_anh():
    global MSSV
    MSSV = mssv.get()
    Lop = lop.get()
    if (len(MSSV) == 10) and int(MSSV) > 0:
        if len(Lop) == 7:
            if((name.get() != "") or (mssv.get() != "") or (lop.get() != "")):
                global picture_name
                picture_name = unidecode(name.get())
                # cv2.namedWindow("Press Space to capture")
                face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                # img_counter = 0
                cam = cv2.VideoCapture(0)
                while True:
                    ret, frame = cam.read()
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

                    for (x, y, w, h) in faces:
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                        if not ret:
                            print("failed to grab frame")
                            break

                        cv2.imshow("Press Space to capture", frame)
                        k = cv2.waitKey(1)
                        if k % 256 == 27:
                            # ESC pressed
                            print("Escape hit, closing...")
                            cam.release()
                            cv2.destroyAllWindows()
                            break

                        elif k % 256 == 32:
                            # SPACE pressed
                            t = time.strftime("%H-%M-%S")
                            img_name = 'C:/Users/HA_ANH/PycharmProjects/Recognition/ImagesAttendance/' + picture_name + '-' + MSSV + '.jpg'
                            cv2.imwrite(img_name, frame)
                            print("{} written!".format(img_name))
                            # img_counter += 1
                            cam.release()
                            cv2.destroyAllWindows()
                            mbox.showinfo("Thông báo", "Thêm ảnh thành công", )
                            break

                    btn_chonanh["state"] = "disabled",
                    btn_themAnh["state"] = "disabled"
                    txt_lop.configure(state="disabled")
                    txt_mssv.configure(state="disabled")
                    txt_name.configure(state="disabled")
            else:
                    mbox.askokcancel("Error", "Vui lòng nhập đầy đủ thông tin!")
        else:
            mbox.showerror("Error", "Lớp phải có ít nhất 7 ký tự!")
    else:
        mbox.showerror("Error", "Vui lòng nhập đúng MSSV")
def btn_clicked():
    Ten = name.get()
    global tensv
    tensv = Ten
    MSSV = mssv.get()
    Class = lop.get()
    ten = name.get()
    add_DB(MSSV, ten, Class)
def add_DB(mssv,name,lop):
    try:

        ds = [mssv,name,lop]
        print(ds)

        c.executemany("INSERT INTO Students VALUES (?,?,?)", [ds])
        conn.commit()
        conn.close()
        mbox.showerror("Success", "Thêm sinh viên thành công!")
        window.destroy()
    except:
        mbox.showerror("Error","MSSV đã tồn tại")
def chonanh():
    MSSV = mssv.get()
    Lop = lop.get()
    if (len(MSSV) == 10) and int(MSSV) > 0:
        if len(Lop) == 7:
            if ((name.get() != "") or (mssv.get() != "") or (lop.get() != "")):
                final = "C:/Users/HA_ANH/PycharmProjects/Recognition/ImagesAttendance/"
                filename = filedialog.askopenfilename(initialdir="C:/Users/HA_ANH/Desktop/Test_1", title="Select A File",
                                                           filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
                print(filename)
                save = Image.open(filename)
                ImageTk.PhotoImage(save)
                save.save("C:/Users/HA_ANH/PycharmProjects/Recognition/ImagesAttendance/" + str(mssv.get()) + "-" + str(name.get())+".png", "png", save_all=False)
                final = os.path.realpath(final)
                os.startfile(final)
                mbox.showinfo("Thành công", "Thêm ảnh thành công")
                btn_chonanh["state"] = "disabled",
                btn_themAnh["state"] = "disabled"
                txt_lop.configure(state="disabled")
                txt_mssv.configure(state="disabled")
                txt_name.configure(state="disabled")
            else:
                    mbox.askokcancel("Error", "Vui lòng nhập đầy đủ thông tin!")
        else:
            mbox.showerror("Error", "Lớp phải có ít nhất 7 ký tự!")
    else:
        mbox.showerror("Error", "Vui lòng nhập đúng MSSV")

window = Toplevel()
name = tkinter.StringVar()
mssv = tkinter.StringVar()
lop = tkinter.StringVar()
window.geometry("1246x745")
window.title("Thêm sinh viên")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 745,
    width = 1246,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"Background/ThemSV_bg/background.png")
background = canvas.create_image(
    643.0, 414.5,
    image=background_img)

img0 = PhotoImage(file = f"Background/ThemSV_bg/img0.png")
btn_xacnhan = Button(window,
    background = "white",
    activebackground = "white",
    image = img0,

    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

btn_xacnhan.place(
    x = 1014, y = 522,
    width = 204,
    height = 49)

img1 = PhotoImage(file = f"Background/ThemSV_bg/img1.png")
btn_themAnh = Button(window,
    background = "white",
    activebackground = "white",
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = them_anh,
    relief = "flat")

btn_themAnh.place(
    x = 399, y = 520,
    width = 204,
    height = 53)

img2 = PhotoImage(file = f"Background/ThemSV_bg/img2.png")
btn_chonanh = Button(window,
    background = "white",
    activebackground = "white",
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = chonanh,
    relief = "flat")

btn_chonanh.place(
    x = 707, y = 522,
    width = 204,
    height = 50)
txt_name = tkinter.Entry(window,bg = "#F6F2F2",font = ("Roboto", 15), borderwidth = 0, border = 0, textvariable = name)
txt_name.place(
    x = 450,
    y = 137,
    width=700,
    height=40
)

txt_mssv = tkinter.Entry(window,bg = "#F6F2F2",font = ("Roboto", 15), borderwidth = 0, border = 0, textvariable = mssv)
txt_mssv.place(
    x = 450,
    y = 260,
    width=700,
    height=35
)

txt_lop = tkinter.Entry(window,bg = "#F6F2F2",font = ("Roboto", 15),  borderwidth = 0, border = 0, textvariable = lop)
txt_lop.place(
    x = 450,
    y = 380,
    width=700,
    height=35
)
def on_closing():
    if mbox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
        for i in c.execute("SELECT * FROM Students ").fetchall():
            print(i)
            if mssv.get() in i:
                c.execute("DELETE FROM Students WHERE MSSV = ?", (mssv.get()))
        conn.commit()
        os.remove("C:/Users/HA_ANH/PycharmProjects/Recognition/ImagesAttendance"+ "/" + mssv.get() + "-" + name.get())


window.protocol("WM_DELETE_WINDOW", on_closing)
window.resizable(False, False)
window.mainloop()
