import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mbx
from tkcalendar import Calendar,DateEntry
import sqlite3
from Database import Database_Subjects
from Database import Database_HP
from Database import Database_NhomHP
import datetime

dbNHP = Database_NhomHP('Database/db.db')
database = Database_Subjects('Database/db.db')
dbHP = Database_HP('Database/db.db')

window = Toplevel()
window.title("Thêm buổi học")
window.geometry("800x500")
window.configure(bg = "#ffffff")

canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 500,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"Background/ThemMonHoc_bg/background.png")
background = canvas.create_image(
    400.0, 250.0,
    image=background_img)

clicked = StringVar()

global count
count = 0
style = ttk.Style()
style.theme_use("xpnative")
style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3"
                )
# Change selected color
style.map('Treeview',
          background=[('selected', 'blue')])

# Create Treeview Frame
tree_frame = Frame(window)
tree_frame.pack(pady=10)

# Treeview Scrollbar
# tree_scroll = Scrollbar(tree_frame)
# tree_scroll.pack(side=RIGHT, fill=Y)
# mytree = ttk.Treeview(window,yscrollcommand=tree_scroll.set, selectmode="extended")

mytree = ttk.Treeview(window, selectmode="extended")
mytree.pack()
# tree_scroll.config(command=mytree.yview)

mytree['columns'] = ("Mã học phần","Ngày học","Giờ vào","Giờ ra", "Nhóm học phần")

mytree.column("#0", width=0, stretch=NO)
mytree.column("Mã học phần", width=150, minwidth=50, anchor=tkinter.CENTER)
mytree.column("Ngày học", width = 150, minwidth = 50, anchor = tkinter.CENTER)
mytree.column("Giờ vào", width=150, minwidth=50, anchor=tkinter.CENTER)
mytree.column("Giờ ra", width=150, minwidth=50, anchor=tkinter.CENTER)
mytree.column("Nhóm học phần", width=150, minwidth=50, anchor=tkinter.CENTER)


mytree.heading("#0", text="", anchor=W)
mytree.heading("Mã học phần", text="Mã học phần", anchor=tkinter.CENTER)
mytree.heading("Ngày học", text="Ngày học", anchor=tkinter.CENTER)
mytree.heading("Giờ vào", text="Giờ vào", anchor=tkinter.CENTER)
mytree.heading("Giờ ra", text="Giờ ra", anchor=tkinter.CENTER)
mytree.heading("Nhóm học phần", text="Nhóm học phần", anchor=tkinter.CENTER)

mytree.tag_configure('oddrow', background="white")
mytree.tag_configure('evenrow', background="lightblue")
for i in database.fetch():
    if count % 2 == 0:
        mytree.insert('',tkinter.END,value = (i[1], i[2], i[3], i[4], i[5]),tags=('evenrow',))
    else:
        mytree.insert('',tkinter.END,value = (i[1], i[2], i[3], i[4], i[5]),tags=('oddrow',))
    count += 1
mytree.pack()

hp = []
for i in dbNHP.LayMaHP():
    hp.extend(i)

input_NHP = StringVar()
def LayNHP(*args):
    listNHP = []
    for i in dbNHP.LayNhomHP(clicked.get()):
        if i != "":
            listNHP.extend(i)

    global input_NHP
    # print(input_NHP.get())
    input_NHP.set(listNHP[0])
    print(input_NHP.get())

    # Option Menu Nhóm HP
    drop_NHP = OptionMenu(window, input_NHP, *listNHP)
    drop_NHP.config(width=15, highlightthickness=0, border=0, bg = "white")
    drop_NHP.place(x = 620,y = 396)

clicked.set(hp[0])
clicked.trace("w", LayNHP)

#Option Menu
drop = OptionMenu(window, clicked, *hp)
drop.config(width=15, highlightthickness=0, border = 0, bg = "white")
drop.place(x = 40,y = 397)


