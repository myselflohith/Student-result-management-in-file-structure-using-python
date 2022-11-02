from tkinter import *
import sys,os
from PIL import Image, ImageTk
import dele

def ver():
    a=0
    if not usnname.get():
        t1.insert(END,"<>Name is required<>\n")
        a=1
    return a
def ser():
    t=ver()
    if (t==0):
        f=open("positive.txt")
        lines = f.readlines()
        f.close()
        for i in lines:
            if i.find(usnname.get())!=-1:
                t1.insert(END,"\n|PASS|"+i+"\n")
            
            
        g=open("negative.txt")
        lines1 = g.readlines()
        g.close()
        for j in lines1:
            if j.find(usnname.get())!=-1:
                t1.insert(END,"\n|FAIL|"+j+"\n")
              



if __name__=="__main__":
    root=Tk()
    
    width= root.winfo_screenwidth()
    height= root.winfo_screenheight()

    
    root.title("Yenepoya")
    root.geometry("%dx%d" % (width, height))
    root.config(bg = '#76ABFF')


    usnname=StringVar()

    labelstudent=Label(root,text="ENTER YOUR USN:",background="black",foreground="white",font=("Arial", 20),width="35")
    labelstudent.place(x=450,y=210)

    labelhead=Label(root,text="Yenepoya Institute of Technology",bg='#76ABFF',font=("Arial", 15))
    labelhead.place(x=130,y=20)

    labelhead_line=Label(root,text="----------------------------------------------------------------------------------------------------------------------------------------------",bg='#76ABFF',font=("Arial", 25))
    labelhead_line.place(x=0,y=80)

    labeladmin=Label(root,text="STUDENT RESULT",bg='#76ABFF',font=("Arial", 25))
    labeladmin.place(x=600,y=120)

    labelhead_line1=Label(root,text="----------------------------------------------------------------------------------------------------------------------------------------------",bg='#76ABFF',font=("Arial", 25))
    labelhead_line1.place(x=0,y=160)
    
    eS=Entry(root,textvariable=usnname,width="35")
    eS.place(x=615,y=255,height="27")
    
    t1=Text(root,width=60,height=24)
    t1.place(x=480,y=350) 
 
    b0=Button(root,text="SEARCH",command=ser,width=45)
    b0.place(x=560,y=290) 

   
    root.mainloop()
