import tkinter as tk
import mysql.connector
from tkinter import messagebox as mb
m=tk.Tk()
m.resizable(0,0)
fn=tk.StringVar()
ln=tk.StringVar()
em=tk.StringVar()
ph=tk.IntVar()
v=tk.IntVar()
def db():
        f=fn.get()
        l=ln.get()
        p=ph.get()
        ema=em.get()
        v1=v.get()
        if f=='' and l==''and p==0 and ema=='' and v1==0 :
            mb.showinfo("WARNING", "PLEASE INSERT DETAILS FIRST")
        else:
            mydb=mysql.connector.connect(user='root',passwd='Somesh@1998',host='localhost',database="student")
            db=mydb.cursor()
            db.execute("CREATE TABLE IF NOT EXISTS sdata(fname varchar(20),lanme varchar(20),phone varchar(20),email varchar(50),gender varchar(10))")
            db.execute("INSERT INTO sdata(fname,lanme,phone,email,gender)VALUES(%s,%s,%s,%s,%s)",(f,l,p,ema,v1))
            mydb.commit()
            mb.showinfo("MESSEGE", "INSERTED SUCCESSFULLY")
l=tk.Label(master=m, text="Registration form",width=20,font=("bold", 20))
l.pack()
f=tk.Frame(relief=tk.GROOVE)
f.pack(fill=tk.BOTH,expand=True)
l=tk.Label(master=f,text="FIRSTNAME:")
l.grid(row=0,column=0)
e=tk.Entry(master=f,width=40,textvariable=fn,border=5)
e.grid(row=0,column=1,padx=10,pady=10)
l=tk.Label(master=f,text="LASTNAME:")
l.grid(row=1,column=0)
e=tk.Entry(master=f,width=40,textvariable=ln,border=5)
e.grid(row=1,column=1,padx=10,pady=10)
l=tk.Label(master=f,text="PHONE NUMBER:")
l.grid(row=2,column=0)
e=tk.Entry(master=f,width=40,textvariable=ph,border=5)
e.grid(row=2,column=1,padx=10,pady=10)
l=tk.Label(master=f,text="GENDER")
l.grid(row=3,column=0)
e=tk.Radiobutton(master=f,text="Male",variable=v,value=1,cursor="dot",border=5).grid(row=3,column=1,sticky='w')
e=tk.Radiobutton(master=f,text="Female",variable=v,value=2,cursor="dot",border=5).grid(row=4,column=1,sticky='w')
e=tk.Radiobutton(master=f,text="Others",variable=v,value=3,cursor="dot",border=5).grid(row=5,column=1,sticky='w')
l=tk.Label(master=f,text="EMAIL:")
l.grid(row=6,column=0)
e=tk.Entry(master=f,width=40,textvariable=em,border=5)
e.grid(row=6,column=1,padx=10,pady=10)
submit = tk.Button(master=f, text="Submit",command=db)
submit.grid(row=7,column=1,padx=5,pady=5)
m.mainloop()

