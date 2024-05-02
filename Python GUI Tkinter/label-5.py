# 1 hour 40 mint 
from tkinter import Tk, Label
win = Tk()
win.config(bg="red")
# label = Label(win,text="Let's learn about the Label",font=("Times New Roman",32,"bold"),bg='red',cursor="Plus")
label = Label(win,text="Let's \nlearn about the Label",font=("Times New Roman",32,"bold"),cursor="Plus",relief="groove",justify="right",underline=2)
label.place(x=200,y=200)
win.mainloop()