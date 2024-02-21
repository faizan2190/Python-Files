from tkinter import Tk,Label
r=Tk()
r.title("My Window")
r.geometry("200x400")
lab1=Label(r,text='Hello World',fg='red',bg='green',relief="groove")
lab1.pack()

lab2=Label(r,text='Hello World',fg='green',bg='red',relief="groove",borderwidth=6)
lab2.pack()

lab3=Label(r,text='Hello World',fg='red',bg='green',padx=12,pady=4)
lab3.pack()

r.mainloop()
