import tkinter
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar,DateEntry
import sqlite3
from Database import Database_HP
from Database import Database_NhomHP
from Database import Database_GV
from tkinter import messagebox as mbx
database = Database_HP('Database/db.db')
db = Database_NhomHP('Database/db.db')
dbgv = Database_GV('Database/db.db')
window = Toplevel()
window.geometry("1051x630")
window.title("Thêm học phần")
global count
count = 0
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 645,
    width = 1051,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)
background_img = PhotoImage(file = f"Background/ThemHP_bg/background.png")
background = canvas.create_image(
    525.5, 310.5,
    image=background_img)

style = ttk.Style()
style.theme_use("xpnative")
style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=35,
                fieldbackground="#D3D3D3"
                )
# Change selected color
style.map('Treeview',
          background=[('selected', 'blue')])

mytree = ttk.Treeview(canvas, selectmode="extended")
mytree.place(x = 100, y = 20)
# tree_scroll.config(command=mytree.yview)

mytree['columns'] = ("Mã học phần","Mã GV","Nhóm học phần")

mytree.column("#0", width=0, stretch=NO)
mytree.column("Mã học phần", width = 300, minwidth = 50, anchor = tkinter.CENTER)
mytree.column("Mã GV", width = 300, minwidth = 50, anchor = tkinter.CENTER)
mytree.column("Nhóm học phần", width=300, minwidth=50, anchor=tkinter.CENTER)

mytree.heading("#0", text="", anchor=W)
mytree.heading("Mã học phần", text="Mã học phần", anchor=tkinter.CENTER)
mytree.heading("Mã GV", text="Mã GV", anchor=tkinter.CENTER)
mytree.heading("Nhóm học phần", text="Nhóm học phần", anchor=tkinter.CENTER)
mytree.tag_configure('oddrow', background="white")
mytree.tag_configure('evenrow', background="lightblue")

for i in db.fetch():
    if count % 2 == 0:
        mytree.insert('',tkinter.END,value = (i[0], i[1], i[2]),tags=('evenrow',))
    else:
        mytree.insert('',tkinter.END,value = (i[0], i[1], i[2]),tags=('oddrow',))
    count += 1
mytree.place(x = 100, y = 20)

# Create striped row tags
mytree.tag_configure('oddrow', background="white")
mytree.tag_configure('evenrow', background="lightblue")
mahp = Entry(canvas)
mahp.config(width= 22, border = 0, borderwidth = 0, justify='center',font = ("Roboto", 12 ), bg = "#f8f9f9")
mahp.place(x = 140, y = 512)

magv = Entry(canvas)
magv.config(width = 21, border = 0, borderwidth = 0, bg = "#f8f9f9",font = ("Roboto", 12 ), justify='center')
magv.place(x = 445, y = 512)

nhomhp = Entry(canvas)
nhomhp.config(width=22, border = 0, borderwidth = 0, bg = "#f2f3f3",font = ("Roboto", 12 ),justify='center')
nhomhp.place(x = 745, y = 512)

btn_frame = Frame(window)
btn_frame.pack(pady=0)

listMGV = []
for i in dbgv.LayMaGV():
    listMGV.extend(i)
listMHP = []
for i in database.LayMaHP():
    listMHP.extend(i)

def update_record():
    Mahp = mahp.get()
    Magv = magv.get()
    Nhomhp = nhomhp.get()
    print(mahp.get(), magv.get(), nhomhp.get())
    if (Mahp == '') or (Mahp == "") or (Mahp == ""):

        db.update(mahp.get(), magv.get(), nhomhp.get())
        # Grab record number
        selected = mytree.focus()
        # Save new data
        mytree.item(selected, text="", values=( mahp.get(), magv.get(),nhomhp.get()))

        # Clear entry boxes
        mahp.delete(0, END)
        magv.delete(0, END)
        nhomhp.delete(0, END)
        mbx.showinfo("Thành công", "Lưu thành công học phần")
    else:
        mbx.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin")
def add_record():
    mytree.tag_configure('oddrow', background="white")
    mytree.tag_configure('evenrow', background="lightblue")
    global count
    Mahp = mahp.get()
    Magv = magv.get()
    Nhomhp = nhomhp.get()
    if Nhomhp != "" or Magv != "" or Mahp != "":
        if len(Nhomhp) <= 3 and type(Nhomhp) != int:
            if len(Mahp) == 6:
                if Mahp in listMHP:
                    if Magv in listMGV:
                        listNhomHP = []
                        for i in db.LayNhomHP(Mahp):
                            listNhomHP.extend(i)
                        if Nhomhp not in listNhomHP:

                            db.insert(Mahp,Magv,Nhomhp)
                            if count % 2 == 0:
                                mytree.insert('', tkinter.END, value=( Mahp,  Magv, Nhomhp), tags=('evenrow',))
                            else:
                                mytree.insert('', tkinter.END, value=( Mahp, Magv,Nhomhp), tags=('oddrow',))
                            count += 1
                            mytree.pack()
                            mahp.delete(0, END)
                            magv.delete(0, END)
                            nhomhp.delete(0, END)
                            mahp.focus()
                            mbx.showinfo("Thành công", "Thêm thành công!")
                        else:
                            mbx.showerror("Lỗi", "Nhóm học phần đã tồn tại")
                    else:
                        mbx.showerror("lỗi", "Vui lòng nhập chính xác mã giảng viên!")
                else:
                    mbx.showerror("lỗi", "Vui lòng nhập chính xác mã học phần!")
            else:
                mbx.showerror("lỗi", "Mã học phần phải có 6 ký tự!")
        else:
            mbx.showerror("Lỗi", "Nhóm học phần chỉ được nhập ít nhất 3 số!!!")
    else:
        mbx.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin")

def delete_record():
    global count
    x = mytree.selection()[0]
    mytree.delete(x)
    db.remove(mahp.get(), magv.get(), nhomhp.get())
    for i in database.fetch():
        print(i)
    mbx.showinfo("Thành công","Xoá học phần thành công")
def select_record():
    # Clear entry boxes
    mahp.delete(0, END)
    magv.delete(0, END)
    nhomhp.delete(0, END)

    # Grab record number
    selected = mytree.focus()

    # Grab record values
    values = mytree.item(selected, 'values')

    # output to entry boxes
    mahp.insert(0, values[0])
    magv.insert(0, values[1])
    nhomhp.insert(0, values[2])

def clicker(e):
    select_record()
def btn_clicked():
    print("clicked")

#Button
img0 = PhotoImage(file = f"Background/ThemHP_bg/img0.png")
b0 = Button(window,
    image = img0,
    border = 0,
    borderwidth = 0,
    background = "#ffe298",
    highlightthickness = 0,
    command = update_record,
    relief = "flat")

b0.place(
    x = 200, y = 580,
    width = 139,
    height = 33)

img1 = PhotoImage(file = f"Background/ThemHP_bg/img1.png")
b1 = Button(window,
    image = img1,
    borderwidth = 0,
    border = 0,
    background = "#ffe298",
    highlightthickness = 0,
    command = delete_record,
    relief = "flat"
    )

b1.place(
    x = 700, y = 580,
    width = 139,
    height = 33)

img2 = PhotoImage(file = f"Background/ThemHP_bg/img2.png")
b2 = Button(window,
    image = img2,
    border = 0,
    borderwidth = 0,
    background = "#ffe298",
    highlightthickness = 0,
    command = add_record,
    relief = "flat")

b2.place(
    x = 450, y = 580,
    width = 139,
    height = 33)

mytree.bind("<ButtonRelease-1>", clicker)
window.resizable(False,False)
window.mainloop()
