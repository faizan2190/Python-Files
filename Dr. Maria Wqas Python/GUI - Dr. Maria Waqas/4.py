# Create a GUI based application that convert celcius to fehrenhiet
from tkinter import Tk,Label,Button,Entry
def converter():
    fah=int(e.get())*9/5+32
    l=Label(r,text="The temperature in fehrenheit is"+str(fah))
    l.pack()
r=Tk()
r.title("Converter")
r.geometry("200x200")
l=Label(r,text="Enter a temperature in celcius")
l.pack()
e=Entry()
e.pack()
b=Button(r,text="please enter",command=converter)
b.pack()
r.mainloop()
