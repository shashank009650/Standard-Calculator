from tkinter import *
from tkinter import messagebox
import math

screen=Tk()
screen.configure(bg='violet')             #bg is used for change the background color
screen.title("Calculator")
screen.minsize(width=400,height=532)
screen.maxsize(width=525,height=532)
screen.geometry('400x532')

################To define the use of buttons (btn):
def click(number):
    global operator
    operator+=str(number)
    tex.set(operator)

def clear():
    global operator
    operator=''
    tex.set(operator)

def equal():
    global operator
    try:
        result = eval(operator)
        operator = str(result)
        tex.set(result)
    except:
        messagebox.showinfo('Notification','Try again! something went wrong')

tex=StringVar()
operator=''

def cmsin():
    global operator
    try:
        result=math.sin(eval(tex.get()))
        operator = str(result)
        tex.set(operator)

    except:
        messagebox.showinfo('Notification', 'Try again! something went wrong')

def cmcos():
    global operator
    try:
        result=math.cos(eval(tex.get()))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again! something went wrong')

def cmtan():
    global operator
    try:
        result=math.tan(eval(tex.get()))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again! something went wrong')

def cmlog():
    global operator
    try:
        result=math.log(eval(tex.get()))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again! something went wrong')

def cmsqrt():
    global operator
    try:
        result=math.sqrt(eval(tex.get()))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again! something went wrong')

#**********Binding function
#for row-0
def on_enterentry(e):
    entry.configure(bg="red")
def on_leaveentry(e):
    entry.configure(bg="violet")

def on_entersin(e):
    btnsin.configure(bg="red")
def on_leavesin(e):
    btnsin.configure(bg="powder blue")

#for row-1
def on_enter7(e):
    btn7.configure(bg="red")
def on_leave7(e):
    btn7.configure(bg="powder blue")

def on_enter8(e):
    btn8.configure(bg="red")
def on_leave8(e):
    btn8.configure(bg="powder blue")

def on_enter9(e):
    btn9.configure(bg="red")
def on_leave9(e):
    btn9.configure(bg="powder blue")

def on_enteradd(e):
    btnadd.configure(bg="red")
def on_leaveadd(e):
    btnadd.configure(bg="powder blue")

def on_entercos(e):
    btncos.configure(bg="red")
def on_leavecos(e):
    btncos.configure(bg="powder blue")

#for row-2
def on_enter4(e):
    btn4.configure(bg="red")
def on_leave4(e):
    btn4.configure(bg="powder blue")

def on_enter5(e):
    btn5.configure(bg="red")
def on_leave5(e):
    btn5.configure(bg="powder blue")

def on_enter6(e):
    btn6.configure(bg="red")
def on_leave6(e):
    btn6.configure(bg="powder blue")

def on_entersub(e):
    btnsub.configure(bg="red")
def on_leavesub(e):
    btnsub.configure(bg="powder blue")

def on_entertan(e):
    btntan.configure(bg="red")
def on_leavetan(e):
    btntan.configure(bg="powder blue")

#for row-3
def on_enter1(e):
    btn1.configure(bg="red")
def on_leave1(e):
    btn1.configure(bg="powder blue")

def on_enter2(e):
    btn2.configure(bg="red")
def on_leave2(e):
    btn2.configure(bg="powder blue")

def on_enter3(e):
    btn3.configure(bg="red")
def on_leave3(e):
    btn3.configure(bg="powder blue")

def on_entermul(e):
    btnmul.configure(bg="red")
def on_leavemul(e):
    btnmul.configure(bg="powder blue")

def on_enterlog(e):
    btnlog.configure(bg="red")
def on_leavelog(e):
    btnlog.configure(bg="powder blue")

#for row-3
def on_enterdiv(e):
    btndiv.configure(bg="red")
def on_leavediv(e):
    btndiv.configure(bg="powder blue")

def on_enter0(e):
    btn0.configure(bg="red")
def on_leave0(e):
    btn0.configure(bg="powder blue")

def on_enterequal(e):
    btnequal.configure(bg="red")
def on_leaveequal(e):
    btnequal.configure(bg="powder blue")

