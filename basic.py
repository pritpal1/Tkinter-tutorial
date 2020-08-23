from tkinter import *
win =Tk()
win.geometry("500x500")

win.title("Sementic")
Tops = Frame(win, width = 600, relief = SUNKEN)
Tops.pack(side = TOP)
f1 = Frame(win, width = 800, height = 700, relief = SUNKEN)
f1.pack(side = LEFT)

Result = StringVar()

lblInfo = Label(Tops, font = ('helvetica', 50, 'bold'),
          text = "Sentimental",fg = "Black")
lblInfo.pack()
lblReference = Label(f1, font=('arial', 16, 'bold'),
                     text="Enter Query:", bd=16, anchor="w")

lblReference.grid(row=0, column=0)

txtReference = Entry(f1, font=('arial', 16, 'bold'),
                      bd=10,
                     bg="powder blue", justify='right')

txtReference.grid(row=0, column=1)

lblService = Label(f1, font=('arial', 16, 'bold'),
                   text="The Result-", bd=16, anchor="w")

lblService.grid(row=2, column=2)

txtService = Entry(f1, font=('arial', 16, 'bold'),
                   textvariable=Result, bd=10, insertwidth=4,
                   bg="powder blue", justify='right')

txtService.grid(row=2, column=3)

def Result():
    print("Pos,,,,neg")

def qExit():
    win.destroy()

btn1 = Button(f1,fg = "black", font = ('arial', 16, 'bold'),
                      width = 10, text = "Result", bg = "red",
              command=Result ).grid(row = 8, column = 0)

btnExit = Button(f1,fg = "black", font = ('arial', 16, 'bold'),
                      width = 10, text = "Exit", bg = "red",
                  command = qExit).grid(row = 8, column =1)

win.mainloop()
