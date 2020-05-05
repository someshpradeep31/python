import tkinter as tk
from tkinter import *
from tkinter import messagebox
m=tk.Tk()
val=''
a=''
def clear():
    global a
    global val
    val=''
    a=0    
    t.set(val)
def button(num,t):
    global val
    global a
    val=val+str(num)
    t.set(val)
def result():
    global val
    global a
    try:
       a=eval(val)
       t.set(a)
       val=str(a)
    except ZeroDivisionError:
        t.set("UNDEFINED")
m.geometry('220x300')
t=tk.StringVar()
e=tk.Entry(master=m,textvariable=t)
e.pack(expand=True,fill='both')
f=tk.Frame(master=m)
f.pack(expand=True,fill='both')
b=tk.Button(master=f,text='1',border=5,command=lambda:button(1,t)).pack(expand=True,side=LEFT,fill='both')
b=tk.Button(master=f,text='2',border=5,command=lambda:button(2,t)).pack(expand=True,side=LEFT,fill='both')
b=tk.Button(master=f,text='3',border=5,command=lambda:button(3,t)).pack(expand=True,side=LEFT,fill='both')
b=tk.Button(master=f,text='+',command=lambda:button('+',t)).pack(expand=True,side=LEFT,fill='both')
f1=tk.Frame(master=m)
f1.pack(expand=True,fill='both')
b=tk.Button(master=f1,text='4',border=5,command=lambda:button(4,t)).pack(expand=True,side=LEFT,fill='both')
b=tk.Button(master=f1,text='5',border=5,command=lambda:button(5,t)).pack(expand=True,side=LEFT,fill='both')
b=tk.Button(master=f1,text='6',border=5,command=lambda:button(6,t)).pack(expand=True,side=LEFT,fill='both')
b=tk.Button(master=f1,text='-',command=lambda:button('-',t)).pack(expand=True,side=LEFT,fill='both')
f2=tk.Frame(master=m)
f2.pack(expand=True,fill='both')
b=tk.Button(master=f2,text='7',border=5,command=lambda:button(7,t)).pack(expand=True,side=LEFT,fill='both')
b=tk.Button(master=f2,text='8',border=5,command=lambda:button(8,t)).pack(expand=True,side=LEFT,fill='both')
b=tk.Button(master=f2,text='9',border=5,command=lambda:button(9,t)).pack(expand=True,side=LEFT,fill='both')
b=tk.Button(master=f2,text='*',command=lambda:button('*',t)).pack(expand=True,side=LEFT,fill='both')
f3=tk.Frame(master=m)
f3.pack(expand=True,fill='both')
b=tk.Button(master=f3,text='clear',command=clear).pack(expand=True,side=LEFT,fill='both')
b=tk.Button(master=f3,text='0',border=5,command=lambda:button(0,t)).pack(expand=True,side=LEFT,fill='both')
b=tk.Button(master=f3,text='=',command=result).pack(expand=True,side=LEFT,fill='both')
b=tk.Button(master=f3,text='/',command=lambda:button('/',t)).pack(expand=True,side=LEFT,fill='both')


m.mainloop()
