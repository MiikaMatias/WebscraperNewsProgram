from tkinter import *

def gui():
    root = Tk()

    myLabel1 = Label(root,text="Hello World!")
    myLabel2 = Label(root,text="Sheeesh")
    myLabel3 = Label(root,text="Sheeesh")


    myLabel1.grid(row=0,column=0)
    myLabel2.grid(row=1,column=1)
    myLabel3.grid(row=2,column=3)


    root.mainloop()
gui()