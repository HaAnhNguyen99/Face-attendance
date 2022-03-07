import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mbx
from Database import Database_Accounts
from Database import Database_GV
import sqlite3

window = Toplevel()
window.geometry("800x500")
window.configure(bg = "#ffffff")

dbGV = Database_GV('Database/db.db')
database = Database_Accounts('Database/db.db')
window.title("Quản lý tài khoản")
window.geometry("850x500")

canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 500,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"Background/Account_bg/background.png")
background = canvas.create_image(
    400.0, 250.0,
    image=background_img)

global count
count = 0
style = ttk.Style()
style.theme_use("xpnative")
style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")
# Change selected color
style.map('Treeview',
          background=[('selected', 'gray')])

# Create Treeview Frame
tree_frame = Frame(window)
tree_frame.pack( pady=10)

mytree = ttk.Treeview(window, selectmode="extended")
mytree.pack()

mytree['columns'] = ("Tài khoản","Mật khẩu","Mã giảng viên", "Tên giảng viên", "SDT", "CMND")

mytree.column("#0", width=0, stretch=NO)
mytree.column("Tài khoản", width = 120, minwidth = 50, anchor = tkinter.CENTER)
mytree.column("Mật khẩu", width = 120, minwidth = 50, anchor = tkinter.CENTER)
mytree.column("Mã giảng viên", width=120, minwidth=50, anchor=tkinter.CENTER)
mytree.column("Tên giảng viên", width=120, minwidth=50, anchor=tkinter.CENTER)
mytree.column("SDT", width=120, minwidth=50, anchor=tkinter.CENTER)
mytree.column("CMND", width=120, minwidth=50, anchor=tkinter.CENTER)

mytree.heading("#0", text="", anchor=W)
mytree.heading("Tài khoản", text="Tài khoản", anchor=tkinter.CENTER)
mytree.heading("Mật khẩu", text="Mật khẩu", anchor=tkinter.CENTER)
mytree.heading("Mã giảng viên", text="Mã giảng viên", anchor=tkinter.CENTER)
mytree.heading("Tên giảng viên", text="Tên giảng viên", anchor=tkinter.CENTER)
mytree.heading("SDT", text="SDT", anchor=tkinter.CENTER)
mytree.heading("CMND", text="CMND", anchor=tkinter.CENTER)

mytree.tag_configure('oddrow', background="white")
mytree.tag_configure('evenrow', background="lightblue")

dsacc = []
dsgv = []
for i in database.fetch():
    dsacc.extend(i)
    for j in dbGV.fetchGV(i[2]):
        dsgv.extend(j)
        if count % 2 == 0:
            mytree.insert('',tkinter.END,value = (i[0], i[1], i[2], j[1], j[2], j[3]),tags=('evenrow',))
        else:
            mytree.insert('',tkinter.END,value = (i[0], i[1], i[2], j[1], j[2], j[3]),tags=('oddrow',))
        count += 1
mytree.pack()

account = Entry(window)
account.config(width = 15, border = 0)
account.place(x = 15, y = 400)

password = Entry(window)
password.config(width = 20, border = 0)
password.place(x = 146, y = 400)

namebox = Entry(window)
namebox.config(width = 15, border = 0)
namebox.place(x = 285, y = 400)

tengv = Entry(window)
tengv.config(width = 15, border = 0)
tengv.place(x = 423, y = 400)

sdt = Entry(window)
sdt.config(width = 20, border = 0)
sdt.place(x = 558, y = 400)

cmnd = Entry(window)
cmnd.config(width = 20, border = 0)
cmnd.place(x = 690, y = 400)

def update_record():
    tk = account.get()
    mk = password.get()
    Magv = namebox.get()
    Tengv = tengv.get()
    SDT = sdt.get()
    CMND = cmnd.get()
    # Grab record number
    selected = mytree.focus()
    # Save new data
    mytree.item(selected, text="", values=(account.get(), password.get(), namebox.get(), Tengv, SDT,CMND))
    database.update(tk,mk,Magv)
    dbGV.update(Magv,Tengv,SDT,CMND)
    mbx.showinfo("Thành công", "Cập nhật thành công!!")
    # Clear entry boxes
    account.delete(0, END)
    password.delete(0, END)
    namebox.delete(0, END)
    tengv.delete(0, END)
    sdt.delete(0, END)
    cmnd.delete(0, END)
    account.focus()
