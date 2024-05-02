# 2:26


# from tkinter import *
# def test():
#     print(var.get())
# win = Tk()
# var = BooleanVar()
# win.title("Let's talk about the checkbox")
# check_box = Checkbutton(win, text="Python", variable=var)
# check_box.pack()
# button = Button(win, text="Press me", command=test)
# button.pack()
# win.mainloop()

from tkinter import *
def test():
    label = Label(win, text=var.get())
    label.pack()
win = Tk()
var = BooleanVar()
win.title("Let's talk about the checkbox")
check_box = Checkbutton(win, text="Python", variable=var)
check_box.pack()
button = Button(win, text="Press me", command=test)
button.pack()
win.mainloop()



# from tkinter import *
# def test():
#     label = Label(win, text=var.get())
#     label.pack()
# win = Tk()
# var = StringVar()
# win.title("Let's talk about the checkbox")
# check_box = Checkbutton(win, text="Python", variable=var, onvalue="Python", offvalue="Java")
# check_box.pack()
# check_box.deselect()
# button = Button(win, text="Press me", command=test)
# button.pack()
# win.mainloop()