from tkinter import *
a=Tk()
a.title("my first window")
a.geometry("500x500+0+0")
l1=Label(text='Label1',fg='red',bg='green',font='25').pack()
button2=Button(text='submit',fg='black',bg='white',font='38').pack()
l2=Label(text='label2',fg='blue',bg='yellow',font='48').pack()
button1=Button(text='submit',fg='blue',bg='red',font='38').pack()
a.mainloop()