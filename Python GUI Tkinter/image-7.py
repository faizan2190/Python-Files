# 2 hour 57 mint

from tkinter import Tk, Label, PhotoImage
from PIL import ImageTk, Image
win = Tk()
win.title("Let's talk about the images in Tkinter")
image = Image.open("cat.jpeg")
photo = ImageTk.PhotoImage(image)
label = Label(win, image=photo, text="cat", compound="top")
label.pack()
win.mainloop()