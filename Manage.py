from tkinter import *
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib.patches as mpatches
from datetime import date
from Database import Database_NhomHP
from Database import Database_DiemDanh
import pandas.io.sql as sql

def btn_clicked():
    print("Button Clicked")


window = Toplevel()
window.geometry("1266x734")
window.title("Quản lý sinh viên")
window.configure(bg = "#ffffff")


conn = sqlite3.connect('Database/db.db')
c = conn.cursor()
listmonhoc = []
db = Database_NhomHP('Database/db.db')
dbDD = Database_DiemDanh('Database/db.db')

tongSV_CheckIn = []

def chart():
    # Chart sinh vien check out va check in
    if (clicked.get() == "Check In + Check Out"):
        global tongSV_CheckIn
        global tongSV_CheckOut
        tongSV_CheckOut = []
        TongSV = []
        tatcacacngay = []

        img_counter = 0
        today = date.today()
        day = today.strftime("%d/%m/%y")
        width = 0.3

        def tong():
            count = 0
            for i in dbDD.layngay():
                tatcacacngay.extend(i)
                count += 1
            return count

        N = tong()

        def tinhtong_SVCheckOut():
            dem = 0
            listSvCheckOut = []
            list = []
            for i in dbDD.layngay():
                list.extend(i)
            for i in list:
                for j in dbDD.ListTongCheckOut(i):
                    listSvCheckOut.extend(j)
            print(listSvCheckOut)
            return listSvCheckOut
        tongSV_CheckOut = tinhtong_SVCheckOut()

        def tinhtong_SVCheckIn():
            dem = 0
            listSvCheckIn = []
            list = []
            for i in dbDD.layngay():
                list.extend(i)
            for i in list:
                for j in dbDD.ListTongCheckIn(i):
                    listSvCheckIn.extend(j)
            print(listSvCheckIn)
            return listSvCheckIn
        tongSV_CheckIn = tinhtong_SVCheckIn()

        p1 = plt.bar(np.arange(N), tongSV_CheckIn, width, color='#d62728')
        p2 = plt.bar(np.arange(N), tongSV_CheckOut, width, color='#d62728',bottom=tongSV_CheckIn)

        plt.ylabel('Sinh vien')
        plt.xlabel('Ngày')
        plt.title('Điểm danh')
        plt.xticks(np.arange(N))
        # plt.xticks(np.arange(0,1,1))
        sum = np.max(tongSV_CheckOut) + np.max(tongSV_CheckIn)
        if sum < 10:
            x = 2
        else:
            x = 10
        plt.yticks(np.arange(0, sum + (sum % 10), x))
        xstickcacngay = np.array(tatcacacngay)
        plt.xticks(np.arange(N), xstickcacngay)

        svCheckIn_patch = mpatches.Patch(color='red', label='Tổng số sinh viên')
        plt.legend(handles=[svCheckIn_patch])
        plt.show()

    # Chart sinh vien check in
    # elif clicked.get() == "Check In":
    #     tongSV_CheckIn = []
    #     tongSV_CheckOut = []
    #     TongSV = []
    #     tatcacacngay = []
    #
    #     img_counter = 0
    #     today = date.today()
    #     day = today.strftime("%d/%m/%y")
    #     width = 0.3
    #
    #     def tong():
    #         count = 0
    #         for i in dbDD.layngay():
    #             tatcacacngay.extend(i)
    #             count += 1
    #         return count
    #
    #     N = tong()
    #
    #     def tinhtong_SVCheckIn():
    #         dem = 0
    #         listSvCheckIn = []
    #         list = []
    #         for i in dbDD.layngay():
    #             list.extend(i)
    #         for i in list:
    #             for j in dbDD.ListTongCheckIn(i):
    #                 listSvCheckIn.extend(j)
    #         print(listSvCheckIn)
    #         return listSvCheckIn
    #
    #     tongSV_CheckIn = tinhtong_SVCheckIn()
    #     print("Tổng SV Check In = ", tongSV_CheckIn)
    #
    #     p1 = plt.bar(np.arange(N), tongSV_CheckIn, width, color='#d62728')
    #
    #     plt.ylabel('Sinh vien')
    #     plt.xlabel('Ngày')
    #     plt.title('Điểm danh')
    #     plt.xticks(np.arange(N))
    #     # plt.xticks(np.arange(0,1,1))
    #     Sum = np.max(tongSV_CheckIn)
    #     if Sum < 10:
    #         x = 2
    #     else:
    #         x = 10
    #     plt.yticks(np.arange(0, Sum + (Sum % 10), x))
    #     xstickcacngay = np.array(tatcacacngay)
    #     plt.xticks(np.arange(N), xstickcacngay)
    #     svCheckIn_patch = mpatches.Patch(color='red', label='Sinh viên Check In')
    #     plt.legend(handles=[svCheckIn_patch])
    #     plt.show()
    #
    # # Chart sinh vien check out
    # elif clicked.get() == "Check Out":
    #     tongSV_CheckOut = []
    #     TongSV = []
    #     tatcacacngay = []
    #
    #     img_counter = 0
    #     today = date.today()
    #     day = today.strftime("%d/%m/%y")
    #     width = 0.3
    #
    #     def tong():
    #         count = 0
    #         for i in dbDD.layngay():
    #             tatcacacngay.extend(i)
    #             count += 1
    #         return count
    #
    #     N = tong()
    #
    #     def tinhtong_SVCheckOut():
    #         dem = 0
    #         listSvCheckOut = []
    #         list = []
    #         for i in dbDD.layngay():
    #             list.extend(i)
    #         for i in list:
    #             for j in dbDD.ListTongCheckOut(i):
    #                 listSvCheckOut.extend(j)
    #         print(listSvCheckOut)
    #         return listSvCheckOut
    #
    #     tongSV_CheckOut = tinhtong_SVCheckOut()
    #     print("Tổng SV Check Out = ", tongSV_CheckOut)
    #
    #     p2 = plt.bar(np.arange(N), tongSV_CheckOut, width, color='blue')
    #     plt.ylabel('Sinh vien')
    #     plt.xlabel('Ngày')
    #     plt.title('Điểm danh')
    #
    #     plt.xticks(np.arange(N))
    #     # plt.xticks(np.arange(0,1,1))
    #     sum = np.max(tongSV_CheckOut)
    #     if sum < 10:
    #         x = 2
    #     plt.yticks(np.arange(0, sum + (sum % 10), x))
    #
    #     xstickcacngay = np.array(tatcacacngay)
    #     plt.xticks(np.arange(N), xstickcacngay)
    #     svCheckOut_patch = mpatches.Patch(color='blue', label='Sinh viên Check Out')
    #     plt.legend(handles=[svCheckOut_patch])
    #     plt.show()

