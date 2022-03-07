import numpy as np
import sqlite3
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

conn = sqlite3.connect('Database/db.db')
c = conn.cursor()
# import time
# t = time.localtime()
# GioRa = time.strftime("%H:%M", t)
# NgayHoc = '04/12/21'
# c.execute("DELETE FROM Monhoc WHERE idMon = 17")
# c.execute("SELECT * FROM Monhoc")
# for i in c.fetchall():
#     print(i)

class Database_DSLop:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS DSLop (
                                                            MaHP   TEXT REFERENCES HocPhan (MaHP),
                                                            NhomHP TEXT NOT NULL,
                                                            MSSV   TEXT REFERENCES Students (MSSV),
                                                            Ten    TEXT NOT NULL,
                                                            Lop    TEXT NOT NULL)''')
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM DSLop")
        rows = self.cur.fetchall()
        return rows

    def insert(self, MaHP, NhomHP, MSSV, Ten, Lop):
        self.cur.execute("INSERT INTO DSLop VALUES (?, ?, ?, ?, ?)",(MaHP, NhomHP, MSSV, Ten, Lop))
        self.conn.commit()

    def remove(self, MaHP, NhomHP, MSSV):
        self.cur.execute("DELETE FROM DSLop WHERE (MSSV = ?) AND (MaHP = ?) AND (NhomHP = ?)", (MSSV, MaHP, NhomHP))
        self.conn.commit()

    def update(self, MaHP, NhomHP, MSSV, Ten, Lop):
        self.cur.execute("UPDATE DSLop SET MaHP = ?, NhomHP = ?, MSSV = ?, Ten = ?, Lop = ? WHERE (MSSV = ?) AND ( MaHP = ?) AND ( NhomHP = ?)",
                         (MaHP, NhomHP, MSSV, Ten, Lop, MSSV, MaHP, NhomHP))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

class Database_DiemDanh:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS DiemDanh (MSSV     TEXT REFERENCES Students (MSSV),
                                                                 Ten      TEXT NOT NULL,
                                                                 Gio      TEXT NOT NULL,
                                                                 Ngay     DATE  NOT NULL,
                                                                 MaHP     TEXT NOT NULL
                                                                               REFERENCES NhomHP (MaHP),
                                                                 NhomHP   TEXT,
                                                                 CheckIn  TEXT,
                                                                 CheckOut TEXT)''')
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM DiemDanh")
        rows = self.cur.fetchall()
        return rows

    def fetch_sv(self, MSSV, MaHP, NhomHP, Ngay):
        self.cur.execute("SELECT MSSV FROM DiemDanh WHERE (MSSV = ?) AND (MaHP = ?)  AND (NhomHP = ?) AND (Ngay = ?)", (MSSV, MaHP, NhomHP, Ngay))
        rows = self.cur.fetchall()
        return rows

    def insert(self, MSSV, Ten, Gio, Ngay, MaHP, NhomHP, CheckIn, CheckOut):
        self.cur.execute("INSERT INTO DiemDanh VALUES (?, ?, ?, ?, ?, ?, ?, ?)",(MSSV, Ten, Gio, Ngay, MaHP, NhomHP, CheckIn, CheckOut))
        self.conn.commit()

    def insert_checkOut(self, MSSV, MaHP, NhomHP, Ngay):
        self.cur.execute("UPDATE DiemDanh SET CheckOut = 'Check Out' WHERE (MSSV = ?) AND ( MaHP = ?) AND ( NhomHP = ?) AND (Ngay = ?)",(MSSV, MaHP, NhomHP, Ngay))
        self.conn.commit()

    def Check_ckOut_Not(self, MaHP, NhomHP, MSSV, Ngay):
        self.cur.execute("SELECT * FROM DiemDanh WHERE  (MaHP = ?) AND (NhomHP = ?) AND (MSSV = ?) AND (Ngay = ?)",
                         (MaHP, NhomHP, MSSV, Ngay))
        rows = self.cur.fetchall()
        return rows

    def remove(self, MSSV, Mon, NhomHP):
        self.cur.execute("DELETE FROM DiemDanh WHERE (MSSV = ?) AND (MaHP = ?) AND (NhomHP = ?)", (MSSV, MaHP, NhomHP))
        self.conn.commit()

    def update(self, MSSV, Ten, Gio, Ngay, MaHP, NhomHP, CheckIn, CheckOut):
        self.cur.execute("UPDATE DiemDanh SET MSSV = ?, Ten = ?, Gio = ?, Ngay = ?, MaHP = ?, NhomHP = ?, CheckIn = ?, CheckOut = ? WHERE (MSSV = ?) AND ( MaHP = ?) AND ( NhomHP = ?)",
                         (MSSV, Ten, Gio, Ngay, MaHP, NhomHP, CheckIn, CheckOut, MSSV, MaHP, NhomHP))
        self.conn.commit()

    def countall(self, MaHP,NhomHP):
        self.cur.execute("SELECT COUNT (Ten) FROM DiemDanh WHERE  (MaHP = ?) AND (NhomHP = ?)", (MaHP,NhomHP))
        rows = self.cur.fetchall()
        return rows

    def countcheckIn(self, MaHP, NhomHP):
        self.cur.execute("SELECT COUNT (*) FROM DiemDanh WHERE( CheckIn = 'Check In') AND (MaHP = ?) AND (NhomHP = ?)", (MaHP,NhomHP))
        rows = self.cur.fetchall()
        return rows

    def countcheckOut(self, MaHP,NhomHP):
        self.cur.execute("SELECT COUNT (*) FROM DiemDanh WHERE (CheckOut = 'Check Out') AND (MaHP = ?) AND (NhomHP = ?)", (MaHP,NhomHP))
        rows = self.cur.fetchall()
        return rows

    def layngay(self):
        self.cur.execute("SELECT DISTINCT Ngay FROM DiemDanh ORDER BY Ngay")
        rows = self.cur.fetchall()
        return rows

    def ListTongCheckOut(self, Ngay):
        self.cur.execute("SELECT Count (*) FROM DiemDanh WHERE (Ngay = ?) AND (CheckOut = 'Check Out')", (Ngay,))
        rows = self.cur.fetchall()
        return rows

    def ListTongCheckIn(self, Ngay):
        self.cur.execute("SELECT Count (*) FROM DiemDanh WHERE (Ngay = ?) AND (CheckIn = 'Check In') ", (Ngay,))
        rows = self.cur.fetchall()
        return rows

    def Droptable(self):
        self.cur.execute("DELETE FROM DiemDanh WHERE (MSSV = '1711062518')")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

