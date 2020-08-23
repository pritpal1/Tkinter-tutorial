import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random
root=tk.Tk()
root.title("Random Number Generator")

def play():
    random_no = random.randint(1,6)
    number.config(text=f'Number is : {random_no}')
    if random_no==6:
        showinfo("Congratulation, you won ! !")

number=ttk.Label(root,text="")
number.pack(pady=10)       

play=ttk.Button(root,text="Play",command=play)
play.pack(padx=50)
root.mainloop()