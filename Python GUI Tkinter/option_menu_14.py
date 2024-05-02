# 3:40
from tkinter import *
win = Tk()
win.title("Let's talk about the option menu")
option_lst = ['python','java','c#','c++']
value = StringVar()
value.set('hello')
option = OptionMenu(win,value, *option_lst)
option.place(x=100,y=150)
win.mainloop()