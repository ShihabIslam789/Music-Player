from tkinter import (
    Tk,HORIZONTAL,Label,Button,
    END,PhotoImage,Listbox,
    LEFT,StringVar,Menu,Toplevel,
    ACTIVE,BOTH,TOP
    )
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showerror,askquestion,showinfo
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.icons import Emoji


import os
import threading
import time

from PIL import Image, ImageTk
import pygame
from mutagen.mp3 import MP3


CURRENT_SONG_INDEX = 0
NUMBER_OF_SONGS_IN_LIST = 0
IMAGE_PATH = 'images/best.png'

class Player(ttk.Frame):
    
    pygame.init()
    pygame.mixer.init()
    
    def __init__(self, master):
        self.master = master
        
        #=======all Button symbols and variables======#
        self.PLAY = "►"
        self.PAUSE = "║║"
        self.RWD = "⏮"
        self.FWD = "⏭"
        self.STOP = "■"
        self.UN_PAUSE = "||"
        self.MUTE = "🔇"
        self.UN_MUTE = u"\U0001F50A"
        self.vol_mute = 0.0
        self.vol_unmute = 1

   #==========music playlist listbox=========#
        self.scroll = ttk.Scrollbar(master, bootstyle="round")
        self.play_list = Listbox(master, font="Sansarif 12 bold", bd=5,
                            bg="white", width=37, height=19, selectbackground="blue")
        self.play_list.place(x=600, y=77)
        self.scroll.place(x=946, y=80, height=389, width=15)
        self.scroll.config(command=self.play_list.yview)
        self.play_list.config(yscrollcommand=self.scroll.set)
        
        self.img1 = Image.open(IMAGE_PATH)
        self.img1 =  self.img1.resize((600, 470), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(self.img1)
        self.lab = Label(master)
        self.lab.grid(row=0, column=0)
        self.lab["compound"] = LEFT
        self.lab["image"] = self.img

           #=====show the song playing==========#
        self.var = StringVar()
        self.var.set("..............................................................................")
        self.song_title = Label(master, font="Helvetica 12 bold", bg="black",
                        fg="white", width=55, textvariable=self.var)
        self.song_title.place(x=3, y=0)
        
        #===================bindings=================#
        
        self.master.bind("<space>", lambda x: self.play_thread())
        self.master.bind('<Left>', lambda x: self.prev())
        self.master.bind('<Right>', lambda x: self.next())
        
     