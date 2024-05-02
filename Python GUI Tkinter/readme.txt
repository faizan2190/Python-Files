Tkinter is the inbuild library

Widget -> A widget is a graphical component or element that users can interact with on a graphical user interface (GUI). Examples of widgets include buttons, labels, text boxes, check buttons, radio buttons, and more. Each widget in Tkinter has a set of attributes that define its appearance and behavior. These attributes can be configured to customize the widget according to the needs of the application. For example, a button widget might have attributes such as text (the label displayed on the button), foreground color, background color, font, command (the function to be executed when the button is clicked), and many more.

Tkinter ke ander ager logo change kerna hay to logo .icu ke format me jata ahy png jpg me nahi

To transparent the GUI window, the value of alpha is in between 0 and 1
~ root.attributes('-alpha',0.5)

To change the background colour
~ root.config(bg='red')

~ rt.geometry('100x300+200+200') #(width,height,distance from x and y axis)

~ .winfo_screenwidth(): method in Tkinter is used to retrieve the width of the screen in pixels.
~ .winfo_screenheight(): method in Tkinter is used to retrieve the height of the screen in pixels.

~ rt.minsize(100,100) Window minimum size
~ rt.maxsize(100,100) Window maximum size

To off the resize option
~ rt.resizable(False,False)

Geometry management refers to the methods used to organize and position widgets within a window or frame.

Label displacement from s and y within the label
~ label.pack(ipadx=20,ipady=20)
~ label.pack(fill="x") #fill the entire line of the label with the label properties
~ label.pack(expand= True) # To center the label on the screen
~ label.place(x=20,y=20,height=444,width=444) #hight, width box ki hay jabke x and y distance hay from x and y axis

The diffrence betweewn padx and ipadx is that ipadx apply padding inside the widget or box while padx apply the padding outside the Widget

In Tkinter, variables are used to store and manage the data associated with widgets, such as text entered into an entry field or the state of a checkbox or radio button.
In Tkinter, the get() and set() methods are commonly used to interact with tkinter variables associated with widgets. These methods are particularly useful for widgets like Entry, Label, Checkbutton, Radiobutton, and more, where you need to retrieve or modify the data displayed or entered by the user.

from tkinter import Tk, Label, PhotoImage
from PIL import ImageTk, Image
win = Tk()
win.title("Let's talk about the images in Tkinter")
image = Image.open("cat.jpeg")
photo = ImageTk.PhotoImage(image)
label = Label(win, image=photo, text="cat", compound="top")
label.pack()
win.mainloop()

~ LabelFrame() # to make a frame