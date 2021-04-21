"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""



import tkinter as tk 
from tkinter import *

win = tk.Tk()

def clickFunction():
    b = int(e1.get())
    c = int(e2.get())
    
    r = abs(c)
    for i in range(-r, r+1):
        if i == 0:
            continue
        if c % i == 0:
            f1 = i
            f2 = int(c/i)
            if f1 + f2 == b:
                answer = "(x "
                if f1 < 0:
                    answer += "-"
                else:
                    answer += "+"
                answer += str(abs(f1))
                answer += ")(x "
                if f2 < 0:
                    answer += "-"
                else:
                    answer += "+"
                answer += str(abs(f2))
                answer += ")"
                break
    a_entry.delete(0, END)
    a_entry.insert(0, answer)

e1 = Entry(win,width=5)
e2 = Entry(win, width=5)

b1 = Button(win, text="Click to play", command=clickFunction)
a_entry = Entry(win, width=20, textvariable="")

e1.grid(row=1,column=1)
e2.grid(row=2,column=1)

b1.grid(row=3, column=1, columnspan=2)
a_entry.grid(row=4, column=1, columnspan=3)

win.mainloop()