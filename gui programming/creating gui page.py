from tkinter import *
a=Tk()
a.title("my first window")
a.geometry("500x500+0+0")
def hello():
    l3=Label(text='u have press submit').pack()
def login():
    l4 = Label(text='u have press login').pack()
t=StringVar()
button1=Button(text='submit',fg='black',bg='white',command=hello,font='38').pack()
button2=Button(text='login',fg='blue',bg='red',command=login,font='38').pack()
text=Entry(textvariable=t).pack()
menu1 = Menu()
listone = Menu()
listone.add_command(label='New File')
listone.add_command(label='Open File')
listone.add_command(label='Save File')

listtwo = Menu()
listtwo.add_command(label='Copy')
listtwo.add_command(label='Past')
listtwo.add_command(label='Undo')

menu1.add_cascade(label="File",menu=listone)
menu1.add_cascade(label="Edit",menu=listtwo)
menu1.add_cascade(label="Help")
a.config(menu=menu1)
a.mainloop()