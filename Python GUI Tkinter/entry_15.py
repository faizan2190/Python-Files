from tkinter import *
def login():
    label = Label(win, text=var.get())
    label.pack()
win = Tk()
var = StringVar()
win.title("Let's talk about the entry box")
label = Label(win, text="Email : ",)
label.place(x=100,y=150)
entry = Entry(win,variable=var)
entry.place(x=170,y=150,width=220)

label_1 = Label(win, text="Password : ",)
label_1.place(x=100,y=190)
entry_1 = Entry(win,show="*")
entry_1.place(x=170,y=190,width=220)

button = Button(win, text="Login",command = login)
button.place(x=250,y=230)
win.mainloop()