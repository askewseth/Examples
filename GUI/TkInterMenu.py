import sys
from Tkinter import *
import tkMessageBox

def mhello():
    mtext = mEnt.get()
    mlabel2 = Label(mGui, text=mtext).pack()
    return

def mNew():
    mlabel3 = Label(mGui,text="You Clicked New").pack()
    return

def mAbout():
    tkMessageBox.showinfo(title='About', message="This is my About Box")
    return

def mQuit():
    mExit = tkMessageBox.askyesno(title='Quit',message='Are You Sure?')
    if mExit > 0:
        mGui.destroy()
    

mGui = Tk()
mEnt = StringVar()

mGui.geometry('450x250+200+750')
mGui.title('Tkinter Menu')

mlabel = Label(mGui, text = 'My Label').pack()

mbutton = Button(mGui,text="OK", command = mhello).pack()

mEntry = Entry(mGui, textvariable=mEnt).pack()



#Menu Construction

menubar =Menu(mGui)


filemenu = Menu(menubar,tearoff = 0)
filemenu.add_command(label="New",command = mNew)
filemenu.add_command(label="Save as..")
filemenu.add_command(label="Open")
filemenu.add_command(label="Close",command= mQuit)
menubar.add_cascade(label="File",menu=filemenu)


#Help Menu
helpmenu = Menu(menubar,tearoff = 0)
helpmenu.add_command(label="Help Docs")
helpmenu.add_command(label="About", command = mAbout)
menubar.add_cascade(label="Help",menu = helpmenu)


mGui.config(menu=menubar)

mGui.mainloop()

