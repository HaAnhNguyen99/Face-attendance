import tkinter
from tkinter import *
from tkinter import *
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib.patches as mpatches
from datetime import date
from Database import Database_NhomHP
from Database import Database_DiemDanh

window = Toplevel()
def import_():
    import Manage
def Manage():
    import_()

def btn_clicked():
    import Treeview_Account

def Themsv():
    import Them_SV

def ThemHP():
    import ThemHP

def ThemMonHoc():
    import themmonhoc
window.geometry("1138x750")
window.configure(bg = "#2088c2")
canvas = Canvas(
    window,
    bg = "#2088c2",
    height = 701,
    width = 1138,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"Background/MainFrm_bg/background.png")
background = canvas.create_image(
    600.0, 300.5,
    image=background_img)

img0 = PhotoImage(file = f"Background/MainFrm_bg/img0.png")
b0 = Button(window,
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = Manage,
    relief = "flat")

b0.place(
    x = 529, y = 290,
    width = 226,
    height = 164)

img1 = PhotoImage(file = f"Background/MainFrm_bg/img1.png")
b1 = Button(window,
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = ThemMonHoc,
    relief = "flat")

b1.place(
    x = 529, y = 510,
    width = 226,
    height = 164)

img2 = PhotoImage(file = f"Background/MainFrm_bg/img2.png")
b2 = Button(window,
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = ThemHP,
    relief = "flat")

b2.place(
    x = 210, y = 510,
    width = 226,
    height = 164)

img3 = PhotoImage(file = f"Background/MainFrm_bg/img3.png")
b3 = Button(window,
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = Themsv,
    relief = "flat")

b3.place(
    x = 849, y = 290,
    width = 226,
    height = 164)

img4 = PhotoImage(file = f"Background/MainFrm_bg/img4.png")
b4 = Button(window,
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 210, y = 290,
    width = 226,
    height = 164)

window.resizable(False, False)
window.mainloop()