def bieudo2cot():
    # width of the bars
    img_counter = 0
    today = date.today()
    day = today.strftime("%d/%m/%y")

    tongSV_CheckOut = []
    TongSV = []
    tatcacacngay = []

    def tong():
        count = 0
        for i in dbDD.layngay():
            tatcacacngay.extend(i)
            count += 1
        return count

    TongNgay = tong()

    def tinhtong_SVCheckOut():
        dem = 0
        listSvCheckOut = []
        list = []
        for i in dbDD.layngay():
            list.extend(i)
        for i in list:
            for j in dbDD.ListTongCheckOut(i):
                listSvCheckOut.extend(j)
        return listSvCheckOut

    tongSV_CheckOut = tinhtong_SVCheckOut()

    def tinhtong_SVCheckIn():
        dem = 0
        listSvCheckIn = []
        list = []
        for i in dbDD.layngay():
            list.extend(i)
        for i in list:
            for j in dbDD.ListTongCheckIn(i):
                listSvCheckIn.extend(j)
        return listSvCheckIn

    tongSV_CheckIn = tinhtong_SVCheckIn()

    print("Tong sv check in = ",tongSV_CheckIn)
    print("Tong sv check out = ",tongSV_CheckOut)

    barWidth = 0.3

    # Choose the height of the blue bars
    # Lấy 1 mảng tất cả sinh viên check in
    bars1 = tongSV_CheckIn

    # Lấy 1 mảng tất cả sinh viên check out
    # Choose the height of the cyan bars
    bars2 = tongSV_CheckOut
    # The x position of bars
    r1 = np.arange(len(bars1))
    r2 = [n + barWidth for n in r1]

    print("bar1 = ", bars1)
    print("bar2 = ", bars2)
    # Create blue bars
    plt.bar(r1, bars1, width=barWidth, color='blue', edgecolor='black', capsize=7, label='Sinh viên check in')

    # Create cyan bars
    plt.bar(r2, bars2, width=barWidth, color='cyan', edgecolor='black', capsize=7, label='Sinh viên check out')

    # general layout
    plt.xticks(np.arange(TongNgay))
    xstickcacngay = np.array(tatcacacngay)
    plt.xticks(np.arange(TongNgay), xstickcacngay)
    if (np.max(tongSV_CheckIn) > np.max(tongSV_CheckOut)):
        Sum = np.max(tongSV_CheckIn)
    else:
        Sum = np.max(tongSV_CheckOut)
    if Sum < 10:
        x = 2
    else:
        x = 10
    plt.yticks(np.arange(0, Sum + (Sum % 10), x))
    plt.title("Danh sách điểm danh")
    plt.ylabel('Số lượng')
    plt.ylabel('Ngày')
    plt.legend()
    plt.show()

def showfolder():
    con = sqlite3.connect('Database/db.db')
    MaHp = input_mon.get()
    NHP = str(hp.get())
    print(type(MaHp),type(NHP))
    print(type(conn))

    # Val = 'abc'
    # product = pd.read_sql_query(
    #     "SELECT * FROM StoringTF WHERE Product_Code = %(val)s",
    #     c, params={'val': Val}
    # )
    sql_string = "select * from DiemDanh WHERE (MaHP = %s)  AND  (NhomHP = %s)" %(str("'"+MaHp+"'"),str(NHP))

    table = sql.read_sql_query(sql_string , con)
    table.to_csv('output.csv')
    os.system('C:/Users/HA_ANH/PycharmProjects/Recognition/output.csv')

