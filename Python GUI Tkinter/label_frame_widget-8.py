# 2hour 5 mint 
from tkinter import *
win = Tk()
win.title("Let's talk about the frames")
label_frame = LabelFrame(win, text="Hello World",font=32, labelanchor="n")
label_frame.place(x=100, y=100, height=100, width=300)
label = Label(win, text="java", font=34)
label.place(x=100,y=120)
win.mainloop()