"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""


import tkinter as tk 
from tkinter import *

win = tk.Tk()

def clickFunction():
    non1 = e1.get()
    verb = e2.get()
    adj = e3.get()
    non2 = e4.get()
    answer = non1 + " " + verb + " " + adj + " " + non2
    
    a_entry.insert(0, answer)

e1 = Entry(win,width=5)
e2 = Entry(win, width=5)
e3 = Entry(win, width=5)
e4 = Entry(win, width=5)

b1 = Button(win, text="Click to play", command=clickFunction)
a_entry = Entry(win, width=20, textvariable="")

e1.grid(row=1,column=1)
e2.grid(row=2,column=1)
e3.grid(row=3,column=1)
e4.grid(row=4,column=1)

b1.grid(row=5, column=1, columnspan=2)
a_entry.grid(row=6, column=1, columnspan=3)

win.mainloop()