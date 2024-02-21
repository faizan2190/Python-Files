from tkinter import Tk,Label,Frame
r=Tk()
r.title("Keypad")
r.geometry("200x200")
f=Frame()
value=0
for i in range(3):
    for j in range(3):
        lab=Label(f,text=value,border=5,bg="orange",fg="black",relief="sunken")
        lab.grid(row=i,column=j)
        value+=1
f.pack()
r.mainloop()