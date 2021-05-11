#===============================menu definitions=============================================
import tkinter.messagebox
from entry import *
def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def iAbout():
    iAbout = tkinter.messagebox.showinfo("About", "A calculator is a machine which allows people to do math operations more easily. For example, most calculators will add, subtract, multiply, and divide. Some also do square roots, and more complex calculators can help with calculus and draw function graphs. Calculators are found everywhere. A smartphone or other computer can also act as a calculator")

def Standard():
    root.resizable(width=False, height=False)
    root.geometry("410x378+0+0")
    
def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("820x378+0+0")