import tkinter
from tkinter import *

root=tkinter.Tk()
root.geometry('300x300')

root.title('CGPA Calculator')

cgpa=StringVar()
def calci():
    a=float(e1.get())
    b=float(e2.get())
    c=float(e3.get())
    d=float(e4.get())
    e=float(e5.get())
    f=float(e6.get())
    add=(a+b+c+d+e+f)/6
    result=(add/10)
    cgpa.set(result)

sub1=Label(root,text='Subject 1',font='Stencil 18').grid(row=1,column=0)
e1=Entry(root,bd=5)
e1.grid(row=1,column=1)
sub2=Label(root,text='Subject 2',font='Stencil 18').grid(row=2,column=0)
e2=Entry(root,bd=5)
e2.grid(row=2,column=1)
sub3=Label(root,text='Subject 3',font='Stencil 18').grid(row=3,column=0)
e3=Entry(root,bd=5)
e3.grid(row=3,column=1)
sub4=Label(root,text='Subject 4',font='Stencil 18').grid(row=4,column=0)
e4=Entry(root,bd=5)
e4.grid(row=4,column=1)
sub5=Label(root,text='Subject 5',font='Stencil 18').grid(row=5,column=0)
e5=Entry(root,bd=5)
e5.grid(row=5,column=1)
sub6=Label(root,text='Subject 6',font='Stencil 18').grid(row=6,column=0)
e6=Entry(root,bd=5)
e6.grid(row=6,column=1)

button=Button(root,text='CGPA',font='Stencil 10',bg='blue',fg='white',activebackground='white',command=calci).grid(row=8,column=1)
e7=Entry(root,bd=5,textvariable=cgpa).grid(row=9,column=1)
root.mainloop()
