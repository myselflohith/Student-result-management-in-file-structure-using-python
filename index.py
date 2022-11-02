from tkinter import *
import sys,os
from PIL import Image, ImageTk
import dele


def verifier():
    a=b=c=d=e=f=g=h=i=j=0
    if not usn.get():
        t1.insert(END,"<>USN is required<>\n")
        a=1
    if not adhar.get():
        t1.insert(END,"<>Name is required<>\n")
        b=1
    if not branch.get():
        t1.insert(END,"<>BRANCH is required<>\n")
        c=1
    if not section.get():
        t1.insert(END,"<>SECTION number is requrired<>\n")
        d=1
    if not result.get():
        t1.insert(END,"<>SEM is required<>\n")
        e=1
    if not m1.get():
        t1.insert(END,"<>MARK is Required<>\n")
        f=1
    if not m2.get():
        t1.insert(END,"<>MARK is Required<>\n")
        g=1
    if not m3.get():
        t1.insert(END,"<>MARK is Required<>\n")
        h=1    
    if not m4.get():
        t1.insert(END,"<>MARK is Required<>\n")
        i=1
    if not m5.get():
        t1.insert(END,"<>MARK is Required<>\n")
        j=1
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1 or g==1 or h==1 or i==1 or j==1:
        return 1
    else:
        return 0


def ver():
    a=0
    if not name.get():
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
            if i.find(name.get())!=-1:
                t1.insert(END,"\n|PASS|"+i+"\n")
            
            
        g=open("negative.txt")
        lines1 = g.readlines()
        g.close()
        for j in lines1:
            if j.find(name.get())!=-1:
                t1.insert(END,"\n|FAIL|"+j+"\n")


def ad():

    ls=usn.get()+'|'+adhar.get()+'|'+branch.get()+'|'+section.get()+'|'+result.get()+'|'+m1.get()+'|'+m2.get()+'|'+m3.get()+'|'+m4.get()+'|'+m5.get()+"\n"
    if ((int(m1.get())>= 35) and (int(m2.get())>= 35) and (int(m3.get())>= 35) and (int(m4.get())>= 35) and (int(m5.get())>= 35)) :
        p=open('positive.txt','a')
        p=open('positive.txt','a')
        p.write(ls)
        p.close()
    else:
        n=open('negative.txt','a')
        n.write(ls)
        n.close()


def add_result():
            ret=verifier()
            if ret==0:
                ad()
                t1.insert(END,"\nADDED SUCCESSFULLY\n")

               
def view_result():
    p=open('positive.txt')
    n=open('negative.txt')
    c1=p.read()
    c2=n.read()
    p.close()
    n.close()
    t1.insert(END,"\npass"+"\n")
    t1.insert(END,c1)
    t1.insert(END,"\n"+"fail"+"\n")
    t1.insert(END,c2)


def delete_result():
    if not adhar.get():
        t1.insert(END,"<>USN is required<>\n")
    else:
        dele.pos(adhar.get())
        dele.neg(adhar.get())
        t1.insert(END,"\nDeleted successfully\n")

def update_result():
    ret=verifier()
    if ret==0:
        dele.pos(adhar.get())
        dele.neg(adhar.get())
        ad()
        t1.insert(END,"\nUpdated successfully\n")

def clse():
    root.destroy()
    os.system('python script.py')
def add():
    root.destroy()
    os.system('python signup.py')
def im():
   

    load1 = Image.open("logo.png")
    load1 = load1.resize((50,50), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load1)
    img1 = Label(root, image=render)
    img1.image = render
    img1.place(x=0, y=0)

    

