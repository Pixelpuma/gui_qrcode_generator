import qrcode
from tkinter import *


def create():
    data=inp.get()
    name=inp2.get()
    code=qrcode.make(data)
    type(code)
    code.save(name+'.png')



window=Tk()
window.geometry('400x500')
window.title('Pixelpuma Qrcode Generator')

label=Label(text='Enter the data')


inp=Entry(window,width=30)
label2=Label(text='Enter a name for the qrcode')


inp2=Entry(window,width=30)

btn=Button(text='Create',command=create)
label.pack()
inp.pack()
label2.pack()
inp2.pack()
btn.pack()
window.mainloop()
