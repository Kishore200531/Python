#Step 1: Importing
from tkinter import *

#Step 2: GUI Interaction
window = Tk()
window.geometry("300x400")
window.title("Calculator")

#Step 3: Adding inputs

#Entry box
entry = Entry(window, width=45, borderwidth=5)
entry.place(x=0, y=0)

#Buttons

#Digits

def click(num):
    result = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(result) + str(num))

button = Button(window, text="1", width=12, command=lambda: click(1))
button.place(x=0, y=60)

button = Button(window, text="2", width=12, command=lambda: click(2))
button.place(x=90, y=60)

button = Button(window, text="3", width=12, command=lambda: click(3))
button.place(x=180, y=60)

button = Button(window, text="4", width=12, command=lambda: click(4))
button.place(x=0, y=120)

button = Button(window, text="5", width=12, command=lambda: click(5))
button.place(x=90, y=120)

button = Button(window, text="6", width=12, command=lambda: click(6))
button.place(x=180, y=120)

button = Button(window, text="7", width=12, command=lambda: click(7))
button.place(x=0, y=180)

button = Button(window, text="8", width=12, command=lambda: click(8))
button.place(x=90, y=180)

button = Button(window, text="9", width=12, command=lambda: click(9))
button.place(x=180, y=180)

button = Button(window, text="0", width=12, command=lambda: click(0))
button.place(x=0, y=240)

#Operators

def add():
    num1 = entry.get()
    global math
    math = "addition"
    global i
    i = int(num1)
    entry.delete(0, END)

button = Button(window, text="+", width=12, command=add)
button.place(x=90, y=240)

def sub():
    num1 = entry.get()
    global math
    math = "subtraction"
    global i
    i = int(num1)
    entry.delete(0, END)

button = Button(window, text="-", width=12, command=sub)
button.place(x=180, y=240)

def mul():
    num1 = entry.get()
    global math
    math = "multiplication"
    global i
    i = int(num1)
    entry.delete(0, END)

button = Button(window, text="*", width=12, command=mul)
button.place(x=0, y=300)

def div():
    num1 = entry.get()
    global math
    math = "division"
    global i
    i = int(num1)
    entry.delete(0, END)

button = Button(window, text="/", width=12, command=div)
button.place(x=90, y=300)

def equal():
    num2 = entry.get()
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, i + int(num2))
    elif math == "subtraction":
        entry.insert(0, i - int(num2))
    elif math == "multiplication":
        entry.insert(0, i * int(num2))
    elif math == "division":
        entry.insert(0, i / int(num2))

button = Button(window, text="=", width=12, command=equal)
button.place(x=180, y=300)

def clear():
    entry.delete(0, END)

button = Button(window, text="Clear", width=12, command=clear)
button.place(x=0, y=360)

#Step 4: Mainloop
mainloop()
