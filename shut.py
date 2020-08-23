from tkinter import *
import os 
root = Tk()
root.title("Shutdown And Restart")
root.geometry("270x60")

def shutdown():
    os.system(" shutdown /s /t 1")

def restart():
    os.system(" shutdown /r /t 1")  

btn1= Button(root,text="Shutdown",command=shutdown,height=3,width=17)
btn1.grid(row=1,column=1)
btn2= Button(root,text="Restart",command=restart,height=3,width=17)
btn2.grid(row=1,column=2)
root.mainloop()