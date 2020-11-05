from tkinter import *
a=Tk()
a.title("my first window")
a.geometry("500x500+0+0")
l1=Label(text='Label1',fg='red',bg='green',font='25').pack()
l2=Label(text='label2',fg='blue',bg='yellow',font='48').pack()
a.mainloop()