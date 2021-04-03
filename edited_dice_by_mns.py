import random
from tkinter import Button,Tk,Label
def fun(l,t):
    t.destroy()
    maintk=Tk()
    maintk.config(bg='red')
    value=Label(maintk,text=' ',bg='yellow',font='arial 80 bold',height=5,width=9)
    value.grid(row=1,column=1)
    roll=Button(maintk,text='Roll the Dice',height=3,width=18,bg='powder blue',command=lambda:mainfun(value,l))
    roll.grid(row=2,column=1)
    back=Button(maintk,text='Back',height=3,width=18,bg='powder blue',command=lambda:select(maintk))
    back.grid(row=2,column=2)
def mainfun(label,l):
    s=str(random.choice(l))
    label['text']=s
def select(t=None):
    if t!=None:
        t.destroy()
    tk=Tk()
    tk.config(bg='white')
    biased1=Button(tk,text='Biased Dice 1',height=11,width=20,bg='powder blue',command=lambda:fun([1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6],tk))
    biased1.grid(row=1,column=1)
    biased2=Button(tk,text='Biased Dice 2',height=11,width=20,bg='powder blue',command=lambda:fun([6,5,5,4,4,4,3,3,3,3,2,2,2,2,2,1,1,1,1,1,1],tk))
    biased2.grid(row=2,column=1)
    unbiased=Button(tk,text='Unbiased Dice',height=11,width=20,bg='powder blue',command=lambda:fun([6,5,4,3,2,1],tk))
    unbiased.grid(row=3,column=1)
    biased1lab=Label(tk,text='chances of big output is more',bg='powder blue')
    biased2lab=Label(tk,text='chances of small output is more',bg='powder blue')
    unbiasedlab=Label(tk,text='each output has same chance',bg='powder blue')
    biased1lab.grid(row=1,column=2)
    biased2lab.grid(row=2,column=2)
    unbiasedlab.grid(row=3,column=2)
    tk.mainloop()
select()