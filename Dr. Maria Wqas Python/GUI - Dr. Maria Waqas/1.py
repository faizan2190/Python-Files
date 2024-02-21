# Create a button called click it by clicking it, it will print hello on shell
from tkinter import Tk,Button
r=Tk()
def func():
    print("Hello")
b=Button(r,text="Click it",command=func)
b.pack()
r.mainloop()