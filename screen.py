import tkinter as tk
import pyautogui as pg 
root=tk.Tk()
root.title("Screenshot GUI")
root.geometry('500x500')

def screenshot():
    screenshot=pg.screenshot()
    screenshot.save("E:/screen.png")

capture=tk.Button(root,text="Capture Screenshot",command=screenshot)
capture.grid(row=3,column=3)
root.mainloop()