def on_enterclear(e):
    btnclear.configure(bg="red")
def on_leaveclear(e):
    btnclear.configure(bg="powder blue")

def on_entersqrt(e):
    btnsqrt.configure(bg="red")
def on_leavesqrt(e):
    btnsqrt.configure(bg="powder blue")


#*****************Row-0
entry=Entry(screen,bg='violet',bd=30,font=('algerian',20,'bold'),justify='right',textvariable=tex)        #bd is used for chnge the size of the border
entry.grid(row=0,columnspan=4)

btnsin=Button(screen,text='sin',font=('algerian',20,'bold'),bg='powder blue',bd=15,padx=14,pady=15,\
              activebackground='green',activeforeground='white',command=cmsin)
btnsin.grid(row=0,column=4)

#*****************Row-1
btn7=Button(screen,text='7',font=('algerian',20,'bold'),bg='powder blue',bd=15,padx=15,pady=15,\
            activebackground='green',activeforeground='white',command=lambda:click(7))
btn7.grid(row=1,column=0)

btn8=Button(screen,text='8',font=('algerian',20,'bold'),bg='powder blue',bd=15,padx=15,pady=15,\
            activebackground='green',activeforeground='white',command=lambda:click(8))
btn8.grid(row=1,column=1)

btn9=Button(screen,text='9',font=('algerian',20,'bold'),bg='powder blue',bd=15,padx=15,pady=15,\
            activebackground='green',activeforeground='white',command=lambda:click(9))
btn9.grid(row=1,column=2)

btnadd=Button(screen,text='+',font=('algerian',20,'bold'),bg='powder blue',bd=15,padx=15,pady=15,\
              activebackground='green',activeforeground='white',command=lambda:click('+'))
btnadd.grid(row=1,column=3)

btncos=Button(screen,text='cos',font=('algerian',20,'bold'),bg='powder blue',bd=15,padx=10,pady=15,\
              activebackground='green',activeforeground='white',command=cmcos)
btncos.grid(row=1,column=4)

#*****************Row-2
btn4=Button(screen,text='4',font=('algerian',20,'bold'),bg='powder blue',bd=15,padx=15,pady=15,\
            activebackground='green',activeforeground='white',command=lambda:click(4))
btn4.grid(row=2,column=0)

btn5=Button(screen,text='5',font=('algerian',20,'bold'),bg='powder blue',bd=15,padx=15,pady=15,\
            activebackground='green',activeforeground='white',command=lambda:click(5))
btn5.grid(row=2,column=1)

btn6=Button(screen,text='6',font=('algerian',20,'bold'),bg='powder blue',bd=15,padx=15,pady=15,\
            activebackground='green',activeforeground='white',command=lambda:click(6))
btn6.grid(row=2,column=2)

btnsub=Button(screen,text='-',font=('algerian',20,'bold'),bg='powder blue',bd=15,padx=18,pady=15,\
              activebackground='green',activeforeground='white',command=lambda:click('-'))
btnsub.grid(row=2,column=3)

btntan=Button(screen,text='tan',font=('algerian',20,'bold'),bg='powder blue',bd=15,padx=10,pady=15,\
              activebackground='green',activeforeground='white',command=cmtan)
btntan.grid(row=2,column=4)

#*****************Row-3
btn1=Button(screen,text='1',font=('algerian',20,'bold'),bg='powder blue',bd=15,padx=15,pady=15,\
            activebackground='green',activeforeground='white',command=lambda:click(1))
btn1.grid(row=3,column=0)

btn2=Button(screen,text='2',font=('algerian',20,'bold'),bg='powder blue',bd=15,padx=15,pady=15,\
            activebackground='green',activeforeground='white',command=lambda:click(2))
btn2.grid(row=3,column=1)

btn3=Button(screen,text='3',font=('algerian',20,'bold'),bg='powder blue',bd=15,padx=15,pady=15,\
            activebackground='green',activeforeground='white',command=lambda:click(3))
btn3.grid(row=3,column=2)

