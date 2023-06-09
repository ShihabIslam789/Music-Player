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


