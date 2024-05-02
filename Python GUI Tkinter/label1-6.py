# 1 hour 47 mint
from tkinter import Tk, Label, StringVar
label_entry = input("Enter the text for label : ")
win = Tk()
var = StringVar()
win.config(bg="red")
label = Label(win,font=("Times New Roman",32,"bold"),cursor="Plus",relief="groove",textvariable=var)
var.set(label_entry)
label.place(x=200, y=200)
win.mainloop()