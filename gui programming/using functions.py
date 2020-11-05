from tkinter import *
a=Tk()
a.title("my first window")
a.geometry("500x500+0+0")
def hello():
    l3=Label(text='u have press submit').pack()
def login():
    l4 = Label(text='u have press login').pack()
button1=Button(text='submit',fg='black',bg='white',command=hello,font='38').pack()
button2=Button(text='login',fg='blue',bg='red',command=login,font='38').pack()
a.mainloop()
