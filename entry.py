from tkinter import *

root = Tk()
root.title("Scientific Calculator")
root.configure(background="black")
root.resizable(width=False, height=False)
root.geometry("410x378+0+0")

#============================================================================================================

calc=Frame(root)
calc.grid()

#============================================================================================================
            
e = Entry(calc,  width=60,borderwidth=10, fg="white", bg="black", justify=RIGHT)
e.grid(row=0, columnspan=4, padx=10, pady=10)
e.insert(0,"0")
