#Step1:importing the required libraries 
import tkinter as Tkinter 

#Step2:set the counter as -1 to start counting from 0 and running false
counter = -1
running = False
#Step3:Function to start the counting
def counter_label(label): 
	def count(): 
		if running: 
			global counter 
			# To manage the intial delay. 
			if counter==-1:			 
				display="Starting..."
			else: 
				display=str(counter) 

			label['text']=display # Or label.config(text=display) 

# Step4:label.after(arg1, arg2) delays by first argument given in milliseconds 
# and then calls the function given as second argument. Generally like here we need to call the 
# function in which it is present repeatedly.Delays by 1000ms=1 seconds and call count again. 
			label.after(1000, count) 
			counter += 1

	#Step4: Triggering the start of the counter. 
	count()	 

#Step5: start function of the stopwatch 
def Start(label): 
	global running 
	running=True
	counter_label(label) 
	start['state']='disabled'
	stop['state']='normal'
	reset['state']='normal'

#Step6: Stop function of the stopwatch 
def Stop(): 
	global running 
	start['state']='normal'
	stop['state']='disabled'
	reset['state']='normal'
	running = False

#Step7: Reset function of the stopwatch 
def Reset(label): 
	global counter 
	counter=-1

	# If rest is pressed after pressing stop. 
	if running==False:	 
		reset['state']='disabled'
		label['text']='Welcome!'

	# If reset is pressed while the stopwatch is running. 
	else:			 
		label['text']='Starting...'
#Step8: creating root object 
root = Tkinter.Tk() 
root.title("Stopwatch")
root.configure(bg="black")
# Step9:Fixing the window size. 
root.minsize(width=250, height=100) 
#Step10:Setting the label
label = Tkinter.Label(root, text="Welcome!",bg="black" ,fg="white", font="Verdana 30 bold") 
label.pack() 
start = Tkinter.Button(root, text='Start', 
width=15, command=lambda:Start(label)) 
stop = Tkinter.Button(root, text='Stop', 
width=15, state='disabled', command=Stop) 
reset = Tkinter.Button(root, text='Reset', 
width=15, state='disabled', command=lambda:Reset(label)) 
start.pack() 
stop.pack() 
reset.pack()
#Step11 keeps window alive  
root.mainloop() 
