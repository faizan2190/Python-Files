# #50 mint
# from tkinter import Tk, Label
# win = Tk()
# win.title("Learning Tkinter")
# win.config(bg="blue")
# label = Label(win, text="Hello World", font=("Times New Roman",30,"bold"),bg="red")
# label.pack(side="left")
# label1 = Label(win, text="Hello World", font=("Times New Roman",30,"bold"),bg="red")
# label1.pack(side = 'right')
# # label.pack(ipadx=20,ipady=20) #label displacement from s and y within the label
# # label.pack(fill="x")
# # label.pack(expand= True)
# win.mainloop()


# from tkinter import Tk, Label
# win = Tk()
# win.title("Learning Tkinter")
# win.config(bg="yellow")
# label = Label(win, text="Hello World", font=("Times New Roman",30,"bold"),bg="red")
# label.grid(row=0,column=0)
# label1 = Label(win, text="Hello World", font=("Times New Roman",30,"bold"),bg="red")
# label1.grid(row=0,column=1)
# win.mainloop()


from tkinter import Tk, Label
win = Tk()
win.title("Learning Tkinter")
win.config(bg="yellow")
label = Label(win, text="Hello World", font=("Times New Roman",30,"bold"),bg="red")
label.place(x=20,y=20,height=100,width=300) #hight, width box ki hay jabke x and y distance hay from x and y axis
label1 = Label(win, text="Hello World", font=("Times New Roman",30,"bold"),bg="red")
label1.place(x=20,y=140,height=100,width=300)
win.mainloop()