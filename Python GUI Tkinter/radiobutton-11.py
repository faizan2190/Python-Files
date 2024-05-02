# from tkinter import Tk, Label, Button, Radiobutton, StringVar
# win = Tk()
# win.title("Let's talk about the radio button")
# var = StringVar()
# radio = Radiobutton(win, text="Hello World", value = "Python")
# radio.deselect()
# radio.pack()
# radio1 = Radiobutton(win, text="Hello World", value = "Java")
# # value must be different
# radio1.pack()
# win.mainloop()

from tkinter import Tk, Label, Button, Radiobutton, StringVar
def ok():
    label.config(text=var.get())
win = Tk()
win.title("Let's talk about the radio button")
lst = ['python','java','html']
var = StringVar()
for i in range(len(lst)):
    radio = Radiobutton(win, text=lst[i], value = lst[i], variable=var)
    radio.pack()
label = Label(win, text="", font=43)
label.pack()
button = Button(win, text="OK", command=ok)
button.pack()
win.mainloop()