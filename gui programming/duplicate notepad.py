from tkinter import *
a=Tk()
a.title("New Text Document.txt-Notepad")
a.geometry("5000x5000+0+0")
menu1 = Menu()
listone = Menu()
listone.add_command(label='New')
listone.add_command(label='new Window')
listone.add_command(label='Open...')
listone.add_command(label='Save')
listone.add_command(label='Save As...')
listone.add_command(label='Page Setup...')
listone.add_command(label='Print...')
listone.add_command(label='Exit')
listtwo = Menu()
listtwo.add_command(label='Undo')
listtwo.add_command(label='Cut')
listtwo.add_command(label='Copy')
listtwo.add_command(label='Paste')
listtwo.add_command(label='Delete')
listtwo.add_command(label='Search With Bing...')
listtwo.add_command(label='Find...')
listtwo.add_command(label='Find Next')
listtwo.add_command(label='Find Previous')
listtwo.add_command(label='Replace')
listtwo.add_command(label='Go To...')
listtwo.add_command(label='Select All')
listtwo.add_command(label='Time/Date')
listthree = Menu()
listthree.add_command(label='Word Wrap')
listthree.add_command(label='Font...')
listfour = Menu()
listfour.add_command(label='Zoom')
listfour.add_command(label='Status Bar')
listfive = Menu()
listfive.add_command(label='View Help')
listfive.add_command(label='Send Feedback')
listfive.add_command(label='About Notepad')
menu1.add_cascade(label="File",menu=listone)
menu1.add_cascade(label="Edit",menu=listtwo)
menu1.add_cascade(label="Format",menu=listthree)
menu1.add_cascade(label="View",menu=listfour)
menu1.add_cascade(label="Help",menu=listfive)
a.config(menu=menu1)
a.mainloop()