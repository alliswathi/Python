from tkinter import *
from definitions import *
from menudef import *
import parser
 
#===========================standard calling functions========================================================================

button_1 = Button(calc, text="1", padx=45, pady=20, fg="white", bg="black", command=lambda: button_click(1)).grid(row=4, column=0)
button_2 = Button(calc, text="2", padx=45, pady=20, fg="white", bg="black", command=lambda: button_click(2)).grid(row=4, column=1)
button_3 = Button(calc, text="3", padx=45, pady=20, fg="white", bg="black", command=lambda: button_click(3)).grid(row=4, column=2)
button_4 = Button(calc, text="4", padx=45, pady=20, fg="white", bg="black", command=lambda: button_click(4)).grid(row=3, column=0)
button_5 = Button(calc, text="5", padx=45, pady=20, fg="white", bg="black", command=lambda: button_click(5)).grid(row=3, column=1)
button_6 = Button(calc, text="6", padx=45, pady=20, fg="white", bg="black", command=lambda: button_click(6)).grid(row=3, column=2)
button_7 = Button(calc, text="7", padx=45, pady=20, fg="white", bg="black", command=lambda: button_click(7)).grid(row=2, column=0)
button_8 = Button(calc, text="8", padx=45, pady=20, fg="white", bg="black", command=lambda: button_click(8)).grid(row=2, column=1)
button_9 = Button(calc, text="9", padx=45, pady=20, fg="white", bg="black", command=lambda: button_click(9)).grid(row=2, column=2)
button_0 = Button(calc, text="0", padx=45, pady=20, fg="white", bg="black", command=lambda: button_click(0)).grid(row=5, column=1)
button_add = Button(calc, text="+", padx=40, pady=20, fg="orange", bg="black", command=button_add).grid(row=4, column=3)
button_equal = Button(calc, text="=", padx=39, pady=20,fg="white", bg="orange", command=button_equal).grid(row=5, column=3)
button_clear = Button(calc, text="⌫", padx=40, pady=20, fg="orange", bg="black", command=button_clear).grid(row=1, column=1)
button_dot = Button(calc, text=".", padx=46, pady=20, fg="orange", bg="black", command=button_add).grid(row=5, column=2)
button_divide = Button(calc, text="÷", padx=40, pady=20, fg="orange", bg="black",command=button_divide).grid(row=1, column=3)
button_multiply = Button(calc, text="x", padx=41, pady=20, fg="orange", bg="black", command=button_multiply).grid(row=2, column=3)
button_subtract = Button(calc, text="-", padx=41, pady=20, fg="orange", bg="black", command=button_subtract).grid(row=3, column=3)
button_allclear = Button(calc, text="AC", padx=40, pady=20, fg="orange", bg="black", command=button_allclear).grid(row=1, column=0)
button_modulus = Button(calc, text="%", padx=43, pady=20, fg="orange", bg="black", command=button_add).grid(row=1, column=2)
button_back = Button(calc, text="←", padx=43, pady=20, fg="orange", bg="black",command=button_add).grid(row=5, column=0)

#================================scientific calling functions==========================================================

button_rad = Button(calc, text="Rad", padx=36, pady=20, fg="orange", bg="black", command=button_add).grid(row=1 ,column=4 )
button_deg = Button(calc, text="Deg", padx=38, pady=20,fg="orange", bg="black", command=button_deg).grid(row=1 ,column=5 )
button_fac = Button(calc, text="x!", padx=39, pady=20, fg="orange", bg="black", command=button_add).grid(row=1 ,column=6 )
button_inv = Button(calc, text="Inv", padx=38, pady=20, fg="orange", bg="black", command=button_add).grid(row=2 ,column=4 )
button_sin = Button(calc, text="sin", padx=40, pady=20, fg="orange", bg="black",command=button_sin).grid(row=2 ,column=5 )
button_in = Button(calc, text="In", padx=39, pady=20, fg="orange", bg="black", command=button_add).grid(row=2 ,column=6 )
button_pi = Button(calc, text="π", padx=43, pady=20, fg="orange", bg="black", command=button_pi).grid(row=3 ,column=4 )
button_cos = Button(calc, text="cos", padx=38, pady=20, fg="orange", bg="black", command=button_cos).grid(row=3 ,column=5 )
button_log = Button(calc, text="log", padx=36, pady=20, fg="orange", bg="black", command=button_log).grid(row=3 ,column=6 )
button_e = Button(calc, text="e", padx=43, pady=20, fg="orange", bg="black",command=button_e).grid(row=4 ,column=4 )
button_tan = Button(calc, text="tan", padx=39, pady=20, fg="orange", bg="black",command=button_tan).grid(row=4 ,column=5 )
button_sqrroot = Button(calc, text="√", padx=40, pady=20, fg="orange", bg="black",command=button_sqrt).grid(row=4 ,column=6 )
button_negpow = Button(calc, text="1/x", padx=38, pady=20, fg="orange", bg="black",command=button_add).grid(row=5 ,column=4 )
button_pow = Button(calc, text="x^y", padx=38, pady=20, fg="orange", bg="black",command=button_add).grid(row=5 ,column=5 )
button_sininv = Button(calc, text="sin-1", padx=30, pady=20, fg="orange", bg="black",command=button_add).grid(row=3 ,column=7 )
button_cosinv = Button(calc, text="cos-1", padx=30, pady=20, fg="orange", bg="black",command=button_add).grid(row=4 ,column=7 )
button_brace1 = Button(calc, text="(", padx=40, pady=20, fg="orange", bg="black",command=button_add).grid(row=1 ,column=7 )
button_brace2 = Button(calc, text=")", padx=40, pady=20, fg="orange", bg="black",command=button_add).grid(row=2 ,column=7 )
button_ans = Button(calc, text="Ans", padx=34, pady=20, fg="orange", bg="black",command=button_add).grid(row=5 ,column=6 )
button_taninv = Button(calc, text="tan-1", padx=30, pady=20, fg="white", bg="orange",command=button_add).grid(row=5 ,column=7 )
    
#================================menu calling functions=======================================================================

menu = Menu(calc)
root.config(menu=menu)

filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Standard', command=Standard)
filemenu.add_command(label='Scientific', command=Scientific)
filemenu.add_command(label="Exit", command=iExit)

editmenu = Menu(menu,tearoff=0)
menu.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='cut')
editmenu.add_command(label='copy')
editmenu.add_command(label='paste')

helpmenu = Menu(menu,tearoff=0)
m=menu.add_cascade(label='help', menu=helpmenu)
helpmenu.add_command(label='About', command=iAbout)
helpmenu.add_command(label='History')

root.mainloop()