cal = DateEntry(window, width=30, bg="darkblue", fg="white", date_pattern='dd/mm/yy')
cal.config(width = 20)
cal.place(x = 185,y = 397)

giovao = Entry(window)
giovao.config(border = 0, width = 17)
giovao.place(x = 350,y = 397)

giora = Entry(window)
giora.config( border = 0, width = 16)
giora.place(x = 493,y = 397)

dt = cal.get_date()
ngayhoc = dt.strftime("%d/%m/%y")

def update_record():
    if (giovao.get() != "") or (giora.get() != ""):
        database.update(clicked.get(), ngayhoc, giovao.get(),giora.get(),input_NHP.get())
        # Grab record number
        selected = mytree.focus()
        # Save new data
        mytree.item(selected, text="", values=( clicked.get(), ngayhoc, giovao.get(),giora.get(),input_NHP.get()))
        # Clear entry boxes
        giovao.delete(0, END)
        giora.delete(0, END)
    else:
        mbx.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin")
def add_record():
    print("NHM = ",input_NHP.get())
    if input_NHP.get() != "":
        mytree.tag_configure('oddrow', background="white")
        mytree.tag_configure('evenrow', background="lightblue")
        global count
        Giovao = giovao.get()
        Giora = giora.get()
        NhomHP = input_NHP.get()
        if (Giovao != "") or (Giora != ""):
            database.insert(clicked.get(),ngayhoc,Giovao,Giora,NhomHP)
            if count % 2 == 0:
                mytree.insert('', tkinter.END, value=( clicked.get(), ngayhoc, giovao.get(), giora.get(),NhomHP), tags=('evenrow',))

            else:
                mytree.insert('', tkinter.END, value=( clicked.get(), ngayhoc, giovao.get(),giora.get(),NhomHP), tags=('oddrow',))
            count += 1

            mytree.pack()
            giovao.delete(0, END)
            giora.delete(0, END)
            giovao.focus()
            mbx.showinfo("Thành công", "Thêm thành công!")
        else:
            mbx.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin")
    else:
        mbx.showerror("Lỗi", "Vui lòng chọn mã học phần")
def delete_record():
    x = mytree.selection()[0]
    mytree.delete(x)
    database.remove(clicked.get(), ngayhoc, giovao.get(),giora.get(), input_NHP.get())
    for i in database.fetch():
        print(i)
def select_record():
    # Clear entry boxes
    giovao.delete(0, END)
    giora.delete(0, END)

    # Grab record number
    selected = mytree.focus()

    # Grab record values
    values = mytree.item(selected, 'values')

    # output to entry boxes
    clicked.set(values[0])
    cal.set_date(str(values[1]))
    giovao.insert(0, values[2])
    giora.insert(0, values[3])
    input_NHP.set(str(values[4]))
def clicker(e):
    select_record()


def btn_clicked():
    print("Button Clicked")

img0 = PhotoImage(file = f"Background/ThemMonHoc_bg/img0.png")
b0 = Button(window,
    image = img0,
    background = "#f0b3a9",
    borderwidth = 0,
    highlightthickness = 0,
    command = update_record,
    relief = "flat")

b0.place(
    x = 181, y = 443,
    width = 107,
    height = 26)

img1 = PhotoImage(file = f"Background/ThemMonHoc_bg/img1.png")
b1 = Button(window,
    image = img1,
    background = "#f0b3a9",
    borderwidth = 0,
    highlightthickness = 0,
    command = delete_record,
    relief = "flat")

b1.place(
    x = 561, y = 443,
    width = 107,
    height = 26)

img2 = PhotoImage(file = f"Background/ThemMonHoc_bg/img2.png")
b2 = Button(window,
    image = img2,
    background = "#f0b3a9",
    borderwidth = 0,
    highlightthickness = 0,
    command = add_record,
    relief = "flat")

b2.place(
    x = 371, y = 443,
    width = 107,
    height = 26)
mytree.bind("<ButtonRelease-1>", clicker)
window.resizable(False, False)
window.mainloop()
