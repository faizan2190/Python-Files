# 3:01
from tkinter import *
# win = Tk()
# win.title("Let's talk about the MenuButton")
# menu_button = Menubutton(win, text="File")
# menu_button.menu = Menu(menu_button, tearoff=0)
# menu_button["menu"]=menu_button.menu
# menu_button.menu.add_checkbutton(label="New File")
# menu_button.menu.add_checkbutton(label="Open File")
# menu_button.menu.add_checkbutton(label="Save File")
# # All properties of button 
# menu_button.pack()
# win.mainloop()




win = Tk()
win.title("Let's talk about the Menu button")
menu_button = Menubutton(win, text="File")
menu = Menu(menu_button, tearoff=0)
menu.add_command(label="Open File")
menu.add_command(label="Save File")
menu.add_command(label="Delete File")
menu_button['menu'] = menu
# bracket ke ander jo menu likha gia hay wo mwnubutton ki property hay 
menu_button.pack()
win.mainloop()