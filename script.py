import sys
from tkinter import *
import os
from tkinter import font
from PIL import Image, ImageTk

def clse():
    sys.exit() 
def pos():
    ret=verifier()
    if ret==0:
        h=open("admin.txt")
        lines = h.readlines()
        h.close()
        for i in lines:
            if i.find(eid.get())!=-1 and i.find(psw.get())!=-1:
                root.destroy()
                os.system('python index.py')

def student():
    os.system('python student.py')

def verifier():
    a=b=0
    if not eid.get():
        a=1
    if not psw.get():
        b=1
    if a==1 or b==1 :
        return 1
    else:
        return 0            


if __name__=="__main__":
    root=Tk()
    width= root.winfo_screenwidth()
    height= root.winfo_screenheight()

    
    root.title("Yenepoya")
    root.geometry("%dx%d" % (width, height))
    root.config(bg = 'black')
    
    eid=StringVar()
    psw=StringVar()
    label=Label(root,text="LOGIN",font=("bold",25),bg="white",fg="black",width=33)
    label.place(x=500,y=200)
    label1=Label(root,text="Admin id :",width=15)
    label1.place(x=700,y=255)

    label2=Label(root,text="Password :",width=15)
    label2.place(x=700,y=280)


    e1=Entry(root,textvariable=eid)
    e1.place(x=815,y=255,height=21)

    e2=Entry(root,show='*',textvariable=psw)
    e2.place(x=815,y=280,height=21)
   
    b4=Button(root,text="Submit",command=pos,activebackground="Green",bg="green",width=33)
    b4.place(x=698,y=320)
    b3=Button(root,text="Close",command=clse,bg="#ff0000",activebackground="red",width=20)
    b3.place(x=740,y=350)

    b5=Button(root,text="Student Login",command=student,bg="pink",activebackground="white",width=20)
    b5.place(x=740,y=380)

    root.mainloop()

