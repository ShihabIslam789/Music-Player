from tkinter import *
from tkinter.filedialog import askdirectory
import pygame
import os
from mutagen.mp3 import MP3
import threading
from tkinter.messagebox import *
from tkinter import ttk
import time

root = Tk()
root.geometry("865x460+250+100")
root.title("Mp3 Music Player")
root.configure(bg="black")
root.resizable(width=0, height=0)

#=====initialize pygame=====#
pygame.init()
pygame.mixer.init()

#===empty thread list=========#
threads = []

# =====show an icon for the application

def get_icon():
    winicon = PhotoImage(file="best (2).png")
    root.iconphoto(False, winicon)

#=====run the get_icon on a different thread from the gui=====#

def icon():
    mythreads = threading.Thread(target=get_icon)
    threads.append(mythreads)
    mythreads.start()

icon()

#=======all Button symbols and variables======#
PLAY = "►"
PAUSE = "║║"
RWD = "⏮"
FWD = "⏭"
STOP = "■"
UNPAUSE = "||"
mute = "🔇"
unmute = u"\U0001F50A"
vol_mute = 0.0
vol_unmute = 1

#==========music playlist listbox=========#
scroll = Scrollbar(root)
play_list = Listbox(root, font="Sansarif 12 bold", bd=5,
                    bg="white", width=37, height=19, selectbackground="black")
scroll.place(x=850, y=80, height=380, width=15)
play_list.place(x=505, y=77)
scroll.config(command=play_list.yview)
play_list.config(yscrollcommand=scroll.set)

img = PhotoImage(file="best (2).png", width=500, height=460)
lab = Label(root)
lab.grid()
lab["compound"] = LEFT
lab["image"] = img


