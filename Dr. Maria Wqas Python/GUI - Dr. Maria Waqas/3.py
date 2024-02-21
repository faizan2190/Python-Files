# Create a button called click it by clicking it, it will print hello on separate window
from tkinter import Tk,Button
from tkinter.messagebox import showinfo
r=Tk()
def func():
    showinfo(message="Hello")
b=Button(r,text="Click it",command=func)
b.pack()
r.mainloop()