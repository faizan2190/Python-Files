from tkinter import Tk,Label,PhotoImage
r=Tk()
r.title("My Window")
r.geometry("200x200+400+400")
# lab1=Label(r,text="Let's talk about images")
# lab1.pack()

photo1=PhotoImage(file="download.png")
lab2=Label(r,image=photo1)
lab2.grid(row=0,column=0)

photo2=PhotoImage(file="images.png")
lab3=Label(r,image=photo2)
lab3.grid(row=0,column=1)

r.mainloop()