if __name__=="__main__":
    root=Tk()
    
    width= root.winfo_screenwidth()
    height= root.winfo_screenheight()

    
    root.title("Yenepoya")
    root.geometry("%dx%d" % (width, height))
    root.config(bg = '#76ABFF')


    

    usn=StringVar()
    name=StringVar()
    adhar=StringVar()
    branch=StringVar()
    section=StringVar()
    result=StringVar()
    m1=StringVar()
    m2=StringVar()
    m3=StringVar()
    m4=StringVar()
    m5=StringVar()
    


    labelhead=Label(root,text="Yenepoya Institute of Technology",bg='#76ABFF',font=("Arial", 15))
    labelhead.place(x=130,y=20)

    labelhead_line=Label(root,text="----------------------------------------------------------------------------------------------------------------------------------------------",bg='#76ABFF',font=("Arial", 25))
    labelhead_line.place(x=0,y=80)

    labeladmin=Label(root,text="ADMINISTRATOR",bg='#76ABFF',font=("Arial", 25))
    labeladmin.place(x=600,y=120)

    labelhead_line1=Label(root,text="----------------------------------------------------------------------------------------------------------------------------------------------",bg='#76ABFF',font=("Arial", 25))
    labelhead_line1.place(x=0,y=160)
    
    labelstudent=Label(root,text="ENTER USN FOR SEARCH STUDENT MARK:",background="black",foreground="white",font=("Arial", 10),width="45")
    labelstudent.place(x=50,y=200)
    
    label1=Label(root,text="USN:",background="black",foreground="white",font=("Arial", 15),width="15")
    label1.place(x=500,y=200)

    label2=Label(root,text="STUDENT NAME:",background="black",foreground="white",font=("Arial", 15),width="15")
    label2.place(x=500,y=240)

    label3=Label(root,text="BRANCH:",background="black",foreground="white",font=("Arial", 15),width="15")
    label3.place(x=500,y=280)

    label4=Label(root,text="SECTION:",background="black",foreground="white",font=("Arial", 15),width="15")
    label4.place(x=500,y=320)

    label5=Label(root,text="SEM:",background="black",foreground="white",font=("Arial", 15),width="15")
    label5.place(x=500,y=360)

    label6=Label(root,text="18CS61:",background="black",foreground="white",font=("Arial", 15),width="15")
    label6.place(x=500,y=400)

    label6=Label(root,text="18CS62:",background="black",foreground="white",font=("Arial", 15),width="15")
    label6.place(x=500,y=440)

    label6=Label(root,text="18CS63:",background="black",foreground="white",font=("Arial", 15),width="15")
    label6.place(x=500,y=480)

    label6=Label(root,text="18CS65:",background="black",foreground="white",font=("Arial", 15),width="15")
    label6.place(x=500,y=520)

    label6=Label(root,text="18CS65:",background="black",foreground="white",font=("Arial", 15),width="15")
    label6.place(x=500,y=560)

    e1=Entry(root,textvariable=usn,width="35")
    e1.place(x=700,y=200,height="27")

    e2=Entry(root,textvariable=adhar,width="35")
    e2.place(x=700,y=240,height="27")

    e3=Entry(root,textvariable=branch,width="35")
    e3.place(x=700,y=280,height="27")

    e4=Entry(root,textvariable=section,width="35")
    e4.place(x=700,y=320,height="27")
    
    e5=Entry(root,textvariable=result,width="35")
    e5.place(x=700,y=360,height="27")

    e6=Entry(root,textvariable=m1,width="35")
    e6.place(x=700,y=400,height="27")

    e7=Entry(root,textvariable=m2,width="35")
    e7.place(x=700,y=440,height="27")

    e8=Entry(root,textvariable=m3,width="35")
    e8.place(x=700,y=480,height="27")

    e9=Entry(root,textvariable=m4,width="35")
    e9.place(x=700,y=520,height="27")

    e10=Entry(root,textvariable=m5,width="35")
    e10.place(x=700,y=560,height="27")

    eS=Entry(root,textvariable=name,width="35")
    eS.place(x=120,y=230,height="27")
    
    t1=Text(root,width=60,height=24)
    t1.place(x=1000,y=200) 
 
    b0=Button(root,text="SEARCH",command=ser,width=40)
    b0.place(x=80,y=270) 

    im()

    b1=Button(root,text="ADD RESULT",command=add_result,width=40)
    b1.place(x=570,y=615,height="27")

    b2=Button(root,text="VIEW ALL RESULT",command=view_result,width=40)
    b2.place(x=1100,y=615)

    b3=Button(root,text="DELETE RESULT",command=delete_result,width=40)
    b3.place(x=570,y=685)

    b4=Button(root,text="UPDATE RESULT",command=update_result,width=40)
    b4.place(x=570,y=650)

    b5=Button(root,text="LOGOUT",command=clse,width=40)
    b5.place(x=1100,y=685)

    b6=Button(root,text="ADD STAF",command=add,width=40)
    b6.place(x=1100,y=650)



    root.mainloop()