class Database_GV:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS GiangVien (
                                                                MaGV  TEXT PRIMARY KEY,
                                                                TenGV TEXT,
                                                                SDT   TEXT,
                                                                CMND  TEXT UNIQUE)''')
        self.conn.commit()
    def fetch(self):
        self.cur.execute("SELECT * FROM GiangVien")
        rows = self.cur.fetchall()
        return rows

    def insert(self, MaGV, TenGV, SDT, CMND):
        self.cur.execute("INSERT INTO GiangVien VALUES (?, ?, ?, ?)",
                         (MaGV, TenGV, SDT, CMND))
        self.conn.commit()

    def remove(self,MaGV):
        self.cur.execute("DELETE FROM GiangVien WHERE MaGV=? ", (MaGV,))
        self.conn.commit()

    def update(self, MaGV, TenGV, SDT, CMND):
        self.cur.execute("UPDATE GiangVien SET MaGV = ?, TenGV = ?, SDT = ?, CMND = ?  WHERE MaGV = ? ",
                         (MaGV, TenGV, SDT, CMND,MaGV))
        self.conn.commit()

    def LayMaGV(self):
        self.cur.execute("SELECT MaGV FROM GiangVien")
        rows = self.cur.fetchall()
        return rows

    def fetchGV(self, MaGV):
        self.cur.execute("SELECT * FROM GiangVien WHERE MaGV = ?", (MaGV,))
        rows = self.cur.fetchall()
        return rows

    def delete(self):
        self.cur.execute("DELETE FROM GiangVien")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

class Database_NhomHP:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS NhomHP (
                                                MaHP   TEXT REFERENCES HocPhan (MaHP),
                                                MaGV   TEXT REFERENCES GiangVien (MaGV),
                                                NhomHP TEXT NOT NULL)''')
        self.conn.commit()
    def fetch(self):
        self.cur.execute("SELECT * FROM NhomHP ORDER BY MaHP, NhomHP")
        rows = self.cur.fetchall()
        return rows

    def insert(self, MaHP, MaGV, NhomHP):
        self.cur.execute("INSERT INTO NhomHP VALUES (?, ?, ?)",
                         (MaHP, MaGV,NhomHP))
        self.conn.commit()

    def remove(self, MaHP,  MaGV, NhomHP):
        self.cur.execute("DELETE FROM NhomHP WHERE (MaHP=?) AND (NhomHP = ?)", (MaHP,NhomHP))
        self.conn.commit()

    def update(self, MaHP, MaGV, NhomHP):
        self.cur.execute("UPDATE NhomHP SET MaHP = ?, MaGV = ?, NhomHP = ? WHERE (MaHP = ?) AND (NhomHP = ?)",
                         (MaHP, MaGV,NhomHP, MaHP, NhomHP))
        self.conn.commit()

    def LayNhomHP(self, MaHP):
        self.cur.execute("SELECT NhomHP FROM NhomHP Where MaHP = ? ORDER BY NHOMHP", (MaHP,))
        rows = self.cur.fetchall()
        return rows

    def LayMaHP(self):
        self.cur.execute("SELECT DISTINCT MaHP FROM NhomHP ORDER BY MaHP")
        rows = self.cur.fetchall()
        return rows

    def __del__(self):
        self.conn.close()

