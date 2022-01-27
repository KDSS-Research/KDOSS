from tkinter import *
import requests
import tkinter
from tkinter import ttk
import tkinter as tk
from tkinter.filedialog import *
from tkinter.messagebox import *
import tkinter.colorchooser 
import tkinter.font as tkFont
import os
import datautils
import configparser
import hashlib
___inf32=configparser.ConfigParser()
___inf32.read("./_inf32.ini")
___inf33=configparser.ConfigParser()
___inf33.read("./_inf33.ini")
#___evr32=configparser.ConfigParser()
#___evr32.read("./__evr32.ini")
___base=datautils.ssb256Data(___inf32.get('baseinf','basefile'))
___base.load()
#___evristic=datautils.ssbEvrData(___evr32.get('baseinf','basefile'))
#___evristic.load()
def scanfile(___file):
    ___sha256 = hashlib.sha256()

    with open(___file,"rb") as f:
        for ___byte_block in iter(lambda: f.read(4096),b""):
            ___sha256.update(___byte_block)
        ___hash = ___sha256.hexdigest()
    for i in range(int(___inf33.get('inf33','before')),int(___inf33.get('inf33','after'))):
        ___int32=i+1
        ___group = ___base.getgroup(___int32)
        if ___int32 == int(___inf33.get('inf33','after'))+1:
            ___rslt = {"result": 0, "signame":None}
            return ___rslt
            #try:
            #    
            break
        if str(___hash) == ___group["sha256"]:
            ___rslt = {"result": 1, "sig":___group["sig"]}
            return ___rslt
            break
            
def start():
    def scan2(event):
        file = askopenfilename()
        if os.path.exists(file) == True:
            res1 = scanfile(file)
            if res1["result"] == 1:
                su1 = Toplevel()
                def cl0se(event):
                    su1.destroy()
                su1.geometry('300x300')
                img2 = PhotoImage(file="./gui/images/alert.png")
                lab1 = Label(su1, image=img2, width=30, height=30)
                lab2 = Label(su1, text="Угроза найдена! Название: "+res1["sig"])
                butt2 = Button(su1,text="ОК")
                lab1.pack()
                lab2.pack()
                butt2.pack()
                butt2.bind('<Button-1>', cl0se)
            else:
                su2 = Toplevel()
                def cl0se2(event):
                    su2.destroy()
                su2.geometry('300x300')
                img3 = PhotoImage(file="./gui/images/information.png")
                lab3 = Label(su2, image=img2, width=30, height=30)
                lab4 = Label(su2, text="Угроза не найдена!")
                butt3 = Button(su2,text="ОК")
                lab3.pack()
                lab4.pack()
                butt3.pack()
                butt3.bind('<Button-1>', cl0se2)
        else:
            showerror('Файл не найден!', 'Файл не найден!')
    root = Tk()
    root.title("-KD Security Scanner-")
    root.iconbitmap('./gui/images/main_ico.ico')
    root.geometry("700x500")
    img = PhotoImage(file="./gui/images/main_png.png")
    label = Label(root, text="Загрузите файл")
    butt = Button(root, text="Открыть..")
    label.pack()
    butt.pack()
    butt.bind('<Button-1>', scan2)
    root.mainloop()
start()