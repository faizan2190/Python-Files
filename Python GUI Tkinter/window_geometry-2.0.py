# 33 mint
from tkinter import Tk
rt = Tk()
rt.title('Learn about the Geometry')
# rt.geometry('100x300+200+200') #(width,height,distance from x and y axis)
# rt.geometry('100x300-200-200') #(width,height,distance from x and y axis)

# For center:
width = 300
height = 300
screen_height = rt.winfo_screenheight()
screen_center_height = int(screen_height/2 - height/2) #for y
screen_width = rt.winfo_screenwidth()
screen_center_width = int(screen_width/2 - width/2) #for x
rt.geometry(f'{width}x{height}+{screen_center_width}+{screen_center_height}')
# rt.minsize(100,100)
# rt.maxsize(100,100)
# To off the resize option
rt.resizable(False,False)
rt.mainloop()

