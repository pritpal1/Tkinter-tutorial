#Step1:Importing Required Modules & libraries
from tkinter import *
import pygame
import os

#Step2:Defining MusicPlayer Class
class MusicPlayer:
  #Step3: Defining Constructor
  def __init__(self,root):
    self.root = root
    #Step4: Title of the window and Geometry
    self.root.title("Music Player")
    self.root.geometry("1000x200+200+200")
    #Step5: Initiating Pygame and Pygame Mixer
    pygame.init()
    pygame.mixer.init()
    #Step6 Declaring track nd Status Variable
    self.track = StringVar()
    self.status = StringVar()
    #Step7: Creating Track Frame for Song label & status label
    trackframe = LabelFrame(self.root,text="Song Track",font=("times new roman",15,"bold"),
    bg="grey",fg="white",bd=5,relief=GROOVE)
    trackframe.place(x=0,y=0,width=600,height=100)
    #Step8 Inserting Song Track Label,Status Label
    songtrack = Label(trackframe,textvariable=self.track,width=20,font=("times new roman",24,"bold"),
    bg="grey",fg="crimson").grid(row=0,column=0,padx=10,pady=5) 
    trackstatus = Label(trackframe,textvariable=self.status,font=("times new roman",24,"bold"),
    bg="grey",fg="crimson").grid(row=0,column=1,padx=10,pady=5)
    #Step9: Creating Button Frame
    buttonframe = LabelFrame(self.root,text="Control Panel",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
    buttonframe.place(x=0,y=100,width=600,height=100)
    #Play Button
    playbtn = Button(buttonframe,text="PLAY",command=self.playsong,width=6,height=1,
    font=("times new roman",16,"bold"),fg="Moccasin",bg="crimson").grid(row=0,column=0,padx=10,pady=5)
    #Pause Button
    playbtn = Button(buttonframe,text="PAUSE",command=self.pausesong,width=8,height=1,
    font=("times new roman",16,"bold"),fg="Moccasin",bg="crimson").grid(row=0,column=1,padx=10,pady=5)
    #Unpause Button
    playbtn = Button(buttonframe,text="UNPAUSE",command=self.unpausesong,width=10,height=1,font=("times new roman",16,"bold"),fg="Moccasin",bg="crimson").grid(row=0,column=2,padx=10,pady=5)
    #Stop Button
    playbtn = Button(buttonframe,text="STOP",command=self.stopsong,width=6,height=1,font=("times new roman",16,"bold"),fg="Moccasin",bg="crimson").grid(row=0,column=3,padx=10,pady=5)
    #Step10:Creating Playlist Frame
    songsframe = LabelFrame(self.root,text="Song Playlist",font=("times new roman",15,"bold"),
    bg="DimGrey",fg="white",bd=5,relief=GROOVE)
    songsframe.place(x=600,y=0,width=400,height=200)
    #Step11:Inserting scrollbar
    scrol_y = Scrollbar(songsframe,orient=VERTICAL)
    #Playlist listbox
    self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="crimson",
    selectmode=SINGLE,font=("times new roman",12,"bold"),bg="dimgrey",fg="Moccasin",bd=5,relief=GROOVE)
    # Applying Scrollbar to listbox
    scrol_y.pack(side=RIGHT,fill=Y)
    scrol_y.config(command=self.playlist.yview)
    self.playlist.pack(fill=BOTH)
    #Step12:Changing Directory for fetching Songs
    os.chdir("D:\music")
    # Fetching Songs
    songtracks = os.listdir()
    #Step13:-Inserting Songs into Playlist
    for track in songtracks:
      self.playlist.insert(END,track)
  #Step14:- Defining Play Song Function
  def playsong(self):
    # Displaying Selected Song title
    self.track.set(self.playlist.get(ACTIVE))
    #Status
    self.status.set("-Playing")
    # Loading nd Playing Selected Song
    pygame.mixer.music.load(self.playlist.get(ACTIVE))
    pygame.mixer.music.play()
    
  def stopsong(self):
    self.status.set("-Stopped")   
    pygame.mixer.music.stop()
    
  def pausesong(self):
    self.status.set("-Paused")
    pygame.mixer.music.pause()
  def unpausesong(self):
    self.status.set("-Playing")
    # Playing back Song
    pygame.mixer.music.unpause()
    
#Creating TK Container
root = Tk()
#Step15: Passing Root to MusicPlayer Class
MusicPlayer(root)
#Step16:keeps window alive 
root.mainloop()
