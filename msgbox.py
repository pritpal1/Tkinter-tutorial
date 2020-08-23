from tkinter import *
from tkinter import messagebox
top=Tk()
top.geometry("200x200")
def fun():
    messagebox.showinfo("h","hlololllololl")

b1= Button(top,text="Red",command=fun,activeforeground="red",
           activebackground="blue",pady=10
           )
b1.pack(side =LEFT)
top.mainloop()