btnmul=Button(screen,text='*',font=('algerian',20,'bold'),bg='powder blue',bd=15,padx=18,pady=15,\
              activebackground='green',activeforeground='white',command=lambda:click('*'))
btnmul.grid(row=3,column=3)

btnlog=Button(screen,text='log',font=('algerian',20,'bold'),bg='powder blue',bd=15,padx=10,pady=15,\
              activebackground='green',activeforeground='white',command=cmlog)
btnlog.grid(row=3,column=4)

#*****************Row-4
btndiv=Button(screen,text='/',font=('algerian',20,'bold'),bg='powder blue',bd=15,padx=17,pady=15,\
            activebackground='green',activeforeground='white',command=lambda:click('/'))
btndiv.grid(row=4,column=3)

btn0=Button(screen,text='0',font=('algerian',20,'bold'),bg='powder blue',bd=15,padx=15,pady=15,\
            activebackground='green',activeforeground='white',command=lambda:click(0))
btn0.grid(row=4,column=0)

btnequal=Button(screen,text='=',font=('algerian',20,'bold'),bg='powder blue',bd=15,padx=15,pady=15,\
            activebackground='green',activeforeground='white',command=equal)
btnequal.grid(row=4,column=1)

btnclear=Button(screen,text='C',font=('algerian',20,'bold'),bg='powder blue',bd=15,padx=15,pady=15,\
            activebackground='green',activeforeground='white',command=clear)
btnclear.grid(row=4,column=2)

btnsqrt=Button(screen,text='sqrt',font=('algerian',20,'bold'),bg='powder blue',bd=15,padx=3,pady=15,\
              activebackground='green',activeforeground='white',command=cmsqrt)
btnsqrt.grid(row=4,column=4)

#***********Binding
#for row-0
entry.bind('<Enter>',on_enterentry)
entry.bind('<Leave>',on_leaveentry)

btnsin.bind('<Enter>',on_entersin)
btnsin.bind('<Leave>',on_leavesin)

#for row-1
btn7.bind('<Enter>',on_enter7)
btn7.bind('<Leave>',on_leave7)

btn8.bind('<Enter>',on_enter8)
btn8.bind('<Leave>',on_leave8)

btn9.bind('<Enter>',on_enter9)
btn9.bind('<Leave>',on_leave9)

btnadd.bind('<Enter>',on_enteradd)
btnadd.bind('<Leave>',on_leaveadd)

btncos.bind('<Enter>',on_entercos)
btncos.bind('<Leave>',on_leavecos)

#for row-2
btn4.bind('<Enter>',on_enter4)
btn4.bind('<Leave>',on_leave4)

btn5.bind('<Enter>',on_enter5)
btn5.bind('<Leave>',on_leave5)

btn6.bind('<Enter>',on_enter6)
btn6.bind('<Leave>',on_leave6)

btnsub.bind('<Enter>',on_entersub)
btnsub.bind('<Leave>',on_leavesub)

btntan.bind('<Enter>',on_entertan)
btntan.bind('<Leave>',on_leavetan)

#for row-3
btn1.bind('<Enter>',on_enter1)
btn1.bind('<Leave>',on_leave1)

btn2.bind('<Enter>',on_enter2)
btn2.bind('<Leave>',on_leave2)

btn3.bind('<Enter>',on_enter3)
btn3.bind('<Leave>',on_leave3)

btnmul.bind('<Enter>',on_entermul)
btnmul.bind('<Leave>',on_leavemul)

btnlog.bind('<Enter>',on_enterlog)
btnlog.bind('<Leave>',on_leavelog)

#for row-4
btndiv.bind('<Enter>',on_enterdiv)
btndiv.bind('<Leave>',on_leavediv)

btn0.bind('<Enter>',on_enter0)
btn0.bind('<Leave>',on_leave0)

btnequal.bind('<Enter>',on_enterequal)
btnequal.bind('<Leave>',on_leaveequal)

btnclear.bind('<Enter>',on_enterclear)
btnclear.bind('<Leave>',on_leaveclear)

btnsqrt.bind('<Enter>',on_entersqrt)
btnsqrt.bind('<Leave>',on_leavesqrt)

screen.mainloop()