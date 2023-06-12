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

#=====show the song playing==========#
var = StringVar()
var.set("..............................................................................")
song_title = Label(root, font="Helvetica 12 bold", bg="black",
                   fg="white", width=48, textvariable=var)
song_title.place(x=10, y=5)

# =====add a music list to the listbox======"
def append_listbox():
    directory = askdirectory()
    try:
        os.chdir(directory)# it permits to change the current dir
        song_list = os.listdir()
        song_list.reverse()
        for item in song_list: # it returns the list of files song
            pos = 1
            play_list.insert(pos, item)
            pos += 1
    except:
        showerror("File selcted error", "Please choose a file correctly")  

# =====run the append_listbox function on separate thread======"
def add_songs_playlist():
    mythreads = threading.Thread(target=append_listbox)
    threads.append(mythreads)
    mythreads.start()

    #=====show music time=========#
def get_time():
    global next_one
    current_time = pygame.mixer.music.get_pos() / 1000
    formated_time = time.strftime("%H:%M:%S", time.gmtime(current_time))
    next_one = play_list.curselection()
    song = play_list.get(next_one)
    song_timer = MP3(song)
    song_length = int(song_timer.info.length)
    format_for_length = time.strftime("%H:%M:%S", time.gmtime(song_length))
    label_time.config(text=f"{ format_for_length} / {formated_time}")
    progress["maximum"] = song_length
    progress["value"] = int(current_time)
    root.after(100, get_time)



