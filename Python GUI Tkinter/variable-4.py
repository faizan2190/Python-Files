from tkinter import Tk, StringVar, IntVar, BooleanVar,DoubleVar
win = Tk()
str_var = StringVar(win,value="Hello World")
# print(str_var)
# str_var.set("Python")
print(str_var.get())
int_var = IntVar(win, value=3.14)
print(int_var.get())
bool_var = BooleanVar(win,value=True)
print(bool_var.get())
double_var = DoubleVar(win, value=3.14)
print(double_var.get())
win.mainloop()