def add_record():
    tk = account.get()
    mk = password.get()
    Magv = namebox.get()
    Tengv = tengv.get()
    SDT = sdt.get()
    CMND = cmnd.get()
    dsacc = []
    dsgv = []

    for i in database.fetch():
        dsacc.extend(i)
    for j in dbGV.fetch():
        dsgv.extend(j)

    if tk != "" and mk != "" and (Magv != "") and (Tengv != "") and (SDT != "") and (CMND != ""):
        if tk not in dsacc:
            if Magv not in dsgv or Magv not in dsacc:
                if CMND not in dsgv and len(CMND) == 12 and int(CMND) > 0:
                    if len(SDT) == 10 and int(SDT) > 0:
                        mytree.tag_configure('oddrow', background="white")
                        mytree.tag_configure('evenrow', background="lightblue")
                        global count

                        dbGV.insert(Magv, Tengv, SDT, CMND)
                        database.insert(tk,mk,Magv)

                        if count % 2 == 0:
                            mytree.insert('', tkinter.END, value=( tk, mk, Magv, Tengv, SDT, CMND), tags=('evenrow',))
                        else:
                            mytree.insert('', tkinter.END, value=( tk, mk, Magv, Tengv, SDT, CMND), tags=('oddrow',))
                        count += 1
                        mytree.pack()

                        account.delete(0, END)
                        password.delete(0, END)
                        namebox.delete(0, END)
                        tengv.delete(0,END)
                        sdt.delete(0,END)
                        cmnd.delete(0,END)
                        account.focus()

                        mbx.showinfo("Thành công", "Thêm thành công")
                    else:
                        mbx.showerror("Lỗi", "vui lòng nhập đúng sdt: ")
                else:
                    mbx.showerror("Lỗi", "Vui lòng nhập đúng CMND, CMND phải có ít nhất 12 số và không được trùng")
            else:
                mbx.showerror("Lỗi", "Giảng viên đã có tài khoản")
        else:
            mbx.showerror("Lỗi", "Đã tồn tại tài khoản trong cơ sở dữ liệu ")
    else:
        mbx.showerror("Lỗi", "Vui lòng nhập đầy đủ dữ liệu")
def delete_record():
    x = mytree.selection()[0]
    mytree.delete(x)
    database.remove(account.get())
    dbGV.remove(namebox.get())
    mbx.showinfo("Lỗi", "Xoá thành công")
def select_record():
    try:
        # Clear entry boxes
        account.delete(0, END)
        password.delete(0, END)
        namebox.delete(0, END)
        tengv.delete(0,END)
        sdt.delete(0,END)
        cmnd.delete(0,END)

        # Grab record number
        selected = mytree.focus()

        # Grab record values
        values = mytree.item(selected, 'values')

        # output to entry boxes
        account.insert(0, values[0])
        password.insert(0, values[1])
        namebox.insert(0, values[2])
        tengv.insert(0,values[3])
        sdt.insert(0,values[4])
        cmnd.insert(0,values[5])
    except:
        account.delete(0, END)
        password.delete(0, END)
        namebox.delete(0, END)
        tengv.delete(0, END)
        sdt.delete(0, END)
        cmnd.delete(0, END)
def clicker(e):
    select_record()

img0 = PhotoImage(file = f"Background/Account_bg/img0.png")
b0 = Button(window,
    image = img0,
    borderwidth = 0,
    background = "#ffa498",
    highlightthickness = 0,
    command = update_record,
    relief = "flat")

b0.place(
    x = 156, y = 443,
    width = 107,
    height = 26)

img1 = PhotoImage(file = f"Background/Account_bg/img1.png")
b1 = Button(window,
    image = img1,
    borderwidth = 0,
    background = "#ffa498",
    highlightthickness = 0,
    command = delete_record,
    relief = "flat")

b1.place(
    x = 536, y = 443,
    width = 107,
    height = 26)

img2 = PhotoImage(file = f"Background/Account_bg/img2.png")
b2 = Button(window,
    image = img2,
    background = "#ffa498",
    borderwidth = 0,
    highlightthickness = 0,
    command = add_record,
    relief = "flat")

b2.place(
    x = 346, y = 443,
    width = 107,
    height = 26)
mytree.bind("<ButtonRelease-1>", clicker)
window.resizable(False, False)
window.mainloop()
