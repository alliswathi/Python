#============================standard and scientific definitions=============================================
from entry import *
import math
def button_click(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    
def button_clear():
    e.delete(0,1)
    
def button_allclear():
    e.delete(0,END)
    
def button_add():
    first_number = e.get()
    global f_num
    global maths
    maths="addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global maths
    maths="subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global maths
    maths="multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global maths
    maths="division"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if maths == "addition":
        e.insert(0, f_num + int(second_number))
    if maths == "subtraction":
        e.insert(0, f_num - int(second_number))   
    if maths == "multiplication":
        e.insert(0, f_num * int(second_number))
    if maths == "division":
        e.insert(0, f_num / int(second_number))

def button_pi():
    first_number = e.get()
    global f_num
    e.insert(0, math.pi) 
    f_num = int(first_number)

def button_sin():
    first_number = e.get()
    global f_num
    e.insert(0, math.sin(math.radians(float(e.get())))) 
    f_num = int(first_number)

def button_cos():
    first_number = e.get()
    global f_num
    e.insert(0, math.cos(math.radians(float(e.get())))) 
    f_num = int(first_number)

def button_tan():
    first_number = e.get()
    global f_num
    e.insert(0, math.tan(math.radians(float(e.get())))) 
    f_num = int(first_number)

def button_log():
    first_number = e.get()
    global f_num
    e.insert(0, math.log(float(e.get()))) 
    f_num = int(first_number)

def button_e():
    first_number = e.get()
    global f_num
    e.insert(0, math.e)
    f_num = int(first_number)

def button_exp():
    first_number = e.get()
    global f_num
    e.insert(0, math.exp(float(e.get())))
    f_num = int(first_number)

def button_deg():
    first_number = e.get()
    global f_num
    e.insert(0, math.degrees(float(e.get())))
    f_num = int(first_number)

def button_sqrt():
    first_number = e.get()
    global f_num
    e.insert(0, math.sqrt(float(e.get())))
    f_num = int(first_number)