def laysiso():
    sum = []
    for i in dbDD.countall():
        sum.extend(i)
    print("Sinh vien = ", sum)
    return sum

def countCheckIn():
    sum = []
    for i in dbDD.countcheckIn():
        sum.extend(i)
    print("Sinh vien check in = ",sum)
    return sum

def countCheckOut():
    sum = []
    for i in dbDD.countcheckOut():
        sum.extend(i)
    print("Sinh vien check out = ", sum)
    return sum

def LISTMH():
    listmonhoc = []
    for i in db.LayMaHP():
        listmonhoc.append(i)
    list = []
    for i in listmonhoc:
        if i not in list:
            list.extend(i)
    return list

def layNhomHP(*args):
    listNHP = []
    for i in db.LayNhomHP(input_mon.get()):
        listNHP.extend(i)

    # Option Menu Nhóm học phần
    global hp

    hp = StringVar()
    hp.trace("w", setlabel)
    hp.set(listNHP[0])
    drop = OptionMenu(window, hp, *listNHP)
    drop.config(width=20, highlightthickness=0,background = "#e8e9de",border = 0, borderwidth = 0, activebackground = "#e8e9de")
    drop.place(x=660, y=388)

def setlabel(*args):
    global siso
    global ssckin
    global ssckout
    print("input_mon = ", input_mon.get())
    print("hp = ", hp.get())

    ss = []
    for i in dbDD.countall(input_mon.get(), hp.get()):
        ss.extend(i)
    ckin = []
    for i in dbDD.countcheckIn(input_mon.get(), hp.get()):
        ckin.extend(i)
    ckout = []
    for i in dbDD.countcheckOut(input_mon.get(), hp.get()):
        ckout.extend(i)

    siso = StringVar()
    ssckin = StringVar()
    ssckout = StringVar()
    siso.set(ss[0])
    ssckin.set(ckin[0])
    ssckout.set(ckout[0])

    print("Sĩ số = ",siso.get())
    print("check in = ", ssckin.get())
    print("check out = ", ssckout.get())

    lbl_SiSo = Label(window, text=siso.get(), font=('Time New Roman', 35, 'bold'), bg="#92e5d1", anchor="nw")
    lbl_SiSo.place(x=190, y=170)

    lbl_SiSo = Label(window, text=ssckin.get(), font=('Time New Roman', 35, 'bold'), bg="#e9a0a0", anchor="nw")
    lbl_SiSo.place(x=520, y=170)

    lbl_SiSo = Label(window, text=ssckout.get(), font=('Time New Roman ', 35, 'bold'), bg="#808ae7")
    lbl_SiSo.place(x=850, y=170)
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 734,
    width = 1266,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"Background/manage_bg/background.png")
background = canvas.create_image(
    614.0, 377.5,
    image=background_img)

img0 = PhotoImage(file = f"Background/manage_bg/img0.png")
b0 = Button(window,
    activebackground = "white",
    background = "white",
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = chart,
    relief = "flat")

b0.place(
    x = 327, y = 575,
    width = 206,
    height = 80)

img1 = PhotoImage(file = f"Background/manage_bg/img1.png")
b1 = Button(window,
    activebackground = "white",
    background = "white",
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = bieudo2cot,
    relief = "flat")

b1.place(
    x = 593, y = 573,
    width = 231,
    height = 78)

img2 = PhotoImage(file = f"Background/manage_bg/img2.png")
b2 = Button(window,
    activebackground = "white",
    background = "white",
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = showfolder,
    relief = "flat")

b2.place(
    x = 894, y = 575,
    width = 221,
    height = 80)

# Option menu Sort by
clicked = StringVar()
clicked.set("Check In + Check Out")
drop = OptionMenu(window, clicked, "Check In + Check Out", "Check In", "Check Out")
drop.config(width = 20,highlightthickness = 0)
drop.place(x=2075, y=470)

#OptionMenu mon hoc
listmonhoc = LISTMH()
input_mon = StringVar()
input_mon.trace("w", layNhomHP)
input_mon.set(listmonhoc[0])
drop = OptionMenu(window, input_mon, *listmonhoc)
drop.config(width = 20, border = 0, highlightthickness = 0, borderwidth = 0, background = "#e8e9de", activebackground = "#e8e9de")
drop.place(x=340, y=388)

lbl_SiSo = Label(window, text= siso.get(), font= ('Time New Roman',35,'bold'), bg = "#92e5d1", anchor = "nw")
lbl_SiSo.place(x = 190, y = 170)

lbl_SiSo = Label(window, text= ssckin.get(), font= ('Time New Roman',35,'bold'), bg = "#e9a0a0", anchor = "nw")
lbl_SiSo.place(x = 520, y = 170)

lbl_SiSo = Label(window, text= ssckout.get(), font= ('Time New Roman ',35,'bold'), bg = "#808ae7", )
lbl_SiSo.place(x = 850, y = 170)
window.resizable(False, False)
window.mainloop()