class Database_HP:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS HocPhan 
                            (MaHP  TEXT     NOT NULL    PRIMARY KEY,
                            TenHP  TEXT)''')
        self.conn.commit()
    def fetch(self):
        self.cur.execute("SELECT * FROM HocPhan")
        rows = self.cur.fetchall()
        return rows

    def insert(self, MaHP, TenHP ):
        self.cur.execute("INSERT INTO HocPhan VALUES (?, ?)",
                         (MaHP, TenHP))
        self.conn.commit()

    def remove(self, MaHP):
        self.cur.execute("DELETE FROM HocPhan WHERE MaHP=?", (MaHP,))
        self.conn.commit()

    def update(self, MaHP, TenHP ):
        self.cur.execute("UPDATE HocPhan SET MaHP = ?, TenHP = ? WHERE MaHP = ?",
                         (MaHP, TenHP,MaHP))
        self.conn.commit()

    def LayMaHP(self):
        self.cur.execute("SELECT MaHP FROM HocPhan")
        rows = self.cur.fetchall()
        return rows

    def __del__(self):
        self.conn.close()

class Database_Subjects:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Monhoc (idMon   INTEGER PRIMARY KEY AUTOINCREMENT
                                                                                        NOT NULL,
                                                                        MaHP    TEXT    REFERENCES HocPhan (MaHP) MATCH SIMPLE,
                                                                        NgayHoc DATE    NOT NULL,
                                                                        GioVao  TIME    NOT NULL,
                                                                        GioRa   TIME    NOT NULL,
                                                                        NhomHP  TEXT    REFERENCES NhomHP (NhomHP) )''')
        self.conn.commit()
    def fetch(self):
        self.cur.execute("SELECT * FROM Monhoc")
        rows = self.cur.fetchall()
        return rows
    def insert(self, MaHP, NgayHoc, GioVao, GioRa,NhomHP):
        self.cur.execute("INSERT INTO Monhoc VALUES (NULL, ?,?,?,?,?)",
                         (MaHP, NgayHoc, GioVao, GioRa, NhomHP))
        self.conn.commit()

    def remove(self, MaHP, NgayHoc, GioVao, GioRa, NhomHP):
        self.cur.execute("DELETE FROM Monhoc WHERE (MaHP = ?) AND  (NgayHoc=?) AND (GioVao=?) AND (GioRa=?) AND (NhomHP = ?)", (MaHP, NgayHoc, GioVao, GioRa,NhomHP))
        self.conn.commit()

    def update(self, MaHP, NgayHoc, GioVao, GioRa, NhomHP):
        self.cur.execute("UPDATE Monhoc SET MaHP = ?, NgayHoc = ?, GioVao = ?, GioRa = ?, NhomHP = ? WHERE ((MaHP = ?) AND (NgayHoc = ?) AND (GioVao = ?) AND (NhomHP = ?) ",(MaHP, NgayHoc, GioVao, GioRa, MaHP, NgayHoc, GioVao,NhomHP))
        self.conn.commit()

    def Mon_TrongNgay(self, NgayHoc, GioRa):
        self.cur.execute("SELECT DISTINCT (MaHP) FROM Monhoc WHERE (NgayHoc = ?) AND (GioRa > ?)", (NgayHoc, GioRa))
        rows = self.cur.fetchall()
        return rows

    def Lay_NhomHP(self, NgayHoc, GioRa):
        self.cur.execute("SELECT DISTINCT (NhomHP) FROM Monhoc WHERE (NgayHoc = ?) AND (GioRa > ?)", (NgayHoc, GioRa))
        rows = self.cur.fetchall()
        return rows

    def __del__(self):
        self.conn.close()

class Database_Accounts:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Accounts (
                                                                account  TEXT PRIMARY KEY,
                                                                password TEXT,
                                                                MaGV     TEXT REFERENCES GiangVien (MaGV)   )''')
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM Accounts")
        rows = self.cur.fetchall()
        return rows

    def insert(self, account, password, MaGV):
        self.cur.execute("INSERT INTO Accounts VALUES (?, ?, ?)",
                         (account, password, MaGV))
        self.conn.commit()

    def remove(self, account):
        self.cur.execute("DELETE FROM Accounts WHERE account =?", (account,))
        self.conn.commit()

    def update(self, account, password, MaGV):
        self.cur.execute("UPDATE Accounts SET account = ?, password = ?, MaGV = ? WHERE account = ?",
                         (account, password, MaGV, account))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

conn.commit()
conn.close()