from tkinter import Tk,Label
r=Tk()
r.title('My Window')
r.geometry('400x400+200+0')
lab=Label(r,text='Hello World')
lab.pack()
r.mainloop()