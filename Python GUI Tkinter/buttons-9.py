# 2:12
# from tkinter import Tk, Label, Button, PhotoImage
# from PIL import ImageTk, Image
# win = Tk()
# win.config(bg="yellow")
# win.title("Let's tslk about the Buttuns")
# image = Image.open("cat.jpeg")
# photo = ImageTk.PhotoImage(image)
# button = Button(win, font=43, image=photo)
# button.place(x=100, y=100)
# win.mainloop()

# from tkinter import Tk, Label, Button, PhotoImage
# from PIL import ImageTk, Image
# def Python():
#     print("Python")
# win = Tk()
# win.config(bg="yellow")
# win.title("Let's tslk about the Buttuns")
# image = Image.open("cat.jpeg")
# photo = ImageTk.PhotoImage(image)
# button = Button(win, text="Hello World", font=43, image=photo, compound="top", command=Python)
# button.place(x=100, y=100)
# win.mainloop()


from tkinter import Tk, Label, Button, PhotoImage
from PIL import ImageTk, Image
def Python():
    label = Label(win,text="Hello Python")
    label.place(x=110,y=110)
win = Tk()
win.config(bg="yellow")
win.title("Let's tslk about the Buttuns")
image = Image.open("cat.jpeg")
photo = ImageTk.PhotoImage(image)
button = Button(win, text="Hello World", font=43, image=photo, compound="top", command=Python)
button.place(x=100, y=100)
win.mainloop()