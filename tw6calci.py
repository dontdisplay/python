from tkinter import *

calculator = Tk()
calculator.title("SIMPLE CALULATOR")
calculator.geometry("400x400")



def add():
    a = int(t1.get("1.0", 'end-1c'))
    b=int(t2.get("1.0",'end-1c'))
    c=a+b
    result.insert('1.0',c)
    #print(c)

def sub():
    a = int(t1.get("1.0", 'end-1c'))
    b = int(t2.get("1.0", 'end-1c'))
    s=a-b
    result.insert('1.0', s)
    #print(c)

def mul():
    a = int(t1.get("1.0", 'end-1c'))
    b = int(t2.get("1.0", 'end-1c'))
    m=a*b
    result.insert('1.0',m)
    #print(c)

def div():
    a = int(t1.get("1.0", 'end-1c'))
    b = int(t2.get("1.0", 'end-1c'))
    d=a/b
    result.insert('1.0', d)
    #print(c)






l1=Label(calculator,text="NUMBER1")
l1.place(x=20,y=30)

l2=Label(calculator,text="NUMBER2")
l2.place(x=20,y=90)

l3=Label(calculator,text="RESULT")
l3.place(x=20,y=160)

t1=Text(calculator)
t1.place(x=100,y=30,height=30,width=100)

t2=Text(calculator)
t2.place(x=100,y=90,height=30,width=100)

result=Text(calculator)
result.place(x=100,y=160,height=30,width=100)



b1=Button(calculator,text="ADD",command=add)
b1.place(x=20,y=280,width=60,height=40)

b2 = Button(calculator, text="SUB", command=sub)
b2.place(x=90, y=280, width=60, height=40)

b3 = Button(calculator, text="MUL", command=mul)
b3.place(x=160, y=280, width=60, height=40)

b4 = Button(calculator, text="DIV", command=div)
b4.place(x=230, y=280, width=60, height=40)

calculator.mainloop()
