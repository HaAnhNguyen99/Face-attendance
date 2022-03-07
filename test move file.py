from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image
import os
import cv2

# # from class filedialog
# from tkinter.filedialog import askopenfile
#
root = Tk()
root.withdraw()
final = "C:/Users/HA_ANH/PycharmProjects/Recognition/ImagesAttendance/"
root.filename = filedialog.askopenfilename(initialdir="C:/Users/HA_ANH/Desktop/Test_1", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
print(root.filename)
save = Image.open(root.filename)
save.save("C:/Users/HA_ANH/PycharmProjects/Recognition/ImagesAttendance/new.png", "png", save_all=False)
final = os.path.realpath(final)
os.startfile(final)
root.mainloop()

# path = "C:/Users/HA_ANH/Desktop/Demo"
# final = "C:/Users/HA_ANH/Desktop/final"
# ten = os.listdir(path)
# for i in ten:
#     print(i)
#     a = path + '/' + i
#     check = Image.open(a)
#     if check.format == "WEBP" or check.format == "PNG" or check.format == "JPEG":
#         save = Image.open(a).convert("RGB")
#         save.save(final + i.split(".webp")[0] + ".png","jpeg", save_all=False)
#
# final = os.path.realpath(final)
# os.startfile(final)