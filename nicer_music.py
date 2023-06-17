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
