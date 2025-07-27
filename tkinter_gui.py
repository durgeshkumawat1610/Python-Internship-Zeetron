
# Tkinter GUI Example
from tkinter import *

def greet():
    label.config(text="Hello, " + name_entry.get())

root = Tk()
root.title("Greeting App")

name_entry = Entry(root)
name_entry.pack()

Button(root, text="Greet", command=greet).pack()
label = Label(root, text="")
label.pack()

root.mainloop()
