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



