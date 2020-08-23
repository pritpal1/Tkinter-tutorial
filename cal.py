#Step1:importing required library
from tkinter import *
from tkinter import messagebox

#Step2:creating globalvariables
val=""
A = 0
operator =""

#Step3:Creating functions of all buttons
def btn1Click():
	global val
	val= val +"1"
	data.set(val) #set the value of val
def btn2Click():
	global val
	val= val +"2"
	data.set(val)
def btn3Click():
	global val
	val =val +"3"
	data.set(val)
def btn4Click():
	global val
	val= val+ "4"
	data.set(val)
def btn5Click():
	global val
	val= val+ "5"
	data.set(val)
def btn6Click():
	global val
	val= val+ "6"
	data.set(val)
def btn7Click():
	global val
	val= val+ "7"
	data.set(val)
def btn8Click():
	global val
	val= val+ "8"
	data.set(val)
def btn9Click():
	global val
	val= val+ "9"
	data.set(val)
def btn0Click():
	global val
	val= val+ "0"
	data.set(val)

#Step4:function for setting operators
#Addition
def btnP():
	global val
	global  A
	global operator
	A = int(val)
	operator="+"
	val=val + "+"
	data.set(val)

#Substraction
def btnS():
	global val
	global A
	global operator
	A=int(val)
	operator="-"
	val=val+"-"
	data.set(val)

# Multiplication
def btnM():
	global val
	global A
	global operator
	A=int(val)
	operator="*"
	val=val+"*"
	data.set(val)

#modules
def btnMo():
	global val
	global A
	global operator
	A=int(val)
	operator="%"
	val=val+"%"
	data.set(val)

#Division
def btnD():
	global val
	global A
	global operator
	A=int(val)
	operator="/"
	val=val+"/"
	data.set(val)
    
#clearing the value    
def Clear():
	global A
	global operator
	global val
	val =""
	A = 0
	operator=""
	data.set(val)

#Step5:Functions for calculation
def result():
	global A
	global operator
	global val
	val2 =val
	if operator=="+":
		x=int((val2.split("+")[1]))
		c=A+x
		data.set(c)
		val=str(c)
	elif operator=="-":
		x=int((val2.split("-")[1]))
		c=A-x
		data.set(c)
		val=str(c)
	elif operator=="*":
		x=int((val2.split("*")[1]))
		c=A*x
		data.set(c)
		val=str(c)

	elif operator=="/":
		x = int((val2.split("/")[1]))
		if x ==0:
			messagebox.showerror("Error","Division by 0not supported")
			A=""
			val=""
			data.set(val)
		else:
			c = int(A / x)
			data.set(c)
			val = str(c)

	elif operator=="%":
		x = int((val2.split("%")[1]))
		if x ==0:
			messagebox.showerror("Error","Division by 0 not supported")
			A=""
			val=""
			data.set(val)
		else:
			c = int(A % x)
			data.set(c)
			val = str(c)
#Step6:creating root object
root=Tk()
root.geometry("230x300+100+200")
root.resizable(0,0)

data=StringVar()

lbl=Label(root,textvariable=data,background="powderblue",
		  text="",anchor=SE,font="20").pack(expand=True,fill="both")

#Step7:Creating rows for buttons
btnrow1=Frame(root)
btnrow1.pack(expand= True,fill="both")
btnrow2=Frame(root)
btnrow2.pack(expand= True,fill="both")
btnrow3=Frame(root)
btnrow3.pack(expand= True,fill="both")
btnrow4=Frame(root)
btnrow4.pack(expand= True,fill="both")

#Step8:Setting button position and text
btn1=Button(btnrow1,text="1",command=btn1Click)
btn1.pack(side=LEFT,expand="True",fill="both")
btn2=Button(btnrow1,text="2",command=btn2Click)
btn2.pack(side=LEFT,expand="True",fill="both")
btn3=Button(btnrow1,text="3",command=btn3Click)
btn3.pack(side=LEFT,expand="True",fill="both")
btnplus=Button(btnrow1,text="+",command=btnP)
btnplus.pack(side=LEFT,expand="True",fill="both")

btn4=Button(btnrow2,text="4",command=btn4Click)
btn4.pack(side=LEFT,expand="True",fill="both")
btn5=Button(btnrow2,text="5",command=btn5Click)
btn5.pack(side=LEFT,expand="True",fill="both")
btn6=Button(btnrow2,text="6",command=btn6Click)
btn6.pack(side=LEFT,expand="True",fill="both")
btnsub=Button(btnrow2,text="-",command=btnS)
btnsub.pack(side=LEFT,expand="True",fill="both")

btn7=Button(btnrow3,text="7",command=btn7Click)
btn7.pack(side=LEFT,expand="True",fill="both")
btn8=Button(btnrow3,text="8",command=btn8Click)
btn8.pack(side=LEFT,expand="True",fill="both")
btn9=Button(btnrow3,text="9",command=btn9Click)
btn9.pack(side=LEFT,expand="True",fill="both")
btnmul=Button(btnrow3,text="*",command=btnM)
btnmul.pack(side=LEFT,expand="True",fill="both")

btn0=Button(btnrow4,text="0",command=btn0Click)
btn0.pack(side=LEFT,expand="True",fill="both")
btneql=Button(btnrow4,text="=",command=result)
btneql.pack(side=LEFT,expand="True",fill="both")
btnmod=Button(btnrow4,text="%",command=btnMo)
btnmod.pack(side=LEFT,expand="True",fill="both")
btndiv=Button(btnrow4,text="/",command=btnD)
btndiv.pack(side=LEFT,expand="True",fill="both")
btnc=Button(root,text="C",command=Clear)
btnc.pack(side=BOTTOM,expand="True",fill="both")

#Step9:keeps window alive 
root.mainloop()