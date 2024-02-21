# Create a button called click it by clicking it, it will print hello on main window
from tkinter import Tk,Label,Button
r=Tk()
def func():
    l=Label(r,text="Hello")
    l.pack()
b=Button(r,text="Click it",command=func)
b.pack()
r.mainloop()