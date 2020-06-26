# coding:UTF-8
from pygame.mixer import music
import tkinter as tk
from tkinter import messagebox as messb
from pygame import init
from os.path import exists
from webbrowser import open_new

tf1=0
init()
mTkObj=tk.Tk()
mTkObj.title("我的音乐播放器")
mTkObj.maxsize(200,150)
mTkObj.minsize(200,150)


def musfObjl():
    try:
        a=open("getm",mode="r",encoding="utf8")
        b=a.read()
        if exists(b)==True:
            a.close()
            c=['F:\下山.mp3']
            c.append(b)
            return c
        else:
            messb.showinfo("文件不存在","请确保文件存在")
    except:
        mustf1=open("getm", mode="a")
        mustf1.close()
def tkObjBcom1():
    try:
        t1=int(tkObjSV1.get())
    except ValueError:
        messb.showinfo("输入不是数字","请输入正确的索引")
    else:
        try:
            c=musfObjl()[t1]
            b=c
            a = "编号" + str(t1) + "的歌曲\n" + str(b) + "可以播放"
            messb.showinfo("正确", a)
            return t1
        except:
            messb.showinfo("错误","歌曲不存在")

def musObjPlay1():
    index=tkObjBcom1()
    musLp1=music.load(musfObjl()[index])
    music.play(1,0)

tkObjstr1=tk.Label(mTkObj,text="输入播放音乐").place(x=50,y=0)

tkObjSV1=tk.StringVar()
tkObjE=tk.Entry(mTkObj,textvariable=tkObjSV1).place(x=50,y=20)

tkObjBut2=tk.Button(mTkObj,text="播放",command=musObjPlay1).place(x=70,y=40)
tkObjBut3=tk.Button(mTkObj,text="暂停",command=music.pause()).place(x=40,y=100)
tkObjBut4=tk.Button(mTkObj,text="开始",command=music.unpause()).place(x=100,y=100)

mTkObj.mainloop()