import tkinter
from tkinter import*
import tkinter.messagebox as Msg

def BTK():
    chBath=bath.get()
    chRate=rate.get()
    if bath.get()=='':
        Msg.showinfo('Infor','Enter bath please!!!',icon='warning')
        txt1.focus_set()
    elif rate.get()=='':
        Msg.showinfo('Infor', 'Enter rate please!!!', icon='warning')
        txt2.focus_set()
    elif chBath.isalpha():
        Msg.showinfo('Infor','Enter bath number only please!!!', icon='warning')
        txt1.focus_set()
    elif chRate.isalpha():
        Msg.showinfo('Infor','Enter rate number only please!!!', icon='warning')
        txt2.focus_set()
    else:
        b=int(bath.get())
        r=int(rate.get())
        k=b*r
        kip.set(f'{k:,} kip')


def allclear():
    bath.set('')
    rate.set('')
    kip.set('')
    txt1.focus()


root=Tk()
root.title('Exchange')
root.geometry('500x400')

bath=StringVar()
rate=StringVar()
kip=StringVar()


lb1=Label(root,font=('Time new roman',16),text='Bath to Kip')
lb1.place(x=200,y=25)


lb2=Label(root,font=('Time new roman',16),text='Enter Bath:')
lb2.place(x=25,y=100)
txt1=Entry(root,font=('Time new roman',16),textvariable=bath)
txt1.place(x=180,y=100)


lb3=Label(root,font=('Time new roman',16),text='Enter Rate:')
lb3.place(x=25,y=160)
txt2=Entry(root,font=('Time new roman',16),textvariable=rate)
txt2.place(x=180,y=160)


btn1=Button(root,font=('Time new roman',16),width=10,text='Exchange',command=BTK)
btn1.place(x=100,y=250)


btn2=Button(root,font=('Time new roman',16),width=10,text='Clear',command=allclear)
btn2.place(x=300,y=250)


lb4=Label(root,font=('Time new roman',16),text='Totle:')
lb4.place(x=25,y=320)
txt3=Entry(root,font=('Time new roman',16),textvariable=kip)
txt3.place(x=180,y=320)


root.mainloop()